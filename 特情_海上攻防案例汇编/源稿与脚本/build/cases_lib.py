# -*- coding: utf-8 -*-
"""案例库：合并、清洗、编号、渲染为块。"""
import glob
import hashlib
import json
import os
import re
import urllib.parse

from xgengine import norm_text

RESEARCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'research')
IMGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'imgs')

CATS = [
    ('岛屿防卫', '岛', 'island'),
    ('周边港口', '港', 'port'),
    ('海上小岛', '礁', 'islet'),
    ('远海机动编组', '编', 'fleet'),
    ('海上交通线', '航', 'sea'),
]
MERCHANT_KW = ('商船', '油轮', '货轮', '散货船', '集装箱船', '化学品船', '运输船', '滚装船', '渔船', '援助船', '船队')
NAVY_KW = ('海军', '驱逐舰', '护卫舰', '航母', '巡洋舰', '舰艇', '打击群', '编队')
CAT_ALIAS = {'周边重要港口': '周边港口', '港口': '周边港口', '小岛': '海上小岛',
             '远海编组': '远海机动编组', '岛屿': '岛屿防卫'}

BANNED = [('值得注意的是，', ''), ('值得注意的是', ''), ('总的来说，', ''), ('总而言之，', ''),
          ('不难看出，', ''), ('毋庸置疑，', ''), ('赋能', '支撑'), ('深刻揭示了', '表明了'),
          ('深刻地', ''), ('这一事件深刻', '这一事件'), ('无疑', ''), ('换句话说，', '即'),
          ('一言以蔽之，', ''), ('显而易见，', ''), ('不可忽视', '需要重视'), ('凸显', '显示'),
          ('与此同时，', '同时，')]


def clean(s):
    if not s:
        return ''
    s = str(s).strip()
    for a, b in BANNED:
        s = s.replace(a, b)
    return norm_text(s)


def commons_url(file_name):
    """由 Commons 文件名计算 upload.wikimedia.org 原图直链（MD5 目录规则）。"""
    name = file_name.strip()
    if name.lower().startswith('file:'):
        name = name[5:]
    name = urllib.parse.unquote(name).replace(' ', '_')
    name = name[0].upper() + name[1:] if name else name
    h = hashlib.md5(name.encode('utf-8')).hexdigest()
    q = urllib.parse.quote(name, safe="()_-.,!'")
    return 'https://upload.wikimedia.org/wikipedia/commons/%s/%s/%s' % (h[0], h[:2], q)


def file_from_page(page):
    if not page or '/wiki/File:' not in page:
        return None
    return urllib.parse.unquote(page.split('/wiki/File:', 1)[1].split('#')[0].split('?')[0])


def load_all():
    cases = []
    for f in sorted(glob.glob(os.path.join(RESEARCH, '*.json'))):
        base = os.path.basename(f)
        if base[0] in 'GH' or base.startswith('_') or 'backup' in base or 'round' in base:
            continue
        try:
            data = json.load(open(f, encoding='utf-8'))
        except Exception as e:
            print('!! JSON 解析失败', base, e)
            continue
        if isinstance(data, dict):
            data = data.get('cases') or []
        for c in data:
            c['_group'] = base.split('_')[0]
            cat = c.get('category', '').strip()
            c['category'] = CAT_ALIAS.get(cat, cat)
            if c['category'] == '远海机动编组':
                d = (c.get('defender') or '') + (c.get('title_cn') or '')
                if any(k in d for k in MERCHANT_KW) and not any(k in (c.get('defender') or '') for k in NAVY_KW):
                    c['category'] = '海上交通线'
            cases.append(c)
    # 同键去重：保留信息量大者，合并来源与图片
    best = {}
    for c in cases:
        k = c.get('case_key')
        size = len(json.dumps(c, ensure_ascii=False))
        if k not in best or size > best[k][0]:
            if k in best:
                c = merge_into(c, best[k][1])
            best[k] = (size, c)
        else:
            merge_into(best[k][1], c)
    out = [v[1] for v in best.values()]
    for keep, drop in MANUAL_MERGE:
        a = [c for c in out if c.get('case_key') == keep]
        b = [c for c in out if c.get('case_key') == drop]
        if a and b:
            merge_into(a[0], b[0]); out.remove(b[0])
    for k in MANUAL_DROP:
        out = [c for c in out if c.get('case_key') != k]
    for c in out:
        if c.get('region') == '台海' or str(c.get('case_key', '')).startswith(('kinmen', 'joint_sword', 'strait_thunder', 'justice_mission', 'matsu', 'penghu')):
            tw_normalize(c)
    for c in out:
        if c.get('case_key') in OUTCOME_OVERRIDE:
            c['outcome'] = OUTCOME_OVERRIDE[c['case_key']]
    for k, cat in CAT_OVERRIDE.items():
        for c in out:
            if c.get('case_key') == k:
                c['category'] = cat
    return out


MANUAL_MERGE = [('rs_perim_mokha_2026_09_11', 'rs_perim_island_seized_2026_09'), ('sd_port_sudan_drones_2025_05', 'sd_port_sudan_2025_05_04'), ('vn_spratly_reclamation_2023_2026', 'scs_vietnam_spratly_reclamation_2025')]   # (保留键, 并入键)
MANUAL_DROP = []
OUTCOME_OVERRIDE = {'vn_spratly_reclamation_2023_2026': '防务建设（非袭击事件）', 'luzon_strait_typhon_nmesis_2024_2026': '防务建设（非袭击事件）',
                    'scs_natuna_buildup_2025': '防务建设（非袭击事件）', 'scs_layanglayang_radar_2026': '防务建设（非袭击事件）'}
CAT_OVERRIDE = {'scs_natuna_ccg5402_2024_10': '海上小岛', 'rs_tutor_2024_06_12': '海上交通线', 'io_chem_pluto_2023_12_23': '海上交通线',
                'io_abdullah_2024_03_12': '海上交通线', 'ca_cuba_fuel_interdiction_2026_02_2026_09': '海上交通线',
                'med_arctic_metagaz_2026_03_03': '海上交通线', 'bs_jaguar_su35_2025_05_13': '海上交通线'}


TW_TERMS = [('共机', '解放军军机'), ('共舰', '解放军舰艇'), ('共军', '解放军'), ('国军', '台军'), ('陆方', '大陆方面'),
            ('台湾国防部', '台湾防务部门'), ('台国防部', '台湾防务部门'), ('总统府', '台湾地区领导人办公室'),
            ('总统赖清德', '台湾地区领导人赖清德'), ('总统召开', '台湾地区领导人召开'), ('赖清德总统', '台湾地区领导人赖清德'), ('蔡英文总统', '时任台湾地区领导人蔡英文'),
            ('“国防部”', '台湾防务部门'), ('陆委会', '台湾陆委会'), ('台湾台湾', '台湾')]


def tw_normalize(c):
    for k, v in list(c.items()):
        if isinstance(v, str) and k not in ('case_key',):
            v = v.replace('大陆方面', '\x00DL\x00')
            for a, b in TW_TERMS:
                v = v.replace(a, b)
            v = v.replace('\x00DL\x00', '大陆方面')
            c[k] = v.replace('台湾台湾', '台湾').replace('大大陆方面', '大陆方面')


def merge_into(dst, src):
    """把 src 的来源与图片并入 dst（按 URL 去重）。"""
    seen = set(s.get('url') for s in dst.get('sources') or [])
    for s in src.get('sources') or []:
        if s.get('url') not in seen:
            dst.setdefault('sources', []).append(s); seen.add(s.get('url'))
    seen = set((i.get('file_page'), i.get('file_name')) for i in dst.get('images') or [])
    for i in src.get('images') or []:
        if (i.get('file_page'), i.get('file_name')) not in seen:
            dst.setdefault('images', []).append(i)
    return dst


def sort_key(c):
    return (c.get('date_start') or '9999', c.get('case_key', ''))


def number(cases):
    out = []
    for cat, code, _ in CATS:
        group = sorted([c for c in cases if c.get('category') == cat], key=sort_key)
        for i, c in enumerate(group, 1):
            c['code'] = '%s-%02d' % (code, i)
            c['anchor'] = 'c_%s_%02d' % (_, i)
            out.append(c)
    rest = [c for c in cases if c.get('category') not in [x[0] for x in CATS]]
    for c in rest:
        print('!! 未归类案例', c.get('case_key'), c.get('category'))
    return out


def ref_key(s):
    return 'u_' + hashlib.md5((s.get('url') or (s.get('title', '') + s.get('date', ''))).encode()).hexdigest()[:12]


def register_sources(c, refs):
    keys = []
    for s in c.get('sources') or []:
        if not (s.get('url') or s.get('title')):
            continue
        k = ref_key(s)
        refs.add(k, s)
        keys.append(k)
    return keys


def fmt_date(c):
    a = c.get('date_start') or ''
    b = c.get('date_end') or ''
    if b and b != a:
        return '%s 至 %s' % (a, b)
    return a


_GM = None


def matched():
    global _GM
    if _GM is None:
        p = os.path.join(RESEARCH, 'G_matched.json')
        _GM = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {'by_case': {}, 'equipment': []}
    return _GM


def case_images(c):
    imgs = []
    src = []
    seen = set()
    IMG_EXT = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.tif', '.tiff')
    for im in (c.get('images') or []):
        fp = im.get('file_page') or ''
        if 'commons.wikimedia.org/wiki/File:' in fp and fp not in seen and fp.lower().endswith(IMG_EXT):
            seen.add(fp); src.append(im)
    for im in matched()['by_case'].get(c.get('case_key'), []):
        fp = im.get('file_page') or ''
        if fp and fp not in seen and fp.lower().endswith(IMG_EXT):
            seen.add(fp); im = dict(im)
            if im.get('level') == 'subject' and '资料' not in (im.get('desc_cn') or ''):
                im['desc_cn'] = (im.get('desc_cn') or '') + '（资料照片，非事件现场）'
            src.append(im)
    for i, im in enumerate(src[:3], 1):
        fn = im.get('file_name') or file_from_page(im.get('file_page'))
        url = im.get('direct_url')
        if not url and fn and (im.get('file_page', '').startswith('https://commons.wikimedia.org') or not im.get('file_page')):
            url = commons_url(fn)
        if not url:
            continue
        local = None
        for ext in ('.jpg', '.jpeg', '.png', '.webp'):
            p = os.path.join(IMGDIR, '%s_%d%s' % (c.get('case_key', 'x'), i, ext))
            if os.path.exists(p):
                local = p
                break
        imgs.append(dict(url=url, page=im.get('file_page') or url, local=local,
                         desc=clean(im.get('desc_cn') or ''), credit=im.get('credit') or '',
                         license=im.get('license') or '', date=im.get('date') or '',
                         save_as='%s_%d' % (c.get('case_key', 'x'), i), verified=im.get('verified')))
    return imgs


CONF_TXT = {'A': 'A（多源交叉印证）', 'B': 'B（单方官方或主流媒体，未见独立核实）',
            'C': 'C（单方声称，细节存疑）'}


def case_blocks(c, refs):
    keys = register_sources(c, refs)
    cite = '[@' + ','.join(keys) + ']' if keys else ''
    B = []
    B.append({'t': 'h2', 'tag': c['code'], 'text': clean(c.get('title_cn')), 'anchor': c['anchor'],
              'toc': True})
    if c.get('subtitle_cn'):
        B.append({'t': 'small', 'text': clean(c['subtitle_cn'])})
    pats = '、'.join((c.get('domains') or []) + (c.get('patterns') or []))
    rows = [('时间', fmt_date(c)), ('地点', clean(c.get('location_cn'))),
            ('攻击方', clean(c.get('attacker'))), ('防御方', clean(c.get('defender'))),
            ('表现样式', pats), ('结果', clean(c.get('outcome'))),
            ('攻击手段', clean(c.get('attack_means_cn'))), ('防御手段', clean(c.get('defense_means_cn'))),
            ('损失', clean(c.get('losses_cn'))),
            ('可信度', CONF_TXT.get((c.get('confidence') or '').strip()[:1], c.get('confidence') or ''))]
    rows = [(k, v) for k, v in rows if v]
    B.append({'t': 'kv', 'rows': rows, 'wide': ['攻击手段', '防御手段', '损失', '可信度']})
    imgs = case_images(c)
    leads = []
    for im in c.get('images') or []:
        fp = im.get('file_page') or ''
        if fp and ('commons.wikimedia.org' not in fp or fp.lower().endswith(('.webm', '.ogv', '.mp4'))):
            leads.append('%s（%s）' % (clean(im.get('desc_cn') or '影像'), fp))
    paras = [x.strip() for x in re.split(r'\n+', c.get('narrative_cn') or '') if x.strip()]
    if paras:
        B.append({'t': 'h3', 'text': '事件经过'})
        for i, ptxt in enumerate(paras):
            B.append({'t': 'p', 'text': clean(ptxt) + (cite if i == len(paras) - 1 else '')})
    # 图片插在经过之后
    for im in imgs:
        cap = im['desc'] or clean(c.get('title_cn'))
        src = 'Wikimedia Commons'
        if im['credit']:
            src += '，' + im['credit']
        if im['license']:
            src += '，' + im['license']
        if im['date']:
            src += '，' + im['date']
        B.append({'t': 'figure', 'kind': 'photo', 'remote_url': im['url'], 'page_url': im['page'],
                  'local': im['local'], 'caption': cap, 'source': src, 'width_mm': 140,
                  'case': c['code'], 'save_as': im['save_as']})
    if leads:
        B.append({'t': 'small', 'text': '影像线索：' + '；'.join(leads)})
    for field, head in (('defense_effect_cn', '防御与效果'), ('claims_compare_cn', '各方口径比对'),
                        ('analysis_cn', '简评')):
        txt = c.get(field)
        if not txt:
            continue
        B.append({'t': 'h3', 'text': head})
        ps = [x.strip() for x in re.split(r'\n+', txt) if x.strip()]
        for i, ptxt in enumerate(ps):
            add = cite if (field == 'claims_compare_cn' and i == len(ps) - 1) else ''
            B.append({'t': 'p', 'text': clean(ptxt) + add})
    return B
