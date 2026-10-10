# -*- coding: utf-8 -*-
"""
《Lattice 与 Maven 系统调研》专题图文版组装：标记源稿 -> docx（多遍回填页码）/ PDF / HTML 图文热链版。

复用《析光》排版引擎 xgengine（特情汇编目录），本文件只做：
  源稿解析（含 !photo 实物照片）、引注库加载、版头版尾文字定制、封面封底、页码回填与 HTML 组装。
标记语法见 content/_SPEC.md。
"""
import glob
import html as H
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
XG = os.path.abspath(os.path.join(HERE, '..', '..', '..', '特情_海上攻防案例汇编', '源稿与脚本', 'build'))
sys.path.insert(0, XG)
sys.path.insert(0, os.path.join(XG, 'scripts'))
import xgengine  # noqa
from xgengine import (DocxBuilder, HtmlBuilder, RefRegistry, HTML_CSS, norm_text, add_text, set_run,  # noqa
                      field_inline, p_border, p_tabs, WD_ALIGN_PARAGRAPH, HEI, KAI, FS, SONG, NAVY, GREY, BRASS, INK)

SP = os.path.abspath(os.path.join(HERE, '..'))
ROOT = os.path.abspath(os.path.join(SP, '..'))
OUT = os.path.join(SP, 'out')
FIGS = os.path.join(SP, 'figs')
IMGS = os.path.join(SP, 'imgs')
CONTENT = os.path.join(HERE, 'content')
PHOTOS = os.path.abspath(os.path.join(ROOT, '..', 'research_notes', 'Lattice与Maven系统调研', 'images_candidates.json'))
for d in (OUT, IMGS):
    os.makedirs(d, exist_ok=True)

TITLE_MAIN = '边缘网格与目标工厂'
TITLE_SUB = '——Anduril Lattice 与 Maven Smart System 两系统深度调研（2017—2026）'
BASENAME = '析光专题_Lattice与Maven系统深度调研'
ISSUE = '专题 · 2026年10月'
COLUMN = '专题调研｜DEEP DIVE'
ACCESS = '2026-10-10'
DELIVER = os.path.join(ROOT, '成品')
MODE = {'name': 'full'}
BRIEF_BASENAME = '析光专题精要_Lattice与Maven系统调研精要'
BRIEF_TITLE_SUB = '——Lattice 与 Maven 两系统调研精要（总结·概括·架构·统计·观点）'

# GB/T 7714 网络文献：访问日期改为本期检索日
_ref_entry = xgengine.ref_entry


def ref_entry(r):
    return _ref_entry(r).replace('[2026-10-09]', '[%s]' % ACCESS)


xgengine.ref_entry = ref_entry


class LMDocx(DocxBuilder):
    def header(self, s):
        hp = s.header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_tabs(hp, 9070, 'right', 'none')
        r = hp.add_run('XIGUANG · DEEP DIVE'); set_run(r, HEI, 9, color=NAVY)
        r = hp.add_run('\t《析光》专题 · Lattice 与 Maven'); set_run(r, HEI, 9, color=GREY)
        p_border(hp, 'bottom', '12233B', '6')

    def footer(self, s, mode):
        fp = s.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if mode == 'digest':
            r = fp.add_run('专题精要 · '); set_run(r, SONG, 10.5, color=GREY)
            field_inline(fp, ' PAGE ', '1', SONG, 10.5, GREY)
        elif mode == 'front':
            r = fp.add_run('析光·科研情报｜鸿眼·无人体系中心　　看得早·看得懂·看得准·看得透')
            set_run(r, KAI, 9, color=GREY)
        elif mode == 'body':
            r = fp.add_run('— '); set_run(r, SONG, 12, color=INK)
            field_inline(fp, ' PAGE ', '1', SONG, 12, INK)
            r = fp.add_run(' —'); set_run(r, SONG, 12, color=INK)

    def b_close(self, b):
        p = self.para(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=None, before=14)
        p_border(p, 'bottom', 'A8842F', '6')
        p = self.para(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=None, before=4)
        add_text(p, '—— 本文完 ｜《析光》2026年10月专题 · Lattice 与 Maven ——', KAI, 10, False, GREY,
                 kai_brackets=False)


class LMHtml(HtmlBuilder):
    def b_figure(self, b):
        if b.get('kind') == 'photo' and b.get('local') and os.path.exists(b['local']):
            # 已有本地原图：压缩后内嵌，保证离线可看；无本地图时才走热链
            import base64, io
            from PIL import Image
            im = Image.open(b['local']).convert('RGB'); im.thumbnail((1100, 1100))
            bio = io.BytesIO(); im.save(bio, 'JPEG', quality=78)
            self.fig_n += 1
            anchor = 'hfig_%d' % self.fig_n
            self.ctx.setdefault('html_figs', []).append((self.fig_n, b['caption'], anchor))
            cap = '图%d  %s' % (self.fig_n, H.escape(norm_text(b['caption'])))
            src = '<span class="src">来源：%s</span>' % self._inline(b['source']) if b.get('source') else ''
            self.add('<figure class="photo" id="%s"><img loading="lazy" src="data:image/jpeg;base64,%s" alt="%s">'
                     '<figcaption>%s%s</figcaption></figure>' % (anchor, base64.b64encode(bio.getvalue()).decode(), cap, cap, src))
            return
        if not b.get('remote_url') and not (b.get('local') and os.path.exists(b['local'])):
            return
        return HtmlBuilder.b_figure(self, b)

    def b_close(self, b):
        self.add('<div class="close">—— 本文完 ｜《析光》2026年10月专题 · Lattice 与 Maven ——</div>')


# ---------------------------------------------------------------- 源稿解析
def photo_index():
    if not os.path.exists(PHOTOS):
        return {}
    return {d['id']: d for d in json.load(open(PHOTOS, encoding='utf-8'))}


EXCLUDE = set(json.load(open(os.path.join(IMGS, '_exclude.json')))) if os.path.exists(os.path.join(IMGS, '_exclude.json')) else set()


def local_photo(pid):
    if pid in EXCLUDE:
        return None
    for ext in ('.jpg', '.jpeg', '.png', '.webp'):
        p = os.path.join(IMGS, 'lm_' + pid + ext)
        if os.path.exists(p):
            return p
    return None


def parse_markup(text, ctx):
    blocks = []
    lines = text.split('\n')
    i = 0
    para = []

    def flush():
        if para:
            t = ''.join(x.strip() for x in para).strip()
            if t:
                m = re.match(r'^【([^】]+)】(.*)$', t)
                if m:
                    blocks.append({'t': 'p', 'head': '【%s】' % m.group(1), 'text': m.group(2)})
                else:
                    blocks.append({'t': 'p', 'text': t})
            para.clear()

    while i < len(lines):
        s = lines[i].strip()
        if not s:
            flush(); i += 1; continue
        if s.startswith('# '):
            flush()
            if '、' in s[2:]:
                num, name = s[2:].split('、', 1)
            else:
                num, name = '', s[2:]
            ctx['chap_n'] = ctx.get('chap_n', 0) + 1
            blocks.append({'t': 'chapter', 'num': num.strip(), 'name': name.strip(), 'anchor': 'ch_%d' % ctx['chap_n']})
            i += 1; continue
        if s.startswith('## '):
            flush()
            ctx['h1_n'] = ctx.get('h1_n', 0) + 1
            blocks.append({'t': 'h1', 'text': s[3:], 'anchor': 'h_%d' % ctx['h1_n']})
            i += 1; continue
        if s.startswith('### '):
            flush(); blocks.append({'t': 'h3', 'text': s[4:]}); i += 1; continue
        if s.startswith(':::lead'):
            flush(); buf = []; i += 1
            while not lines[i].strip().startswith(':::'):
                buf.append(lines[i].strip()); i += 1
            blocks.append({'t': 'lead', 'text': ''.join(buf)}); i += 1; continue
        if s.startswith(':::judge'):
            flush(); title = s[8:].strip(); items = []; i += 1
            while not lines[i].strip().startswith(':::'):
                t = lines[i].strip()
                if t.startswith('- '):
                    items.append(t[2:])
                elif t and items:
                    items[-1] += t
                i += 1
            blocks.append({'t': 'judge', 'title': title, 'items': items[:10]}); i += 1; continue
        if s.startswith('!fig '):
            flush()
            key, path, cap, src, w = (s[5:].split('|') + ['', '', '', '', ''])[:5]
            path = path.strip()
            p = path if os.path.isabs(path) else os.path.join(FIGS, path)
            try:
                wmm = float(w or 160)
            except ValueError:
                wmm = 160
            blocks.append({'t': 'figure', 'key': key.strip(), 'local': p, 'caption': cap.strip(),
                           'source': src.strip(), 'width_mm': min(wmm, 160)})
            i += 1; continue
        if s.startswith('!photo '):
            flush()
            pid, cap, src = (s[7:].split('|') + ['', '', ''])[:3]
            pid = pid.strip()
            ph = ctx['photos'].get(pid, {})
            remote = ph.get('thumb_url') or ph.get('image_url') or ''
            credit = '；'.join(x for x in (ph.get('credit'), ph.get('license')) if x)
            blocks.append({'t': 'figure', 'key': pid, 'local': local_photo(pid), 'remote_url': remote,
                           'page_url': ph.get('page_url') or remote, 'caption': cap.strip() or ph.get('caption_zh', pid),
                           'source': src.strip() or credit, 'width_mm': 120, 'kind': 'photo', 'save_as': 'lm_' + pid,
                           'photo_id': pid})
            if pid not in ctx['photos']:
                ctx.setdefault('warn', []).append('未知照片 id：' + pid)
            i += 1; continue
        if s.startswith('!table ') or s.startswith('!table- '):
            flush()
            nonum = s.startswith('!table- ')
            parts = (s[(8 if nonum else 7):].split('|') + ['', '', '', ''])[:4]
            key, cap, src, widths = [x.strip() for x in parts]
            i += 1
            head = [x.strip() for x in lines[i].split('|')]; i += 1
            rows = []
            while not lines[i].strip().startswith('!end'):
                if lines[i].strip():
                    r = [x.strip() for x in lines[i].split('|')]
                    if len(r) != len(head):
                        ctx.setdefault('warn', []).append('表 %s 列数不符：%s' % (key, lines[i][:40]))
                        r = (r + [''] * len(head))[:len(head)]
                    rows.append(r)
                i += 1
            ws = None
            if widths:
                try:
                    ws = [float(x) for x in widths.split(',')]
                except ValueError:
                    ws = None
            if not ws or len(ws) != len(head):
                ws = [160.0 / len(head)] * len(head)
            tot = sum(ws)
            ws = [w * 160.0 / tot for w in ws]
            size = 9.5 if len(head) <= 4 else (8.5 if len(head) <= 6 else 7.5)
            blocks.append({'t': 'table', 'key': key, 'caption': cap, 'source': src, 'headers': head,
                           'rows': rows, 'widths': ws, 'nonum': nonum, 'size': size})
            i += 1; continue
        m = re.match(r'^\{\{(\w+)(?::(.+))?\}\}$', s)
        if m:
            flush()
            kind, arg = m.group(1), m.group(2)
            if kind in ('close', 'pagebreak'):
                blocks.append({'t': kind})
            elif kind == 'block':
                bp = os.path.join(CONTENT, arg + '.md')
                if os.path.exists(bp):
                    blocks.extend(parse_markup(open(bp, encoding='utf-8').read(), ctx))
                else:
                    ctx.setdefault('warn', []).append('缺少源稿：' + arg)
            i += 1; continue
        para.append(lines[i]); i += 1
    flush()
    return blocks


def load_refs():
    R = RefRegistry()
    for f in sorted(glob.glob(os.path.join(CONTENT, 'refs_*.json'))):
        for k, v in json.load(open(f, encoding='utf-8')).items():
            R.add(k, v)
    return R


def make_ctx():
    return {'refs': load_refs(), 'fignum': {}, 'tabnum': {}, 'photos': photo_index(), 'counts': {}}


def read(name):
    p = os.path.join(CONTENT, name + '.md')
    return open(p, encoding='utf-8').read() if os.path.exists(p) else ''


def dedupe_photos(blocks):
    """同一张照片（按文件内容）只收录一次；无本地图也无直链的照片块删除。"""
    import hashlib
    seen, keys, out = set(), set(), []
    for b in blocks:
        if b['t'] == 'figure' and b.get('kind') != 'photo':
            if b['key'] in keys:      # 同一自绘图只在首次出现处收录
                continue
            keys.add(b['key'])
        if b['t'] == 'figure' and b.get('kind') == 'photo':
            if b.get('local') and os.path.exists(b['local']):
                h = hashlib.md5(open(b['local'], 'rb').read()).hexdigest()
                if h in seen:
                    continue
                seen.add(h)
            elif not b.get('remote_url'):
                continue
        out.append(b)
    return out


def resolve_numbers(blocks, ctx, include_remote):
    f = t = 0
    ctx['fignum'], ctx['tabnum'] = {}, {}
    for b in blocks:
        if b['t'] == 'figure':
            if (b.get('local') and os.path.exists(b['local'])) or (include_remote and b.get('remote_url')):
                f += 1
                ctx['fignum'][b['key']] = f
        elif b['t'] == 'table' and not b.get('nonum'):
            t += 1
            ctx['tabnum'][b['key']] = t


def check_refs(blocks, ctx):
    missing = set()
    for b in blocks:
        txts = [b.get('text', ''), b.get('source', '')] + list(b.get('items', [])) + \
               [c for r in b.get('rows', []) for c in r]
        for t in txts:
            for m in re.finditer(r'\[@([^\]]+)\]', t or ''):
                for k in m.group(1).split(','):
                    if k.strip() not in ctx['refs'].by_key:
                        missing.add(k.strip())
    return sorted(missing)


# ---------------------------------------------------------------- 封面
def covers():
    import xiguang_cover as xc
    from PIL import ImageFont, Image, ImageDraw
    _o = xc.font
    xc.font = lambda p, s: (ImageFont.truetype(p, s, index=2) if p.endswith('.ttc') else _o(p, s))
    org = '无人体系中心 · 鸿眼科情团队'
    cov = os.path.join(HERE, 'tmp', 'cover.png'); back = os.path.join(HERE, 'tmp', 'back.png')
    os.makedirs(os.path.dirname(cov), exist_ok=True)
    brief = MODE['name'] == 'brief'
    if brief:
        cov = cov.replace('cover.png', 'cover_brief.png')
    xc.make_cover(cov, title=['Lattice 与 Maven', '两系统调研精要' if brief else '两系统深度调研'],
                  subtitle=('总结 · 概括 · 架构 · 统计 · 观点' if brief else
                            '边缘网格与目标工厂：前世今生·功能·架构·能力·案例·合作·合同'),
                  issue='专 题 · 2026 年 10 月', org=org)
    im = Image.open(cov); d = ImageDraw.Draw(im)
    f = xc.font(xc.F_BOLD, 44)
    d.rectangle([630, 1580, 870, 1660], fill=xc.NAVY)
    xc.tracked(d, (750, 1636), '精　要' if brief else '专　题', f, (255, 255, 255), target_w=150, anchor='ms')
    im.save(cov)
    xc.make_back(back, issue='专 题', date='2026 年 10 月', org=org)
    return cov, back


# ---------------------------------------------------------------- docx
EDIT_ROWS = [('刊　　名', '《析光》科研情报刊物 · 专题'), ('期　　次', ISSUE),
             ('题　　目', TITLE_MAIN + TITLE_SUB), ('编　　制', '无人体系中心 · 鸿眼科情团队'),
             ('资料截止', '2026年10月10日（检索日期 2026年10月10日）'),
             ('资料性质', '公开来源情报（OSINT）汇编与分析；各方口径并列呈现，弱源与推断均已标注'),
             ('密　　级', '非密·内部资料'),
             ('版本说明', 'docx 编辑版 · HTML 图文热链版（含原图链接）· 精要版 docx · 配图采集清单')]


def edit_page(D):
    D.plain_heading('本 期 编 制', outline=None, before=60, after=16)
    for k, v in EDIT_ROWS:
        p = D.para(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=30, left=60)
        add_text(p, k + '　', HEI, 12, True, NAVY, kai_brackets=False)
        add_text(p, v, FS, 12, False, INK, kai_brackets=False)
    p = D.para(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=None, before=40)
    add_text(p, '看得早 · 看得懂 · 看得准 · 看得透', HEI, 13, True, BRASS, kai_brackets=False)


def collect_toc(blocks):
    toc = []
    for b in blocks:
        if b['t'] == 'chapter':
            toc.append((0, ('%s、%s' % (b['num'], b['name'])) if b['num'] else b['name'], b['anchor']))
        elif b['t'] == 'h1':
            toc.append((1, b['text'], b['anchor']))
    toc.append((0, '参考文献', 'refs'))
    return toc


def build_docx(ctx, secs, cov, back, pages=None, path=None):
    D = LMDocx(ctx, column=COLUMN, issue=ISSUE)
    brief = MODE['name'] == 'brief'
    D.full_image(cov)
    if not brief:
        s = D.new_section('digest'); D.header(s); D.footer(s, 'digest'); D.pg_start(s, 1)
        D.plain_heading('专 题 精 要', outline=0, before=4, after=10)
        D.render(ctx['digest_blocks'])
    s = D.new_section('front'); D.footer(s, 'front')
    if not brief:
        D.plain_heading('摘　　要', anchor='abstract', outline=0, before=4)
        D.render(ctx['abstract_blocks'])
        D.b_pagebreak({})
    D.plain_heading('目　　录', anchor='toc', outline=0, before=4)
    pages = pages or {}
    for lvl, text, anchor in ctx['toc_entries']:
        D.toc_entry(text, pages.get(anchor), anchor, lvl)
    if not brief:
        D.b_pagebreak({})
        D.plain_heading('插 图 目 录', anchor='lof', outline=0, before=4)
        for n, cap, anchor in ctx.get('lof', []):
            D.toc_entry('图%d  %s' % (n, cap), pages.get(anchor), anchor, 1, size=11)
        D.b_pagebreak({})
        D.plain_heading('表 格 目 录', anchor='lot', outline=0, before=4)
        for n, cap, anchor in ctx.get('lot', []):
            D.toc_entry('表%d  %s' % (n, cap), pages.get(anchor), anchor, 1, size=11)
    s = D.new_section('body'); D.footer(s, 'body'); D.pg_start(s, 1)
    D.masthead()
    D.title(TITLE_MAIN, BRIEF_TITLE_SUB if brief else TITLE_SUB)
    D.render(ctx['body_blocks'])
    D.refs()
    D.b_close({})
    D.b_pagebreak({})
    edit_page(D)
    D.new_section('back')
    D.full_image(back)
    path = path or os.path.join(OUT, (BRIEF_BASENAME if brief else BASENAME) + '.docx')
    D.save(path)
    return path


def soffice_pdf(docx, outdir, final=False):
    flt = 'pdf:writer_pdf_Export:{"ExportBookmarks":{"type":"boolean","value":true}}'
    if final:
        flt = ('pdf:writer_pdf_Export:{"UseLosslessCompression":{"type":"boolean","value":false},'
               '"Quality":{"type":"long","value":75},"ReduceImageResolution":{"type":"boolean","value":true},'
               '"MaxImageResolution":{"type":"long","value":220},"ExportBookmarks":{"type":"boolean","value":true}}')
    subprocess.run(['soffice', '--headless', '--convert-to', flt, '--outdir', outdir, docx],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1500)
    return os.path.splitext(os.path.join(outdir, os.path.basename(docx)))[0] + '.pdf'


def nospace(s):
    return re.sub(r'\s+', '', s or '')


def locate_pages(pdf, entries):
    txt = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
    pages = [nospace(p) for p in txt.split('\f')]
    start = None
    for i, p in enumerate(pages):
        if '◆' in p and '析光XIGUANG' in p:
            start = i
            break
    if start is None:
        return {}, None
    res, cur_p, cur_off = {}, start, 0
    for text, anchor in entries:
        key = nospace(norm_text(text))[:18]
        res[anchor] = None
        for pi in range(cur_p, len(pages)):
            off = cur_off if pi == cur_p else 0
            j = pages[pi].find(key, off)
            if j >= 0:
                res[anchor] = pi - start + 1
                cur_p, cur_off = pi, j + len(key)
                break
    return res, start


def prepare(include_remote):
    ctx = make_ctx()
    if MODE['name'] == 'brief':
        secs = {'digest': '', 'abstract': '', 'body': read('brief'), 'appendix': ''}
    else:
        secs = {k: read(k) for k in ('digest', 'abstract', 'body', 'appendix')}
    body = dedupe_photos(parse_markup(secs['body'], ctx) + (parse_markup(secs['appendix'], ctx) if secs['appendix'] else []))
    resolve_numbers(body, ctx, include_remote)
    ctx['body_blocks'] = body
    ctx['digest_blocks'] = parse_markup(secs['digest'], ctx)
    ctx['abstract_blocks'] = parse_markup(secs['abstract'], ctx)
    ctx['toc_entries'] = collect_toc(body)
    return ctx, secs


def main(mode='full'):
    MODE['name'] = mode
    ctx, secs = prepare(include_remote=False)
    miss = check_refs(ctx['body_blocks'] + ctx['digest_blocks'] + ctx['abstract_blocks'], ctx)
    print('未定义引注:', len(miss), miss[:20])
    print('告警:', ctx.get('warn', [])[:20])
    blocks = ctx['body_blocks']
    lof, lot = [], []
    fn = tn = 0
    for b in blocks:
        if b['t'] == 'figure' and b.get('local') and os.path.exists(b['local']):
            fn += 1; lof.append((fn, b['caption'], 'fig_%d' % fn))
        elif b['t'] == 'table' and not b.get('nonum'):
            tn += 1; lot.append((tn, b['caption'], 'tab_%d' % tn))
    ctx['lof'], ctx['lot'] = lof, lot
    cov, back = covers()
    tmpdir = os.path.join(HERE, 'tmp'); os.makedirs(tmpdir, exist_ok=True)
    entries = []
    fn = tn = 0
    for b in blocks:
        if b['t'] == 'chapter':
            entries.append((('%s、%s' % (b['num'], b['name'])) if b['num'] else b['name'], b['anchor']))
        elif b['t'] == 'h1':
            entries.append((b['text'], b['anchor']))
        elif b['t'] == 'figure' and b.get('local') and os.path.exists(b['local']):
            fn += 1; entries.append(('图%d%s' % (fn, b['caption']), 'fig_%d' % fn))
        elif b['t'] == 'table' and not b.get('nonum'):
            tn += 1; entries.append(('表%d%s' % (tn, b['caption']), 'tab_%d' % tn))
    entries.append(('参考文献', 'refs'))
    pages = {}
    for it in range(4):
        by_key = ctx['refs'].by_key
        ctx['refs'] = RefRegistry(); ctx['refs'].by_key = by_key
        p = build_docx(ctx, secs, cov, back, pages, os.path.join(tmpdir, 'pass.docx'))
        pdf = soffice_pdf(p, tmpdir)
        newpages, start = locate_pages(pdf, entries)
        miss = [a for a, v in newpages.items() if v is None]
        print('pass', it, 'body starts at pdf page', start, 'missing', len(miss), miss[:6])
        if newpages == pages:
            break
        pages = newpages
    by_key = ctx['refs'].by_key
    ctx['refs'] = RefRegistry(); ctx['refs'].by_key = by_key
    final = build_docx(ctx, secs, cov, back, pages)
    print('docx:', final, '页数（PDF 校样口径）:', pdf_pagecount(pdf))
    import shutil
    os.makedirs(DELIVER, exist_ok=True)
    shutil.copy(final, DELIVER)
    html = None
    if mode == 'full':
        html, n = build_html(cov, back)
        print('html:', html, n, 'figures')
        shutil.copy(html, DELIVER)
    return final, html


def pdf_pagecount(pdf):
    out = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    m = re.search(r'Pages:\s+(\d+)', out)
    return int(m.group(1)) if m else None


# ---------------------------------------------------------------- HTML
def b64(path):
    import base64
    return base64.b64encode(open(path, 'rb').read()).decode()


def build_html(cov, back):
    ctx, secs = prepare(include_remote=True)
    blocks = ctx['body_blocks']
    hb_d = LMHtml(ctx); hb_d.render(ctx['digest_blocks'])
    hb_a = LMHtml(ctx); hb_a.render(ctx['abstract_blocks'])
    hb = LMHtml(ctx); hb.render(blocks)
    toc = ''.join('<div class="l%d"><a href="#%s">%s</a></div>' % (l, a, H.escape(norm_text(t)))
                  for l, t, a in hb.toc)
    lof = ''.join('<div class="l1"><a href="#%s">图%d  %s</a></div>' % (a, n, H.escape(norm_text(c)))
                  for n, c, a in ctx.get('html_figs', []))
    lot = ''.join('<div class="l1"><a href="#%s">表%d  %s</a></div>' % (a, n, H.escape(norm_text(c)))
                  for n, c, a in ctx.get('html_tabs', []))
    from PIL import Image
    import io
    def jpg64(p):
        im = Image.open(p).convert('RGB'); im.thumbnail((1000, 1414)); bio = io.BytesIO(); im.save(bio, 'JPEG', quality=82)
        import base64
        return base64.b64encode(bio.getvalue()).decode()
    cover = '<div class="cover"><img src="data:image/jpeg;base64,%s" alt="封面"></div>' % jpg64(cov)
    backh = '<div class="cover"><img src="data:image/jpeg;base64,%s" alt="封底"></div>' % jpg64(back)
    edit = ('<h2 class="chapter">本期编制</h2><table class="kv"><tbody>'
            + ''.join('<tr><td class="k">%s</td><td>%s</td></tr>' % (k, H.escape(v)) for k, v in EDIT_ROWS)
            + '</tbody></table>')
    doc = ('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1">'
           '<title>Lattice与Maven深度调研</title><style>%s</style></head><body>'
           '<div class="band"><span>XIGUANG · DEEP DIVE</span><span>《析光》%s</span></div>'
           '%s<div class="digest"><h2>专 题 精 要</h2>%s</div>'
           '<h2 class="chapter" id="abstract">摘　要</h2>%s'
           '<h2 class="chapter" id="toc">目　录</h2><div class="toc">%s</div>'
           '<h2 class="chapter">插图目录</h2><div class="toc">%s</div>'
           '<h2 class="chapter">表格目录</h2><div class="toc">%s</div>'
           '<div class="mast"><b>析光 XIGUANG</b><span>鸿眼·科研情报刊物　%s</span></div>'
           '<div class="colbar">◆ %s</div>'
           '<h1 class="title">%s</h1><div class="subtitle">%s</div>'
           '<div class="byline">文｜无人体系中心科技情报组（鸿眼）</div>'
           '%s%s<div class="close">—— 本文完 ｜《析光》2026年10月专题 · Lattice 与 Maven ——</div>%s'
           '<div class="brand">鸿眼 HONGEYE ｜ 析光 XIGUANG · 看得早 · 看得懂 · 看得准 · 看得透</div>%s'
           '</body></html>') % (HTML_CSS, ISSUE, cover, ''.join(hb_d.parts), ''.join(hb_a.parts), toc, lof, lot,
                                ISSUE, COLUMN, H.escape(TITLE_MAIN), H.escape(TITLE_SUB), ''.join(hb.parts),
                                hb.refs_html(), edit, backh)
    path = os.path.join(OUT, BASENAME + '（HTML图文热链版）.html')
    open(path, 'w', encoding='utf-8').write(doc)
    return path, len(ctx.get('html_figs', []))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'full')
