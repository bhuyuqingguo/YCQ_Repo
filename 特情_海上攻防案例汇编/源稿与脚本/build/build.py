# -*- coding: utf-8 -*-
"""
特情全书组装：标记源稿 + 案例库 -> docx（两遍页码）/ PDF / HTML / 配图采集页

标记语法（content/*.md）：
  # 一、章名                章
  ## （一）节名             一级标题（进目录二级）
  ### 小标题                三级小标题（不进目录）
  :::lead ... :::           导读框
  :::judge 标题 / - 条目 :::  判断框
  !fig key|path|题目|来源|宽mm
  !table key|题目|来源|列宽mm,列宽mm
  表头1|表头2
  单元格|单元格
  !end
  {{cases:周边港口}}        插入该类全部案例
  {{casetable:周边港口}}    插入该类案例一览表
  {{refs}} {{close}} {{pagebreak}}
  普通段落：空行分隔；以【xxx】开头的段落，【xxx】按黑体提示语处理
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from xgengine import (DocxBuilder, HtmlBuilder, RefRegistry, HTML_CSS, norm_text, ref_entry,  # noqa
                      WD_ALIGN_PARAGRAPH, add_text, p_border, p_outline, bookmark, HEI, KAI, FS, NAVY, GREY,
                      BRASS, INK)
import cases_lib
from cases_lib import load_all, number, case_blocks, clean, CATS, case_images
import imgpage

SP = os.path.abspath(os.path.join(HERE, '..'))
OUT = os.path.join(SP, 'out')
os.makedirs(OUT, exist_ok=True)
CONTENT = os.path.join(HERE, 'content')

TITLE_MAIN = '港口与锚地已成前沿'
TITLE_SUB = '——全球海上岛屿、周边港口、小岛与远海编组遭袭与防卫案例汇编（2023—2026）'
BASENAME = '析光特情_海上岛屿港口小岛远海编组遭袭与防卫案例汇编'


def cat_case_table(cs, cat):
    rows = []
    for c in cs:
        if c['category'] != cat:
            continue
        rows.append([c['code'], (c.get('date_start') or '')[:10], clean(c.get('title_cn')),
                     '、'.join((c.get('domains') or [])[:3]), clean(c.get('outcome')), (c.get('confidence') or '')[:1]])
    return rows


def parse_markup(text, ctx):
    blocks = []
    lines = text.split('\n')
    i = 0
    para = []
    h1n = [0]

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
        ln = lines[i]
        s = ln.strip()
        if not s:
            flush(); i += 1; continue
        if s.startswith('#! '):
            flush()
            ctx['chap_n'] = ctx.get('chap_n', 0) + 1
            blocks.append({'t': 'chapter', 'num': '', 'name': s[3:], 'anchor': 'ch_%d' % ctx['chap_n']})
            i += 1; continue
        if s.startswith('# '):
            flush()
            num, name = s[2:].split('、', 1)
            ctx['chap_n'] = ctx.get('chap_n', 0) + 1
            blocks.append({'t': 'chapter', 'num': num, 'name': name, 'anchor': 'ch_%d' % ctx['chap_n']})
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
            blocks.append({'t': 'judge', 'title': title, 'items': items}); i += 1; continue
        if s.startswith('!fig '):
            flush()
            key, path, cap, src, w = (s[5:].split('|') + ['', '', '', '', ''])[:5]
            p = path if os.path.isabs(path) else os.path.join(SP, 'figs', path)
            blocks.append({'t': 'figure', 'key': key.strip(), 'local': p, 'caption': cap.strip(),
                           'source': src.strip(), 'width_mm': float(w or 155)})
            i += 1; continue
        if s.startswith('!rfig '):
            flush()
            key, page, cap, src = (s[6:].split('|') + ['', '', '', ''])[:4]
            from cases_lib import commons_url, file_from_page, IMGDIR
            fn = file_from_page(page.strip())
            local = None
            if fn:
                for ext in ('.jpg', '.jpeg', '.png'):
                    pth = os.path.join(IMGDIR, 'eq_' + key.strip() + ext)
                    if os.path.exists(pth):
                        local = pth
            blocks.append({'t': 'figure', 'key': key.strip(), 'remote_url': commons_url(fn) if fn else page.strip(),
                           'page_url': page.strip(), 'local': local, 'caption': cap.strip(), 'source': src.strip(),
                           'width_mm': 120, 'kind': 'photo', 'save_as': 'eq_' + key.strip()})
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
                    rows.append([x.strip() for x in lines[i].split('|')])
                i += 1
            ws = [float(x) for x in widths.split(',')] if widths else None
            blocks.append({'t': 'table', 'key': key, 'caption': cap, 'source': src, 'headers': head,
                           'rows': rows, 'widths': ws, 'nonum': nonum})
            i += 1; continue
        m = re.match(r'^\{\{(\w+)(?::(.+))?\}\}$', s)
        if m:
            flush()
            kind, arg = m.group(1), m.group(2)
            if kind == 'cases':
                for c in ctx['cases']:
                    if c['category'] == arg:
                        blocks.extend(case_blocks(c, ctx['refs']))
            elif kind == 'casetable':
                cap, src = arg.split('|') if '|' in arg else (arg + '案例一览', '本报告整理')
                cat = cap.split('｜')[0] if '｜' in cap else arg.split('|')[0]
                blocks.append({'t': 'table', 'key': 'ct_' + cat, 'caption': cat_label(cat) + '案例一览',
                               'source': '本报告整理（可信度：A 多源交叉印证，B 单方官方或主流媒体，C 单方声称）',
                               'headers': ['编号', '日期', '案例', '主要域', '结果', '可信度'],
                               'rows': cat_case_table(ctx['cases'], cat),
                               'widths': [14, 20, 70, 22, 24, 10], 'size': 9.5})
            elif kind == 'regiontable':
                from collections import OrderedDict
                feats = REGION_FEATS
                abbr = {'岛屿防卫': '岛', '周边港口': '港', '海上小岛': '礁', '远海机动编组': '编', '海上交通线': '航'}
                rows = []
                for reg, feat in feats.items():
                    cs_r = [c for c in ctx['cases'] if (c.get('region') or '其他') in reg.split('/')]
                    if not cs_r:
                        continue
                    from collections import Counter
                    cnt = Counter(c['category'] for c in cs_r)
                    comp = '、'.join('%s%d' % (abbr[k], cnt[k]) for k in abbr if cnt.get(k))
                    rows.append([reg.split('/')[0].replace('-', '—'), str(len(cs_r)), comp, feat])
                blocks.append({'t': 'table', 'key': 'regions', 'caption': '各海域案例数量与主要特点',
                               'source': '本报告统计（场景构成：岛＝岛屿防卫，港＝周边港口，礁＝海上小岛，编＝远海机动编组，航＝海上交通线）',
                               'headers': ['海域', '案例数', '场景构成', '主要特点'], 'rows': rows,
                               'widths': [30, 14, 34, 82], 'aligns': ['left', 'center', 'left', 'left']})
            elif kind == 'atlas':
                blocks.extend(ctx.get('atlas_blocks', []))
            elif kind == 'alltable':
                rows = [[c['code'], (c.get('date_start') or '')[:10], c.get('region') or '', clean(c.get('title_cn')),
                         clean(c.get('outcome')), (c.get('confidence') or '')[:1]] for c in ctx['cases']]
                blocks.append({'t': 'table', 'key': 'all_cases', 'caption': '全部案例总表（按场景与日期排序）',
                               'source': '本报告整理', 'headers': ['编号', '日期', '海域', '案例', '结果', '级'],
                               'rows': rows, 'widths': [13, 19, 24, 74, 22, 8], 'size': 8.5})
            elif kind == 'chronology':
                cs = sorted(ctx['cases'], key=lambda c: (c.get('date_start') or '9999'))
                rows = [[(c.get('date_start') or '')[:10], c['code'], clean(c.get('subtitle_cn') or c.get('title_cn'))[:90]]
                        for c in cs]
                blocks.append({'t': 'table', 'key': 'chrono', 'caption': '大事年表（2023—2026）',
                               'source': '本报告整理', 'headers': ['日期', '编号', '事件'], 'rows': rows,
                               'widths': [20, 14, 126], 'size': 8.5})
            elif kind == 'doubts':
                rows = []
                for c in ctx['cases']:
                    if (c.get('confidence') or '').strip()[:1] in ('C',) or '待核' in (c.get('claims_compare_cn') or ''):
                        cc = clean(c.get('claims_compare_cn') or '')
                        cut = cc.find('。')
                        rows.append([c['code'], clean(c.get('title_cn')), (cc[:cut + 1] if 0 < cut < 160 else cc[:160] + '……'),
                                     (c.get('confidence') or '')[:1]])
                blocks.append({'t': 'table', 'key': 'doubts', 'caption': '存疑事项与待核清单',
                               'source': '本报告整理（C级案例及口径比对中含"待核"项的案例）',
                               'headers': ['编号', '案例', '主要存疑点', '级'], 'rows': rows,
                               'widths': [13, 45, 94, 8], 'size': 8.5})
            elif kind in ('close', 'pagebreak'):
                blocks.append({'t': kind})
            elif kind == 'block':
                bp = os.path.join(CONTENT, 'blocks', arg + '.md')
                if os.path.exists(bp):
                    blocks.extend(parse_markup(open(bp, encoding='utf-8').read(), ctx))
            i += 1; continue
        para.append(ln); i += 1
    flush()
    return blocks


REGION_FEATS = {
    '黑海/亚速海': '港口与基地遭导弹、无人艇、无人潜航器及异构打击；无人艇击沉航行舰艇并发展对空作战；双方互打航运与港口',
    '红海-亚丁湾': '多国编组长期防空拦截；商船遭导弹、无人机、无人艇攻击；港口遭空袭；2026年近岸岛屿易手',
    '波斯湾-霍尔木兹-阿曼湾': '2026年战争集中爆发：岛上基地与能源设施遭远程打击、港内舰艇被成批摧毁、海峡布雷与反水雷、编组过航遇袭',
    '东地中海': '远程导弹与无人机打击岛上基地、港口与离岸设施；舰艇参与区域防空拦截',
    '阿拉伯海-印度洋': '反海盗与解救行动、无人机袭船、远程弹道导弹打击岛上基地、潜艇击沉远海单舰、印巴对峙',
    '波罗的海-北海': '海底管线与电缆损伤、影子船队拦检与扣押、无人机滋扰港口与军事设施、导航干扰',
    '南海': '岛礁补给对峙（水炮、拦阻、登临、联合拦截），中国海警与马、印尼执法力量对峙，周边国家岛礁吹填与导弹部署',
    '台海': '离岛执法巡查、演习中的离岛与要港封控科目、海缆中断',
    '马六甲-新加坡海峡': '海峡船舶持械抢劫与沿岸国联合巡逻',
    '东海-西太/日本海-朝鲜半岛': '岛屿防空部署、无人机抵近、炮击与岛民避难',
    '加勒比': '美军编组打击小艇、对港口实施打击、油轮拦截与扣押',
    '非洲沿岸/其他': '地中海中部船队遇袭、西非外海油轮爆炸、苏丹港遭无人机打击等',
}


def cat_label(cat):
    return {'岛屿防卫': '岛屿防卫类', '周边港口': '周边重要港口类', '海上小岛': '海上小岛（含礁、平台、离岸设施）类',
            '远海机动编组': '远海机动编组类', '海上交通线': '海上交通线（关联）类'}.get(cat, cat)


def resolve_numbers(blocks, ctx, include_remote):
    """按后端实际收录的图表计算编号，供 {fig:key}/{tab:key} 引用。"""
    f = t = 0
    ctx['fignum'], ctx['tabnum'] = {}, {}
    for b in blocks:
        if b['t'] == 'figure':
            has = (b.get('local') and os.path.exists(b['local'])) or (include_remote and b.get('remote_url'))
            if has:
                f += 1
                if b.get('key'):
                    ctx['fignum'][b['key']] = f
        elif b['t'] == 'table' and not b.get('nonum'):
            t += 1
            if b.get('key'):
                ctx['tabnum'][b['key']] = t


def load_sections():
    secs = {}
    for name in ('digest', 'abstract', 'body', 'appendix'):
        p = os.path.join(CONTENT, name + '.md')
        secs[name] = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return secs


def make_ctx():
    cs = number(load_all())
    ctx = {'refs': RefRegistry(), 'fignum': {}, 'tabnum': {}, 'cases': cs, 'extra_blocks': {}}
    from collections import Counter
    cnt = Counter(c['category'] for c in cs)
    conf = Counter((c.get('confidence') or '?').strip()[:1] for c in cs)
    ctx['counts'] = dict(cnt)
    ctx['counts'].update({'all': len(cs), 'A': conf.get('A', 0), 'B': conf.get('B', 0), 'C': conf.get('C', 0)})
    ctx['casecode'] = {c['case_key']: c['code'] for c in cs}
    # 装备与成本数据出处
    import hashlib
    H = json.load(open(os.path.join(SP, 'research', 'H_equipment_costs.json'), encoding='utf-8'))
    ctx['H'] = H
    ctx['halias'] = {}
    for grp in ('attack_platforms', 'interceptors', 'statistics'):
        for it in H.get(grp, []):
            name = it.get('name') or it.get('item_cn') or ''
            ks = []
            for s in it.get('sources', []):
                if not s.get('url'):
                    continue
                k = 'u_' + hashlib.md5(s['url'].encode()).hexdigest()[:12]
                s.setdefault('title_cn', '')
                ctx['refs'].add(k, s)
                ks.append(k)
            ctx['halias'][name] = ks
    return ctx


def pdf_pages(pdf):
    txt = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
    return txt.split('\f')


def nospace(s):
    return re.sub(r'\s+', '', s or '')


def locate_pages(pdf, entries, body_marker='◆'):
    """entries: [(text, anchor)] 按顺序；返回 anchor->正文页码。游标只前进。"""
    pages = [nospace(p) for p in pdf_pages(pdf)]
    start = None
    for i, p in enumerate(pages):
        if body_marker in p and '析光XIGUANG' in p:
            start = i
            break
    if start is None:
        return {}, None
    res = {}
    cur_p, cur_off = start, 0
    for text, anchor in entries:
        key = nospace(norm_text(text))[:18]
        found = False
        for pi in range(cur_p, len(pages)):
            off = cur_off if pi == cur_p else 0
            j = pages[pi].find(key, off)
            if j >= 0:
                res[anchor] = pi - start + 1
                cur_p, cur_off = pi, j + len(key)
                found = True
                break
        if not found:
            res[anchor] = None
    return res, start


def build_docx(ctx, secs, pages=None, path=None):
    D = DocxBuilder(ctx)
    D.full_image(os.path.join(HERE, 'cover.png'))
    # 精要
    s = D.new_section('digest'); D.header(s); D.footer(s, 'digest'); D.pg_start(s, 1)
    D.plain_heading('特 情 精 要', outline=0, before=4, after=10)
    dblocks = parse_markup(secs['digest'], ctx)
    D.render(dblocks)
    # 前置：摘要 + 目录系列
    s = D.new_section('front'); D.footer(s, 'front')
    D.plain_heading('摘　　要', anchor='abstract', outline=0, before=4)
    D.render(parse_markup(secs['abstract'], ctx))
    D.b_pagebreak({})
    D.plain_heading('目　　录', anchor='toc', outline=0, before=4)
    pages = pages or {}
    for lvl, text, anchor in ctx['toc_entries']:
        D.toc_entry(text, pages.get(anchor), anchor, lvl)
    D.b_pagebreak({})
    D.plain_heading('插 图 目 录', anchor='lof', outline=0, before=4)
    for n, cap, anchor in ctx.get('lof', []):
        D.toc_entry('图%d  %s' % (n, cap), pages.get(anchor), anchor, 1, size=11)
    D.b_pagebreak({})
    D.plain_heading('表 格 目 录', anchor='lot', outline=0, before=4)
    for n, cap, anchor in ctx.get('lot', []):
        D.toc_entry('表%d  %s' % (n, cap), pages.get(anchor), anchor, 1, size=11)
    # 正文
    s = D.new_section('body'); D.footer(s, 'body'); D.pg_start(s, 1)
    D.masthead()
    D.title(TITLE_MAIN, TITLE_SUB)
    D.render(ctx['body_blocks'])
    D.refs()
    D.b_close({})
    # 本期编制
    D.b_pagebreak({})
    edit_page(D)
    s = D.new_section('back')
    D.full_image(os.path.join(HERE, 'back.png'))
    path = path or os.path.join(OUT, BASENAME + '.docx')
    D.save(path)
    return path


def edit_page(D):
    D.plain_heading('本 期 编 制', outline=None, before=60, after=16)
    for k, v in EDIT_ROWS:
        p = D.para(WD_ALIGN_PARAGRAPH.LEFT, indent=False, line=30, left=60)
        add_text(p, k + '　', HEI, 12, True, NAVY, kai_brackets=False)
        add_text(p, v, FS, 12, False, INK, kai_brackets=False)
    p = D.para(WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=None, before=40)
    add_text(p, '看得早 · 看得懂 · 看得准 · 看得透', HEI, 13, True, BRASS, kai_brackets=False)
    D.brand = None


def collect_toc(blocks):
    toc = []
    for b in blocks:
        if b['t'] == 'chapter':
            toc.append((0, ('%s、%s' % (b['num'], b['name'])) if b['num'] else b['name'], b['anchor']))
        elif b['t'] == 'h1':
            toc.append((1, b['text'], b['anchor']))
        elif b['t'] == 'h2' and b.get('toc'):
            toc.append((2, '%s　%s' % (b.get('tag', ''), b['text']), b['anchor']))
    toc.append((0, '参考文献', 'refs'))
    return toc


def soffice_pdf(docx, outdir):
    subprocess.run(['soffice', '--headless', '--convert-to',
                    'pdf:writer_pdf_Export:{"ExportBookmarks":{"type":"boolean","value":true}}',
                    '--outdir', outdir, docx], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                   timeout=900)
    return os.path.splitext(os.path.join(outdir, os.path.basename(docx)))[0] + '.pdf'


def main():
    secs = load_sections()
    # ---------- 正文块（docx 口径：只收本地图）
    ctx = make_ctx()
    body = parse_markup(secs['body'], ctx)
    appendix = parse_markup(secs['appendix'], ctx) if secs['appendix'] else []
    blocks = body + appendix
    resolve_numbers(blocks, ctx, include_remote=False)
    # 重新解析一遍使引用号就位（parse 阶段不输出号码，渲染时才取）
    ctx['body_blocks'] = blocks
    ctx['toc_entries'] = collect_toc(blocks)
    # 图表目录（docx 口径）
    lof, lot = [], []
    fn = tn = 0
    for b in blocks:
        if b['t'] == 'figure' and b.get('local') and os.path.exists(b['local']):
            fn += 1; lof.append((fn, b['caption'], 'fig_%d' % fn))
        elif b['t'] == 'table' and not b.get('nonum'):
            tn += 1; lot.append((tn, b['caption'], 'tab_%d' % tn))
    ctx['lof'], ctx['lot'] = lof, lot
    tmpdir = os.path.join(SP, 'build', 'tmp'); os.makedirs(tmpdir, exist_ok=True)
    pages = {}
    for it in range(4):
        # 引注号按首次出现顺序：每遍重置
        refs_backup = ctx['refs']
        ctx['refs'] = RefRegistry(); ctx['refs'].by_key = refs_backup.by_key
        p = build_docx(ctx, secs, pages, os.path.join(tmpdir, 'pass.docx'))
        pdf = soffice_pdf(p, tmpdir)
        entries = [(t, a) for _, t, a in ctx['toc_entries']]
        entries_all = []
        # 正文中的顺序：章/节/案例与图表交织，按块顺序构造
        fn = tn = 0
        for b in blocks:
            if b['t'] == 'chapter':
                entries_all.append((('%s、%s' % (b['num'], b['name'])) if b['num'] else b['name'], b['anchor']))
            elif b['t'] == 'h1':
                entries_all.append((b['text'], b['anchor']))
            elif b['t'] == 'h2' and b.get('toc'):
                entries_all.append((b.get('tag', '') + b['text'], b['anchor']))
            elif b['t'] == 'figure' and b.get('local') and os.path.exists(b['local']):
                fn += 1; entries_all.append(('图%d%s' % (fn, b['caption']), 'fig_%d' % fn))
            elif b['t'] == 'table' and not b.get('nonum'):
                tn += 1; entries_all.append(('表%d%s' % (tn, b['caption']), 'tab_%d' % tn))
        entries_all.append(('参考文献', 'refs'))
        newpages, start = locate_pages(pdf, entries_all)
        miss = [a for a, v in newpages.items() if v is None]
        print('pass', it, 'body starts at pdf page', start, 'missing', len(miss), miss[:8])
        if newpages == pages:
            break
        pages = newpages
    final = build_docx(ctx, secs, pages)
    ctx['pages'] = pages
    return ctx, final


if __name__ == '__main__':
    main()


# ================================================================= HTML 与配图采集页
def b64(path):
    import base64
    return base64.b64encode(open(path, 'rb').read()).decode()


def build_html(secs, path=None):
    import html as H
    ctx = make_ctx()
    blocks = parse_markup(secs['body'], ctx)
    resolve_numbers(blocks, ctx, include_remote=True)
    dig = parse_markup(secs['digest'], ctx)
    abs_ = parse_markup(secs['abstract'], ctx)
    hb_d = HtmlBuilder(ctx); hb_d.render(dig)
    hb_a = HtmlBuilder(ctx); hb_a.render(abs_)
    hb = HtmlBuilder(ctx); hb.render(blocks)
    toc = ''.join('<div class="l%d"><a href="#%s">%s</a></div>' % (l, a, H.escape(norm_text(t)))
                  for l, t, a in hb.toc)
    lof = ''.join('<div class="l1"><a href="#%s">图%d  %s</a></div>' % (a, n, H.escape(norm_text(c)))
                  for n, c, a in ctx.get('html_figs', []))
    lot = ''.join('<div class="l1"><a href="#%s">表%d  %s</a></div>' % (a, n, H.escape(norm_text(c)))
                  for n, c, a in ctx.get('html_tabs', []))
    cover = '<div class="cover"><img src="data:image/png;base64,%s" alt="封面"></div>' % b64(os.path.join(HERE, 'cover.png'))
    back = '<div class="cover"><img src="data:image/png;base64,%s" alt="封底"></div>' % b64(os.path.join(HERE, 'back.png'))
    edit = ('<h2 class="chapter">本期编制</h2><table class="kv"><tbody>'
            + ''.join('<tr><td class="k">%s</td><td>%s</td></tr>' % (k, H.escape(v)) for k, v in EDIT_ROWS)
            + '</tbody></table>')
    doc = ('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1">'
           '<title>析光特情·海上攻防案例汇编</title><style>%s</style></head><body>'
           '<div class="band"><span>XIGUANG · INTELLIGENCE REPORT</span><span>《析光》特情 · 2026年10月</span></div>'
           '%s<div class="digest"><h2>特 情 精 要</h2>%s</div>'
           '<h2 class="chapter" id="abstract">摘　要</h2>%s'
           '<h2 class="chapter" id="toc">目　录</h2><div class="toc">%s</div>'
           '<h2 class="chapter">插图目录</h2><div class="toc">%s</div>'
           '<h2 class="chapter">表格目录</h2><div class="toc">%s</div>'
           '<div class="mast"><b>析光 XIGUANG</b><span>鸿眼·科研情报刊物　特情 · 2026年10月</span></div>'
           '<div class="colbar">◆ 本期聚焦｜FOCUS</div>'
           '<h1 class="title">%s</h1><div class="subtitle">%s</div>'
           '<div class="byline">文｜无人体系中心科技情报组（鸿眼）</div>'
           '%s%s<div class="close">—— 本文完 ｜《析光》2026年10月特情 · 本期聚焦 ——</div>%s'
           '<div class="brand">鸿眼 HONGEYE ｜ 析光 XIGUANG · 看得早 · 看得懂 · 看得准 · 看得透</div>%s'
           '</body></html>') % (HTML_CSS, cover, ''.join(hb_d.parts), ''.join(hb_a.parts), toc, lof, lot,
                                H.escape(TITLE_MAIN), H.escape(TITLE_SUB), ''.join(hb.parts), hb.refs_html(), edit, back)
    path = path or os.path.join(OUT, BASENAME + '（HTML图文热链版）.html')
    open(path, 'w', encoding='utf-8').write(doc)
    # 配图采集页
    items, seen = [], set()
    for b in blocks:
        if b['t'] == 'figure' and b.get('remote_url') and b['remote_url'] not in seen:
            seen.add(b['remote_url'])
            items.append({'case': b.get('case') or '装备', 'desc': H.escape(norm_text(b['caption']))[:80],
                          'url': b['remote_url'], 'page': b.get('page_url') or b['remote_url'],
                          'save_as': b.get('save_as') or ('img_%d' % len(items))})
    ipath = os.path.join(OUT, BASENAME + '（配图采集清单）.html')
    imgpage.build(items, ipath)
    return path, ipath, len(items), ctx


EDIT_ROWS = [('刊　　名', '《析光》科研情报刊物 · 特情'), ('期　　次', '特情 · 2026年10月'),
             ('题　　目', TITLE_MAIN + TITLE_SUB), ('编　　制', '无人体系中心 · 鸿眼科情团队'),
             ('资料截止', '2026年9月30日（检索日期 2026年10月9日）'),
             ('资料性质', '公开来源情报（OSINT）汇编，各方口径并列呈现，不代表我部对争议事实的立场'),
             ('密　　级', '非密·内部资料'),
             ('版本说明', 'docx 编辑版 · PDF 校样 · HTML 图文热链版（含原图链接）')]
