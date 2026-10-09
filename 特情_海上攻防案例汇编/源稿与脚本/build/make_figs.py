# -*- coding: utf-8 -*-
"""数据驱动自绘图。用法：python3 make_figs.py  -> ../figs/*.png"""
import sys, os, json, datetime as dt
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figs_lib import *  # noqa
from cases_lib import load_all, number, CATS

CATCOL['海上交通线'] = '#1F8A70'
CATS_ORDER = [c[0] for c in CATS]
CAT_LABEL = {'岛屿防卫': '岛屿防卫', '周边港口': '周边重要港口', '海上小岛': '海上小岛（含礁、平台、离岸设施）',
             '远海机动编组': '远海机动编组', '海上交通线': '海上交通线（关联）'}


def outcome_class(o):
    o = o or ''
    if '灰色' in o or '对峙' in o:
        return '灰色地带对峙'
    if '击沉' in o or '摧毁' in o:
        return '被击沉/摧毁'
    if '部分' in o:
        return '部分拦截'
    if '防御成功' in o or '挫败' in o or '成功' in o:
        return '防御成功'
    if '受损' in o or '偷袭' in o or '攻击' in o:
        return '遭袭受损'
    return '其他'


OUTCOLS = {'被击沉/摧毁': '#C0392B', '遭袭受损': '#E07B67', '部分拦截': '#A8842F', '防御成功': '#2E93D6',
           '灰色地带对峙': '#6A4FA3', '其他': '#8A8474'}
MARK = {'被击沉/摧毁': 'X', '遭袭受损': 'o', '部分拦截': 'D', '防御成功': 's', '灰色地带对峙': '^', '其他': 'o'}


def pdate(s):
    try:
        return dt.date.fromisoformat((s or '')[:10])
    except Exception:
        return None


# ---------------------------------------------------------------- 世界图
def fig_world(cs):
    fig, ax = plt.subplots(figsize=(7.4, 4.1), dpi=200)
    fig.patch.set_facecolor(PAL['cream'])
    m = basemap(ax, (-12, 66, -95, 150), res='c')
    for c in cs:
        if c.get('lat') is None or c.get('lon') is None:
            continue
        try:
            x, y = m(float(c['lon']), float(c['lat']))
        except Exception:
            continue
        oc = outcome_class(c.get('outcome'))
        ax.plot(x, y, marker=MARK[oc], color=CATCOL.get(c['category'], '#888'), markersize=4.2,
                markeredgecolor='white', markeredgewidth=0.4, alpha=0.9, zorder=5)
    # 区域标注
    regions = [('黑海', 34, 46.5), ('红海—亚丁湾', 42, 15), ('东地中海', 33, 34.5), ('波斯湾—霍尔木兹', 54, 27.5),
               ('波罗的海', 20, 58.5), ('南海', 114, 13), ('台海—西太', 124, 24.5), ('加勒比', -70, 15),
               ('阿拉伯海—印度洋', 64, 13)]
    for name, lon, lat in regions:
        x, y = m(lon, lat)
        label(ax, x, y, name, size=6.5, color=PAL['grey'], ha='center', box=False)
    hs = [plt.Line2D([], [], marker='o', ls='', color=CATCOL[k], markersize=5, label=CAT_LABEL[k]) for k in CATS_ORDER]
    hs += [plt.Line2D([], [], marker=MARK[k], ls='', color='#555', markersize=4.5, label=k)
           for k in ('被击沉/摧毁', '遭袭受损', '部分拦截', '防御成功', '灰色地带对峙')]
    lg = ax.legend(handles=hs, loc='lower left', ncol=2, prop=FP(6), frameon=True, columnspacing=0.8,
                   handletextpad=0.3, borderpad=0.4)
    lg.get_frame().set_facecolor('white'); lg.get_frame().set_alpha(0.88); lg.get_frame().set_edgecolor('#C9C2B0')
    return save(fig, 'f_world.png')


# ---------------------------------------------------------------- 区域图
REGIONS = {
    'blacksea': dict(box=(41.0, 47.6, 27.5, 41.5), regions=['黑海', '亚速海'], name='f_blacksea.png', size=(7.2, 4.2)),
    'redsea': dict(box=(10.5, 30.5, 32.0, 52.0), regions=['红海-亚丁湾', '阿拉伯海-印度洋'], name='f_redsea.png', size=(6.4, 6.0),
                   lonlim=(32, 52)),
    'mideast': dict(box=(23.0, 37.5, 28.0, 60.5), regions=['东地中海', '波斯湾-霍尔木兹-阿曼湾'], name='f_mideast.png', size=(7.2, 3.8)),
    'asia': dict(box=(5.0, 39.0, 108.0, 146.0), regions=['南海', '台海', '东海-西太', '日本海-朝鲜半岛'], name='f_asia.png', size=(6.8, 6.0)),
    'baltic': dict(box=(53.5, 61.5, 8.0, 31.0), regions=['波罗的海-北海'], name='f_baltic.png', size=(7.2, 4.4)),
}


def fig_region(cs, key, extra=None):
    R = REGIONS[key]
    fig, ax = plt.subplots(figsize=R['size'], dpi=200)
    fig.patch.set_facecolor(PAL['cream'])
    lat0, lat1, lon0, lon1 = R['box']
    m = basemap(ax, R['box'], res='i', grid=(2 if key in ('blacksea', 'baltic') else 5))
    pts = []
    for c in cs:
        try:
            lat, lon = float(c['lat']), float(c['lon'])
        except Exception:
            continue
        if not (lat0 <= lat <= lat1 and lon0 <= lon <= lon1):
            continue
        x, y = m(lon, lat)
        oc = outcome_class(c.get('outcome'))
        ax.plot(x, y, marker=MARK[oc], color=CATCOL.get(c['category'], '#888'), markersize=6,
                markeredgecolor='white', markeredgewidth=0.6, zorder=5)
        pts.append((x, y, c['code']))
    # 编号标注：同点聚合
    groups = defaultdict(list)
    W = (m.xmax - m.xmin)
    for x, y, code in pts:
        k = (round(x / (W * 0.03)), round(y / (W * 0.03)))
        groups[k].append((x, y, code))
    for k, items in groups.items():
        x = sum(i[0] for i in items) / len(items); y = sum(i[1] for i in items) / len(items)
        codes = sorted(set(i[2] for i in items))
        txt = '、'.join(codes) if len(codes) <= 3 else '、'.join(codes[:3]) + '等%d案' % len(codes)
        label(ax, x, y, ' ' + txt, size=6, dx=W * 0.008)
    if extra:
        extra(m, ax)
    present = sorted(set(c['category'] for c in cs if c.get('code') in [p[2] for p in pts]),
                     key=CATS_ORDER.index)
    hs = [plt.Line2D([], [], marker='o', ls='', color=CATCOL[k], markersize=5, label=CAT_LABEL[k]) for k in present]
    hs += [plt.Line2D([], [], marker=MARK[k], ls='', color='#555', markersize=4.5, label=k)
           for k in ('被击沉/摧毁', '遭袭受损', '部分拦截', '防御成功', '灰色地带对峙')]
    lg = ax.legend(handles=hs, loc=R.get('legend', 'lower left'), prop=FP(6), frameon=True, ncol=1)
    lg.get_frame().set_facecolor('white'); lg.get_frame().set_alpha(0.88); lg.get_frame().set_edgecolor('#C9C2B0')
    return save(fig, R['name'])


# ---------------------------------------------------------------- 时间线
LANES = [('黑海', ['黑海', '亚速海']), ('红海—亚丁湾', ['红海-亚丁湾']),
         ('东地中海—海湾', ['东地中海', '波斯湾-霍尔木兹-阿曼湾']),
         ('亚太', ['南海', '台海', '东海-西太', '日本海-朝鲜半岛']),
         ('波罗的海—北海', ['波罗的海-北海']), ('其他海域', None)]


def lane_of(region):
    for i, (name, regs) in enumerate(LANES):
        if regs and region in regs:
            return i
    return len(LANES) - 1


def fig_timeline(cs, notes=()):
    fig, ax = plt.subplots(figsize=(7.4, 3.9), dpi=200)
    fig.patch.set_facecolor(PAL['cream']); ax.set_facecolor(PAL['cream'])
    import random
    random.seed(3)
    for c in cs:
        d = pdate(c.get('date_start'))
        if not d:
            continue
        ln = lane_of(c.get('region'))
        y = len(LANES) - 1 - ln + random.uniform(-0.22, 0.22)
        oc = outcome_class(c.get('outcome'))
        ax.plot(d, y, marker=MARK[oc], color=CATCOL.get(c['category'], '#888'), markersize=4.6,
                markeredgecolor='white', markeredgewidth=0.4, zorder=4, alpha=0.92)
    ax.set_yticks(range(len(LANES)))
    ax.set_yticklabels([l[0] for l in LANES][::-1])
    for lab in ax.get_yticklabels():
        lab.set_fontproperties(FP(7.5)); lab.set_color(PAL['navy'])
    ax.set_xlim(dt.date(2023, 1, 1), dt.date(2026, 10, 15))
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 7]))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y.%m'))
    for i in range(len(LANES)):
        ax.axhspan(i - 0.45, i + 0.45, color=('#EFEBDF' if i % 2 else '#F3F0E7'), zorder=0)
    style_axes(ax, ygrid=False)
    ax.spines['left'].set_visible(False)
    for d, text, lane in notes:
        y = len(LANES) - 1 - lane + 0.33
        ax.annotate(text, (dt.date.fromisoformat(d), y), fontproperties=FP(5.6), color=PAL['grey'],
                    ha='center', va='bottom')
    hs = [plt.Line2D([], [], marker='o', ls='', color=CATCOL[k], markersize=4.5, label=CAT_LABEL[k].split('（')[0])
          for k in CATS_ORDER]
    lg = ax.legend(handles=hs, loc='upper center', bbox_to_anchor=(0.5, -0.09), ncol=5, prop=FP(6.5), frameon=False)
    return save(fig, 'f_timeline.png')


# ---------------------------------------------------------------- 统计：场景×样式
STYLES = ['空中', '水面', '水下', '岸基', '电磁', '蜂群', '集群', '异构', '饱和', '偷袭/突防', '单平台']


def fig_heat(cs):
    M = np.zeros((len(CATS_ORDER), len(STYLES)))
    for c in cs:
        i = CATS_ORDER.index(c['category'])
        tags = set((c.get('domains') or []) + (c.get('patterns') or []))
        for j, s in enumerate(STYLES):
            if any(s == t or (s in t) for t in tags):
                M[i, j] += 1
    fig, ax = plt.subplots(figsize=(7.2, 2.9), dpi=200)
    fig.patch.set_facecolor(PAL['cream'])
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list('xg', ['#F7F4EC', '#9CC8E8', '#2E93D6', '#12233B'])
    ax.imshow(M, cmap=cmap, aspect='auto', vmin=0, vmax=max(1, M.max()))
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            v = int(M[i, j])
            if v:
                ax.text(j, i, str(v), ha='center', va='center', fontproperties=FPB(8),
                        color='white' if v > M.max() * 0.55 else PAL['navy'])
    ax.set_xticks(range(len(STYLES))); ax.set_xticklabels(STYLES)
    ax.set_yticks(range(len(CATS_ORDER))); ax.set_yticklabels([CAT_LABEL[c].split('（')[0] for c in CATS_ORDER])
    for lab in ax.get_xticklabels() + ax.get_yticklabels():
        lab.set_fontproperties(FP(7.5)); lab.set_color(PAL['navy'])
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks(np.arange(-.5, len(STYLES), 1), minor=True); ax.set_yticks(np.arange(-.5, len(CATS_ORDER), 1), minor=True)
    ax.grid(which='minor', color='white', linewidth=1.2); ax.tick_params(which='minor', length=0)
    return save(fig, 'f_heat.png'), M


def fig_outcome(cs):
    order = ['被击沉/摧毁', '遭袭受损', '部分拦截', '防御成功', '灰色地带对峙', '其他']
    fig, ax = plt.subplots(figsize=(7.0, 2.8), dpi=200)
    fig.patch.set_facecolor(PAL['cream']); ax.set_facecolor(PAL['cream'])
    cats = CATS_ORDER[::-1]
    left = np.zeros(len(cats))
    for o in order:
        vals = np.array([sum(1 for c in cs if c['category'] == k and outcome_class(c.get('outcome')) == o) for k in cats])
        if vals.sum() == 0:
            continue
        ax.barh(range(len(cats)), vals, left=left, color=OUTCOLS[o], label=o, height=0.62, edgecolor='white', linewidth=0.6)
        for i, v in enumerate(vals):
            if v:
                ax.text(left[i] + v / 2, i, str(v), ha='center', va='center', fontproperties=FPB(7), color='white')
        left += vals
    ax.set_yticks(range(len(cats))); ax.set_yticklabels([CAT_LABEL[c].split('（')[0] for c in cats])
    style_axes(ax, ygrid=False)
    ax.grid(axis='x', color=PAL['grid'], linewidth=0.7)
    for lab in ax.get_yticklabels():
        lab.set_fontproperties(FP(7.5)); lab.set_color(PAL['navy'])
    ax.set_xlabel('案例数', fontproperties=FP(7.5), color=PAL['grey'])
    lg = ax.legend(loc='lower right', prop=FP(6.5), frameon=False, ncol=1)
    return save(fig, 'f_outcome.png')


def fig_year(cs):
    years = [2023, 2024, 2025, 2026]
    fig, ax = plt.subplots(figsize=(6.6, 2.8), dpi=200)
    fig.patch.set_facecolor(PAL['cream']); ax.set_facecolor(PAL['cream'])
    bottom = np.zeros(len(years))
    for k in CATS_ORDER:
        vals = np.array([sum(1 for c in cs if c['category'] == k and (c.get('date_start') or '')[:4] == str(y)) for y in years])
        ax.bar(range(len(years)), vals, bottom=bottom, color=CATCOL[k], width=0.58, label=CAT_LABEL[k].split('（')[0],
               edgecolor='white', linewidth=0.6)
        for i, v in enumerate(vals):
            if v >= 2:
                ax.text(i, bottom[i] + v / 2, str(v), ha='center', va='center', fontproperties=FPB(7), color='white')
        bottom += vals
    ax.set_xticks(range(len(years))); ax.set_xticklabels(['2023年', '2024年', '2025年', '2026年（至9月）'])
    style_axes(ax)
    for lab in ax.get_xticklabels():
        lab.set_fontproperties(FP(7.5)); lab.set_color(PAL['navy'])
    ax.legend(prop=FP(6.5), frameon=False, loc='upper left', ncol=1, bbox_to_anchor=(1.0, 1.0))
    return save(fig, 'f_year.png')


if __name__ == '__main__':
    cs = number(load_all())
    print(fig_world(cs)); print(fig_timeline(cs))
    for k in REGIONS:
        print(fig_region(cs, k))
    print(fig_heat(cs)[0]); print(fig_outcome(cs)); print(fig_year(cs))
