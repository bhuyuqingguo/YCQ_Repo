# -*- coding: utf-8 -*-
"""分析类自绘图：成本量级、拦截弹消耗、无人艇能力演进、港口多层防御示意。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figs_lib import *  # noqa
import matplotlib.patches as mp

C5 = ['#2E93D6', '#C0392B', '#A8842F', '#6A4FA3', '#1F8A70']


def fig_cost():
    rows = [  # (组, 名称, 低, 高, 备注)
        ('攻击方平台', '“沙希德-136”类无人机', 2e4, 2.9e5, '估算与泄露文件口径差异大'),
        ('攻击方平台', '“海宝宝”无人艇（Sea Baby）', 2.16e5, 2.46e5, '乌安全局自述约850万格里夫纳'),
        ('攻击方平台', 'Magura V5 无人艇', 2.73e5, 2.73e5, '约1000万格里夫纳（含控制站）'),
        ('攻击方平台', '“玛丽奇卡”无人潜航器', 4.33e5, 4.33e5, '约1600万格里夫纳（乌媒）'),
        ('拦截手段', '“铁束”激光（单次）', 2, 5, '单次边际成本'),
        ('拦截手段', 'APKWS 激光制导火箭', 1.8e4, 2.2e4, ''),
        ('拦截手段', '“塔米尔”拦截弹（铁穹）', 4e4, 1e5, ''),
        ('拦截手段', 'RAM 近程舰空导弹', 9e5, 9.5e5, ''),
        ('拦截手段', 'ESSM Block II', 1.49e6, 1.49e6, ''),
        ('拦截手段', '“紫菀”15/30', 1.5e6, 2.5e6, ''),
        ('拦截手段', '“标准-6”', 4.0e6, 4.9e6, ''),
        ('拦截手段', '“标准-3” Block IB', 1.0e7, 1.25e7, ''),
        ('拦截手段', '“标准-3” Block IIA', 2.87e7, 3.64e7, ''),
        ('被毁目标参考', 'MQ-9 无人机（单架）', 3.0e7, 3.0e7, '美方官员口径'),
        ('被毁目标参考', '“谢尔盖·科托夫”号巡逻舰', 6.5e7, 6.5e7, '乌方估值'),
    ]
    fig, ax = plt.subplots(figsize=(7.4, 5.2), dpi=200)
    fig.patch.set_facecolor(PAL['cream']); ax.set_facecolor(PAL['cream'])
    gc = {'攻击方平台': '#C0392B', '拦截手段': '#2E93D6', '被毁目标参考': '#A8842F'}
    y = 0; yt = []; yl = []; prev = None
    for g, n, lo, hi, note in rows[::-1]:
        if prev and g != prev:
            y += 0.6
        prev = g
        if hi / lo > 1.05:
            ax.plot([lo, hi], [y, y], color=gc[g], lw=5.5, solid_capstyle='round', alpha=0.85)
        else:
            ax.plot([lo], [y], 'o', color=gc[g], markersize=7)
        txt = '%s' % (fmt(lo) if hi / lo <= 1.05 else fmt(lo) + '—' + fmt(hi))
        ax.text(hi * 1.35, y, txt, fontproperties=FP(6.5), color=PAL['navy'], va='center')
        yt.append(y); yl.append(n); y += 1
    ax.set_xscale('log'); ax.set_xlim(1, 3e8)
    ax.set_yticks(yt); ax.set_yticklabels(yl)
    for lab in ax.get_yticklabels():
        lab.set_fontproperties(FP(7)); lab.set_color(PAL['navy'])
    ax.set_xticks([1, 1e2, 1e4, 1e5, 1e6, 1e7, 1e8])
    ax.set_xticklabels(['1美元', '100美元', '1万', '10万', '100万', '1000万', '1亿'])
    style_axes(ax, ygrid=False)
    ax.grid(axis='x', color=PAL['grid'], linewidth=0.7)
    for lab in ax.get_xticklabels():
        lab.set_fontproperties(FP(7))
    hs = [plt.Line2D([], [], color=gc[k], lw=5, label=k) for k in gc]
    ax.legend(handles=hs, prop=FP(7), frameon=False, loc='upper right')
    ax.set_xlabel('单价（美元，对数坐标；区间表示不同来源口径）', fontproperties=FP(7), color=PAL['grey'])
    return save(fig, 'f_cost.png')


def fmt(v):
    if v >= 1e8: return '%.1f亿' % (v / 1e8)
    if v >= 1e4: return ('%.0f万' % (v / 1e4)) if v >= 1e5 else ('%.1f万' % (v / 1e4))
    return '%.0f美元' % v


def fig_expend():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 2.9), dpi=200, gridspec_kw={'width_ratios': [1.05, 1]})
    fig.patch.set_facecolor(PAL['cream'])
    vals = [120, 80, 20]; labs = ['“标准-2”约120枚', '“标准-6”约80枚', 'ESSM与“标准-3”约20枚']
    w, _ = a1.pie(vals, colors=['#2E93D6', '#12233B', '#A8842F'], startangle=90, counterclock=False,
                  wedgeprops=dict(width=0.38, edgecolor=PAL['cream'], linewidth=1.5))
    a1.text(0, 0.06, '约220枚', fontproperties=FPB(10), ha='center', color=PAL['navy'])
    a1.text(0, -0.2, '舰空导弹', fontproperties=FP(7), ha='center', color=PAL['grey'])
    a1.legend(w, labs, prop=FP(6.5), frameon=False, loc='upper center', bbox_to_anchor=(0.5, 0.02), ncol=1)
    a1.set_title('美海军红海作战拦截弹构成（至2025-01）', fontproperties=FPB(8), color=PAL['navy'])
    a2.set_facecolor(PAL['cream'])
    items = [('舰空导弹', 220), ('5英寸炮弹', 160), ('交战次数', 380)]
    a2.barh(range(3), [v for _, v in items][::-1], color=['#8A8474', '#A8842F', '#2E93D6'], height=0.55)
    a2.set_yticks(range(3)); a2.set_yticklabels([n for n, _ in items][::-1])
    for i, v in enumerate([v for _, v in items][::-1]):
        a2.text(v + 6, i, str(v), va='center', fontproperties=FPB(7.5), color=PAL['navy'])
    style_axes(a2, ygrid=False); a2.set_xlim(0, 440)
    for lab in a2.get_yticklabels():
        lab.set_fontproperties(FP(7.5)); lab.set_color(PAL['navy'])
    a2.set_title('消耗与交战次数', fontproperties=FPB(8), color=PAL['navy'])
    fig.tight_layout()
    return save(fig, 'f_expend.png')


def fig_usv():
    ev = [  # (日期, 文本, 层, 颜色)
        ('2023-05-24', '远程奔袭俄侦察船\n（博斯普鲁斯东北）', 1, C5[0]),
        ('2023-08-04', '航程约740千米\n新罗西斯克命中登陆舰', -1, C5[0]),
        ('2024-02-01', '多艇围攻击沉\n“伊万诺韦茨”号', 1, C5[1]),
        ('2024-03-05', '两个月内第三艘\n“谢尔盖·科托夫”号', -1, C5[1]),
        ('2024-12-31', '艇载R-73\n击落Mi-8', 1, C5[2]),
        ('2025-05-02', '艇载AIM-9\n击落两架苏-30', -1, C5[2]),
        ('2025-08-28', '俄无人艇首次击中\n乌海军“辛菲罗波尔”号', 0.55, C5[3]),
        ('2025-11-28', '土耳其专属经济区\n打击“影子船队”油轮', -1, C5[4]),
        ('2025-12-15', '无人潜航器突入\n新罗西斯克打潜艇', 1.25, C5[3]),
        ('2026-08-12', '15类武器异构齐袭\n新罗西斯克', -1, C5[1]),
    ]
    import datetime as dt
    fig, ax = plt.subplots(figsize=(7.4, 3.3), dpi=200)
    fig.patch.set_facecolor(PAL['cream']); ax.set_facecolor(PAL['cream'])
    d0, d1 = dt.date(2023, 4, 1), dt.date(2026, 10, 1)
    ax.plot([d0, d1], [0, 0], color=PAL['navy'], lw=1.6)
    for y in range(2023, 2027):
        d = dt.date(y, 1, 1)
        if d0 <= d <= d1:
            ax.plot([d, d], [-0.08, 0.08], color=PAL['navy'], lw=1)
            ax.text(d, -0.2, str(y), ha='center', fontproperties=FPB(7), color=PAL['navy'])
    for s, t, lvl, col in ev:
        d = dt.date.fromisoformat(s)
        h = (0.95 * lvl) if lvl > 0 else -0.75
        ax.plot([d, d], [0, h * 0.78], color=col, lw=0.8)
        ax.plot(d, 0, 'o', color=col, markersize=5, markeredgecolor='white')
        ax.text(d, h, s[2:].replace('-', '.') + '\n' + t, ha='center', va='center', fontproperties=FP(6),
                color=PAL['navy'], bbox=dict(boxstyle='round,pad=0.25', fc='white', ec=col, lw=0.8))
    ax.set_ylim(-1.35, 1.65); ax.set_xlim(d0, d1); ax.axis('off')
    lab = [('远程打击', C5[0]), ('集群击沉', C5[1]), ('对空作战', C5[2]), ('水下/对手反制', C5[3]), ('打击航运', C5[4])]
    hs = [plt.Line2D([], [], marker='o', ls='', color=c, label=n, markersize=5) for n, c in lab]
    ax.legend(handles=hs, prop=FP(6.5), frameon=False, loc='lower center', ncol=5, bbox_to_anchor=(0.5, -0.1))
    return save(fig, 'f_usv.png')


def fig_layers():
    fig, ax = plt.subplots(figsize=(7.4, 4.4), dpi=200)
    fig.patch.set_facecolor(PAL['cream']); ax.set_facecolor(PAL['cream'])
    cx, cy = 0, 0
    rings = [(8.4, '外层：预警与情报', '卫星/商业影像、巡逻机、AIS 关联、电子侦察；对发射阵地与母船的先期打击', '#E3EEF6'),
             (6.6, '中层：区域拦截', '战斗机/舰载机截击、区域舰空导弹、岸基中远程防空、对远程弹道导弹的高层拦截', '#CFE2F0'),
             (4.8, '近层：低成本处置', '舰炮、近防炮、机枪组、直升机、拦截无人机、电子干扰、激光（新兴）', '#B3D2EA'),
             (3.0, '港口门口：物理拦阻', '浮栅、拦阻网、沉船堵口、水下声呐与拦阻网、入口检查', '#8DBCE0')]
    for r, name, desc, col in rings:
        ax.add_patch(mp.Wedge((cx, cy), r, 180, 360, color=col, ec='white', lw=1.6, zorder=1))
    radii = [r for r, *_ in rings] + [1.25]
    for i, (r, name, desc, col) in enumerate(rings):
        mid = (r + radii[i + 1]) / 2
        ax.text(cx, cy - mid + 0.28, name, ha='center', va='center', fontproperties=FPB(7.5), color=PAL['navy'], zorder=3)
        ax.text(cx, cy - mid - 0.32, desc, ha='center', va='center', fontproperties=FP(5.6), color=PAL['navy'], zorder=3)
    ax.add_patch(mp.Wedge((cx, cy), 1.25, 180, 360, color='#12233B', zorder=2))
    ax.text(cx, cy - 0.62, '核心目标', ha='center', va='center', fontproperties=FPB(6.5), color='white', zorder=3)
    ax.add_patch(mp.Rectangle((-9.2, 0), 18.4, 1.1, color='#EFEBDF', zorder=2))
    ax.plot([-9.2, 9.2], [0, 0], color=PAL['grey'], lw=1.2, zorder=3)
    ax.text(0, 0.55, '岸线 · 泊位 / 船坞 / 指挥所：加固、遮蔽、分散、伪装、损管', ha='center', va='center',
            fontproperties=FPB(7), color=PAL['navy'], zorder=4)
    ax.text(8.9, -8.2, '海  向', ha='right', fontproperties=FP(7), color=PAL['grey'])
    ax.set_xlim(-9.2, 9.2); ax.set_ylim(-8.6, 1.15); ax.set_aspect('equal'); ax.axis('off')
    return save(fig, 'f_layers.png')


if __name__ == '__main__':
    for f in (fig_cost, fig_expend, fig_usv, fig_layers):
        print(f())
