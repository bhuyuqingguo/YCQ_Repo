# -*- coding: utf-8 -*-
"""精要版专用图：关键数字看板、能力证据矩阵。"""
from diag_lib import *  # noqa


def c_kpis():
    fig, ax = canvas(7.8, 5.6, ylim=(0, 72))
    cols = [('Lattice / Anduril', LAT, [
        ('610 亿美元', 'Anduril 估值（2026-05 H 轮）'), ('约 22 亿美元', '2025 年营收（公司口径）'),
        ('200 亿美元', '陆军企业协议上限（2026-03）'), ('18 亿美元', 'NGC2 扩展合同上限（2026-10）'),
        ('300+ 座', 'CBP 边境监视塔（2024-09）'), ('12+ 项', '来源明示以 Lattice 为核心的合同')]),
        ('Maven / Palantir', MAV, [
        ('10 万+', 'MSS 用户（2026-09）'), ('约 12.75 亿美元', 'MSS 主合同上限（2025-05）'),
        ('100 亿美元', '陆军—Palantir 企业协议（2025-07）'), ('23 亿美元', 'FY2027 MSS+联合火力网申请'),
        ('约 1.3 万个', '伊朗战役 38 天打击目标'), ('179 个', 'CENTCOM 部署接入数据源（2024）')])]
    for c, (title, col, items) in enumerate(cols):
        x0 = 1 + c * 50
        box(ax, x0, 64, 48, 7, title, fc=col, ec=col, size=8.4, bold=True, color='white')
        for i, (num, lab) in enumerate(items):
            r, k = divmod(i, 2)
            x = x0 + k * 24.2
            y = 44 - r * 21
            box(ax, x, y, 23.6, 18.5, '', fc='white', ec=col, lw=0.9)
            text(ax, x + 11.8, y + 11.6, num, size=11.5, bold=True, color=col)
            text(ax, x + 11.8, y + 4.6, lab, size=5.9, color=NAVY)
    text(ax, 50, -0.8, '注：合同“上限”为可签约额度，不等于实际拨付；伊朗战役数字为五角大楼官员口径。', size=5.8, color=GREY)
    return save(fig, 'c_kpis.png')


LEV = {'已证实': GREEN, '官方/公司声称': ACC, '存疑或有反证': ALERT, '不适用': '#D9D4C7'}


def c_capmatrix():
    rows = [('多源融合与态势感知', '已证实', '规模化部署（边境塔、陆军数据层）', '已证实', '接入 179 个数据源'),
            ('目标识别与分类准确率', '官方/公司声称', '无独立测试数据', '存疑或有反证', '测试约 60%，恶劣天气 <30%'),
            ('目标处理速度与规模', '官方/公司声称', 'Ivy Sting：火力时线缩短九成', '已证实', '30→80 目标/小时；20 人≈2000 人'),
            ('反无人机交战闭环', '已证实', 'IBCS-M 试验 4/4；多项合同', '不适用', '—'),
            ('集群自主与有人-无人协同', '官方/公司声称', 'EDGE23、CCA 自主演示', '不适用', '—'),
            ('拒止环境（DDIL）韧性', '存疑或有反证', '乌克兰受干扰；海军无人艇宕机', '存疑或有反证', '未见公开测试'),
            ('盟军与跨域互通', '官方/公司声称', '北约 eAirC2 评估中', '已证实', 'MSS NATO 全面能力'),
            ('网络安全与数据可信', '存疑或有反证', '陆军 CTO“极高风险”备忘录', '存疑或有反证', '数据投毒、过期数据风险'),
            ('实战检验', '存疑或有反证', '乌克兰实战表现差', '已证实', '伊朗、伊叙空袭；含 Minab 事件')]
    n = len(rows)
    fig, ax = canvas(7.8, 0.42 * n + 1.3, ylim=(-2.2, n + 1.2))
    text(ax, 13, n + 0.55, '能力项', size=7.2, bold=True)
    text(ax, 46, n + 0.55, 'Lattice（证据等级 · 依据）', size=7.2, bold=True, color=LAT)
    text(ax, 80, n + 0.55, 'Maven（证据等级 · 依据）', size=7.2, bold=True, color=MAV)
    for i, (cap, l1, d1, l2, d2) in enumerate(rows):
        y = n - 1 - i
        box(ax, 0.5, y + 0.08, 25, 0.84, cap, fc='white', ec=GREY, size=6.2, lw=0.5, r=0.15)
        for x0, lev, d in ((27, l1, d1), (61, l2, d2)):
            box(ax, x0, y + 0.08, 33, 0.84, '', fc=LIGHT.get(LEV[lev], '#ECE8DE') if lev != '不适用' else '#ECE8DE',
                ec=LEV[lev], lw=0.8, r=0.15)
            text(ax, x0 + 1, y + 0.5, lev, size=5.9, bold=True, color=LEV[lev] if lev != '不适用' else GREY, ha='left')
            text(ax, x0 + 12, y + 0.5, d, size=5.6, color=NAVY, ha='left')
    for i, (k, c) in enumerate(LEV.items()):
        box(ax, 2 + i * 24, -1.75, 3, 0.6, '', fc=c, ec=c, r=0.1)
        text(ax, 6 + i * 24, -1.45, k, size=6, ha='left')
    return save(fig, 'c_capmatrix.png')


if __name__ == '__main__':
    print(c_kpis()); print(c_capmatrix())
    for x in OVERLAP_LOG:
        print('⚠', *x)
