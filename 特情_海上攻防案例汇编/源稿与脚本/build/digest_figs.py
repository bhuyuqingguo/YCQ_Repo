import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figs_lib import *
from digest_stats import *
from make_figs import CATCOL, OUTCOLS
CATCOL['海上交通线'] = '#1F8A70'
cs = load()
REGS = ['黑海','红海—亚丁湾','亚太','波罗的海—北海','波斯湾','东地中海','印度洋','加勒比','其他']
CATS = ['岛屿防卫','周边港口','海上小岛','远海机动编组','海上交通线']
LAB = {'岛屿防卫':'岛屿防卫','周边港口':'周边港口','海上小岛':'海上小岛','远海机动编组':'远海编组','海上交通线':'海上交通线'}

def f_region():
    fig, ax = plt.subplots(figsize=(7.2, 3.6), dpi=200); fig.patch.set_facecolor(PAL['cream']); ax.set_facecolor(PAL['cream'])
    R = REGS[::-1]; left = np.zeros(len(R))
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
    order = ['被击沉/摧毁','遭袭受损','部分拦截','防御成功','灰色地带对峙']
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
