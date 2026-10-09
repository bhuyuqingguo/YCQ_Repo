# -*- coding: utf-8 -*-
"""
《析光》刊物 docx 构建模块（定版）

用法：
    from xiguang_docx import XiguangDoc
    d = XiguangDoc(classification='非密·内部资料', issue='2026年第3期', column='环球瞭望｜GLOBAL WATCH')
    d.title('无人上舰第一步，为什么是加油机', sub='——美海军MQ-25A"黄貂鱼"研发情况全景调研')
    d.byline()
    d.lead('本文以……为切口，判断……')
    d.chapter('壹', '态势与背景')
    d.body('正文段落。', head='其一，')
    d.figure('fig1.png', '图1  研制时间线（数据来源：波音公司新闻稿）', width_mm=145)
    d.refs([('波音公司. MQ-25 完成第二次试飞[EB/OL]. 2026-07-08.', 'https://example.com')])
    d.close_line()
    d.save('out.docx')

关键约束（改动前先读 references/版式规范.md）：
- 正文 仿宋_GB2312 14pt / 固定行距 28.6pt
- 标题作为普通段落设 outlineLvl，不用 Heading 样式
- 图片宽度单位：1 docx unit ≈ 0.2635mm，145mm -> 550
"""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ---------- 析光定版调色板 ----------
CREAM = 'F7F4EC'
NAVY  = RGBColor(0x12, 0x23, 0x3B)
ACC   = RGBColor(0x2E, 0x93, 0xD6)
BRASS = RGBColor(0xA8, 0x84, 0x2F)
ALERT = RGBColor(0xC0, 0x39, 0x2B)
GREY  = RGBColor(0x8A, 0x84, 0x74)
INK   = RGBColor(0x22, 0x22, 0x22)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

MM_PER_UNIT = 0.2635  # 实测标定：ImageRun/add_picture 宽度单位换算


def mm_to_units(mm):
    """毫米 -> docx 图片宽度单位。切勿传 twip。"""
    return int(round(mm / MM_PER_UNIT))


def set_fonts(run, east, size, bold=False, color=INK, latin='Times New Roman'):
    """CJK 字体必须手写 w:eastAsia，只设 run.font.name 仅影响拉丁字符。"""
    run.font.name = latin
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    rFonts.set(qn('w:eastAsia'), east)
    rFonts.set(qn('w:ascii'), latin)
    rFonts.set(qn('w:hAnsi'), latin)


def _rule(p, hexcolor, edge='bottom', sz='6'):
    pPr = p._element.get_or_add_pPr()
    bd = pPr.find(qn('w:pBdr'))
    if bd is None:
        bd = OxmlElement('w:pBdr')
        pPr.append(bd)
    e = OxmlElement('w:' + edge)
    e.set(qn('w:val'), 'single')
    e.set(qn('w:sz'), sz)
    e.set(qn('w:space'), '4')
    e.set(qn('w:color'), hexcolor)
    bd.append(e)


def _shade(p, hexcolor):
    pPr = p._element.get_or_add_pPr()
    sh = OxmlElement('w:shd')
    sh.set(qn('w:val'), 'clear')
    sh.set(qn('w:fill'), hexcolor)
    pPr.append(sh)


def _outline(p, lvl):
    pPr = p._element.get_or_add_pPr()
    o = OxmlElement('w:outlineLvl')
    o.set(qn('w:val'), str(lvl))
    pPr.append(o)


class XiguangDoc:
    def __init__(self, classification='非密·内部资料',
                 issue='2026年·第三季度', column='本期聚焦｜FOCUS'):
        self.classification = classification
        self.issue = issue
        self.column = column
        self.doc = Document()
        self._page()
        self._background()
        self._header_footer()

    # ---------- 基础设置 ----------
    def _page(self):
        s = self.doc.sections[0]
        s.page_width, s.page_height = Cm(21.0), Cm(29.7)
        s.top_margin, s.bottom_margin = Cm(2.6), Cm(2.4)
        s.left_margin, s.right_margin = Cm(2.5), Cm(2.5)
        s.header_distance, s.footer_distance = Cm(1.2), Cm(1.1)

    def _background(self):
        """米色纸底：两步都要设，缺一在 Word 中不显示。"""
        bg = OxmlElement('w:background')
        bg.set(qn('w:color'), CREAM)
        self.doc.element.insert(0, bg)
        dbs = OxmlElement('w:displayBackgroundShape')
        self.doc.settings.element.append(dbs)

    def _header_footer(self):
        s = self.doc.sections[0]
        # 页眉
        hp = s.header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = hp.add_run('XIGUANG · INTELLIGENCE REPORT')
        set_fonts(r, '黑体', 9, color=NAVY)
        r = hp.add_run('\t\t' + self.classification)
        set_fonts(r, '黑体', 9, color=GREY)
        _rule(hp, '12233B', 'bottom', '6')
        # 页脚
        fp = s.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = fp.add_run('析光·科研情报｜鸿眼·无人体系中心　　看得早·看得懂·看得准·看得透')
        set_fonts(r, '楷体_GB2312', 9, color=GREY)

    def _p(self, align=WD_ALIGN_PARAGRAPH.JUSTIFY, indent=True,
           line=28.6, exact=True, before=0, after=0):
        p = self.doc.add_paragraph()
        pf = p.paragraph_format
        p.alignment = align
        if line:
            pf.line_spacing = Pt(line)
            pf.line_spacing_rule = (WD_LINE_SPACING.EXACTLY if exact
                                    else WD_LINE_SPACING.MULTIPLE)
        pf.space_before = Pt(before)
        pf.space_after = Pt(after)
        if indent:
            pf.first_line_indent = Pt(28)  # 2字符 @14pt
        return p

    # ---------- 版面构件 ----------
    def masthead(self):
        """刊名区 + 栏目条。单篇模式在正文最前调用。"""
        p = self._p(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=None, after=2)
        r = p.add_run('析光 XIGUANG')
        set_fonts(r, '黑体', 22, bold=True, color=NAVY)
        r = p.add_run('　｜　鸿眼·科研情报刊物　' + self.issue)
        set_fonts(r, '楷体_GB2312', 11, color=GREY)
        _rule(p, 'A8842F', 'bottom', '12')
        p = self._p(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=None,
                    before=6, after=8)
        r = p.add_run('◆ ' + self.column)
        set_fonts(r, '黑体', 11, bold=True, color=BRASS)

    def title(self, main, sub=None):
        p = self._p(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=30,
                    before=12, after=4)
        r = p.add_run(main)
        set_fonts(r, '黑体', 19, bold=True, color=NAVY)
        _outline(p, 0)
        if sub:
            p = self._p(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=22, after=6)
            r = p.add_run(sub)
            set_fonts(r, '楷体_GB2312', 14, color=GREY)

    def byline(self, text='文｜无人体系中心科技情报组（鸿眼）'):
        p = self._p(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=20, after=10)
        r = p.add_run(text)
        set_fonts(r, '楷体_GB2312', 11, color=GREY)

    def lead(self, text):
        """导读框：白底 + 左侧黄铜金竖线。"""
        p = self._p(WD_ALIGN_PARAGRAPH.JUSTIFY, indent=False, line=24,
                    before=6, after=12)
        _shade(p, 'FFFFFF')
        _rule(p, 'A8842F', 'left', '18')
        p.paragraph_format.left_indent = Pt(12)
        p.paragraph_format.right_indent = Pt(6)
        r = p.add_run(text)
        set_fonts(r, '仿宋_GB2312', 13)

    def chapter(self, num, name):
        """章题：壹/贰/叁 金字 + 藏青章名 + 下压细线。"""
        p = self._p(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=None,
                    before=16, after=6)
        r = p.add_run(num + '　')
        set_fonts(r, '黑体', 17, bold=True, color=BRASS)
        r = p.add_run(name)
        set_fonts(r, '黑体', 15, bold=True, color=NAVY)
        _rule(p, '12233B', 'bottom', '6')
        _outline(p, 1)

    def h1(self, text):
        p = self._p(WD_ALIGN_PARAGRAPH.LEFT, indent=False, before=10, after=2)
        r = p.add_run(text)
        set_fonts(r, '黑体', 14, color=NAVY)
        _outline(p, 2)

    def h2(self, text):
        p = self._p(WD_ALIGN_PARAGRAPH.LEFT, indent=False, before=6, after=0)
        r = p.add_run(text)
        set_fonts(r, '楷体_GB2312', 14, bold=True, color=NAVY)
        _outline(p, 3)

    def body(self, text, head=None):
        """正文段落。head 为提示语（如"其一，"），加粗藏青。"""
        p = self._p()
        if head:
            r = p.add_run(head)
            set_fonts(r, '黑体', 14, bold=True, color=NAVY)
        r = p.add_run(text)
        set_fonts(r, '仿宋_GB2312', 14)
        return p

    def figure(self, path, caption, width_mm=145):
        """图随文走。宽度按毫米传，内部换算，禁止传 twip。"""
        p = self._p(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=None,
                    before=8, after=2)
        p.add_run().add_picture(path, width=Cm(width_mm / 10.0))
        c = self._p(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=22, after=10)
        r = c.add_run(caption)
        set_fonts(r, '楷体_GB2312', 12, color=GREY)

    def refs(self, items, heading='参考文献'):
        """items: [(文献条目, url or None), ...] 悬挂缩进，URL 行 10pt。"""
        p = self._p(WD_ALIGN_PARAGRAPH.LEFT, indent=False, before=16, after=4)
        r = p.add_run(heading)
        set_fonts(r, '黑体', 14, color=NAVY)
        _rule(p, 'A8842F', 'bottom', '6')
        for i, (text, url) in enumerate(items, 1):
            p = self._p(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=20, after=0)
            p.paragraph_format.left_indent = Pt(24)
            p.paragraph_format.first_line_indent = Pt(-24)
            r = p.add_run('[%d] %s' % (i, text))
            set_fonts(r, '仿宋_GB2312', 12)
            if url:
                q = self._p(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=16, after=2)
                q.paragraph_format.left_indent = Pt(24)
                r = q.add_run(url)
                set_fonts(r, '仿宋_GB2312', 10, color=ACC)

    def close_line(self, month=None, column=None):
        p = self._p(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=None, before=14)
        _rule(p, 'A8842F', 'bottom', '6')
        p = self._p(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=None, before=4)
        r = p.add_run('—— 本文完 ｜《析光》%s · %s ——'
                      % (month or self.issue, (column or self.column).split('｜')[0]))
        set_fonts(r, '楷体_GB2312', 10, color=GREY)

    def brand_band(self):
        """整期尾页品牌带。"""
        p = self._p(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=None, before=16)
        _shade(p, '12233B')
        r = p.add_run('鸿眼 HONGEYE ｜ 析光 XIGUANG · 鸿眼观势 · 锋盾铸魂 · 扶摇育才')
        set_fonts(r, '黑体', 10.5, color=WHITE)

    def page_break(self):
        self.doc.add_page_break()

    def save(self, path):
        self.doc.save(path)
        return path
