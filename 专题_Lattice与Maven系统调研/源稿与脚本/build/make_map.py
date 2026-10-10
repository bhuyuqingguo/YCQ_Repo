# -*- coding: utf-8 -*-
"""全球部署与案例分布图：编号标注 + 图下分栏说明，避免地名互相遮挡。"""
from diag_lib import *  # noqa
from mpl_toolkits.basemap import Basemap
import numpy as np

PTS = [  # (系统, 纬度, 经度, 说明)
    ('L', 31.6, -108.5, '美墨边境：CBP 自主监视塔网络（2018— ，300+ 座，2026 增程塔 200+）'),
    ('L', 32.7, -114.6, '尤马试验场：陆军 IBCS-M 反无人机火控试验 4/4 命中（2025）'),
    ('L', 38.7, -104.8, '卡森堡：第4步兵师 NGC2 原型、Ivy Sting / Ivy Mass 演习（2025—2026）'),
    ('L', 47.1, -122.5, '刘易斯-麦科德联合基地：I 军 NGC2 扩展首个部队（2026-10）'),
    ('L', 51.3, -1.8, '英国：TALOS 基地防护试验与常设联合作战基地防护（2021—2023）'),
    ('L', 49.0, 32.0, '乌克兰：ALTIUS、Ghost 无人机受电子干扰表现不佳（2022—2024）'),
    ('L', 29.3, 47.9, '科威特：反无人机一揽子 FMS 获批（估值 19.8 亿美元，2026-06）'),
    ('L', 23.7, 121.0, '台湾：ALTIUS-600M/700M 巡飞弹交付与新订单（2024—2026）'),
    ('L', -33.8, 151.2, '澳大利亚：Ghost Shark 超大型无人潜航器，17 亿澳元（2025）'),
    ('L', 13.4, 144.8, '关岛：Valiant Shield 演习“关岛防御战斗管理器”演示（2026，弱源）'),
    ('M', 38.75, -77.2, 'NGA 总部（斯普林菲尔德）：NGA Maven 采购项目与 GEOINT 模型'),
    ('M', 35.1, -79.0, '布拉格堡：XVIII 空降军“猩红之龙”系列演习（2020— ）'),
    ('M', 50.1, 8.2, '威斯巴登：向乌克兰提供目标情报支援（2022— ）'),
    ('M', 50.45, 3.95, '蒙斯 SHAPE：北约 MSS NATO（2025 采购，2026-06 全面能力）'),
    ('M', 34.0, 41.0, '伊拉克/叙利亚：CENTCOM 2024-02-02 空袭 85 处目标'),
    ('M', 15.5, 42.8, '红海/也门：定位火箭发射架与海上船只（2024）'),
    ('M', 32.0, 53.0, '伊朗：“史诗怒火”行动，38 天打击约 1.3 万个目标（2026）'),
    ('M', 5.0, 46.0, '非洲之角方向（AFRICOM）：2017-12 起用于反 ISIS 视频识别'),
]


def m_world():
    fig = plt.figure(figsize=(7.8, 6.6), dpi=200)
    fig.patch.set_facecolor(CREAM)
    ax = fig.add_axes([0.01, 0.37, 0.98, 0.62])
    m = Basemap(projection='mill', llcrnrlat=-48, urcrnrlat=66, llcrnrlon=-135, urcrnrlon=165, resolution='l', ax=ax)
    m.drawmapboundary(fill_color='#DCE9F2', linewidth=0.5, color=GREY)
    m.fillcontinents(color='#EFEBDF', lake_color='#DCE9F2')
    m.drawcoastlines(linewidth=0.35, color='#8A8474')
    m.drawcountries(linewidth=0.25, color='#B5AE9C')
    for i, (sysn, la, lo, _) in enumerate(PTS, 1):
        x, y = m(lo, la)
        col = LAT if sysn == 'L' else MAV
        ax.plot(x, y, 'o', ms=8.5, color=col, mec='white', mew=0.8, zorder=5)
        ax.text(x, y, str(i), fontproperties=FPB(5.2), color='white', ha='center', va='center', zorder=6)
    # 图下说明：两栏
    lx = [0.03, 0.52]
    L = [(i, p) for i, p in enumerate(PTS, 1) if p[0] == 'L']
    M = [(i, p) for i, p in enumerate(PTS, 1) if p[0] == 'M']
    fig.text(lx[0], 0.365, '● Lattice / Anduril', fontproperties=FPB(7.4), color=LAT)
    fig.text(lx[1], 0.365, '● Maven / Palantir', fontproperties=FPB(7.4), color=MAV)
    for col, lst in ((0, L), (1, M)):
        for k, (i, p) in enumerate(lst):
            fig.text(lx[col], 0.33 - k * 0.033, '%d  %s' % (i, p[3]), fontproperties=FP(5.6), color=NAVY,
                     wrap=False)
    fig.text(0.5, 0.005, '注：编号位置为示意；关岛条目来源可信度低。资料来源：本报告各章所引公开报道。',
             fontproperties=FP(5.6), color=GREY, ha='center')
    return save(fig, 'm_world.png')


if __name__ == '__main__':
    print(m_world())
    for x in OVERLAP_LOG:
        print('⚠', *x)
