# -*- coding: utf-8 -*-
"""数据类自绘图：合同、融资、用户规模等。数据同步导出到 数据/ 目录。"""
import datetime as dt
import json
import os

from diag_lib import *  # noqa
import matplotlib.dates as mdates
import numpy as np

DATA = os.path.abspath(os.path.join(HERE, '..', '..', '数据'))
os.makedirs(DATA, exist_ok=True)


def style(ax):
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    for s in ('left', 'bottom'):
        ax.spines[s].set_color(GREY); ax.spines[s].set_linewidth(0.7)
    ax.tick_params(colors=GREY, labelsize=7)
    ax.set_axisbelow(True)
    for lab in ax.get_xticklabels() + ax.get_yticklabels():
        lab.set_fontproperties(FP(7))


def new(w=7.6, h=4.4):
    fig, ax = plt.subplots(figsize=(w, h), dpi=200)
    fig.patch.set_facecolor(CREAM); ax.set_facecolor(CREAM)
    return fig, ax


CATS = {'反无人机/防空': ALERT, '指挥控制/数据层': LAT, '无人平台/弹药': BRASS, '边境/太空传感': GREEN,
        '工业/其他': GREY}

# (日期, 金额上限美元, 类别, 短名, 是否明确 Lattice, 口径)
ANDURIL = [
    ('2021-09-15', 5.2e6, '指挥控制/数据层', '英 TALOS 基地防御试验', True, '合同'),
    ('2022-01-24', 967.6e6, '反无人机/防空', 'SOCOM 反无人机集成商', True, '合同上限'),
    ('2023-11-02', 2.1e7, '反无人机/防空', '英 TALOS 3 基地防护', False, '合同'),
    ('2024-06-13', 1.9e7, '工业/其他', '海军 SM-6 火箭发动机', False, '合同'),
    ('2024-06-18', 3.0e8, '无人平台/弹药', '台湾 ALTIUS-600M（FMS）', False, 'FMS 估值'),
    ('2024-10-08', 2.5e8, '反无人机/防空', 'Roadrunner-M + Pulsar', False, '合同'),
    ('2024-10-01', 1.44e7, '无人平台/弹药', '陆军连级 Ghost-X', False, '合同'),
    ('2024-11-10', 2.0e8, '反无人机/防空', '陆战队 MADIS 交战系统', False, '合同'),
    ('2024-11-21', 9.97e7, '边境/太空传感', '太空军 SSN 现代化', True, '合同上限'),
    ('2024-12-03', 1.0e8, '指挥控制/数据层', 'CDAO 边缘数据网格', True, '合同上限'),
    ('2025-03-10', 642.2e6, '反无人机/防空', '陆战队基地反无人机', True, '合同上限'),
    ('2025-07-18', 99.6e6, '指挥控制/数据层', '陆军 NGC2 原型（4ID）', False, '合同'),
    ('2025-09-10', 1.12e9, '无人平台/弹药', '澳 Ghost Shark 生产', False, '合同'),
    ('2025-09-25', 1.59e8, '指挥控制/数据层', '陆军 SBMC EagleEye', True, '合同'),
    ('2026-03-14', 2.0e10, '指挥控制/数据层', '陆军企业协议', True, '载体上限'),
    ('2026-03-20', 8.7e7, '反无人机/防空', 'JIATF-401 反无人机 C2', True, '任务订单'),
    ('2026-06-05', 1.98e9, '反无人机/防空', '科威特反无人机（FMS）', True, 'FMS 估值'),
    ('2026-06-12', 3.63e8, '边境/太空传感', 'CBP 增程塔 200+ 座', True, '合同'),
    ('2026-08-28', 8.47e8, '无人平台/弹药', '台湾 Altius-700M/600ISR', False, '合同'),
    ('2026-09-15', 6.5e7, '指挥控制/数据层', 'TITAN 地面站（Anduril 份额）', False, '合同'),
    ('2026-10-06', 1.8e9, '指挥控制/数据层', '陆军 NGC2 扩展（I 军）', False, '合同上限'),
    ('2026-10-06', 2.9e9, '工业/其他', '海军潜艇部件', False, '合同上限'),
]


def fmt_usd(v):
    if v >= 1e9:
        return '%d亿' % round(v / 1e8)
    if v >= 1e8:
        return ('%.2f' % (v / 1e8)).rstrip('0').rstrip('.') + '亿'
    return '%d万' % round(v / 1e4)


def hbar_contracts(rows, cats, fname, title_note, lat_label, xlim=(1e6, 4e10)):
    """rows: (date, value, cat, name, flag, basis)；按日期排序的横向对数条形图。"""
    rows = sorted(rows, key=lambda r: r[0])
    n = len(rows)
    fig, ax = new(7.8, 0.27 * n + 1.3)
    ys = np.arange(n)[::-1]
    for y, (d, v, cat, name, flag, basis) in zip(ys, rows):
        col = cats[cat]
        ax.barh(y, v - xlim[0], left=xlim[0], color=col if flag else 'white', edgecolor=col, lw=1.0,
                height=0.66, zorder=3, hatch=None if flag else '////')
        ax.text(v * 1.18, y, fmt_usd(v) + ('（%s）' % basis if basis not in ('合同',) else ''),
                fontproperties=FP(6.2), color=NAVY, va='center')
    ax.set_yticks(ys)
    ax.set_yticklabels(['%s  %s' % (r[0][:7], r[3]) for r in rows])
    ax.set_xscale('log'); ax.set_xlim(*xlim)
    ax.set_ylim(-0.7, n - 0.3)
    ticks = [t for t in (1e6, 1e7, 1e8, 1e9, 1e10) if xlim[0] <= t <= xlim[1]]
    ax.set_xticks(ticks)
    ax.set_xticklabels([{1e6: '100万', 1e7: '1000万', 1e8: '1亿', 1e9: '10亿', 1e10: '100亿'}[t] for t in ticks])
    ax.grid(axis='x', color=PAL['grid'], lw=0.7)
    style(ax)
    for lab in ax.get_yticklabels():
        lab.set_fontproperties(FP(6.6)); lab.set_color(NAVY)
    hs = [mp.Patch(fc=c, ec=c, label=k) for k, c in cats.items()]
    hs.append(mp.Patch(fc='white', ec=NAVY, hatch='////', label=lat_label))
    lg = ax.legend(handles=hs, prop=FP(6.2), frameon=True, loc='upper right')
    lg.get_frame().set_facecolor('white'); lg.get_frame().set_alpha(0.9); lg.get_frame().set_edgecolor('#C9C2B0')
    ax.set_xlabel(title_note, fontproperties=FP(6.6), color=GREY)
    return save(fig, fname)


def c_anduril_contracts():
    json.dump([dict(zip(['date', 'ceiling_usd', 'category', 'name', 'lattice_explicit', 'basis'], r)) for r in ANDURIL],
              open(os.path.join(DATA, 'anduril_major_contracts.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return hbar_contracts(ANDURIL, CATS, 'c_anduril_contracts.png',
                          '金额（美元，对数坐标）：合同上限/授予额；FMS 为批准估值；陆军企业协议为“合同载体上限”，不承诺支出',
                          '斜线空心＝来源未明示 Lattice')


PCATS = {'Maven / MSS': MAV, '情报与数据平台': PURPLE, 'Maven 生态（标注/集成）': GREEN, '企业协议/其他': GREY}
# (日期, 金额, 类别, 名称, 是否 Maven 专属, 口径)
PALANTIR = [
    ('2016-05-26', 2.22e8, '企业协议/其他', 'SOCOM 全源情报融合', False, '上限'),
    ('2018-03-09', 8.76e8, '情报与数据平台', 'DCGS-A CD1（与雷神共享）', False, '共享上限'),
    ('2019-12-01', 4.58e8, '情报与数据平台', '陆军 Vantage 数据平台', False, '上限'),
    ('2020-02-26', 8.23e8, '情报与数据平台', 'DCGS-A CD2（与 BAE 共享）', False, '共享上限'),
    ('2020-10-01', 9.12e7, '情报与数据平台', 'ARL AI/ML 研发', False, '合同'),
    ('2021-05-15', 1.11e8, '企业协议/其他', 'SOCOM 任务指挥平台', False, '合同'),
    ('2023-06-15', 4.63e8, '企业协议/其他', 'SOCOM 企业能力（含 AI）', False, '上限'),
    ('2024-03-06', 1.784e8, '情报与数据平台', 'TITAN 地面站原型', False, '合同'),
    ('2024-05-29', 4.8e8, 'Maven / MSS', 'MSS 原型 IDIQ', True, '上限'),
    ('2024-07-15', 2.4e7, 'Maven 生态（标注/集成）', 'Scale AI：NGA 标注过渡', True, '合同'),
    ('2024-09-19', 9.98e7, 'Maven / MSS', 'MSS 扩展至各军种（ARL）', True, '合同'),
    ('2024-12-18', 6.189e8, '情报与数据平台', 'Vantage 后续', False, '上限'),
    ('2025-05-20', 7.95e8, 'Maven / MSS', 'MSS 上限追加（至约12.75亿）', True, '追加额'),
    ('2025-05-21', 2.8e7, 'Maven / MSS', 'NGA 分析员 MSS 许可', True, '合同'),
    ('2025-06-15', 1.103e8, '企业协议/其他', '太空军云数据服务延期', False, '合同'),
    ('2025-07-31', 1.0e10, '企业协议/其他', '陆军企业协议 EA', False, '载体上限'),
    ('2025-11-15', 7.08e8, 'Maven 生态（标注/集成）', 'Enabled Intelligence：SEQUOIA 标注', True, '上限'),
    ('2025-12-10', 4.48e8, '企业协议/其他', '海军 ShipOS', False, '上限'),
    ('2026-09-15', 1.27e8, '情报与数据平台', 'TITAN 生产（Palantir 份额）', False, '合同'),
]


def c_palantir_contracts():
    json.dump([dict(zip(['date', 'value_usd', 'category', 'name', 'maven_specific', 'basis'], r)) for r in PALANTIR],
              open(os.path.join(DATA, 'maven_palantir_contracts.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return hbar_contracts(PALANTIR, PCATS, 'c_palantir_contracts.png',
                          '金额（美元，对数坐标）：上限/授予额；Scale AI 与 Enabled Intelligence 为 NGA Maven 标注合同（非 Palantir）；EA 不承诺支出',
                          '斜线空心＝非 Maven 专属', xlim=(1e7, 3e10))


def c_palantir_revenue():
    yrs = ['2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026H1']
    v = [3.44, 6.09, 6.77, 8.263, 9.212, 12.0, 18.55, 14.96]
    est = [True, True, True, False, False, False, False, False]
    fig, ax = new(7.4, 3.6)
    for i, (y_, x, e) in enumerate(zip(yrs, v, est)):
        ax.bar(i, x, color='white' if e else MAV, edgecolor=MAV, hatch='////' if e else None, width=0.6, zorder=3)
        ax.text(i, x + 0.35, '%.1f' % x, fontproperties=FPB(6.8), color=NAVY, ha='center')
    ax.set_xticks(range(len(yrs))); ax.set_xticklabels(yrs)
    ax.set_ylim(0, 26)
    ax.set_ylabel('亿美元', fontproperties=FP(7), color=GREY)
    ax.grid(axis='y', color=PAL['grid'], lw=0.7)
    style(ax)
    ev = [(5, 'MSS 原型\nIDIQ'), (6, '上限增至约13亿\n陆军EA·陆战队'), (7, 'Feinberg备忘录\n对伊朗作战')]
    for i, t in ev:
        ax.text(i, v[i] + 1.5, t, fontproperties=FP(5.6), color=MAV, ha='center', va='bottom')
    ax.text(-0.3, 24.6, '斜线：2019—2021 为推算值（2019、2020 为含国际的政府总收入）；其余为公司披露的美国政府收入。',
            fontproperties=FP(6), color=GREY)
    return save(fig, 'c_palantir_revenue.png')


def c_anduril_funding():
    rounds = [('2017-08', '种子轮', 0.18, None), ('2019-09', 'B 轮', None, 1.0), ('2020-07', 'C 轮', 2.0, 1.9),
              ('2021-06', 'D 轮', 4.5, 4.6), ('2022-12', 'E 轮', 14.8, 8.48), ('2024-08', 'F 轮', 15.0, 14.0),
              ('2025-06', 'G 轮', 25.0, 30.5), ('2026-05', 'H 轮', 50.0, 61.0)]
    fig, ax = new(7.6, 4.0)
    xs = np.arange(len(rounds))
    vals = [r[3] or 0 for r in rounds]
    bars = ax.bar(xs, vals, color=LAT, width=0.58, zorder=3)
    for i, (d, n, raise_, val) in enumerate(rounds):
        if val and i >= 5:
            ax.text(i, val - 2.0, '%g' % val, fontproperties=FPB(7), color='white', ha='center', va='top', zorder=5)
        elif val:
            ax.text(i, val + 1.2, '%g' % val, fontproperties=FPB(7), color=NAVY, ha='center')
        if raise_:
            ax.text(i, -6.2, '融资 %g 亿' % (raise_ * 1 if raise_ >= 1 else raise_), fontproperties=FP(5.8),
                    color=BRASS, ha='center')
    ax.set_xticks(xs); ax.set_xticklabels(['%s\n%s' % (r[1], r[0]) for r in rounds]); ax.set_xlim(-0.6, 8.3)
    ax.set_ylim(-9, 72)
    ax.axhline(0, color=GREY, lw=0.7)
    ax.set_ylabel('估值（10 亿美元）', fontproperties=FP(7), color=GREY)
    ax2 = ax.twinx()
    rev = [('2024', 1.0), ('2025', 2.2), ('2026E', 4.3)]
    rx = [5, 6, 7]
    ax2.plot(rx, [r[1] for r in rev], color=ALERT, marker='o', lw=1.6, zorder=4)
    for x, (y_, v) in zip(rx, rev):
        ax2.text(x + 0.33, v - 0.05, '营收 %s\n约 %g 亿美元' % (y_, v * 10), fontproperties=FP(6), color=ALERT, ha='left', va='top')
    ax2.set_ylim(-0.6, 5.0)
    ax2.set_ylabel('营收（10 亿美元，公司口径）', fontproperties=FP(7), color=ALERT)
    for a in (ax, ax2):
        style(a)
    ax2.spines['right'].set_visible(True); ax2.spines['right'].set_color(ALERT)
    ax.grid(axis='y', color=PAL['grid'], lw=0.7)
    ax.text(0, 60, '“融资”金额单位：亿美元；B 轮金额未披露。2026-07 路透称洽谈约 1000 亿美元估值新一轮，未见完成。',
            fontproperties=FP(6), color=GREY)
    return save(fig, 'c_anduril_funding.png')


def c_maven_scale():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.8, 3.4), dpi=200, gridspec_kw={'width_ratios': [1.1, 1]})
    fig.patch.set_facecolor(CREAM)
    for a in (a1, a2):
        a.set_facecolor(CREAM)
    us = [('2025-05', 2.0), ('2026-01', 5.0), ('2026-09', 10.0)]
    xs = [dt.date.fromisoformat(d + '-15') for d, _ in us]
    a1.plot(xs, [v for _, v in us], color=MAV, marker='o', lw=2, zorder=3)
    for x, (d, v) in zip(xs, us):
        a1.text(x, v + 0.6, '%s\n%g 万+' % (d, v), fontproperties=FP(6.3), color=NAVY, ha='center')
    a1.axvspan(dt.date(2026, 2, 28), dt.date(2026, 4, 7), color=LIGHT[MAV], zorder=0)
    a1.text(dt.date(2026, 3, 18), 1.0, '对伊朗\n“史诗怒火”\n38 天', fontproperties=FP(5.8), color=MAV, ha='center')
    a1.set_ylim(0, 13); a1.set_xlim(dt.date(2025, 2, 1), dt.date(2026, 12, 1))
    a1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    a1.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 7]))
    a1.set_title('MSS 用户数（万人）', fontproperties=FPB(8), color=NAVY)
    a1.grid(axis='y', color=PAL['grid'], lw=0.7)
    style(a1)
    cs = [('2024-05\n原型 IDIQ', 4.8), ('2025-05\n上限上调', 13.0), ('FY2027 申请\n（MSS+联合火力网）', 23.0)]
    a2.bar(range(3), [c[1] for c in cs], color=[MAV, MAV, BRASS], width=0.55, zorder=3)
    for i, (n, v) in enumerate(cs):
        a2.text(i, v + 0.6, '%g 亿美元' % v, fontproperties=FPB(6.6), color=NAVY, ha='center')
    a2.set_xticks(range(3)); a2.set_xticklabels([c[0] for c in cs])
    a2.set_ylim(0, 27)
    a2.set_title('Palantir MSS 合同上限与预算（亿美元）', fontproperties=FPB(8), color=NAVY)
    a2.grid(axis='y', color=PAL['grid'], lw=0.7)
    style(a2)
    fig.text(0.5, -0.03, '说明：FY2027 的 23 亿美元有“跨五年”与“单年 15 亿”两种口径，尚未厘清；陆军 2025 年对 Palantir 的 100 亿美元企业协议另计。',
             fontproperties=FP(6), color=GREY, ha='center')
    fig.tight_layout()
    return save(fig, 'c_maven_scale.png')


if __name__ == '__main__':
    for f in (c_anduril_contracts, c_anduril_funding, c_maven_scale, c_palantir_contracts, c_palantir_revenue):
        print(f())
    for x in OVERLAP_LOG:
        print('⚠', *x)
