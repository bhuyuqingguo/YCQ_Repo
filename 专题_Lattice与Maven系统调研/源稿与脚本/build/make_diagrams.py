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
             ('融合', '自动关联器\n多源合一', LAT), ('识别', '分类后由人\n将属性置为\nHOSTILE', ALERT),
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

# ---------------------------------------------------------------- 分工：从企业到边缘
def d_division():
    fig, ax = canvas(7.8, 6.0, ylim=(0, 80))
    tiers = [('国家/联合层', '国防部长办 · CDAO · 联合参谋部\n作战司令部（CENTCOM 等）· 北约 SHAPE', 67),
             ('战区/军种企业层', '陆军企业数据 · 情报与火力决策\n联合火力网（JFN）· Golden Dome C2', 53),
             ('军/师级指挥层', '陆军 NGC2：I 军、第4步兵师\n师级目标处理与火力分配', 36),
             ('旅/营/连战术层', '反无人机分队 · 炮兵连 · 前沿基地\nJIATF-401 · 陆战队基地防护', 21),
             ('边缘平台层', '塔、雷达、拦截器、巡飞弹、无人机\nCCA、无人潜航器（Ghost Shark）', 6)]
    for name, d, y in tiers:
        box(ax, 34, y, 32, 11, '', fc='white', ec=GREY, lw=0.7)
        text(ax, 50, y + 8.0, name, size=7.4, bold=True)
        text(ax, 50, y + 3.6, d, size=5.8, color=NAVY)
    # Palantir 左侧条
    box(ax, 1, 38, 30, 39, '', fc=LIGHT[MAV], ec=MAV)
    text(ax, 16, 73.5, 'Palantir：企业与决策', size=8, bold=True, color=MAV)
    pl = ['Maven Smart System（MSS）\n情报融合、目标工作台、COA', 'Foundry / AIP / Ontology\n企业数据、大模型代理',
          'Target Workbench\n（NGC2 中师级目标处理）', 'Apollo 跨密级持续交付']
    for i, t in enumerate(pl):
        box(ax, 3, 61 - i * 7.5, 26, 6.6, t, fc='white', ec=MAV, size=5.7)
    # Anduril 右侧条
    box(ax, 69, 3, 30, 45, '', fc=LIGHT[LAT], ec=LAT)
    text(ax, 84, 45, 'Anduril：边缘与执行', size=8, bold=True, color=LAT)
    al = ['Lattice Mesh\n边缘数据网格（DDIL）', 'Lattice for C2 / 反无人机 C2\n传感器到射手、火控', 'Lattice for Mission\nAutonomy：集群自主',
          'Menace / Voyager 边缘硬件', '自研平台：Sentry、Anvil、\nRoadrunner、ALTIUS、Fury']
    for i, t in enumerate(al):
        box(ax, 71, 35.5 - i * 7.6, 26, 6.6, t, fc='white', ec=LAT, size=5.7)
    # 重叠区
    bz = box(ax, 32.5, 34.5, 35, 14, '', fc='none', ec=JOINT, lw=1.6, ls='--', z=1)
    bz._xg_free = True
    tag(ax, 50, 51.0, '交汇区：NGC2 通用数据层 = Lattice（边缘）+ Foundry（云）', color=JOINT, size=6.2)
    arrow(ax, 31, 60, 34, 60, color=MAV, ms=7)
    arrow(ax, 69, 26, 66, 26, color=LAT, ms=7)
    text(ax, 50, 1.5, '自上而下：目标发现、排序、交战分配（人在回路）→ 下发至边缘自主执行；自下而上：传感器数据经 Mesh 回流企业层。',
         size=5.8, color=GREY)
    return save(fig, 'd_division.png')


# ---------------------------------------------------------------- NGC2 架构
def d_ngc2():
    fig, ax = canvas(7.8, 5.2, ylim=(0, 66))
    box(ax, 1, 50, 98, 14, '', fc=LIGHT[MAV], ec=MAV)
    text(ax, 50, 61, '云 / 企业侧（Palantir Foundry）', size=7.6, bold=True, color=MAV)
    for i, t in enumerate(['Foundry 数据平台\n与本体', 'Target Workbench\n目标处理', 'Microsoft 云与\n协作工具', 'Govini 数据分析\n（供应链/决策）']):
        box(ax, 4 + i * 24, 51.5, 21, 7, t, fc='white', ec=MAV, size=5.8)
    box(ax, 1, 34, 98, 13, '', fc=LIGHT[JOINT], ec=JOINT)
    text(ax, 50, 44.3, '通用数据层基线（2026-06 陆军指定 Anduril 牵头）', size=7.4, bold=True, color=JOINT)
    for i, t in enumerate(['Lattice ↔ Foundry\n边缘—云数据网格', 'Raft：数据注册\n与联邦', 'Striveworks：\nMLOps 模型运维', 'Instant Connect：\n语音/通信互通']):
        box(ax, 4 + i * 24, 35.3, 21, 6.8, t, fc='white', ec=JOINT, size=5.8)
    box(ax, 1, 13, 98, 18, '', fc=LIGHT[LAT], ec=LAT)
    text(ax, 50, 28.3, '战术边缘（Anduril Lattice）', size=7.6, bold=True, color=LAT)
    for i, t in enumerate(['Lattice Mesh\n坚固 Voyager 套件', 'AXS 炮兵数据工具\n（M777 实弹）', 'RII 等传感器与\n情报接入', '营/连指挥所\n终端与平板']):
        box(ax, 4 + i * 24, 15, 21, 9.5, t, fc='white', ec=LAT, size=5.8)
    for x in (14.5, 38.5, 62.5, 86.5):
        arrow(ax, x, 42.1, x, 51.5, color=GREY, style='<|-|>', ms=6, lw=0.8)
        arrow(ax, x, 24.5, x, 35.3, color=GREY, style='<|-|>', ms=6, lw=0.8)
    ms = [('2025-07', '9960 万原型\n（第4步兵师）'), ('2025-09', 'Ivy Sting 1\n首次实弹'), ('2025-09', '陆军 CTO 备忘录\n“极高风险”'),
          ('2026-05', 'Ivy Mass\n全师上线'), ('2026-10', '18 亿扩展\n首个 I 军')]
    for i, (d, t) in enumerate(ms):
        x = 3 + i * 19.6
        box(ax, x, 1, 17.6, 9.5, d + '\n' + t, fc='white', ec=ALERT if '风险' in t else NAVY, size=5.5)
    return save(fig, 'd_ngc2.png')


# ---------------------------------------------------------------- 国家层面布局
def d_national():
    fig, ax = canvas(7.8, 6.4, ylim=(0, 84))
    rows = [('政策与采办改革', JOINT, ['EO 14265 采办现代化\n（2025-04）', 'EO 14307 无人机主导\n（2025-06）', 'Hegseth 无人机备忘录\n（2025-07）',
                                  '作战采办体系/PAE\n（2025-11）', '企业协议模式\nPalantir 100亿\nAnduril 200亿']),
            ('AI 指挥控制层', MAV, ['CJADC2（MSS 为基石）', 'MSS 转正式项目\n（Feinberg 2026-03）', 'FY27：MSS+联合火力网\n23 亿美元', 'Golden Dome C2\n“胶水层”（报道）', '北约 MSS NATO\n2026-06 全面能力']),
            ('军种 C2 数据层', PURPLE, ['陆军 NGC2\nLattice + Foundry', 'Army Transformation\nInitiative（2025-05）', 'TITAN 地面站\n（Palantir+Anduril）', 'SBMC 单兵头显\n（Lattice 数据层）', '北约 eAirC2 评估\n两家同场竞争']),
            ('规模化无人系统层', LAT, ['Replicator 1/2\n（Lattice 获 ACT 软件）', 'DAWG 自主作战群\nFY27 申请约 546 亿', 'Drone Dominance\n约 34 万架小型无人机', 'CCA 一期生产\n（Fury，2026-06）', 'JIATF-401 反无人机\nLattice 通用 C2']),
            ('印太与盟友', GREEN, ['INDOPACOM“地狱景观”\n无人拒止构想', '澳 Ghost Shark\n17 亿澳元', '台湾 ALTIUS\n600M / 700M', '英国 Palantir 伙伴关系\n最高 7.5 亿英镑', '日本拟结合\nMSS 与 Lattice（报道）'])]
    y = 70
    for name, col, items in rows:
        box(ax, 1, y, 16, 12, name, fc=col, ec=col, size=7.2, bold=True, color='white')
        for i, t in enumerate(items):
            fc = 'white'
            if 'Lattice' in t or 'Anduril' in t or 'Fury' in t or 'Ghost' in t or 'ALTIUS' in t:
                fc = LIGHT[LAT]
            if 'MSS' in t or 'Palantir' in t or 'Foundry' in t:
                fc = LIGHT[MAV] if fc == 'white' else LIGHT[JOINT]
            box(ax, 18.5 + i * 16.2, y, 15.4, 12, t, fc=fc, ec=col, size=5.4)
        y -= 14.5
    box(ax, 18.5, 0.5, 4, 2.6, '', fc=LIGHT[LAT], ec=LAT); text(ax, 23.5, 1.8, '涉及 Lattice/Anduril', size=5.8, ha='left')
    box(ax, 42, 0.5, 4, 2.6, '', fc=LIGHT[MAV], ec=MAV); text(ax, 47, 1.8, '涉及 MSS/Palantir', size=5.8, ha='left')
    box(ax, 65, 0.5, 4, 2.6, '', fc=LIGHT[JOINT], ec=JOINT); text(ax, 70, 1.8, '两家共同涉及', size=5.8, ha='left')
    return save(fig, 'd_national.png')


# ---------------------------------------------------------------- 双系统大事时间轴
def d_timeline():
    """竖排双栏大事记：中轴为时间，左栏 Lattice/Anduril，右栏 Maven/Palantir，每事件独占一行。"""
    L = [('2017-06', 'Anduril 成立，首个产品为边境监视塔 AI'), ('2018-06', 'CBP 监视塔试点（圣迭戈、尤马）'),
         ('2020-07', 'CBP 监视塔转为采购项目'), ('2022-01', 'SOCOM 反无人机集成商，上限 9.68 亿美元'),
         ('2023-05', '发布 Lattice for Mission Autonomy（EDGE23）'), ('2023-09', '收购 Blue Force（Fury 无人机）'),
         ('2024-12', 'SDK 对外开放；与 Palantir 结盟；CDAO 边缘网格 1 亿'),
         ('2025-03', '陆战队基地反无人机，上限 6.42 亿美元'), ('2025-07', 'NGC2 原型（第4步兵师）9960 万美元'),
         ('2025-10', 'YFQ-44A Fury 首飞'), ('2026-03', '陆军企业协议，上限 200 亿美元'),
         ('2026-07', '北约 eAirC2 评估合同（首个北约合同）'), ('2026-10', 'NGC2 扩展合同，上限 18 亿美元（I 军）')]
    M = [('2017-04', 'Work 备忘录成立算法战跨职能小组（AWCFT）'), ('2017-12', '首次部署：ScanEagle 视频目标识别'),
         ('2018-06', '谷歌员工抗议，宣布不再续约'), ('2020-09', 'XVIII 空降军“猩红之龙”演习起步'),
         ('2022-03', '支援乌克兰目标情报（威斯巴登）'), ('2023-11', 'NGA Maven 列为采购项目'),
         ('2024-02', 'CENTCOM 2·2 空袭伊叙 85 处目标'), ('2024-05', 'Palantir MSS 原型 IDIQ，4.8 亿美元'),
         ('2025-03', '北约采购 MSS NATO'), ('2025-05', 'MSS 上限增至约 12.75 亿美元'),
         ('2025-07', '陆军与 Palantir 企业协议，上限 100 亿'), ('2026-03', '对伊朗作战；Feinberg 备忘录转项目'),
         ('2026-06', 'MSS NATO 达到全面作战能力'), ('2026-09', '用户突破 10 万人')]
    ev = sorted([(d, 'L', t) for d, t in L] + [(d, 'M', t) for d, t in M])
    n = len(ev)
    fig, ax = canvas(7.8, 0.235 * n + 0.9, xlim=(0, 100), ylim=(-1.5, n + 1.6))
    text(ax, 24, n + 0.9, 'Lattice / Anduril', size=8, bold=True, color=LAT)
    text(ax, 76, n + 0.9, 'Maven / Palantir', size=8, bold=True, color=MAV)
    ax.plot([50, 50], [-0.8, n + 0.3], color=NAVY, lw=1.2, zorder=1)
    last_year = None
    for i, (d, side, t) in enumerate(ev):
        y = n - 1 - i
        yr = d[:4]
        col = LAT if side == 'L' else MAV
        if yr != last_year:
            ax.plot([44.5, 55.5], [y + 0.5, y + 0.5], color=PAL['grid'], lw=0.8, zorder=0)
            box(ax, 46, y - 0.38, 8, 0.76, yr, fc=NAVY, ec=NAVY, size=6.2, bold=True, color='white', r=0.2, z=3)
            last_year = yr
        else:
            ax.plot([50], [y], 'o', color=col, markersize=3.2, zorder=3)
        if side == 'L':
            ax.plot([33.5, 45.8], [y, y], color=col, lw=0.6, ls=':')
            text(ax, 33, y, t, size=6.0, ha='right', color=NAVY)
            text(ax, 41.5, y + 0.0, d[5:] + '月', size=5.4, color=col)
        else:
            ax.plot([54.2, 66.5], [y, y], color=col, lw=0.6, ls=':')
            text(ax, 67, y, t, size=6.0, ha='left', color=NAVY)
            text(ax, 58.5, y + 0.0, d[5:] + '月', size=5.4, color=col)
    return save(fig, 'd_timeline.png')

if __name__ == '__main__':
    for f in [d_lattice_arch, d_lattice_entity_task, d_lattice_killchain, d_maven_arch, d_maven_workflow,
              d_maven_governance, d_division, d_ngc2, d_national, d_timeline]:
        print(f())
    for x in OVERLAP_LOG:
        print('⚠', *x)
