import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figs_lib import *
from digest_stats import *
from make_figs import CATCOL, OUTCOLS
CATCOL['海上交通线'] = '#1F8A70'
cs = load()
REGS = ['黑海','红海—亚丁湾','南海','台海及东北亚','东南亚海峡','波罗的海—北海','波斯湾','东地中海','印度洋','加勒比','其他']
CATS = ['岛屿防卫','周边港口','海上小岛','远海机动编组','海上交通线']
LAB = {'岛屿防卫':'岛屿防卫','周边港口':'周边港口','海上小岛':'海上小岛','远海机动编组':'远海编组','海上交通线':'海上交通线'}

def f_region():
    fig, ax = plt.subplots(figsize=(7.2, 3.6), dpi=200); fig.patch.set_facecolor(PAL['cream']); ax.set_facecolor(PAL['cream'])
    R = [r for r in REGS if any(c['R']==r for c in cs)][::-1]; left = np.zeros(len(R))
    for k in CATS:
        v = np.array([sum(1 for c in cs if c['R']==r and c['category']==k) for r in R])
        ax.barh(range(len(R)), v, left=left, color=CATCOL[k], height=0.62, label=LAB[k], edgecolor='white', linewidth=0.6)
        for i, x in enumerate(v):
            if x >= 3: ax.text(left[i]+x/2, i, str(x), ha='center', va='center', fontproperties=FPB(6.5), color='white')
        left += v
    for i, x in enumerate(left): ax.text(x+0.8, i, '%d' % x, va='center', fontproperties=FPB(7), color=PAL['navy'])
    ax.set_yticks(range(len(R))); ax.set_yticklabels(R); style_axes(ax, ygrid=False); ax.grid(axis='x', color=PAL['grid'], lw=0.7)
    for l in ax.get_yticklabels(): l.set_fontproperties(FP(7.5)); l.set_color(PAL['navy'])
    ax.set_xlabel('案例数', fontproperties=FP(7.5), color=PAL['grey']); ax.legend(prop=FP(6.5), frameon=False, loc='lower right')
    return save(fig, 'd_region.png')

def f_threat():
    order = ['被击沉/摧毁','遭袭受损','部分拦截','防御成功','灰色地带对峙','防务建设']
    T = sorted(TYPES, key=lambda k: sum(1 for c in cs if k in c['T']))
    fig, ax = plt.subplots(figsize=(7.2, 3.5), dpi=200); fig.patch.set_facecolor(PAL['cream']); ax.set_facecolor(PAL['cream'])
    left = np.zeros(len(T))
    for o in order:
        v = np.array([sum(1 for c in cs if k in c['T'] and c['O']==o) for k in T])
        ax.barh(range(len(T)), v, left=left, color=OUTCOLS[o], height=0.62, label=o, edgecolor='white', linewidth=0.6)
        for i, x in enumerate(v):
            if x >= 4: ax.text(left[i]+x/2, i, str(x), ha='center', va='center', fontproperties=FPB(6.5), color='white')
        left += v
    for i, x in enumerate(left): ax.text(x+0.8, i, '%d' % x, va='center', fontproperties=FPB(7), color=PAL['navy'])
    ax.set_yticks(range(len(T))); ax.set_yticklabels(T); style_axes(ax, ygrid=False); ax.grid(axis='x', color=PAL['grid'], lw=0.7)
    for l in ax.get_yticklabels(): l.set_fontproperties(FP(7.5)); l.set_color(PAL['navy'])
    ax.set_xlabel('涉及案例数（一个案例可涉及多类威胁）', fontproperties=FP(7.5), color=PAL['grey']); ax.legend(prop=FP(6.5), frameon=False, loc='lower right')
    return save(fig, 'd_threat.png')

def f_trend():
    Y = ['2023','2024','2025','2026']
    n = {y: sum(1 for c in cs if c['Y']==y) for y in Y}
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.0), dpi=200, gridspec_kw={'width_ratios':[1.25,1]}); fig.patch.set_facecolor(PAL['cream'])
    series = [('导弹与火力打击','#12233B'),('无人机','#2E93D6'),('无人艇','#A8842F'),('灰色地带施压','#6A4FA3'),('登临/劫持/登陆','#C0392B')]
    a1.set_facecolor(PAL['cream'])
    for k, col in series:
        v = [100*sum(1 for c in cs if c['Y']==y and k in c['T'])/n[y] for y in Y]
        a1.plot(range(4), v, marker='o', color=col, lw=1.6, markersize=4, label=k)
    a1.set_xticks(range(4)); a1.set_xticklabels(['2023','2024','2025','2026\n（至9月）']); style_axes(a1)
    a1.set_ylabel('占当年案例比例（％）', fontproperties=FP(7), color=PAL['grey']); a1.legend(prop=FP(6), frameon=False, loc='upper left', ncol=2)
    a1.set_title('主要威胁类型占比变化', fontproperties=FPB(8), color=PAL['navy'])
    a2.set_facecolor(PAL['cream'])
    u = [100*sum(1 for c in cs if c['Y']==y and c['T']&{'无人机','无人艇','水下威胁'})/n[y] for y in Y]
    a2.bar(range(4), [n[y] for y in Y], color='#E3DCC9', width=0.55)
    for i, y in enumerate(Y): a2.text(i, 3, '%d案' % n[y], ha='center', fontproperties=FPB(7), color=PAL['navy'])
    b = a2.twinx(); b.plot(range(4), u, color='#C0392B', marker='o', lw=1.8)
    for i, x in enumerate(u): b.text(i, x+3, '%d％' % round(x), ha='center', fontproperties=FPB(7), color='#C0392B')
    b.set_ylim(0, 100); b.tick_params(colors=PAL['grey'], labelsize=7)
    for s in ('top',): b.spines[s].set_visible(False)
    a2.set_xticks(range(4)); a2.set_xticklabels(['2023','2024','2025','2026']); style_axes(a2); a2.set_ylim(0, 70)
    a2.set_title('案例数与无人平台参与比例', fontproperties=FPB(8), color=PAL['navy'])
    fig.tight_layout(); return save(fig, 'd_trend.png')

if __name__ == '__main__':
    for f in (f_region, f_threat, f_trend): print(f())


def f_quarter():
    import datetime as dt
    qs = [(y, q) for y in range(2023, 2027) for q in range(1, 5) if not (y == 2026 and q == 4)]
    grp = [('黑海', '#C0392B'), ('红海—亚丁湾', '#A8842F'), ('南海', '#2E93D6'), ('波斯湾', '#6A4FA3')]
    fig, ax = plt.subplots(figsize=(7.4, 3.0), dpi=200); fig.patch.set_facecolor(PAL['cream']); ax.set_facecolor(PAL['cream'])
    def qof(c):
        d = c.get('date_start') or ''
        try: return (int(d[:4]), (int(d[5:7]) - 1) // 3 + 1)
        except Exception: return None
    tot = [sum(1 for c in cs if qof(c) == q) for q in qs]
    ax.bar(range(len(qs)), tot, color='#E3DCC9', width=0.7, label='全部案例')
    for r, col in grp:
        ax.plot(range(len(qs)), [sum(1 for c in cs if qof(c) == q and c['R'] == r) for q in qs], color=col, marker='o', ms=3, lw=1.4, label=r)
    ax.set_xticks(range(len(qs))); ax.set_xticklabels(['%dQ%d' % (y % 100, q) for y, q in qs])
    style_axes(ax); ax.legend(prop=FP(6.5), frameon=False, ncol=5, loc='upper left')
    for l in ax.get_xticklabels(): l.set_fontproperties(FP(6.5))
    ax.set_ylabel('案例数（按起始日期）', fontproperties=FP(7), color=PAL['grey'])
    return save(fig, 'd_quarter.png')


def f_scene_threat():
    M = np.array([[sum(1 for c in cs if c['category'] == k and t in c['T']) for t in TYPES] for k in CATS])
    fig, ax = plt.subplots(figsize=(7.4, 2.7), dpi=200); fig.patch.set_facecolor(PAL['cream'])
    from matplotlib.colors import LinearSegmentedColormap
    ax.imshow(M, cmap=LinearSegmentedColormap.from_list('x', ['#F7F4EC', '#9CC8E8', '#2E93D6', '#12233B']), aspect='auto')
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i, j]: ax.text(j, i, str(M[i, j]), ha='center', va='center', fontproperties=FPB(7.5), color='white' if M[i, j] > M.max() * .5 else PAL['navy'])
    ax.set_xticks(range(len(TYPES))); ax.set_xticklabels([t.replace('/', '/\n') for t in TYPES]); ax.set_yticks(range(len(CATS))); ax.set_yticklabels([LAB[k] for k in CATS])
    for l in ax.get_xticklabels() + ax.get_yticklabels(): l.set_fontproperties(FP(7)); l.set_color(PAL['navy'])
    ax.tick_params(length=0)
    for s in ax.spines.values(): s.set_visible(False)
    return save(fig, 'd_scene_threat.png')


def f_year_region():
    Y = ['2023', '2024', '2025', '2026']
    RR = [r for r in REGS if any(c['R']==r for c in cs)]
    M = np.array([[sum(1 for c in cs if c['R'] == r and c['Y'] == y) for y in Y] for r in RR])
    fig, ax = plt.subplots(figsize=(5.6, 3.4), dpi=200); fig.patch.set_facecolor(PAL['cream'])
    from matplotlib.colors import LinearSegmentedColormap
    ax.imshow(M, cmap=LinearSegmentedColormap.from_list('x', ['#F7F4EC', '#E9B7A8', '#C0392B', '#6E1F17']), aspect='auto')
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            ax.text(j, i, str(M[i, j]) if M[i, j] else '—', ha='center', va='center', fontproperties=FPB(7.5), color='white' if M[i, j] > M.max() * .5 else PAL['navy'])
    ax.set_xticks(range(4)); ax.set_xticklabels(['2023', '2024', '2025', '2026（1—9月）']); ax.set_yticks(range(len(RR))); ax.set_yticklabels(RR)
    for l in ax.get_xticklabels() + ax.get_yticklabels(): l.set_fontproperties(FP(7.5)); l.set_color(PAL['navy'])
    ax.tick_params(length=0)
    for s in ax.spines.values(): s.set_visible(False)
    return save(fig, 'd_year_region.png')


def f_domain_pattern():
    D = ['空中', '水面', '岸基', '水下', '电磁']; P = ['集群', '单平台', '偷袭/突防', '异构', '饱和', '蜂群']
    dom = Counter(d for c in cs for d in (c.get('domains') or [])); pat = Counter(p for c in cs for p in (c.get('patterns') or []))
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 2.7), dpi=200); fig.patch.set_facecolor(PAL['cream'])
    for ax, keys, cnt, col, t in ((a1, D, dom, '#2E93D6', '按作战域'), (a2, P, pat, '#A8842F', '按组织形态')):
        ax.set_facecolor(PAL['cream']); v = [cnt.get(k, 0) for k in keys]
        ax.bar(range(len(keys)), v, color=col, width=0.6)
        for i, x in enumerate(v): ax.text(i, x + 1.5, str(x), ha='center', fontproperties=FPB(7), color=PAL['navy'])
        ax.set_xticks(range(len(keys))); ax.set_xticklabels(keys); style_axes(ax)
        for l in ax.get_xticklabels(): l.set_fontproperties(FP(7)); l.set_color(PAL['navy'])
        ax.set_title(t + '（案例数，可多选）', fontproperties=FPB(8), color=PAL['navy'])
    fig.tight_layout(); return save(fig, 'd_domain_pattern.png')


def f_outcome_year():
    order = ['被击沉/摧毁', '遭袭受损', '部分拦截', '防御成功', '灰色地带对峙', '防务建设']; Y = ['2023', '2024', '2025', '2026']
    fig, ax = plt.subplots(figsize=(6.4, 2.8), dpi=200); fig.patch.set_facecolor(PAL['cream']); ax.set_facecolor(PAL['cream'])
    bottom = np.zeros(4)
    for o in order:
        v = np.array([100 * sum(1 for c in cs if c['Y'] == y and c['O'] == o) / max(1, sum(1 for c in cs if c['Y'] == y)) for y in Y])
        ax.bar(range(4), v, bottom=bottom, color=OUTCOLS[o], width=0.58, label=o, edgecolor='white', lw=0.6)
        for i, x in enumerate(v):
            if x >= 7: ax.text(i, bottom[i] + x / 2, '%d％' % round(x), ha='center', va='center', fontproperties=FPB(6.5), color='white')
        bottom += v
    ax.set_xticks(range(4)); ax.set_xticklabels(['2023', '2024', '2025', '2026（1—9月）']); style_axes(ax); ax.set_ylim(0, 100)
    for l in ax.get_xticklabels(): l.set_fontproperties(FP(7.5))
    ax.legend(prop=FP(6.5), frameon=False, loc='upper left', bbox_to_anchor=(1, 1))
    return save(fig, 'd_outcome_year.png')


if __name__ == '__main__':
    for f in (f_quarter, f_scene_threat, f_year_region, f_domain_pattern, f_outcome_year): print(f())
