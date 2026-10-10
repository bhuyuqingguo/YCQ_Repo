# -*- coding: utf-8 -*-
"""架构/流程/分工类自绘示意图。"""
from diag_lib import *  # noqa


# ---------------------------------------------------------------- Lattice 分层架构
def d_lattice_arch():
    fig, ax = canvas(7.8, 6.0, ylim=(0, 78))
    layers = [
        ('⑥ 应用层', 'Lattice for Mission Autonomy（集群自主）｜Lattice for C2（AI 战斗管理）｜反无人机 C2\n'
                    'NGC2 师级应用（AXS 炮兵数据工具等）｜第三方伙伴应用（Developer Console 等）', LAT),
        ('⑤ API / SDK', 'Entities API · Tasks API · Objects API · Video API · OAuth2\n'
                       'v1 gRPC 原生 ｜ v2 REST + SSE 流式 ｜ Python / Go / Java / TypeScript / Rust SDK', LAT),
        ('④ 核心服务', 'Entity Manager（实体管理）｜ Task Manager（任务管理）｜ 自动航迹关联器\n'
                      '对象存储（≤1 GiB/对象）｜ 视频服务（RTSP / SRT / MPEG-TS）｜ 字段级密级标记', NAVY),
        ('③ Lattice Mesh 数据网格', '点对点、按优先级选路、存储转发；“实时数据优先、回填只用剩余带宽”（US 10,506,436）\n'
                                 '面向 DDIL（拒止/降级/间断/受限）环境；节点本地存储 + 跨节点复制', GREEN),
        ('② 边缘计算与通信', 'Menace-T（双箱 C4 套件）｜ Menace-X（机动型）｜ 基于 Klas Voyager 坚固计算\n'
                         '亦为 Palantir Edge 软件首选硬件；云端 / 本地机房节点', PURPLE),
        ('① 传感器 / 效应器', 'Sentry 塔 · Wisp · 雷达 · Pulsar 电子战 · Anvil · Roadrunner · ALTIUS · Ghost-X · Bolt\n'
                          'YFQ-44A · Ghost Shark / Dive-LD · 第三方雷达与拦截器（内置“Lattice AI Core”）', BRASS),
    ]
    y = 70
    for name, body, col in layers:
        box(ax, 1, y - 10, 21, 10, name.replace(' 数据网格','\n数据网格'), fc=col, ec=col, size=8.2, bold=True, color='white')
        box(ax, 23, y - 10, 66, 10, body, fc=LIGHT.get(col, '#fff'), ec=col, size=6.6, ha='left')
        y -= 11.5
    # 右侧：节点联邦示意
    text(ax, 95, 72, '部署\n形态', size=7, bold=True, color=NAVY)
    for i, (lab, yy) in enumerate([('云/机房', 58), ('指挥所', 46), ('车辆', 34), ('塔/套件', 22), ('无人平台', 10)]):
        box(ax, 90.5, yy - 3, 9, 6, lab, fc='white', ec=GREEN, size=6.2)
        if i:
            arrow(ax, 95, yy + 3, 95, yy + 9, color=GREEN, style='<|-|>', ms=6, lw=0.8)
    text(ax, 50, -1.8, '注：①—③层与“每节点运行完整服务栈”部分为依据 SDK 与专利的推断；④⑤层依据 Anduril 公开 SDK 源码。',
         size=6, color=GREY)
    return save(fig, 'd_lattice_arch.png')


# ---------------------------------------------------------------- Lattice 实体模型 + 任务状态机
def d_lattice_entity_task():
    fig, ax = canvas(7.8, 5.2, ylim=(0, 66))
    # 左：实体
    box(ax, 1, 6, 44, 58, '', fc='white', ec=LAT, lw=1.1)
    text(ax, 23, 61, 'Entity（实体）＝ 作战环境中的一个已知对象', size=7.6, bold=True, color=LAT)
    text(ax, 23, 57.2, '五类本体模板（ontology template）', size=6.6, color=GREY)
    tm = ['航迹\nTRACK', '传感器关注点\nSPOI', '己方资产\nASSET', '地理区域\nGEO', '关注信号\nSOI']
    for i, t in enumerate(tm):
        box(ax, 2.5 + i * 8.5, 49.8, 7.8, 6, t, fc=LIGHT[LAT], ec=LAT, size=5.2)
    text(ax, 23, 47, '可选、强类型组件（30 余项，节选）', size=6.6, color=GREY)
    comps = [('location / kinematics', '位置与运动学'), ('mil_view', '敌我属性 7 态'), ('tracked', '航迹质量 0–15'),
             ('correlation', '主/从航迹关联'), ('ontology', '类型与平台'), ('task_catalog', '可受领任务目录'),
             ('sensors / payloads', '传感器与载荷'), ('health / supplies', '健康与补给'),
             ('data_classification', '逐字段密级'), ('indicators', '模拟/演习/可外发'),
             ('provenance', '来源与更新时间'), ('expiry_time', '≤30 天必填时效')]
    for i, (a, b) in enumerate(comps):
        cx = 2.5 + (i % 3) * 14.2
        cy = 38 - (i // 3) * 8.2
        box(ax, cx, cy, 13.4, 7, a + '\n' + b, fc='white', ec=NAVY, size=5.4, lw=0.6)
    # 右：任务状态机
    box(ax, 48, 6, 51, 58, '', fc='white', ec=MAV, lw=1.1)
    text(ax, 73.5, 61, 'Task（任务）生命周期 —— 照搬战术数据链确认语义', size=7.6, bold=True, color=MAV)
    seq = ['CREATED\n创建', 'SCHEDULED\n排入管理器', 'SENT\n已发送', 'MACHINE_\nRECEIPT\n机器回执', 'ACK\n确认',
           'WILCO\n将遵照执行', 'EXECUTING\n执行中']
    xs = [50.5, 63, 75.5, 88]
    pos = []
    for i, s in enumerate(seq):
        r, c = divmod(i, 4)
        x = xs[c] if r == 0 else xs[3 - c]
        y = 48 if r == 0 else 34
        pos.append((x, y))
        box(ax, x, y, 10, 7.5, s, fc=LIGHT[MAV] if s.startswith('WILCO') else '#fff', ec=MAV, size=5.5,
            bold=s.startswith('WILCO'))
    for i in range(len(pos) - 1):
        (x0, y0), (x1, y1) = pos[i], pos[i + 1]
        if y0 == y1:
            if x1 > x0:
                arrow(ax, x0 + 10, y0 + 3.75, x1, y1 + 3.75, color=MAV, ms=6)
            else:
                arrow(ax, x0, y0 + 3.75, x1 + 10, y1 + 3.75, color=MAV, ms=6)
        else:
            arrow(ax, x0 + 5, y0, x1 + 5, y1 + 7.5, color=MAV, ms=6)
    ex = pos[-1]
    box(ax, 63, 20, 10, 7, 'DONE_OK\n成功完成', fc=LIGHT[GREEN], ec=GREEN, size=5.5)
    box(ax, 75.5, 20, 10, 7, 'DONE_NOT_OK\n未完成', fc=LIGHT[GREY], ec=GREY, size=5.5)
    arrow(ax, ex[0] + 5, ex[1], 68, 27, color=GREEN, ms=6)
    arrow(ax, ex[0] + 5, ex[1], 80.5, 27, color=GREY, ms=6)
    box(ax, 50.5, 7.5, 46.5, 11, '旁路状态：REPLACED · CANCEL_REQUESTED（请求取消，代理可拒绝）\n'
        '任务要素：specification（protobuf Any）· author · initial_entities\n（目标/限入区）· 重试与执行约束\n'
        '手动控制：摇杆帧流（manual control frames），自主↔遥控随时切换', fc=LIGHT[GREY], ec=GREY, size=5.3,
        ha='left')
    text(ax, 50, 2.5, '资料来源：Anduril 官方 lattice-sdk-python（GitHub）类型定义；本报告整理绘制。', size=6, color=GREY)
    return save(fig, 'd_lattice_entity_task.png')


# ---------------------------------------------------------------- Lattice 交战流程（反无人机/打击）
def d_lattice_killchain():
    fig, ax = canvas(7.8, 3.6, ylim=(0, 44))
    steps = [('探测', '塔/雷达/EO-IR\n边缘 AI 检测', BRASS), ('建航迹', '发布 TRACK 实体\n航迹质量评分', LAT),
             ('融合', '自动关联器\n多源合一', LAT), ('识别', '分类 + 人工将\nmil_view 置 HOSTILE', ALERT),
             ('派任务', '操作员批准\n打击/拦截任务', ALERT), ('执行', '代理 ACK→WILCO\n→EXECUTING', NAVY),
             ('评估', '自动改派 ISR\n毁伤评估 BDA', GREEN)]
    n = len(steps)
    w = 12.2
    for i, (h, b, col) in enumerate(steps):
        x = 1 + i * 14
        box(ax, x, 22, w, 7, h, fc=col, ec=col, size=8, bold=True, color='white')
        box(ax, x, 11, w, 10.2, b, fc=LIGHT.get(col, '#fff'), ec=col, size=6.1)
        if i < n - 1:
            arrow(ax, x + w + 0.2, 25.5, x + 13.8, 25.5, color=NAVY, ms=7)
    # 人机关系标注
    ax.plot([1, 41], [33, 33], color=GREEN, lw=2.2)
    text(ax, 21, 38.5, '人在回路上（human-on-the-loop）', size=6.6, bold=True, color=GREEN)
    text(ax, 21, 35.4, '机动、感知、跟踪自动进行，人监督可干预', size=6.2, color=GREEN)
    ax.plot([43, 69], [33, 33], color=ALERT, lw=2.2)
    text(ax, 56, 38.5, '人在回路中（human-in-the-loop）', size=6.6, bold=True, color=ALERT)
    text(ax, 56, 35.4, '定敌、批准武器释放须由人决定', size=6.2, color=ALERT)
    ax.plot([71, 98], [33, 33], color=GREEN, lw=2.2)
    text(ax, 84.5, 38.5, '自动执行与复盘', size=6.6, bold=True, color=GREEN)
    text(ax, 84.5, 35.4, '代理回报状态，自主模块接续', size=6.2, color=GREEN)
    text(ax, 50, 5.5, '实证：EDGE23 演习中士兵授权 ALTIUS-600M 打击后，Lattice 自动改派 ALTIUS ISR 机做 BDA；陆战队 Anvil 仅在操作员下令后拦截。',
         size=6.1, color=NAVY)
    text(ax, 50, 1.6, '说明：完整流程为依据 SDK 设计与公开演示的推断，未见官方端到端描述。', size=5.8, color=GREY)
    return save(fig, 'd_lattice_killchain.png')


# ---------------------------------------------------------------- Maven 分层架构
def d_maven_arch():
    fig, ax = canvas(7.8, 6.2, ylim=(0, 82))
    layers = [
        ('⑦ 治理与合同', 'CDAO MSS 项目办公室（2026 起）｜合同统一经陆军企业协议（EA）｜R&E 任商业云授权官\n'
                       '北约：NCIA 采办、SHAPE 运行 MSS NATO', JOINT),
        ('⑥ 部署与安全域', '跨 3 个安全域运行（NGA 口径）｜陆战队经 SIPRNet IL6 云接入｜北约机密网与北约自有数据中心\n'
                        '用户：2万+（2025-05）→ 约5万（2026-01）→ 10万+（2026-09）', NAVY),
        ('⑤ AIP / 大模型代理', '自然语言检索与问答 · 目标排序 · 行动方案（COA）草案 · 报告生成\n'
                             '大模型可替换：Claude（据报道，存争议）→ OpenAI 等', PURPLE),
        ('④ 工作流应用', '共用作战图（COP）｜ Target Workbench 看板式目标工作台（含禁打清单 NSL）\n'
                       '资产比较 / 武器-目标配对 ｜ BDA 跟踪 ｜ Open DAGIR 第三方应用', MAV),
        ('③ Palantir 平台', 'Ontology 本体：对象—属性—链接—动作，可写回运营与边缘系统\n'
                          'Foundry / Gotham / AIP ｜ Apollo 跨网络、跨密级持续交付', MAV),
        ('② NGA Maven\n模型流水线', '数据标注：Scale AI（约2400万美元过渡）→ Enabled Intelligence SEQUOIA（≤7.08亿美元）\n'
                                 'AI 集成：ECS（2017 起）｜ 模型认证：AGAIM ｜ 产品标注“machine-generated GEOINT”', GREEN),
        ('① 数据源', '国家与商业卫星（含 ICEYE、Capella 等 SAR）· 无人机全动态视频 · SIGINT · 既有数据库\n'
                   'CENTCOM 2024 年部署接入 179 个数据源（另有“150+”说法）', BRASS),
    ]
    y = 80
    for name, body, col in layers:
        box(ax, 1, y - 10, 22, 10, name, fc=col, ec=col, size=8, bold=True, color='white')
        box(ax, 24, y - 10, 75, 10, body, fc=LIGHT.get(col, '#fff'), ec=col, size=6.5, ha='left')
        y -= 11.3
    text(ax, 50, -1.2, '注：MSS 具体采用 Foundry 还是 Gotham 的组合、是否存在 JWICS 实例，公开资料未证实。', size=6, color=GREY)
    return save(fig, 'd_maven_arch.png')


# ---------------------------------------------------------------- Maven 目标工作流（看板）
def d_maven_workflow():
    fig, ax = canvas(7.8, 4.4, ylim=(0, 54))
    cols = [('发现 Find', '179+ 源融合\nCV 自动检测', BRASS), ('定位 Fix', '地理定位\n生成坐标', BRASS),
            ('跟踪 Track', 'COP 持续跟踪\n航迹/活动', LAT), ('瞄准 Target', '目标核查\n禁打清单比对', ALERT),
            ('交战 Engage', '资产比较/配对\n交 AFATDS 等火控', ALERT), ('评估 Assess', 'ISR 回看\n毁伤评估', GREEN)]
    for i, (h, b, col) in enumerate(cols):
        x = 1 + i * 16.4
        box(ax, x, 41, 15, 7, h, fc=col, ec=col, size=7.6, bold=True, color='white')
        box(ax, x, 14, 15, 26, '', fc=LIGHT.get(col, '#fff'), ec=col, lw=0.8)
        # 卡片
        for k in range(3 if i < 4 else 2):
            box(ax, x + 1.3, 33.5 - k * 5.6, 12.4, 4.6, '目标卡 #%d' % (i * 3 + k + 1), fc='white', ec=GREY, size=5.4,
                lw=0.5)
        text(ax, x + 7.5, 18.2, b, size=5.9, color=NAVY)
        if i < len(cols) - 1:
            arrow(ax, x + 15.1, 44.5, x + 16.3, 44.5, color=NAVY, ms=6)
    ax.plot([1, 98], [10.8, 10.8], color=GREY, lw=0.6)
    text(ax, 50, 7.8, 'Target Workbench：看板式界面，列＝目标定位阶段（可按单位流程自定义），目标卡在列间流转；人对每一目标作出批准。',
         size=6.2, color=NAVY)
    text(ax, 50, 4.3, '量化口径：一名目标军官每小时批准目标 30 → 80 个（Bloomberg 2024）；约 20 人完成 2003 年伊拉克约 2000 人的目标工作量（CSET）。',
         size=6.0, color=NAVY)
    text(ax, 50, 1.0, '资料来源：Palantir Target Workbench 产品说明、CSIS、CSET；本报告整理绘制（阶段划分按 F2T2EA 通用杀伤链对照）。',
         size=5.6, color=GREY)
    return save(fig, 'd_maven_workflow.png')


# ---------------------------------------------------------------- Maven 管理归属演变
def d_maven_governance():
    fig, ax = canvas(7.8, 4.6, xlim=(2016.8, 2027.0), ylim=(-26, 46))
    lanes = [('OSD 情报与安全副部长办（OUSD(I&S)）\n算法战跨职能小组（AWCFT）', 2017.32, 2022.6, JOINT, 34),
             ('NGA Maven（GEOINT AI）\n2023-11 列为采购项目', 2022.6, 2026.95, GREEN, 24),
             ('CDAO + 陆军合同代理\nMSS 原型（Palantir 主承包）', 2022.6, 2026.19, MAV, 14),
             ('CDAO MSS 项目办\nFY26 末转项目', 2026.19, 2026.95, MAV, 4)]
    for lab, x0, x1, col, y in lanes:
        box(ax, x0, y, x1 - x0, 8, '', fc=LIGHT.get(col), ec=col, r=0.12)
        if x1 - x0 > 1.5:
            text(ax, x0 + 0.1, y + 4, lab, size=6.0, ha='left', color=NAVY)
        else:
            text(ax, x0 - 0.08, y + 4, lab, size=6.0, ha='right', color=MAV)
    for yr in range(2017, 2028):
        ax.plot([yr, yr], [-2, 44], color=PAL['grid'], lw=0.6, zorder=0)
        if yr < 2027:
            text(ax, yr + 0.5, 43.5, str(yr), size=6.5, color=GREY)
    ax.plot([2016.9, 2026.95], [-2, -2], color=NAVY, lw=1.0)
    ev = [(2017.32, '2017-04-26\nWork 备忘录成立 AWCFT', -7), (2017.95, '2017-12\n首次部署（ScanEagle 视频）', -15),
          (2018.42, '2018-06\n谷歌宣布不续约', -23), (2022.6, '2022 FY23 预算\n拆分 NGA/CDAO', -7),
          (2023.85, '2023-11\nNGA Maven 成项目', -15), (2024.41, '2024-05\nPalantir 4.8 亿合同', -23),
          (2025.23, '2025-03\n北约采购 MSS', -7), (2025.39, '2025-05\n上限增至约 13 亿', -15),
          (2026.19, '2026-03-09\nFeinberg 备忘录', -23)]
    for x, s_, y in ev:
        ax.plot([x, x], [-2, y + 2.6], color=ALERT, lw=0.5, ls=':')
        ax.plot([x], [-2], marker='o', color=ALERT, markersize=3.2)
        text(ax, x, y, s_, size=5.4, color=ALERT)
    return save(fig, 'd_maven_governance.png')


if __name__ == '__main__':
    for f in [d_lattice_arch, d_lattice_entity_task, d_lattice_killchain, d_maven_arch, d_maven_workflow,
              d_maven_governance]:
        print(f())
