# -*- coding: utf-8 -*-
"""
《析光》特情排版引擎：块模型 -> docx（五节特情体例）/ HTML 图文热链版

块类型（dict，键 t）：
  chapter  {num, name}                章题，进目录一级
  h1       {text}                     一级标题，进目录二级
  h2       {text, toc}                二级标题（案例标题 toc=True 进目录三级）
  p        {text, indent=True}        正文段落，支持 **粗体**、[@ref]、{fig:key}、{tab:key}
  lead     {text}                     导读框
  judge    {items:[...], title}       判断框（①②③）
  figure   {key, src, caption, source, width_mm, remote_url, page_url}
  table    {key, caption, headers, rows, source, widths(mm)}
  kv       {rows:[(k,v),...]}         案例要素表（两列×N，或四列）
  pagebreak
"""
import base64
import html
import os
import re

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, Cm, RGBColor, Mm

CREAM = 'F7F4EC'
NAVY = RGBColor(0x12, 0x23, 0x3B)
ACC = RGBColor(0x2E, 0x93, 0xD6)
BRASS = RGBColor(0xA8, 0x84, 0x2F)
ALERT = RGBColor(0xC0, 0x39, 0x2B)
GREY = RGBColor(0x8A, 0x84, 0x74)
INK = RGBColor(0x22, 0x22, 0x22)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

FS = '仿宋_GB2312'
KAI = '楷体_GB2312'
HEI = '黑体'
SONG = '宋体'

CN_NUM = '一二三四五六七八九十'


def cn_num(n):
    if n <= 10:
        return CN_NUM[n - 1]
    if n < 20:
        return '十' + (CN_NUM[n - 11] if n > 10 else '')
    t, o = divmod(n, 10)
    return CN_NUM[t - 1] + '十' + (CN_NUM[o - 1] if o else '')


# ---------------------------------------------------------------- 文本归一
CJK = r'[㐀-鿿　-〿＀-￯]'


def norm_text(s):
    """中文语境标点归一：% -> ％，直引号 -> 弯引号（仅邻接中文时）。"""
    if not s:
        return s
    s = s.replace(' ', ' ')
    # 百分号
    s = re.sub(r'(?<=[0-9])%', '％', s)
    # 双引号：逐个交替
    if re.search(CJK, s) and '"' in s:
        out, open_ = [], True
        for ch in s:
            if ch == '"':
                out.append('“' if open_ else '”')
                open_ = not open_
            else:
                out.append(ch)
        s = ''.join(out)
    # 单引号：两侧任一为中文时视为引号
    if "'" in s and re.search(CJK, s):
        chars = list(s)
        open_ = True
        for i, ch in enumerate(chars):
            if ch != "'":
                continue
            prev = chars[i - 1] if i > 0 else ''
            nxt = chars[i + 1] if i + 1 < len(chars) else ''
            if re.match(CJK, prev or ' ') or re.match(CJK, nxt or ' ') or prev in ('', ' ') and open_:
                chars[i] = '“' if open_ else '”'
                open_ = not open_
        s = ''.join(chars)
    # 中文括号内半角括号
    s = re.sub(r'(?<=' + CJK + r')\(', '（', s)
    s = re.sub(r'\)(?=' + CJK + r')', '）', s)
    s = s.replace('（', '（').replace('）', '）')
    return s


# ---------------------------------------------------------------- 参考文献登记
class RefRegistry:
    def __init__(self):
        self.by_key = {}      # key -> dict
        self.order = []       # 首次引用顺序
        self.num = {}

    def add(self, key, ref):
        if key not in self.by_key:
            self.by_key[key] = ref
        return key

    def cite(self, key):
        if key not in self.num:
            self.order.append(key)
            self.num[key] = len(self.order)
        return self.num[key]

    def fmt_cites(self, keys):
        ns = sorted(set(self.cite(k) for k in keys if k in self.by_key))
        if not ns:
            return ''
        # 连续号压缩
        parts, i = [], 0
        while i < len(ns):
            j = i
            while j + 1 < len(ns) and ns[j + 1] == ns[j] + 1:
                j += 1
            parts.append(str(ns[i]) if j == i else (
                '%d,%d' % (ns[i], ns[j]) if j == i + 1 else '%d-%d' % (ns[i], ns[j])))
            i = j + 1
        return '[' + ','.join(parts) + ']'


def ref_entry(r):
    """GB/T 7714 网络文献著录。"""
    author = (r.get('author') or r.get('publisher') or '').strip().rstrip('.')
    title = (r.get('title') or '').strip().rstrip('.')
    tcn = (r.get('title_cn') or '').strip()
    pub = (r.get('publisher') or '').strip()
    date = (r.get('date') or '').strip()
    s = '%s. %s' % (author, title)
    if tcn and tcn != title:
        s += '（中译：%s）' % tcn
    s += '[EB/OL]. '
    if pub and pub != author:
        s += '%s, ' % pub
    s += '%s[2026-10-09].' % (date or '日期不详')
    return s


# ---------------------------------------------------------------- 行内解析
INLINE_RE = re.compile(r'(\*\*.+?\*\*|\[@[^\]]+\]|\{fig:[^}]+\}|\{tab:[^}]+\}|\{red:[^}]+\}|\{case:[^}]+\}|\{count:[^}]+\})')


def parse_inline(text, ctx):
    """返回 [(seg_text, style)]，style in normal/bold/sup/red。"""
    out = []
    for part in INLINE_RE.split(text):
        if not part:
            continue
        if part.startswith('**') and part.endswith('**'):
            out.append((norm_text(part[2:-2]), 'bold'))
        elif part.startswith('[@'):
            keys = []
            for k in [k.strip() for k in part[2:-1].split(',')]:
                if k.startswith('H:'):
                    for name, ks in ctx.get('halias', {}).items():
                        if k[2:].lower() in name.lower():
                            keys.extend(ks[:3]); break
                else:
                    keys.append(k)
            c = ctx['refs'].fmt_cites(keys)
            if c:
                out.append((c, 'sup'))
        elif part.startswith('{fig:'):
            out.append(('图%s' % ctx['fignum'].get(part[5:-1], '?'), 'normal'))
        elif part.startswith('{tab:'):
            out.append(('表%s' % ctx['tabnum'].get(part[5:-1], '?'), 'normal'))
        elif part.startswith('{red:'):
            out.append((norm_text(part[5:-1]), 'red'))
        elif part.startswith('{case:'):
            keys = [k.strip() for k in part[6:-1].split(',')]
            codes = [ctx.get('casecode', {}).get(k, '?' + k) for k in keys]
            out.append(('、'.join(codes), 'normal'))
        elif part.startswith('{count:'):
            out.append((str(ctx.get('counts', {}).get(part[7:-1], '?')), 'normal'))
        else:
            out.append((norm_text(part), 'normal'))
    return out


def split_brackets(s):
    """把全角括号（含括号本身）切出来：[(text, in_bracket)]"""
    res, buf, depth = [], '', 0
    for ch in s:
        if ch == '（':
            if depth == 0 and buf:
                res.append((buf, False)); buf = ''
            depth += 1
            buf += ch
        elif ch == '）' and depth > 0:
            buf += ch
            depth -= 1
            if depth == 0:
                res.append((buf, True)); buf = ''
        else:
            buf += ch
    if buf:
        res.append((buf, depth > 0))
    return res


# ================================================================= DOCX
PPR_ORDER = ['pStyle', 'keepNext', 'keepLines', 'pageBreakBefore', 'framePr', 'widowControl',
             'numPr', 'suppressLineNumbers', 'pBdr', 'shd', 'tabs', 'suppressAutoHyphens',
             'kinsoku', 'wordWrap', 'overflowPunct', 'topLinePunct', 'autoSpaceDE', 'autoSpaceDN',
             'bidi', 'adjustRightInd', 'snapToGrid', 'spacing', 'ind', 'contextualSpacing',
             'mirrorIndents', 'suppressOverlap', 'jc', 'textDirection', 'textAlignment',
             'textboxTightWrap', 'outlineLvl', 'divId', 'cnfStyle', 'rPr', 'sectPr', 'pPrChange']
TCPR_ORDER = ['cnfStyle', 'tcW', 'gridSpan', 'hMerge', 'vMerge', 'tcBorders', 'shd', 'noWrap',
              'tcMar', 'textDirection', 'tcFitText', 'vAlign', 'hideMark']
TBLPR_ORDER = ['tblStyle', 'tblpPr', 'tblOverlap', 'bidiVisual', 'tblStyleRowBandSize',
               'tblStyleColBandSize', 'tblW', 'jc', 'tblCellSpacing', 'tblInd', 'tblBorders',
               'shd', 'tblLayout', 'tblCellMar', 'tblLook']


def ordered_set(parent, el, order):
    """按 schema 顺序插入/替换子元素。"""
    tag = el.tag.split('}')[1]
    old = parent.find(qn('w:' + tag))
    if old is not None:
        parent.replace(old, el)
        return el
    idx = order.index(tag)
    for child in parent:
        ctag = child.tag.split('}')[1]
        if ctag in order and order.index(ctag) > idx:
            child.addprevious(el)
            return el
    parent.append(el)
    return el


def p_border(p, edge, color, sz='6', space='4'):
    pPr = p._element.get_or_add_pPr()
    bd = pPr.find(qn('w:pBdr'))
    if bd is None:
        bd = ordered_set(pPr, OxmlElement('w:pBdr'), PPR_ORDER)
    order = ['top', 'left', 'bottom', 'right', 'between', 'bar']
    e = OxmlElement('w:' + edge)
    e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), sz)
    e.set(qn('w:space'), space); e.set(qn('w:color'), color)
    ordered_set(bd, e, order)


def p_shade(p, fill):
    pPr = p._element.get_or_add_pPr()
    sh = OxmlElement('w:shd')
    sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), fill)
    ordered_set(pPr, sh, PPR_ORDER)


def p_outline(p, lvl):
    pPr = p._element.get_or_add_pPr()
    o = OxmlElement('w:outlineLvl'); o.set(qn('w:val'), str(lvl))
    ordered_set(pPr, o, PPR_ORDER)


def p_tabs(p, pos_twips, align='right', leader='dot'):
    pPr = p._element.get_or_add_pPr()
    tabs = OxmlElement('w:tabs')
    t = OxmlElement('w:tab')
    t.set(qn('w:val'), align); t.set(qn('w:leader'), leader); t.set(qn('w:pos'), str(pos_twips))
    tabs.append(t)
    ordered_set(pPr, tabs, PPR_ORDER)


def set_run(r, east=FS, size=14, bold=False, color=INK, sup=False, italic=False):
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    if color is not None:
        r.font.color.rgb = color
    if sup:
        r.font.superscript = True
    rPr = r._element.get_or_add_rPr()
    rf = rPr.get_or_add_rFonts()
    rf.set(qn('w:ascii'), 'Times New Roman')
    rf.set(qn('w:hAnsi'), 'Times New Roman')
    rf.set(qn('w:cs'), 'Times New Roman')
    rf.set(qn('w:eastAsia'), east)
    rf.set(qn('w:hint'), 'eastAsia')
    return r


def add_text(p, text, east=FS, size=14, bold=False, color=INK, kai_brackets=True, sup=False):
    if kai_brackets and not sup:
        for seg, br in split_brackets(text):
            r = p.add_run(seg)
            set_run(r, KAI if br else east, size, bold, color)
    else:
        r = p.add_run(text)
        set_run(r, east, size, bold, color, sup=sup)


def bookmark(p, name, bid):
    el = p._element
    bs = OxmlElement('w:bookmarkStart'); bs.set(qn('w:id'), str(bid)); bs.set(qn('w:name'), name)
    be = OxmlElement('w:bookmarkEnd'); be.set(qn('w:id'), str(bid))
    pPr = el.find(qn('w:pPr'))
    if pPr is not None:
        pPr.addnext(bs)
    else:
        el.insert(0, bs)
    el.append(be)


def _fld(t):
    r = OxmlElement('w:r'); fc = OxmlElement('w:fldChar')
    fc.set(qn('w:fldCharType'), t); r.append(fc)
    return r


def _instr(code, east=FS, size=14):
    r = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    rf = OxmlElement('w:rFonts')
    for k in ('ascii', 'hAnsi', 'cs'):
        rf.set(qn('w:' + k), 'Times New Roman')
    rf.set(qn('w:eastAsia'), east); rf.set(qn('w:hint'), 'eastAsia')
    rPr.append(rf)
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), str(int(size * 2))); rPr.append(sz)
    r.append(rPr)
    it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = code
    r.append(it)
    return r


def wrap_field(p, code, east=FS, size=14):
    """把段落内全部 run 包进一个域：begin/instr/separate/…/end。"""
    el = p._element
    runs = [r for r in el.findall(qn('w:r'))]
    if not runs:
        return
    runs[0].addprevious(_fld('begin'))
    runs[0].addprevious(_instr(code, east, size))
    runs[0].addprevious(_fld('separate'))
    runs[-1].addnext(_fld('end'))


def field_inline(p, code, result, east=FS, size=14, color=INK, bold=False):
    """在段落末尾追加一个带缓存结果的域（SEQ / PAGE）。"""
    el = p._element
    el.append(_fld('begin'))
    el.append(_instr(code, east, size))
    el.append(_fld('separate'))
    r = p.add_run(result)
    set_run(r, east, size, bold, color)
    el.append(_fld('end'))


class DocxBuilder:
    def __init__(self, ctx, column='本期聚焦｜FOCUS', issue='特情 · 2026年10月',
                 classification='非密·内部资料'):
        self.ctx = ctx
        self.column = column
        self.issue = issue
        self.classification = classification
        self.doc = Document()
        self.bid = 100
        self.fig_n = 0
        self.tab_n = 0
        self._setup()

    # ---- 页面
    def _page(self, s, zero=False):
        s.page_width, s.page_height = Cm(21.0), Cm(29.7)
        if zero:
            s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Cm(0)
            s.header_distance = s.footer_distance = Cm(0)
        else:
            s.top_margin, s.bottom_margin = Cm(2.6), Cm(2.4)
            s.left_margin, s.right_margin = Cm(2.5), Cm(2.5)
            s.header_distance, s.footer_distance = Cm(1.2), Cm(1.1)

    def _setup(self):
        d = self.doc
        bg = OxmlElement('w:background'); bg.set(qn('w:color'), CREAM)
        d.element.insert(0, bg)
        d.settings.element.append(OxmlElement('w:displayBackgroundShape'))
        # 默认样式字体
        st = d.styles['Normal']
        st.font.name = 'Times New Roman'; st.font.size = Pt(14)
        rf = st.element.get_or_add_rPr().get_or_add_rFonts()
        rf.set(qn('w:eastAsia'), FS); rf.set(qn('w:hint'), 'eastAsia')
        self._page(d.sections[0], zero=True)

    def new_section(self, kind):
        s = self.doc.add_section(WD_SECTION.NEW_PAGE)
        self._page(s, zero=(kind in ('cover', 'back')))
        parts = [s.footer, s.first_page_footer, s.even_page_footer]
        if kind in ('digest', 'back'):
            parts += [s.header, s.first_page_header, s.even_page_header]
        for part in parts:
            part.is_linked_to_previous = False
        for part in ([s.header] if kind in ('digest', 'back') else []) + [s.footer]:
            for p in part.paragraphs:
                for r in list(p.runs):
                    r._element.getparent().remove(r._element)
        return s

    def pg_start(self, s, start=1):
        sectPr = s._sectPr
        pg = OxmlElement('w:pgNumType'); pg.set(qn('w:start'), str(start))
        # pgNumType 位于 pgMar 之后、cols 之前
        cols = sectPr.find(qn('w:cols'))
        if cols is not None:
            cols.addprevious(pg)
        else:
            sectPr.append(pg)

    def header(self, s):
        hp = s.header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_tabs(hp, 9070, 'right', 'none')
        r = hp.add_run('XIGUANG · INTELLIGENCE REPORT'); set_run(r, HEI, 9, color=NAVY)
        r = hp.add_run('\t《析光》特情 · 2026年10月'); set_run(r, HEI, 9, color=GREY)
        p_border(hp, 'bottom', '12233B', '6')

    def footer(self, s, mode):
        fp = s.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if mode == 'digest':
            r = fp.add_run('特情精要 · '); set_run(r, SONG, 10.5, color=GREY)
            field_inline(fp, ' PAGE ', '1', SONG, 10.5, GREY)
        elif mode == 'front':
            r = fp.add_run('析光·科研情报｜鸿眼·无人体系中心　　看得早·看得懂·看得准·看得透')
            set_run(r, KAI, 9, color=GREY)
        elif mode == 'body':
            r = fp.add_run('— '); set_run(r, SONG, 12, color=INK)
            field_inline(fp, ' PAGE ', '1', SONG, 12, INK)
            r = fp.add_run(' —'); set_run(r, SONG, 12, color=INK)

    # ---- 段落工厂
    def para(self, align=WD_ALIGN_PARAGRAPH.JUSTIFY, indent=True, line=28.6, exact=True,
             before=0, after=0, left=None, keep_next=False):
        p = self.doc.add_paragraph()
        pf = p.paragraph_format
        p.alignment = align
        if line:
            pf.line_spacing = Pt(line)
            pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY if exact else WD_LINE_SPACING.MULTIPLE
        pf.space_before = Pt(before); pf.space_after = Pt(after)
        if indent:
            pf.first_line_indent = Pt(28)
        if left is not None:
            pf.left_indent = Pt(left)
        if keep_next:
            pf.keep_with_next = True
        return p

    def next_bid(self):
        self.bid += 1
        return self.bid

    # ---- 整页图
    def full_image(self, path):
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        pf = p.paragraph_format
        pf.space_before = Pt(0); pf.space_after = Pt(0)
        p.add_run().add_picture(path, width=Cm(21.0), height=Cm(29.66))

    # ---- 刊名区
    def masthead(self):
        p = self.para(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=None, after=2)
        add_text(p, '析光 XIGUANG', HEI, 22, True, NAVY, kai_brackets=False)
        add_text(p, '　｜　鸿眼·科研情报刊物　' + self.issue, KAI, 11, False, GREY, kai_brackets=False)
        p_border(p, 'bottom', 'A8842F', '12')
        p = self.para(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=None, before=6, after=8)
        add_text(p, '◆ ' + self.column, HEI, 11, True, BRASS, kai_brackets=False)

    def title(self, main, sub=None, byline=True):
        p = self.para(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=32, before=12, after=4)
        add_text(p, main, HEI, 20, True, NAVY, kai_brackets=False)
        if sub:
            p = self.para(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=24, after=6)
            add_text(p, sub, KAI, 14, False, GREY, kai_brackets=False)
        if byline:
            p = self.para(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=20, after=10)
            add_text(p, '文｜无人体系中心科技情报组（鸿眼）', KAI, 11, False, GREY, kai_brackets=False)

    def plain_heading(self, text, anchor=None, size=16, outline=0, center=True, before=6, after=10,
                      rule=True):
        p = self.para(WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.LEFT,
                      indent=False, line=None, before=before, after=after)
        add_text(p, text, HEI, size, True, NAVY, kai_brackets=False)
        if rule:
            p_border(p, 'bottom', 'A8842F', '8')
        if outline is not None:
            p_outline(p, outline)
        if anchor:
            bookmark(p, anchor, self.next_bid())
        return p

    # ---- 块渲染
    def render(self, blocks):
        for b in blocks:
            getattr(self, 'b_' + b['t'])(b)

    def b_chapter(self, b):
        p = self.para(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=None, before=18, after=8,
                      keep_next=True)
        if b['num']:
            add_text(p, b['num'] + '、', HEI, 17, True, BRASS, kai_brackets=False)
        add_text(p, norm_text(b['name']), HEI, 15, True, NAVY, kai_brackets=False)
        p_border(p, 'bottom', '12233B', '6')
        p_outline(p, 0)
        bookmark(p, b['anchor'], self.next_bid())

    def b_h1(self, b):
        p = self.para(WD_ALIGN_PARAGRAPH.LEFT, indent=False, before=10, after=2, keep_next=True)
        add_text(p, norm_text(b['text']), HEI, 14, False, NAVY, kai_brackets=False)
        p_outline(p, 1)
        bookmark(p, b['anchor'], self.next_bid())

    def b_h2(self, b):
        p = self.para(WD_ALIGN_PARAGRAPH.LEFT, indent=False, before=8, after=2, keep_next=True)
        if b.get('tag'):
            add_text(p, b['tag'] + '　', HEI, 13, True, BRASS, kai_brackets=False)
        add_text(p, norm_text(b['text']), KAI, 14, True, NAVY, kai_brackets=False)
        p_outline(p, 2)
        if b.get('anchor'):
            bookmark(p, b['anchor'], self.next_bid())

    def b_h3(self, b):
        p = self.para(WD_ALIGN_PARAGRAPH.LEFT, indent=False, before=4, after=0, keep_next=True)
        add_text(p, norm_text(b['text']), HEI, 13, False, NAVY, kai_brackets=False)

    def _inline(self, p, text, size=14, east=FS, color=INK):
        for seg, style in parse_inline(text, self.ctx):
            if style == 'sup':
                add_text(p, seg, east, size, False, ACC, kai_brackets=False, sup=True)
            elif style == 'bold':
                add_text(p, seg, east, size, True, color)
            elif style == 'red':
                add_text(p, seg, east, size, True, ALERT)
            else:
                add_text(p, seg, east, size, False, color)

    def b_p(self, b):
        p = self.para(indent=b.get('indent', True))
        if b.get('head'):
            add_text(p, b['head'], HEI, 14, True, NAVY, kai_brackets=False)
        self._inline(p, b['text'])

    def b_small(self, b):
        p = self.para(indent=False, line=20, before=2, after=2)
        self._inline(p, b['text'], size=11, color=GREY)

    def b_lead(self, b):
        p = self.para(WD_ALIGN_PARAGRAPH.JUSTIFY, indent=False, line=24, before=6, after=12)
        p_shade(p, 'FFFFFF')
        p_border(p, 'left', 'A8842F', '24', '8')
        p.paragraph_format.left_indent = Pt(12); p.paragraph_format.right_indent = Pt(6)
        self._inline(p, b['text'], size=13)

    def b_judge(self, b):
        marks = '①②③④⑤⑥⑦⑧⑨⑩'
        if b.get('title'):
            p = self.para(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=24, before=8, after=0)
            p_shade(p, 'FFFFFF'); p_border(p, 'left', 'A8842F', '24', '8')
            p.paragraph_format.left_indent = Pt(12); p.paragraph_format.right_indent = Pt(6)
            add_text(p, b['title'], HEI, 13, True, BRASS, kai_brackets=False)
        for i, it in enumerate(b['items']):
            p = self.para(WD_ALIGN_PARAGRAPH.JUSTIFY, indent=False, line=24, before=0,
                          after=(10 if i == len(b['items']) - 1 else 0))
            p_shade(p, 'FFFFFF'); p_border(p, 'left', 'A8842F', '24', '8')
            p.paragraph_format.left_indent = Pt(12); p.paragraph_format.right_indent = Pt(6)
            add_text(p, marks[i] + ' ', FS, 13, True, BRASS, kai_brackets=False)
            self._inline(p, it, size=13)

    def b_figure(self, b):
        src = b.get('local')
        if not src or not os.path.exists(src):
            return  # 无原图不收录
        self.fig_n += 1
        p = self.para(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=None, before=8, after=2,
                      keep_next=True)
        w = b.get('width_mm', 150)
        if b.get('kind') == 'photo':
            from PIL import Image as _I
            iw, ih = _I.open(src).size
            if ih / iw > 0.72:
                b = dict(b, height_mm=min(110, 140 * ih / iw))
        if b.get('height_mm'):
            p.add_run().add_picture(src, height=Mm(b['height_mm']))
        else:
            p.add_run().add_picture(src, width=Mm(w))
        c = self.para(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=20, after=2)
        add_text(c, '图', KAI, 12, False, GREY, kai_brackets=False)
        field_inline(c, ' SEQ 图 \\* ARABIC ', str(self.fig_n), KAI, 12, GREY)
        add_text(c, '  ' + norm_text(b['caption']), KAI, 12, False, GREY, kai_brackets=False)
        bookmark(c, 'fig_%d' % self.fig_n, self.next_bid())
        self.ctx.setdefault('docx_figs', []).append((self.fig_n, b['caption'], 'fig_%d' % self.fig_n))
        if b.get('source'):
            s = self.para(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=18, after=10)
            for seg, style in parse_inline('来源：' + b['source'], self.ctx):
                add_text(s, seg, KAI, 10.5, False, ACC if style == 'sup' else GREY,
                         kai_brackets=False, sup=(style == 'sup'))

    def _cell_shade(self, cell, fill):
        tcPr = cell._tc.get_or_add_tcPr()
        sh = OxmlElement('w:shd'); sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto')
        sh.set(qn('w:fill'), fill)
        ordered_set(tcPr, sh, TCPR_ORDER)

    def _cell_width(self, cell, mm):
        tcPr = cell._tc.get_or_add_tcPr()
        w = OxmlElement('w:tcW'); w.set(qn('w:w'), str(int(mm * 56.7))); w.set(qn('w:type'), 'dxa')
        ordered_set(tcPr, w, TCPR_ORDER)

    def _cell_valign(self, cell, v='center'):
        tcPr = cell._tc.get_or_add_tcPr()
        e = OxmlElement('w:vAlign'); e.set(qn('w:val'), v)
        ordered_set(tcPr, e, TCPR_ORDER)

    def _table(self, headers, rows, widths, size, header_fill='EFEBDF', first_col_bold=False,
               aligns=None):
        ncol = len(widths)
        t = self.doc.add_table(rows=(1 if headers else 0) + len(rows), cols=ncol)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl = t._tbl
        tblPr = tbl.tblPr
        # 去掉默认样式
        st = tblPr.find(qn('w:tblStyle'))
        if st is not None:
            tblPr.remove(st)
        tw = OxmlElement('w:tblW'); tw.set(qn('w:w'), str(int(sum(widths) * 56.7))); tw.set(qn('w:type'), 'dxa')
        ordered_set(tblPr, tw, TBLPR_ORDER)
        bd = OxmlElement('w:tblBorders')
        for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
            e = OxmlElement('w:' + edge)
            e.set(qn('w:val'), 'single')
            e.set(qn('w:sz'), '8' if edge in ('top', 'bottom') else '4')
            e.set(qn('w:space'), '0')
            e.set(qn('w:color'), '12233B' if edge in ('top', 'bottom') else 'C9C2B0')
            bd.append(e)
        ordered_set(tblPr, bd, TBLPR_ORDER)
        lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed')
        ordered_set(tblPr, lay, TBLPR_ORDER)
        mar = OxmlElement('w:tblCellMar')
        for edge, v in (('top', 30), ('left', 70), ('bottom', 30), ('right', 70)):
            e = OxmlElement('w:' + edge); e.set(qn('w:w'), str(v)); e.set(qn('w:type'), 'dxa')
            mar.append(e)
        ordered_set(tblPr, mar, TBLPR_ORDER)
        grid = tbl.tblGrid
        for gc, wmm in zip(grid.findall(qn('w:gridCol')), widths):
            gc.set(qn('w:w'), str(int(wmm * 56.7)))
        all_rows = ([headers] if headers else []) + rows
        for ri, row in enumerate(all_rows):
            tr = t.rows[ri]
            if headers and ri == 0:
                trPr = tr._tr.get_or_add_trPr()
                h = OxmlElement('w:tblHeader'); trPr.append(h)
            trPr = tr._tr.get_or_add_trPr()
            cs = OxmlElement('w:cantSplit'); trPr.insert(0, cs)
            for ci in range(ncol):
                val = row[ci] if ci < len(row) else ''
                cell = tr.cells[ci]
                self._cell_width(cell, widths[ci])
                self._cell_valign(cell)
                p = cell.paragraphs[0]
                pf = p.paragraph_format
                pf.space_before = Pt(1); pf.space_after = Pt(1)
                pf.line_spacing = 1.15; pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
                is_head = headers and ri == 0
                if is_head:
                    self._cell_shade(cell, header_fill)
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    add_text(p, norm_text(str(val)), HEI, size, True, NAVY, kai_brackets=False)
                else:
                    al = (aligns[ci] if aligns else 'left')
                    p.alignment = {'left': WD_ALIGN_PARAGRAPH.LEFT, 'center': WD_ALIGN_PARAGRAPH.CENTER,
                                   'just': WD_ALIGN_PARAGRAPH.JUSTIFY}[al]
                    bold = first_col_bold and ci == 0
                    for seg, style in parse_inline(str(val), self.ctx):
                        if style == 'sup':
                            add_text(p, seg, FS, size, False, ACC, kai_brackets=False, sup=True)
                        else:
                            add_text(p, seg, HEI if bold else FS, size, bold or style == 'bold',
                                     NAVY if bold else (ALERT if style == 'red' else INK),
                                     kai_brackets=False)
                    if first_col_bold and ci == 0:
                        self._cell_shade(cell, 'F2EEE3')
        return t

    def b_table(self, b):
        c = self.para(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=20, before=8, after=4,
                      keep_next=True)
        if b.get('nonum'):
            add_text(c, norm_text(b['caption']), HEI, 12, True, NAVY, kai_brackets=False)
        else:
            self.tab_n += 1
            add_text(c, '表', KAI, 12, False, GREY, kai_brackets=False)
            field_inline(c, ' SEQ 表 \\* ARABIC ', str(self.tab_n), KAI, 12, GREY)
            add_text(c, '  ' + norm_text(b['caption']), KAI, 12, False, GREY, kai_brackets=False)
            bookmark(c, 'tab_%d' % self.tab_n, self.next_bid())
            self.ctx.setdefault('docx_tabs', []).append((self.tab_n, b['caption'], 'tab_%d' % self.tab_n))
        ncol = len(b['headers'])
        size = b.get('size') or (10.5 if ncol <= 4 else 9.5 if ncol <= 6 else 8.5)
        widths = b.get('widths') or [160.0 / ncol] * ncol
        self._table(b['headers'], b['rows'], widths, size, aligns=b.get('aligns'))
        s = self.para(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=18, before=2, after=10)
        for seg, style in parse_inline('来源：' + (b.get('source') or '本报告整理'), self.ctx):
            add_text(s, seg, KAI, 10.5, False, ACC if style == 'sup' else GREY,
                     kai_brackets=False, sup=(style == 'sup'))

    def b_kv(self, b):
        """案例要素表：四列 键|值|键|值，无编号（案例卡片）。"""
        rows = b['rows']
        if b.get('cols', 4) == 4:
            grid = []
            i = 0
            while i < len(rows):
                k1, v1 = rows[i]
                if b.get('wide') and k1 in b['wide']:
                    grid.append([k1, v1, None, None]); i += 1; continue
                if i + 1 < len(rows) and not (b.get('wide') and rows[i + 1][0] in b['wide']):
                    k2, v2 = rows[i + 1]; grid.append([k1, v1, k2, v2]); i += 2
                else:
                    grid.append([k1, v1, None, None]); i += 1
            t = self._table(None, [[g[0], g[1], g[2] or '', g[3] or ''] for g in grid],
                            [22, 58, 22, 58], 10.5)
            # 合并宽行
            for ri, g in enumerate(grid):
                if g[2] is None:
                    a = t.cell(ri, 1).merge(t.cell(ri, 3))
                    # 清理合并后多余空段落
                    ps = a.paragraphs
                    for extra in ps[1:]:
                        if not extra.text.strip():
                            extra._element.getparent().remove(extra._element)
            for ri in range(len(grid)):
                for ci in (0, 2):
                    try:
                        cell = t.cell(ri, ci)
                    except Exception:
                        continue
                    if ci == 2 and grid[ri][2] is None:
                        continue
                    self._cell_shade(cell, 'EFEBDF')
                    for p in cell.paragraphs:
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        for r in p.runs:
                            set_run(r, HEI, 10.5, True, NAVY)
        sp = self.para(indent=False, line=8, after=4)

    def b_pagebreak(self, b):
        p = self.doc.add_paragraph()
        p.add_run().add_break(WD_BREAK.PAGE)

    def b_close(self, b):
        p = self.para(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=None, before=14)
        p_border(p, 'bottom', 'A8842F', '6')
        p = self.para(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=None, before=4)
        add_text(p, '—— 本文完 ｜《析光》2026年10月特情 · 本期聚焦 ——', KAI, 10, False, GREY,
                 kai_brackets=False)

    def refs(self, anchor='refs'):
        self.b_chapter({'num': '', 'name': '参考文献', 'anchor': anchor}) if False else None
        p = self.para(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=None, before=18, after=8)
        add_text(p, '参考文献', HEI, 15, True, NAVY, kai_brackets=False)
        p_border(p, 'bottom', '12233B', '6'); p_outline(p, 0)
        bookmark(p, anchor, self.next_bid())
        R = self.ctx['refs']
        for i, key in enumerate(R.order, 1):
            r = R.by_key[key]
            p = self.para(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=20, after=0)
            p.paragraph_format.left_indent = Pt(30); p.paragraph_format.first_line_indent = Pt(-30)
            add_text(p, '[%d] ' % i, FS, 12, False, INK, kai_brackets=False)
            add_text(p, norm_ref(ref_entry(r)), FS, 12, False, INK, kai_brackets=False)
            url = r.get('url')
            if url:
                q = self.para(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=15, after=3)
                q.paragraph_format.left_indent = Pt(30)
                add_text(q, url, FS, 10, False, ACC, kai_brackets=False)
                wrap_field(q, ' HYPERLINK "%s" ' % url.replace('"', '%22'), FS, 10)

    # ---- 目录
    def toc_entry(self, text, page, anchor, level=0, size=None):
        indent = {0: 0, 1: 21, 2: 42}[level]
        size = size or {0: 13, 1: 12, 2: 11}[level]
        p = self.para(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=(24 if level == 0 else 21),
                      before=(4 if level == 0 else 0), after=0, left=indent)
        p_tabs(p, 9070, 'right', 'dot')
        east = HEI if level == 0 else (FS if level == 1 else KAI)
        add_text(p, norm_text(text), east, size, level == 0, NAVY if level == 0 else INK,
                 kai_brackets=False)
        add_text(p, '\t' + (str(page) if page else ''), 'Times New Roman', size, level == 0,
                 NAVY if level == 0 else INK, kai_brackets=False)
        wrap_field(p, ' HYPERLINK \\l "%s" ' % anchor, east, size)

    def save(self, path):
        self.doc.save(path)


def norm_ref(s):
    """参考文献著录：保留半角点号，只做最小归一。"""
    return s.replace(' ', ' ')


# ================================================================= HTML
HTML_CSS = r"""
:root{--cream:#F7F4EC;--grid:#E9E4D6;--navy:#12233B;--accent:#2E93D6;--brass:#A8842F;--alert:#C0392B;--grey:#8A8474;--ink:#222;--head:#EFEBDF}
*{box-sizing:border-box}
html{background:var(--cream);overflow-x:hidden}
p,td,th,div,figcaption,h2,h3,h4,h5{overflow-wrap:anywhere;word-break:break-word}
body{background:var(--cream);color:var(--ink);font-family:"仿宋_GB2312","FangSong","STFangsong","Noto Serif CJK SC","Songti SC",serif;font-size:17px;line-height:1.9;max-width:860px;margin:0 auto;padding:0 18px 60px}
h1,h2,h3,h4,.hei{font-family:"黑体","SimHei","Noto Sans CJK SC","PingFang SC","Microsoft YaHei",sans-serif;color:var(--navy)}
.kai,figcaption,.src{font-family:"楷体_GB2312","KaiTi","STKaiti","AR PL UKai CN",serif}
a{color:var(--accent);text-decoration:none}
.band{background:var(--navy);color:#fff;display:flex;justify-content:space-between;align-items:center;font-family:"黑体",sans-serif;font-size:12px;letter-spacing:.12em;padding:8px 16px;margin:0 -18px}
.cover{text-align:center;padding:30px 0 10px}
.cover img{max-width:100%;box-shadow:0 2px 14px rgba(18,35,59,.15)}
.mast{display:flex;align-items:baseline;gap:14px;border-bottom:3px solid var(--brass);padding:18px 0 6px;margin-top:24px}
.mast b{font-family:"黑体",sans-serif;font-size:30px;color:var(--navy)}
.mast span{font-family:"楷体_GB2312","KaiTi",serif;color:var(--grey)}
.colbar{color:var(--brass);font-family:"黑体",sans-serif;font-weight:bold;margin:8px 0 6px}
.title{text-align:center;font-size:26px;margin:18px 0 4px;line-height:1.4}
.subtitle{text-align:center;color:var(--grey);font-family:"楷体_GB2312","KaiTi",serif;font-size:18px}
.byline{text-align:center;color:var(--grey);font-size:14px;font-family:"楷体_GB2312","KaiTi",serif;margin-bottom:12px}
p{text-indent:2em;margin:0 0 .25em;text-align:justify}
p.noind{text-indent:0}
.lead,.judge{background:#fff;border-left:5px solid var(--brass);padding:12px 16px;margin:14px 0;font-size:16px;line-height:1.8}
.judge .jt{font-family:"黑体",sans-serif;color:var(--brass);font-weight:bold;margin-bottom:4px}
.judge p{text-indent:0;margin:.25em 0}
.judge .mk{color:var(--brass);font-weight:bold;margin-right:4px}
h2.chapter{font-size:22px;border-bottom:1.5px solid var(--navy);padding-bottom:4px;margin:38px 0 12px}
h2.chapter .num{color:var(--brass);font-size:24px;margin-right:4px}
h3.h1{font-size:18px;margin:22px 0 6px}
h4.h2{font-family:"楷体_GB2312","KaiTi","STKaiti",serif;font-size:18px;margin:20px 0 6px;color:var(--navy)}
h4.h2 .tag{font-family:"黑体",sans-serif;color:var(--brass);font-size:15px;margin-right:8px}
h5.h3{font-size:16px;margin:12px 0 2px;color:var(--navy)}
figure{margin:16px 0 14px;text-align:center}
figure img{max-width:100%;height:auto;border:1px solid var(--grid);background:#fff}
figure.photo img{max-height:520px}
figcaption{color:var(--grey);font-size:15px;line-height:1.6;margin-top:6px}
figcaption .src{display:block;font-size:13px}
.img-fallback{display:none;border:1px dashed var(--grey);padding:18px;color:var(--grey);font-size:14px;background:#fff}
.tcap{text-align:center;color:var(--grey);font-family:"楷体_GB2312","KaiTi",serif;font-size:15px;margin:16px 0 4px}
.tsrc{color:var(--grey);font-family:"楷体_GB2312","KaiTi",serif;font-size:13px;margin:4px 0 14px}
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;width:100%;font-size:14px;line-height:1.5;background:#fff}
th{background:var(--head);color:var(--navy);font-family:"黑体",sans-serif;padding:5px 6px;border:1px solid #C9C2B0}
td{padding:5px 6px;border:1px solid #DCD5C3;vertical-align:middle}
table.kv{table-layout:fixed}
table.kv td.k{background:var(--head);color:var(--navy);font-family:"黑体",sans-serif;font-weight:bold;text-align:center;width:5.2em}
table{border-top:2px solid var(--navy);border-bottom:2px solid var(--navy)}
sup{color:var(--accent);font-size:.68em}
.red{color:var(--alert);font-weight:bold}
.toc a{color:var(--ink)}
.toc .l0{font-family:"黑体",sans-serif;font-weight:bold;color:var(--navy);margin-top:8px}
.toc .l1{padding-left:1.5em}
.toc .l2{padding-left:3em;font-size:15px;font-family:"楷体_GB2312","KaiTi",serif}
.toc div{line-height:1.7}
.digest{background:#FBF9F3;border:1px solid var(--grid);padding:8px 22px 18px;margin:26px 0}
.digest h2{text-align:center;font-size:24px;border-bottom:2px solid var(--brass);padding-bottom:6px}
.refs p{text-indent:-2.2em;padding-left:2.2em;font-size:14px;line-height:1.6;margin-bottom:6px}
.refs a{word-break:break-all;font-size:12.5px}
.close{text-align:center;color:var(--grey);font-family:"楷体_GB2312","KaiTi",serif;font-size:14px;border-top:1px solid var(--brass);margin-top:30px;padding-top:8px}
.brand{background:var(--navy);color:#fff;text-align:center;padding:12px;margin:30px -18px 0;font-family:"黑体",sans-serif;font-size:13px;letter-spacing:.08em}
.casecard{border-top:1px dashed var(--grid);margin-top:10px}
@media (max-width:640px){body{font-size:15px;line-height:1.8;padding:0 16px 40px}table.kv td.k{width:4.2em;font-size:12px}.band{font-size:10px;margin:0 -12px}.title{font-size:21px}h2.chapter{font-size:19px}table{font-size:12.5px}.mast b{font-size:24px}.brand{margin:30px -12px 0}}
"""


class HtmlBuilder:
    def __init__(self, ctx):
        self.ctx = ctx
        self.parts = []
        self.fig_n = 0
        self.tab_n = 0
        self.toc = []  # (level, text, anchor)

    def _inline(self, text):
        out = []
        for seg, style in parse_inline(text, self.ctx):
            e = html.escape(seg)
            if style == 'bold':
                out.append('<b>%s</b>' % e)
            elif style == 'sup':
                nums = re.findall(r'\d+', seg)
                first = nums[0] if nums else '1'
                out.append('<sup><a href="#ref%s">%s</a></sup>' % (first, e))
            elif style == 'red':
                out.append('<span class="red">%s</span>' % e)
            else:
                out.append(e)
        return ''.join(out)

    def add(self, s):
        self.parts.append(s)

    def render(self, blocks):
        for b in blocks:
            getattr(self, 'b_' + b['t'])(b)

    def b_chapter(self, b):
        t = ('%s、%s' % (b['num'], b['name'])) if b['num'] else b['name']
        self.toc.append((0, t, b['anchor']))
        num = '<span class="num">%s、</span>' % b['num'] if b['num'] else ''
        self.add('<h2 class="chapter" id="%s">%s%s</h2>' % (b['anchor'], num, html.escape(b['name'])))

    def b_h1(self, b):
        self.toc.append((1, b['text'], b['anchor']))
        self.add('<h3 class="h1" id="%s">%s</h3>' % (b['anchor'], html.escape(norm_text(b['text']))))

    def b_h2(self, b):
        if b.get('toc') and b.get('anchor'):
            self.toc.append((2, ((b.get('tag') or '') + ' ' + b['text']).strip(), b['anchor']))
        tag = '<span class="tag">%s</span>' % html.escape(b['tag']) if b.get('tag') else ''
        idattr = ' id="%s"' % b['anchor'] if b.get('anchor') else ''
        self.add('<h4 class="h2"%s>%s%s</h4>' % (idattr, tag, html.escape(norm_text(b['text']))))

    def b_h3(self, b):
        self.add('<h5 class="h3">%s</h5>' % html.escape(norm_text(b['text'])))

    def b_p(self, b):
        head = '<b class="hei" style="color:var(--navy)">%s</b>' % html.escape(b['head']) if b.get('head') else ''
        cls = '' if b.get('indent', True) else ' class="noind"'
        self.add('<p%s>%s%s</p>' % (cls, head, self._inline(b['text'])))

    def b_small(self, b):
        self.add('<p class="noind" style="font-size:13px;color:var(--grey)">%s</p>' % self._inline(b['text']))

    def b_lead(self, b):
        self.add('<div class="lead">%s</div>' % self._inline(b['text']))

    def b_judge(self, b):
        marks = '①②③④⑤⑥⑦⑧⑨⑩'
        s = '<div class="judge">'
        if b.get('title'):
            s += '<div class="jt">%s</div>' % html.escape(b['title'])
        for i, it in enumerate(b['items']):
            s += '<p><span class="mk">%s</span>%s</p>' % (marks[i], self._inline(it))
        self.add(s + '</div>')

    def b_figure(self, b):
        self.fig_n += 1
        anchor = 'hfig_%d' % self.fig_n
        self.ctx.setdefault('html_figs', []).append((self.fig_n, b['caption'], anchor))
        cap = '图%d  %s' % (self.fig_n, html.escape(norm_text(b['caption'])))
        src = '<span class="src">来源：%s</span>' % self._inline(b['source']) if b.get('source') else ''
        if b.get('remote_url'):
            url = html.escape(b['remote_url'])
            page = html.escape(b.get('page_url') or b['remote_url'])
            self.add('<figure class="photo" id="%s"><img loading="lazy" src="%s" alt="%s" '
                     'onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'block\'">'
                     '<div class="img-fallback">图片需联网加载 · <a href="%s" target="_blank">点击查看原图</a></div>'
                     '<figcaption>%s%s</figcaption></figure>' % (anchor, url, cap, page, cap, src))
        else:
            with open(b['local'], 'rb') as f:
                data = base64.b64encode(f.read()).decode()
            mime = 'image/png' if b['local'].endswith('.png') else 'image/jpeg'
            self.add('<figure id="%s"><img src="data:%s;base64,%s" alt="%s"><figcaption>%s%s</figcaption></figure>'
                     % (anchor, mime, data, cap, cap, src))

    def b_table(self, b):
        if b.get('nonum'):
            s = '<div class="tcap" style="font-family:黑体,sans-serif;color:var(--navy);font-weight:bold">%s</div><div class="tw"><table><thead><tr>' % html.escape(norm_text(b['caption']))
        else:
            self.tab_n += 1
            anchor = 'htab_%d' % self.tab_n
            self.ctx.setdefault('html_tabs', []).append((self.tab_n, b['caption'], anchor))
            s = '<div class="tcap" id="%s">表%d  %s</div><div class="tw"><table><thead><tr>' % (
                anchor, self.tab_n, html.escape(norm_text(b['caption'])))
        s += ''.join('<th>%s</th>' % html.escape(norm_text(h)) for h in b['headers'])
        s += '</tr></thead><tbody>'
        for row in b['rows']:
            s += '<tr>' + ''.join('<td>%s</td>' % self._inline(str(c)) for c in row) + '</tr>'
        s += '</tbody></table></div><div class="tsrc">来源：%s</div>' % self._inline(b.get('source') or '本报告整理')
        self.add(s)

    def b_kv(self, b):
        s = '<div class="tw"><table class="kv"><tbody>'
        rows = b['rows']
        i = 0
        while i < len(rows):
            k1, v1 = rows[i]
            if (b.get('wide') and k1 in b['wide']) or i + 1 >= len(rows) or (b.get('wide') and rows[i + 1][0] in b['wide']):
                s += '<tr><td class="k">%s</td><td colspan="3">%s</td></tr>' % (html.escape(k1), self._inline(v1))
                i += 1
            else:
                k2, v2 = rows[i + 1]
                s += '<tr><td class="k">%s</td><td>%s</td><td class="k">%s</td><td>%s</td></tr>' % (
                    html.escape(k1), self._inline(v1), html.escape(k2), self._inline(v2))
                i += 2
        self.add(s + '</tbody></table></div>')

    def b_pagebreak(self, b):
        pass

    def b_close(self, b):
        self.add('<div class="close">—— 本文完 ｜《析光》2026年10月特情 · 本期聚焦 ——</div>')

    def refs_html(self):
        R = self.ctx['refs']
        s = '<h2 class="chapter" id="refs">参考文献</h2><div class="refs">'
        for i, key in enumerate(R.order, 1):
            r = R.by_key[key]
            url = r.get('url') or ''
            s += '<p class="noind" id="ref%d">[%d] %s<br><a href="%s" target="_blank">%s</a></p>' % (
                i, i, html.escape(ref_entry(r)), html.escape(url), html.escape(url))
        return s + '</div>'
