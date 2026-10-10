# 边缘网格与目标工厂：Lattice 与 Maven 如何重塑美军杀伤链

截至 2026 年 10 月，美军"传感器到射手"的数字化杀伤链主要建立在两套软件上，而且两者已经接在了一起。**Anduril 公司的 Lattice** 起家于 2017 年美墨边境的 AI 监视塔，后来逐步成为反无人机火控内核、无人集群自主软件，再到美陆军"下一代指挥控制"（NGC2）的通用数据层。它最突出的地方是边缘网状数据网（Lattice Mesh）、以"实体（Entity）"为核心的数据模型，以及直接向武器和无人平台下发"任务（Task）"的能力。**Maven** 则起源于国防部 2017 年的"算法战跨职能小组"（Project Maven，最初只做无人机视频的计算机视觉识别）。它现在以 **Palantir 的 Maven Smart System（MSS，Maven 智能系统）** 为主体，成为联合/作战司令部（COCOM）层级的情报融合与目标定位"工作流平台"，用户已超过 10 万人。2026 年对伊朗的"史诗怒火行动"（Operation Epic Fury）中，官方称它支撑了 38 天内对 13,000 个目标的打击。两套系统的分工大体是"Palantir 做企业级数据与决策，Anduril 做战术边缘的传输、融合与效应器控制"。2024 年 12 月两家结盟以后，这种分工已落到陆军 NGC2（Lattice Mesh + Palantir Foundry/Target Workbench）、"金穹"（Golden Dome）导弹防御 C2 和北约等项目上。不过两者的定量效能数据大多来自厂商或官员。可公开核实的负面证据集中在三处：乌克兰战场（Anduril 硬件受电子干扰失效）、伊朗 Minab 学校误炸（据报道与过度依赖 Maven 和过期数据有关），以及陆军 CTO 对 NGC2 原型"极高风险"的网络安全评估。

> **方法与可信度说明（务必先读）**：本报告根据七份调研笔记综合写成。调研期间，WebFetch/curl 对 anduril.com、defensescoop.com、breakingdefense.com、csis.org、Wikipedia 等站点的访问几乎全部被代理拦截（DNS/403），**所以绝大部分事实来自搜索引擎对原文的摘要，没有逐篇读全文**。唯一例外是 Lattice SDK 的数据模型与 API：这部分直接读取了 Anduril 在 GitHub 上公开的官方 Python SDK 源码（`anduril/lattice-sdk-python`），属于一手证据，可信度最高。文中凡标有"公司口径""官员表态""二手/低可信"的数字，以及第四章冲突清单里的条目，引用前都应回到原文核对。数据截止于 2026 年 10 月 10 日。

---

## 一、Lattice：从边境监视塔到陆军全军数据层的九年演进

### 1.1 前世今生：先拿下 CBP 采购项目，再进入国防部

Lattice 与 Anduril 同年诞生。Anduril 由 Oculus 创始人 Palmer Luckey 与 Trae Stephens、Brian Schimpf、Matt Grimm、Joe Chen 于 2017 年共同创立，其中三人出自 Palantir。成立日期有两种说法：一说 2017-04-20 注册，TechCrunch 则称公司于 2017 年 6 月"悄然成立"。较合理的解释是前者为注册日、后者为公开日，但没有找到证实 ([Wikipedia](https://en.wikipedia.org/wiki/Anduril_Industries); [TechCrunch](https://techcrunch.com/?p=1654777))。Lattice 的第一个用例是**为美国海关与边境保护局（CBP）在美墨边境建"虚拟墙"**。Sentry 太阳能监视塔集成雷达、光电/红外和射频传感器，Lattice 用 AI 处理这些数据，识别潜在威胁后自动告警边境人员 ([GovConWire](https://www.govconwire.com/articles/anduril-uav-uuv-lattice-homeland-security))。因此它从一开始就是一个**与硬件无关的融合层**，塔只是载体。正是这一点，让它后来能横向扩展到反无人机、指挥控制和集群自主。

从商业路径看，Anduril 先在国土安全领域拿到"采购项目"（Program of Record，即列入正式预算和采购计划的项目）地位，再进入国防部。2018 年 6 月的首个 DHS 合同金额 480 万美元，在圣迭戈和尤马部署 10 座塔 ([FedScoop](https://fedscoop.com/anduril-sentry-towers-cbp/))。2020 年，**自主监视塔（AST）被 CBP 宣布为采购项目** ([CBP](https://www.cbp.gov/newsroom/national-media-release/cbp-s-autonomous-surveillance-towers-declared-program-record-along))。需要注意，采购项目的对象是塔项目，不是单独的 Lattice 软件。2022 年 1 月，SOCOM（美国特种作战司令部）反无人机系统集成商合同让 Lattice 第一次以"系统集成内核"身份进入国防部。2023 年发布 Lattice for Mission Autonomy，Lattice 开始产品化。2024 年 12 月推出 SDK 和合作伙伴计划，走向平台化。2025–2026 年，陆军 NGC2、200 亿美元企业合同和北约合同相继落地，Lattice 由此成为**军种级通用数据层**。

**表 1-1　Lattice 演进年表（2017–2026.10）**

| 日期 | 事件 | 意义 | 来源 |
|---|---|---|---|
| 2017（4 月注册/6 月公开，存疑） | Anduril 成立，Lattice 同期开发 | 边境监视软件起步 | [Wikipedia](https://en.wikipedia.org/wiki/Anduril_Industries) |
| 2018-06 | 首个 DHS 合同 480 万美元，在圣迭戈、尤马部署 10 座塔；同月在德州私人牧场做非正式测试 | 第一个付费用户 | [FedScoop](https://fedscoop.com/anduril-sentry-towers-cbp/) |
| 2019 | CBP 创新团队在圣迭戈测试 5 座塔，结果成功 | 验证 | [FedScoop](https://fedscoop.com/anduril-sentry-towers-cbp/) |
| 2020 | AST 成为 CBP 采购项目；据报道获 8,500 万美元，扩展到 El Paso、Rio Grande Valley；同年完成 2 亿美元 C 轮融资 | 首个采购项目 | [AI Business](https://aibusiness.com/verticals/anduril-raises-200m-wins-contract-for-autonomous-surveillance-towers-along-us-mexico-border) |
| 2020-10 | AFRL/ABMS 巡航导弹拦截演示：操作员确认 Lattice 跟踪正确后，向效应器下达交战指令 | 首次进入空军/防空场景 | [Defense News](https://www.defensenews.com/digital-show-dailies/ausa/2020/10/16/anduril-adapts-tech-to-detect-cruise-missiles-in-air-force-demo/) |
| 2022-01 | SOCOM 选定 Anduril 为反无人系统集成商：10 年期 IDIQ，上限 9.676 亿美元（常称"约 10 亿"），在 11 家竞标者中胜出 | 进入国防部的转折点 | [Defense News](https://www.defensenews.com/unmanned/2022/01/24/us-special-operations-command-picks-anduril-to-lead-counter-drone-integration-work-in-1b-deal/); [AFCEA Signal](https://www.afcea.org/signal-media/contracting/socom-selects-anduril-integration-partner-967-million-counter-unmanned) |
| 2023-05-03 | 发布 **Lattice for Mission Autonomy**（LMA，任务自主），提出"一人操控多机" | 产品化 | [Defense News](https://www.defensenews.com/industry/2023/05/03/anduril-unveils-software-to-manage-hordes-of-drones/) |
| 2023 | 陆军 EDGE23 演习：单兵操控多型无人机摧毁防空导弹阵地 | 集群自主首次公开展示 | [Anduril blog](https://blog.anduril.com/anduril-demonstrates-lattice-for-mission-autonomy-controlling-teams-of-autonomous-assets-at-us-f617c489441) |
| 2024-09 | 部署第 300 座 AST，公司称覆盖约 30% 南部陆地边境 | 规模化（公司口径） | [ASDNews](https://www.asdnews.com/news/defense/2024/09/27/anduril-deploys-300th-autonomous-surveillance-tower-ast-advancing-capability-border-security) |
| 2024-11 | 太空军太空监视网（SSN）现代化合同，采用基于 Lattice 的网状网络，预计 2026 年底全面部署 | 进入太空域 | [ExecutiveBiz](https://executivebiz.com/2024/11/anduril-contract-award-modernize-space-surveillance-network-ssc) |
| 2024-12-03 | CDAO 授予 3 年期、1 亿美元生产型 OTA，推广基于 Lattice Mesh 的"边缘数据网格" | Mesh 成为国防部采购对象 | [DefenseScoop](https://defensescoop.com/2024/12/03/anduril-awarded-100m-deal-cdao-scale-edge-data-mesh-capabilities-ota/) |
| 2024-12-06 | 与 Palantir 宣布合作（Lattice/Menace + AIP/MSS） | 两大系统结盟 | [BusinessWire](https://www.businesswire.com/news/home/20241206684306/en/Anduril-and-Palantir-to-Accelerate-AI-Capabilities-for-National-Security) |
| 2024-12-10 | **Lattice SDK 公开发布**，同时推出合作伙伴计划（首批 10 余家） | 平台化 | [Defense Daily](https://www.defensedaily.com/anduril-offers-software-development-kit-for-lattice-networking-platform-to-boost-interoperability/advanced-transformational-technology/) |
| 2025-01 至 05 | 收购 Numerica 雷达与 C2 业务；收购 Klas（Voyager 边缘计算）；发布 Menace-T/X | 补齐雷达与边缘硬件 | [Built In](https://builtin.com/articles/what-is-anduril); [TechCrunch](https://techcrunch.com/2025/05/05/anduril-is-working-on-the-difficult-ai-related-task-of-real-time-edge-computing/) |
| 2025-03 | 陆战队 I-CsUAS 合同（上限 6.42 亿美元）；新加坡 DSTA/RSAF 合作（LMA 首个国际合作） | 多军种、国际化 | [DefenseScoop](https://defensescoop.com/2025/03/13/marine-corps-anduril-contract-defend-installations-small-uas-drones/); [Asian Military Review](https://asianmilitaryreview.com/?p=18585) |
| 2025-07-18 | 陆军 NGC2 原型 OTA，9,960 万美元、11 个月，为第 4 步兵师建原型 | 进入师级 C2 | [Army.mil](https://www.army.mil/article/287180/army_announces_next_generation_command_and_control_ngc2_prototype_award) |
| 2025-09 | Ivy Sting 1 实弹演习：师级目标处理流程完全运行在 Lattice Mesh 和 Palantir Target Workbench 上 | 两家首次在实弹杀伤链中集成 | [Defence Industry Europe](https://defence-industry.eu/anduril-and-u-s-army-showcase-next-gen-command-and-control-with-ngc2-in-live-fire-ivy-sting-1/) |
| 2025-11-10 | 陆军选定 Lattice 为 IBCS-M（机动型一体化作战指挥系统）反无人机火控/C2 平台 | 进入陆军防空体系 | [DefenseScoop](https://defensescoop.com/2025/11/11/army-ibcs-maneuver-anduril-lattice-counter-uas/) |
| 2026-02-24 | LMA 首次在 YFQ-44A Fury 上飞行 | 进入 CCA | [Defence Industry Europe](https://defence-industry.eu/u-s-air-force-selects-anduril-lattice-mission-autonomy-software-for-next-collaborative-combat-aircraft-program-phase/) |
| 2026-03-13/14 | **陆军 10 年期企业合同，上限 200 亿美元**，把 120 多项采购行动并入以 Lattice 为中心的框架；首个任务单 8,770 万美元（JIATF 401 反无人机） | 军种级锁定 | [DefenseScoop](https://defensescoop.com/2026/03/14/anduril-20-billion-dollar-army-contract/) |
| 2026-06 | 陆军指定 Anduril 牵头 NGC2 通用数据层基线（Lattice + Foundry）；空军在 CCA 下一阶段选定 LMA；CBP 3.63 亿美元增程塔合同 | 三线同时扩张 | [DefenseScoop](https://defensescoop.com/2026/06/22/army-taps-anduril-lead-ngc2-common-data-layer-baseline/) |
| 2026-07-07 | 北约 NCIA 选择 Lattice 用于 eAirC2 数据平台计划（Anduril 首个北约合同，从 9 个月评估期起步） | 进入北约 | [Anduril](https://www.anduril.com/news/anduril-secures-first-nato-contract-lattice-for-eairc2-data-platform-initiative) |
| 2026-10-05/06 | NGC2 部署合同：5 年、上限 18 亿美元，基础期 1.628 亿美元，从 I 军开始 | 从原型转入部署 | [GovConWire](https://www.govconwire.com/articles/anduril-army-ngc2-contract-i-corps) |

**收购补齐了 Lattice 可编排的"末端节点"。** Anduril 的收购逻辑可以概括为"Lattice 为中枢，硬件为末梢"：Area-I（空射效应器，多数来源记为 2021 年 4 月，另一处列表记为 2022 年 10 月，存在冲突）、Dive Technologies（水下航行器，2022 年 2 月或 2023 年 3 月，存在冲突，是 Ghost Shark 的基础）、Blue Force Technologies（2023-09，Fury 无人机，后来发展为 YFQ-44A）、Numerica 雷达与 Mimir C2 软件（2025-01）、Klas 的 Voyager 坚固边缘计算（2025-05-05 签约）([Contrary Research](https://research.contrary.com/company/anduril); [Janes](https://www.janes.com/defence-intelligence-insights/defence-news/air/anduril-acquires-blue-force-technologies-entering-large-uav-market); [PrivSource](https://www.privsource.com/acquisitions/deal/anduril-industries-acquires-klas-7YSEr6))。每一笔收购都给 Lattice 增加一类可感知或可打击的节点，平台的锁定效应也随之加强。

**估值曲线与 Lattice 地位同步上升。** Anduril 估值从 2019 年 B 轮的约 10 亿美元，涨到 2024-08 F 轮的 140 亿、2025-06 G 轮的 305 亿，再到 **2026-05-13 H 轮的 610 亿美元**（融资 50 亿美元）([TechCrunch](https://techcrunch.com/2026/05/13/anduril-raises-5b-doubles-valuation-to-61b/))。2026-07-24 路透社报道其正以约 1,000 亿美元估值洽谈新一轮，但未见交割确认 ([Defense News](https://www.defensenews.com/industry/techwatch/2026/07/24/anduril-in-talks-to-raise-funding-at-about-100-billion-valuation/))。营收按公司口径计，2024 年约 10 亿美元，2025 年 22 亿美元，2026 年目标约 43 亿美元，均未经审计 ([CNBC](https://www.cnbc.com/2026/05/13/anduril-valuation-defense-tech-funding-boom.html))。截至 2026 年 10 月尚未宣布 IPO。估值跃升的时间点与 SOCOM、NGC2、200 亿美元企业合同的落地高度吻合，说明市场是把 Anduril 当作"软件平台型主承包商"来定价的。

### 1.2 功能设计：以实体为中心的作战图，加上军事化的任务生命周期

Lattice 的功能设计可以从官方 SDK 源码直接还原，这是全报告证据最硬的部分。它的核心是一张**以"实体"（Entity）为中心的共用作战图（COP，Common Operational Picture）**。航迹、己方资产、地理区域（含地理围栏）、信号源都被建模为实体，每个实体由一组可选的、强类型的"组件"（component）构成。COP 之上有三类 API：**实体（Entities）**负责发布、订阅和人工覆写；**任务（Tasks）**负责在操作员与"可受领任务的代理"（taskable agent，即无人机、拦截器等）之间流转军事化指令；**对象（Objects）**是在网格中同步的文件/二进制存储 ([lattice-sdk-python reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md))。

**表 1-2　Lattice 功能模块拆解**

| 模块 | 关键设计（官方 SDK 原名） | 军事含义 | 证据等级 |
|---|---|---|---|
| 实体数据模型 | 一个 Entity 代表"Lattice 作战环境中的一个已知对象"，组件包括 `location/kinematics`（位置/运动学，航迹优先用后者）、`mil_view`、`tracked`、`correlation`、`ontology`、`sensors`、`payloads`、`signal`（信号源）、`orbit`（空间目标轨道）、`transponder_codes`（应答机/IFF 代码）、`symbology`、`target_priority`、`task_catalog`、`health`、`supplies`、`data_classification` 等 30 余项；发布时 `expiry_time` 必须设定，且须在 30 天以内 ([entity.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/entity.py)) | 覆盖陆海空天电全域，所有数据都有时效 | 一手 |
| 本体模板 | 五类：`TEMPLATE_TRACK`（航迹）、`TEMPLATE_SENSOR_POINT_OF_INTEREST`（传感器关注点）、`TEMPLATE_ASSET`（己方平台）、`TEMPLATE_GEO`（地理区域/围栏）、`TEMPLATE_SIGNAL_OF_INTEREST`（关注信号）([ontology_template.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/ontology_template.py)) | 战场对象的五种基本类型 | 一手 |
| 敌我识别 | `MilView` 属性：UNKNOWN / FRIENDLY / HOSTILE / SUSPICIOUS / ASSUMED_FRIENDLY / NEUTRAL / PENDING，另有环境和国籍字段 ([mil_view_disposition.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/mil_view_disposition.py)) | 与北约/美军标准敌我属性一致 | 一手 |
| 航迹与融合 | `tracked` 组件含 0–15 航迹质量分、传感器命中数、雷达截面积，`number_of_objects` 注释为"在 Link 16 中称为 Strength"；`correlation` 组件支持 N 对 1 的主/从航迹关联，并有显式"去关联"记录，用来阻止**自动关联器**把被人判定为不同的两条航迹重新合并 ([tracked.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/tracked.py); [correlation.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/correlation.py)) | 经典的多传感器航迹融合，自动关联，人可推翻 | 一手 |
| 标识与密级 | `indicators` 含 simulated（模拟）、exercise（演习）、emergency、c2、egressable（可外发，例如需要先做模糊化）；`data_classification` 有默认密级和逐字段密级，从非密到绝密，带 NOFORN 等附加标记 ([indicators.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/indicators.py); [classification.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/classification.py)) | 字段级密级，为多级安全和跨域外发预留了接口 | 一手 |
| 所有权与覆写 | 实体归发布者"所有"，UI 不能编辑或删除；只有比 `provenance.sourceUpdateTime` 更新的数据才会被接受；操作员可以覆写可覆写字段（如 `mil_view.disposition`），最终一致，后写者胜 ([reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md)) | "谁把目标定为敌对"有溯源记录 | 一手 |
| 任务（Tasking） | 生命周期：CREATED → SCHEDULED_IN_MANAGER → SENT → MACHINE_RECEIPT → ACK → **WILCO**（无线电用语"将遵照执行"）→ EXECUTING → DONE_OK/DONE_NOT_OK，另有 REPLACED、CANCEL_REQUESTED 等；任务含 `specification`（protobuf Any 封装的任务定义）、`author`、`initial_entities`（如"目标""限入区"）、重试与执行约束；代理可以拒绝取消请求 ([task_status_status.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/task_status_status.py)) | 照搬战术数据链和语音 C2 的确认语义 | 一手 |
| 能力目录 | 资产通过实体的 `task_catalog` 组件声明自己能执行哪些任务 ([task_catalog.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/task_catalog.py)) | 新平台接入后自动"可被调度" | 一手 |
| 手动控制 | `stream_manual_control_frames` 把摇杆动作流式发给执行代理，带纪元号和序号，处理并发控制和过期帧 | 自主与人工遥控可以随时切换 | 一手 |
| 对象与视频 | Objects 单个对象最大 1 GiB，可以只列本节点，也可以列全网格；Video API 支持 RTSP 拉流、SRT/MPEG-TS 推流，MPEG-TS 只在边缘封闭网络中可用 | 情报产品和视频在网格中分发 | 一手 |
| 任务自主（LMA） | "硬件无关、端到端"平台，覆盖威胁建模、任务规划、C2、复盘，管理"数百个"异构无人系统，"从多人操控一机转为一人操控多机" ([Anduril blog](https://blog.anduril.com/anduril-unveils-lattice-for-mission-autonomy-8e0c5fa0e94b)) | 集群作战大脑 | 公司口径 |
| 反无人机杀伤链 | "从探测到摧毁"的传感器融合与自动火控（IBCS-M）([DefenseScoop](https://defensescoop.com/2025/11/11/army-ibcs-maneuver-anduril-lattice-counter-uas/)) | 探测—跟踪—识别—拦截一体 | 合同事实 |
| 火力与师级 C2 | NGC2 中运行炮兵数据工具 AXS，与 Target Workbench 协同完成师级目标处理 ([Breaking Defense](https://breakingdefense.com/2025/10/in-ngc2-first-army-uses-beta-artillery-data-tool-in-howitzer-strike-at-ivy-sting-1/)) | 从传感器到炮位 | 演习事实 |

从这些设计可以推断出 Lattice 的标准交战流程（推断，未见官方完整描述）：边缘 AI 检测并分类，发布航迹实体；自动关联器融合多源航迹；操作员或规则把属性改为 HOSTILE，留下带溯源的覆写记录；操作员创建或批准一条"打击/拦截"任务，发给效应器代理；代理按 ACK → WILCO → EXECUTING → DONE 回报；自主模块随后自动派出 ISR 资产做毁伤评估。EDGE23 演习印证了最后一步：士兵把防空导弹阵地定为"敌对"并授权 ALTIUS-600M 打击之后，**Lattice 自动把一架 ALTIUS ISR 无人机改派去做毁伤评估（BDA）**([Anduril blog](https://blog.anduril.com/anduril-demonstrates-lattice-for-mission-autonomy-controlling-teams-of-autonomous-assets-at-us-f617c489441))。也就是说，机动和感知是"人在回路上"（human-on-the-loop，人监督、可干预），武器释放则是"人在回路中"（human-in-the-loop，必须由人批准）。陆战队的文件也明确，Anvil 拦截器可以自主跟踪，但**只在人工操作员下令后才拦截** ([Marines.mil](https://www.pae.marines.mil/Media/Article/Article/4484189/pm-gbad-successfully-demonstrates-kinetic-interceptor-capability/))。

功能上的空白同样需要说明：告警和地理围栏的专用 API、`tasks/v*` 下的具体任务定义（如目视识别、侦察、打击）、可覆写字段的完整清单、仿真器产品、交战规则（ROE）配置，以及是否存在针对小型无人机的"自动交战"模式，公开资料中都没有找到。

### 1.3 架构设计：节点联邦、网状网格与 protobuf 内核

Lattice 的部署形态是**由 Lattice Mesh 连接起来的一组"节点"**。节点可以是边缘套件、监视塔、车辆，也可以是云端或本地机房。Mesh 是点对点数据网格，设计目标是在链路被拒止、降级、时断时续或带宽受限（DDIL）的条件下继续工作。Anduril 的 Lattice Mesh 专利（US 10,506,436）写明，**"实时数据是系统优先级，回填只使用剩余带宽"**；路由安全依靠点对点授权，普通节点的密钥只放在内存里，不落盘 ([USPTO](https://uspto.report/patent/grant/10506436))。SDK 也印证了节点本地存储加跨节点复制的结构：Objects API 默认只列本节点对象，`all_objects_in_mesh=true` 才列全网格，`last_updated_at` 记录的是"副本到达本节点"的时间，并支持 RFC 9218 优先级头 ([reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md))。

**表 1-3　Lattice 分层架构（事实与推断已分开标注）**

| 层 | 组成 | 关键事实 | 证据 |
|---|---|---|---|
| ① 传感器/效应器端 | Sentry 塔（固定/机动/增程）、Wisp、Pulsar（电子战）、Anvil、ALTIUS-600/600M、Ghost-X、Roadrunner、YFQ-44A，以及第三方雷达和拦截器（如 ORIGIN BLAZE） | 每个 Anduril 产品内置"Lattice AI Core"，在边缘做传感器融合、目标分类和多航迹调和 | 公司口径 ([Air Recognition](https://airrecognition.com/index.php/news/defense-aviation-news/2022-news-aviation-aerospace/january/8118-us-special-ops-command-awards-anduril-industries-a-1b-counter-drone-contract.html)) |
| ② 边缘计算与通信硬件 | Menace-T（双箱 C4 套件，一人数分钟架设）、Menace-X（机动版），基于 Klas Voyager 硬件；NGC2 中使用坚固 Voyager 套件 | Menace 运行 Lattice Mesh，可承载第三方边缘 AI，并且是 **Palantir Edge 软件的首选硬件** | 事实 ([TechCrunch](https://techcrunch.com/2025/05/05/anduril-is-working-on-the-difficult-ai-related-task-of-real-time-edge-computing/); [Defence Connect](https://www.defenceconnect.com.au/land/16047-andurils-menace-systems-preferred-hardware-partner-for-palantirs-edge-software)) |
| ③ Lattice Mesh 数据网格 | P2P、按优先级选路、实时优先、存储转发 | 公司称已"连接全球数千个防务系统"；2024-12 CDAO 1 亿美元 OTA 时已在"多个军种和作战司令部"运行 | 专利 + 合同事实 ([DefenseScoop](https://defensescoop.com/2024/12/03/anduril-awarded-100m-deal-cdao-scale-edge-data-mesh-capabilities-ota/)) |
| ④ 核心服务 | Entity Manager、Task Manager、对象存储、视频服务、自动关联器 | gRPC 的 Entity/Task Manager 与 HTTP 的 Entities/Tasks API ([docs.anduril.com](https://docs.anduril.com/guide/overview)) | 文档事实；"每节点运行完整栈"为推断 |
| ⑤ API/SDK | v1 原生 gRPC；v2 为 OpenAPI/REST + SSE 流式推送；OAuth2 客户端凭证认证；Python、Go、Java、TypeScript、C++（2025-07 归档）、Rust（2026-10）多语言 SDK | 长轮询客户端落后超过环境实体总数 3 倍会被断开；SSE 断线后自动续传；可按组件和过滤语句订阅以节省带宽 | 一手 ([reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md)) |
| ⑥ 应用层 | LMA、Lattice for C2（AI 战斗管理）、反无人机 C2、NGC2 应用（AXS 炮兵工具等）、合作伙伴应用 | 2026 年新增 Developer Console、Schema Registry、Video API、面向编程智能体的"SDK skills" | 开发者更新日志摘要 ([changelog](https://developer.anduril.com/changelog)) |

SDK 定义了三种接入模式 ([reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md))。**生产者**（传感器或 C2 适配器）调用 PublishEntity 发布航迹或资产实体。**消费者**（UI 或分析程序）调用 StreamEntities，先收到全部 PREEXISTING 事件，再收增删改事件，默认每 30 秒一次心跳。**可受领任务的代理**（机器人或效应器）先发布带 `task_catalog` 的资产实体，再通过 StreamAsAgent/ListenAsAgent 接收执行、取消、完成请求，并用 UpdateTaskStatus 回报进度。v2 的 REST 接口使用 `google.protobuf.Any`、`STATUS_`/`TEMPLATE_` 枚举前缀，过滤器也注明与 gRPC 端点"镜像"。由此可以判断 **Lattice 内部是 protobuf/gRPC 原生的**，REST 只是外层封装（推断）。SDK 许可是有限、可撤销、免版税的，只能用于为"兼容的 Lattice 实现"开发应用，禁止用来构建竞品 SDK ([developer.anduril.com/license](https://developer.anduril.com/license))。所以它是"开放接口、封闭实现"，不是开源。

在标准与互操作方面，**只有 A-GRA（政府参考自主架构）合规有明确记录**：YFQ-44A 在一次飞行中通过早期 A-GRA 实现，在 Shield AI 的 Hivemind 与 Anduril 的 LMA 两套自主软件之间切换 ([The Aviationist](https://theaviationist.com/2026/03/03/yfq-44a-tests-shivemind-lattice-ais/))。Link 16 概念直接写进了数据模型（Strength 字段、WILCO 状态），但没有可靠来源证实 Lattice 支持 OMS/UCI 消息标准或有现成的 TAK/CoT 网关。Anduril 在招聘 ATAK 工程师，但这不能证明存在 Lattice–TAK 桥接产品 ([Built In](https://builtin.com/job/sr-atak-engineer/7073600))。安全认证方面，IL5/IL6、SIPR/JWICS 授权等级和跨域解决方案均无公开信息；运行时技术栈（操作系统、是否用 Kubernetes）也未公开。

### 1.4 能力评估：采购决策是硬证据，实战效能几乎全由公司提供

衡量 Lattice 能力，最可靠的指标是**多军种通过竞标作出的采购选择**。SOCOM（11 家竞标中胜出）、陆战队 I-CsUAS（9 家竞标中胜出）、陆军 IBCS-M、陆军 200 亿美元企业合同、陆军 NGC2 从原型直接转入 18 亿美元部署，这一连串决策说明用户确实认可它作为**集成层/数据层/C2 软件**的价值。但几乎所有定量效能数据都来自 Anduril：Ivy Mass 演习"炮兵火力时间缩短 90%"、"炮组 30 秒内完成数字化准备"、"2,500 余台终端"、IBCS-M 测试"完美击杀"等 ([MilitaryLeak](https://militaryleak.com/2026/05/26/how-team-anduril-and-us-army-took-lattice-across-the-4th-infantry-division/))。相比之下，IBCS-M 在尤马试验场为期 7 天的试验较有说服力：Lattice **在数小时内接入了一个此前未公开的传感器和效应器，实弹拦截 4 中 4** ([DefenseScoop](https://defensescoop.com/2025/11/11/army-ibcs-maneuver-anduril-lattice-counter-uas/))。这直接检验了它"硬件无关、快速集成"的核心卖点。

**表 1-4　Lattice 能力：已证实、公司宣称与反证**

| 能力维度 | 较强证据（合同/官方/独立媒体） | 主要依赖公司声明 | 反证或负面证据 |
|---|---|---|---|
| 固定站点传感器融合与自动检测/跟踪 | CBP 采购项目，数百座塔持续运行；CBP 官员称塔跟踪的是物体和活动，不识别个人，不做人脸识别 ([FedScoop](https://fedscoop.com/anduril-sentry-towers-cbp/)) | "覆盖边境 30%"（指地理覆盖，不是检测效果） | 无公开检测率或虚警率；MIT Technology Review 估算 2021 年以来有 110 多人死在塔的覆盖范围内 ([MIT TR](https://www.technologyreview.com/2026/09/21/1144166/border-towers-surveillance-investigation/))；GAO 隐私审查"六项全不达标"的说法只有倡导类网站转述 |
| 多传感器/多效应器反无人机 C2 | IBCS-M 选型与 4/4 拦截；JIATF 401；I-CsUAS；科威特拟议军售 | 伊朗冲突中"主要系统"、"大量参与"（总裁笼统表态）([AOL](https://www.aol.com/articles/andurils-president-says-firm-heavy-040829085.html)) | 没有可独立核实的实战击落记录；Anvil 测试在俄勒冈引发 22 英亩野火 ([Sherwood News](https://sherwood.news/tech/wsj-andurils-weapons-systems-have-failed-during-several-tests/)) |
| 师级战场数据网格与火力链 | 9,960 万美元原型转入 18 亿美元部署；第 4 步兵师整师上线 | 30 秒、90%、65 个以上边缘节点、2,500 台设备 | 陆军 CTO 备忘录称原型"极高风险"（见第三章） |
| 无人平台自主/集群控制 | EDGE23 演示；澳大利亚 Ghost Shark 按期交付并列装 | LMA 管理"数百个"平台 | 美国海军加州近海演习中十余艘 Lattice 控制的无人艇失灵；乌克兰 Altius 和 Ghost 受干扰失败 ([TechCrunch](https://techcrunch.com/2025/11/27/andurils-autonomous-weapons-stumble-in-tests-and-combat-wsj-reports)) |
| AI 识别准确性 | 无 | "AI 识别威胁比人更准" ([PopSci](https://www.popsci.com/technology/sentry-camera-border-security-texas/)) | 没有模型卡、训练数据或准确率指标 |

最大的未证实领域是**强电子对抗环境下的表现**。乌克兰是 Anduril 系统唯一可公开核实的实战场景，结果总体负面。据 WSJ（经 TechCrunch 转述），2022 年交付乌军的约 40 架 Ghost 受俄方干扰严重；SBU（乌克兰安全局）使用的 Altius 坠毁、未命中目标，2024 年被停用 ([TechCrunch](https://techcrunch.com/2025/11/27/andurils-autonomous-weapons-stumble-in-tests-and-combat-wsj-reports))。这些失败主要出在飞行平台和导航/数据链上，不能直接算到 Lattice 软件头上，但 Lattice 宣传的"边缘自主、抗干扰"确实没有得到实战支持。Anduril 的回应是"我们确实失败，而且很多"，属于迭代研发的正常现象 ([Edward Conard 摘要](https://www.edwardconard.com/macro-roundup/tests-in-the-us-and-on-the-battlefield-in-ukraine-suggest-that-anduril-a-leading-new-entrant-into-the-defense-industry-is-facing-challenges-in-developing-and-fielding-attritable-mass-weapons-systems/))。另有一条值得注意的信息：在 CCA 项目中，有来源称空军已在下一阶段选定 LMA，也有笔记认为公开资料没有说清 Lattice 在 CCA 自主软件中的角色，并提到 Anduril、Shield AI、Collins 各获 6 个月自主 CLIN、之后再择优的说法。**Lattice 在 CCA 中的确切地位仍需核实** ([Simple Flying](https://simpleflying.com/software-deal-put-anduril-inside-every-cca-air-force-buys/))。

### 1.5 案例目录：边境、反无人机、师级 C2、海上与盟国

**表 1-5　Lattice 主要案例**

| # | 日期 | 用户/单位 | 地点 | Lattice 做了什么 | 结果/数据 | 可信度与来源 |
|---|---|---|---|---|---|---|
| 1 | 2018 至今 | CBP | 美墨边境 | Sentry/AST 塔自动检测、分类、跟踪人员和车辆，向特工推送告警 | 2020 年成为采购项目；2024 年第 300 座；2026-06 追加 200 余座增程塔（3.63 亿美元） | 官方+公司 ([CBP](https://www.cbp.gov/newsroom/national-media-release/cbp-s-autonomous-surveillance-towers-declared-program-record-along); [ExecutiveBiz](https://www.executivebiz.com/articles/cbp-anduril-extended-range-sentry-towers-363m)) |
| 2 | 2020-10 | AFRL/ABMS | 美国本土 | 巡航导弹替代目标的跟踪与交战引导，由人确认后下令 | 演示成功 | 媒体 ([Defense News](https://www.defensenews.com/digital-show-dailies/ausa/2020/10/16/anduril-adapts-tech-to-detect-cruise-missiles-in-air-force-demo/)) |
| 3 | 2021 起 | 英国国防部 | 英国/海外基地 | 2021 年 520 万美元部队防护演示（Ghost 4 + Lattice）；之后 1,700 万英镑、31 个月合同，研究海外常设联合作战基地防护，Lattice 为指挥层 | 日期约 2023 年，未核实 | 公司+调查媒体 ([Anduril](https://www.anduril.com/news/anduril-industries-awarded-gbp17-million-ministry-of-defence-force-protection-technology); [TBIJ](https://www.thebureauinvestigates.com/stories/2025-07-23/selling-weapons-to-westminster-how-defence-giant-anduril-trained-its-sights-on-the-uk)) |
| 4 | 2022-01 | SOCOM | 美国本土内外 | 反无人系统集成：Sentry + Anvil + Lattice，自主检测、分类、跟踪，并提供处置选项 | 上限 9.676 亿美元，至 2032 年 | 合同事实 ([AFCEA](https://www.afcea.org/signal-media/contracting/socom-selects-anduril-integration-partner-967-million-counter-unmanned)) |
| 5 | 2023 | 陆军 EDGE23 | 美国本土 | 单兵规划并操控多型无人机，把防空阵地定为敌对、授权 ALTIUS-600M 打击，系统自动改派 ISR 做 BDA | 演示成功 | 公司博客 ([Anduril](https://blog.anduril.com/anduril-demonstrates-lattice-for-mission-autonomy-controlling-teams-of-autonomous-assets-at-us-f617c489441)) |
| 6 | 约 2024–2025 | CENTCOM Desert Guardian 1.0 | 中东 | Lattice 作为第三方 C2，参演方用 API/SDK 文档集成自家系统，部分实时完成 | 定性描述 | 媒体 ([OCBJ](https://www.ocbj.com/defense-2/anduril-industries-enabling-partners-to-operate-on-lattice/)) |
| 7 | 2024-11 | 陆战队 MADIS | — | 约 2 亿美元反无人机交战系统合同 | — | 行业媒体 ([Overt Defense](https://www.overtdefense.com/2025/03/21/anduril-secures-642m-deal-to-deliver-ai-driven-counter-drone-defense-for-us-marine-corps/)) |
| 8 | 2025-03 | 陆战队 I-CsUAS | 各设施 | Lattice C2 + Anvil + Pulsar 设施反小型无人机 | 10 年期，上限 6.42 亿美元，首笔 950 万美元 | 媒体 ([DefenseScoop](https://defensescoop.com/2025/03/13/marine-corps-anduril-contract-defend-installations-small-uas-drones/)) |
| 9 | 2025 | 英国陆军 Project Asgard | 英国 | 演示边缘数据网格，把前线数据送到司令部 | 演示 | 媒体 ([Defence Industry EU](https://defence-industry.eu/anduril-uk-demonstrates-edge-data-mesh-capability-for-british-army-on-project-asgard/)) |
| 10 | 2025-03-05 | DIU Thunderforge | INDOPACOM/EUCOM | 由 Scale AI 牵头的 AI 战役规划项目，Lattice 提供数据共享层，配合微软和 Scale 的大模型 | 项目启动 | 官方 ([DIU](https://www.diu.mil/latest/dius-thunderforge-project-to-integrate-commercial-ai-powered-decision-making)) |
| 11 | 2025-09 | 陆军第 4 步兵师 Ivy Sting 1 | 卡森堡 | 实弹：AXS 运行于 Lattice Mesh，引导 M777 射击；师级目标处理全程运行在 Lattice Mesh + Target Workbench 上 | 炮组 30 秒内完成数字化准备（陆军/公司说法） | 媒体 ([Breaking Defense](https://breakingdefense.com/2025/10/in-ngc2-first-army-uses-beta-artillery-data-tool-in-howitzer-strike-at-ivy-sting-1/)) |
| 12 | 2025-10 | Falcon Peak 25.2 / NORTHCOM | 埃格林空军基地 | Mobile Sentry 探测跟踪敌方无人机，Anvil 摧毁；整套反无人机套件交付 NORTHCOM | 成功拦截 | 媒体 ([Inside Unmanned Systems](https://insideunmannedsystems.com/anduril-demonstrates-and-delivers-counter-uas-capabilities-to-usnorthcom/)) |
| 13 | 2025-11 | 陆军 IBCS-M | 尤马试验场 | 反无人机下一代火控，数小时内接入新的第三方传感器和效应器 | 实弹 4/4 拦截 | 媒体 ([DefenseScoop](https://defensescoop.com/2025/11/11/army-ibcs-maneuver-anduril-lattice-counter-uas/)) |
| 14 | 2025 末至 2026 初 | 第 4 步兵师 Ivy Sting 4–5 | — | 50 多个用例；数据网格扩大到 3 倍，连接 65 个以上边缘节点；通信降级时在本地网格上完成"电子战定位到火力打击"全流程 | 公司声明 | 公司 ([Anduril](https://www.anduril.com/news/scaling-next-generation-command-and-control-from-prototype-to-fight)) |
| 15 | 2025-09 至 2026-04 | 澳大利亚皇家海军 | 澳大利亚 | Ghost Shark 超大型无人潜航器，自主功能据称由 Lattice 管理（二手） | 17 亿澳元、5 年生产合同；2026-04 交付首批生产艇，成立 MASU 部队（比原定 1 月推迟） | 官方 ([澳国防部长](https://www.minister.defence.gov.au/media-releases/2025-09-10/equipping-royal-australian-navy-next-generation-autonomous-undersea-vehicles)) |
| 16 | 2025-05（或 2024，存在冲突） | 美国海军 | 加州近海 | 十余艘 Lattice C2 控制的无人艇演习中停机，水兵警告存在安全风险 | **失败** | WSJ 转述 ([Sherwood News](https://sherwood.news/tech/wsj-andurils-weapons-systems-have-failed-during-several-tests/)) |
| 17 | 2022–2024 | 乌克兰 | 乌克兰 | Ghost 侦察无人机和 Altius 巡飞弹 | **受干扰失效，Altius 于 2024 年停用** | WSJ 转述 ([TechCrunch](https://techcrunch.com/2025/11/27/andurils-autonomous-weapons-stumble-in-tests-and-combat-wsj-reports)) |
| 18 | 2026-03 | 陆军 JIATF 401 | 全军 | "通用反无人 C2"，用 Lattice 连接多种反无人机系统 | 首个任务单 8,770 万美元（另记 8,700 万） | 媒体 ([Breaking Defense](https://breakingdefense.com/2026/03/army-awards-anduril-counter-drone-task-order-as-first-in-new-20b-contract-vehicle/)) |
| 19 | 2026 | 史诗怒火行动 | 中东 | Anduril 总裁称公司是对抗"沙希德"无人机的"主要"系统，但拒绝说明具体系统 | 无独立证实 | 公司 ([AOL](https://www.aol.com/articles/andurils-president-says-firm-heavy-040829085.html)) |
| 20 | 2026-05 | 第 4 步兵师 Ivy Mass | — | 整师在 NGC2 上运行，是 Project Convergence 顶点演习 6 前的最后一次活动 | 2,500 余台终端；火力时间缩短 90%（公司口径） | 公司/媒体 ([MilitaryLeak](https://militaryleak.com/2026/05/26/how-team-anduril-and-us-army-took-lattice-across-the-4th-infantry-division/)) |
| 21 | 2026-06-05 | 科威特（拟议军售） | 科威特 | Roadrunner-M、Anvil-Kinetic 与 Lattice | 获批 19.8 亿美元，**只是批准，不等于交付** | DSCA 通知转述 ([Army Recognition](https://www.armyrecognition.com/news/army-news/2026/u-s-approves-1-98b-anduril-counter-drone-system-for-kuwait-to-defend-against-drone-swarm-attacks)) |
| 22 | 2026 | Varda、LeoLabs、Anduril | 太空 | 跟踪 Varda 返回舱轨道机动，数据实时输入 Lattice | 演示 | 媒体 ([ExecutiveBiz](https://www.executivebiz.com/articles/varda-leolabs-anduril-hypersonic-reentry-demo)) |
| 23 | 约 2026-08 | Valiant Shield 2026 | 关岛 | 基于 Lattice 的关岛防御作战管理器，融合陆、空、海军和 MDA 资产 | 截至 9 月未见后续合同 | 二手，需核实 ([Venture Atlas](https://www.ventureatlas.org/company/anduril)) |
| 24 | 2026-10-01 | ORIGIN 公司 | — | BLAZE 拦截器集成进 Lattice | 第三方效应器接入 | 行业媒体 ([Overt Defense](https://www.overtdefense.com/2026/10/01/anduril-and-origin-integrated-origins-blaze-interceptor-with-andurils-lattice-software-for-drone-defense/)) |

---

## 二、Maven：从无人机视频识别到全军"目标工厂"与"万能应用"

### 2.1 前世今生：先是政府项目，后成 Palantir 平台

理解 Maven，首先要分清**三个容易混用的名字**。**Project Maven** 是 2017 年成立的"算法战跨职能小组"（AWCFT，Algorithmic Warfare Cross-Functional Team），是政府项目。**NGA Maven** 是 2022 年起由国家地理空间情报局（NGA）接管的地理空间情报（GEOINT）AI 模型流水线，2023 年成为采购项目。**Maven Smart System（MSS）** 是以 Palantir 软件为主体、面向指挥控制和目标定位的作战平台，2026 年起由 CDAO（首席数字与人工智能办公室）管理。北约专门强调，MSS NATO "不应与 NGA Maven 作战支援系统相混淆" ([SHAPE](https://shape.nato.int/news-archive/2025/nato-acquires-aienabled-warfighting-system.aspx))。

Project Maven 的初衷很窄，目标却很大。2017-04-26，常务副部长 Robert Work 签发备忘录，成立 AWCFT，以"加速国防部整合大数据和机器学习" ([NSArchive 备忘录扫描件](https://nsarchive.gwu.edu/sites/default/files/documents/4164306/Department-of-Defense-Establishment-of.pdf))。首个任务是对战术和中空无人机全动态视频（FMV）做处理、利用和分发（PED），服务于打击 ISIS ([GlobalSecurity](https://www.globalsecurity.org/intell/systems/maven.htm))。Jack Shanahan 中将负责总体指导，陆战队上校 Drew Cukor 负责日常运作。成立约两个月后，国会拨款约 7,000 万美元；**2017 年 12 月，首个 ScanEagle 视频目标识别算法部署到中东**，从立项到上线只用了约 8 个月 ([Nextgov](https://www.nextgov.com/artificial-intelligence/2017/12/pentagons-new-artificial-intelligence-already-hunting-terrorists/144769/))。Maven 本质上是一个"探路者"：一支小而快的团队，用来证明国防部可以在几个月内把商业 AI 用上战场。正因如此，它后来能从 FMV 识别扩展到数据融合和 C2。

2018 年的谷歌员工抗议是 Maven 早期最著名的事件。谷歌通过主承包商 ECS Federal 参与，份额据报约 900 万美元。约 4,000 名员工（另有 4,600、近 5,000 的说法）签名反对，约 12–13 人辞职。2018 年 6 月 1 日前后，谷歌云 CEO Diane Greene 宣布合同到 2019 年 3 月期满后不再续签 ([NBC News](https://www.nbcnews.com/news/military/google-halt-controversial-project-aiding-pentagon-drones-n879471); [Gizmodo AU](https://www.gizmodo.com.au/2018/05/google-employees-resign-in-protest-against-pentagon-contract/))。项目并没有因此放慢：ECS 自 2017 年起陆续持有 3 份与 Maven 相关、总额 3.64 亿美元的合同，Clarifai、微软（约 3,000 万美元）、AWS（约 2,000 万美元）获得分包，后来 Palantir 接手了平台层。不过微软和 AWS 的分包合同并未直接点名 Maven，二者与 Maven 的关联是 Tech Inquiry 的推断 ([ITPro](https://itpro.com/business-strategy/public-sector/360824/amazon-microsoft-google-project-maven-dod-contracts))。

**表 2-1　Maven 演进年表（2017–2026.10）**

| 日期 | 事件 | 来源 |
|---|---|---|
| 2017-04-26 | Work 备忘录成立 AWCFT（Project Maven），首个任务是无人机 FMV 的处理、利用和分发 | [NSArchive](https://nsarchive.gwu.edu/sites/default/files/documents/4164306/Department-of-Defense-Establishment-of.pdf) |
| 2017 年中 | 成立约两个月内获国会约 7,000 万美元 | [Wikipedia](https://en.wikipedia.org/wiki/Project_Maven) |
| 2017-12 | 首个算法（ScanEagle FMV 物体识别）部署到中东，AFRICOM 也同期开始使用 | [Nextgov](https://www.nextgov.com/artificial-intelligence/2017/12/pentagons-new-artificial-intelligence-already-hunting-terrorists/144769/); [Breaking Defense](https://breakingdefense.com/2018/05/pentagons-big-ai-program-maven-already-hunts-data-in-middle-east-africa/) |
| 2018-03 至 06 | 谷歌员工抗议；6 月 1 日前后宣布不续约 | [NBC News](https://www.nbcnews.com/news/military/google-halt-controversial-project-aiding-pentagon-drones-n879471) |
| 2018-12 | Shanahan 调任首任 JAIC（联合人工智能中心）主任 | [Wikipedia](https://en.wikipedia.org/wiki/Project_Maven) |
| 2020 起 | XVIII 空降军通过 Scarlet Dragon 系列演习，与多达 70 家公司把 Maven 发展为 MSS | [Defense One](https://www.defenseone.com/technology/2024/08/dod-getting-better-buying-tech-reports-say/398821/) |
| 2022 起 | MSS 支援乌克兰：XVIII 空降军生成目标情报并分享给乌军 | [Lawfare](https://www.lawfaremedia.org/article/how-the-u.s.-military-learned-to-embrace-ai-warfare) |
| 2022-04 / FY2023 | 拆分：GEOINT AI（约占原项目 80%）交给 NGA，非 GEOINT 部分交给 CDAO；2022 年 10 月因持续决议案而推迟 | [Breaking Defense](https://breakingdefense.com/2022/04/pentagons-flagship-ai-effort-project-maven-moves-to-nga/); [DefenseScoop](https://defensescoop.com/2022/10/07/pentagon-remains-mum-on-project-maven-as-transition-is-held-up-by-continuing-resolution/) |
| 2023-11-07 | "NGA Maven"成为采购项目（软件采购路径） | [Defense Daily](https://defensedaily.com/project-maven-transitions-to-program-of-record-as-nga-looks-to-leverage-program-for-other-uses/intelligence-community) |
| 2023-12 / 2024-02 | CJADC2 最小可行能力（MVC）经 GIDE 实验认证并公布，MSS 被视为其事实骨干 | [DefenseScoop](https://defensescoop.com/2024/02/26/dod-cdao-ai-cjadc2-minimum-viable-capability/) |
| 2024-02-02 | CENTCOM 在伊拉克、叙利亚 85 次以上打击中用 Maven 缩小目标范围 | [The Register](https://www.theregister.com/2024/02/27/us_military_maven_ai_used/) |
| 2024-03 | FY2025 预算把 Maven 经费调整到 CDAO 项目元素 PE 0606135D8Z；整个"AI 开发流水线"交给 NGA | [DefenseScoop](https://defensescoop.com/2024/03/14/project-maven-fiscal-2025-budget-still-evolving/) |
| 2024-05-29 | 陆军授予 Palantir 4.8 亿美元、5 年期 MSS 原型 IDIQ，覆盖 CENTCOM、EUCOM、INDOPACOM、NORTHCOM、TRANSCOM 和联合参谋部 | [DefenseScoop](https://defensescoop.com/2024/05/29/palantir-480-million-army-contract-maven-smart-system-artificial-intelligence) |
| 2024 年末 | 据报道 Anthropic Claude 经 Palantir 接入 Maven | [Arms Control Association](https://www.armscontrol.org/act/2026-05/news/ai-plays-major-role-war-iran) |
| 2025-03-25 / 04-14 | 北约 NCIA 采购 MSS NATO，从提出需求到签约约 6 个月 | [NCIA](https://www.ncia.nato.int/newsroom/news/nato-acquires-aienabled-warfighting-system) |
| 2025-05 | NGA 局长 Whitworth：活跃用户超过 2 万，35 个以上工具，3 个安全域；国防部把 MSS 合同上限提高 7.95 亿美元，至约 13 亿美元 | [Breaking Defense](https://breakingdefense.com/2025/05/ai-unchained-ngas-maven-tool-significantly-decreasing-time-to-targeting-agency-chief-says/); [DefenseScoop](https://defensescoop.com/2025/05/23/dod-palantir-maven-smart-system-contract-increase/) |
| 2025-07-31（或 8 月） | 陆军与 Palantir 签订 10 年期企业协议（EA），上限 100 亿美元，合并 75 份合同 | [DefenseScoop](https://defensescoop.com/2025/07/31/army-palantir-software-enterprise-agreement-10-billion/) |
| 2025-09 | 陆战队把 MSS 定为标准"火力与效果集成平台"，在 SIPRNet IL6 云上无限制访问 | [DefenseScoop](https://defensescoop.com/2025/09/12/marine-corps-maradmin-maven-smart-system-mss-palantir-rollout/) |
| 2025-11 | Enabled Intelligence 赢得 NGA 7.08 亿美元数据标注合同（SEQUOIA） | [Breaking Defense](https://breakingdefense.com/2025/11/startup-enabled-intelligence-nabs-ngas-708-million-ai-training-contract/) |
| 2026-02-28 起 | 史诗怒火行动（对伊朗），MSS 被大规模用于目标定位；同日发生 Minab 学校遇袭 | [Arms Control Association](https://www.armscontrol.org/act/2026-05/news/ai-plays-major-role-war-iran) |
| 2026-03-04 | 据报道国防部把 Anthropic 列为供应链风险，要求 6 个月内淘汰 | 同上 |
| 2026-03-09 | **Feinberg 备忘录**：本财年底前转为采购项目；30 天内管理权从 NGA 移交 CDAO MSS 项目办公室；所有合同并入陆军 EA；R&E 接任授权官 | [DefenseScoop](https://defensescoop.com/2026/04/03/palantir-maven-feinberg-directive/) |
| 2026-03 | Katrina Manson 出版《Project Maven》一书 | [NPR](https://www.npr.org/2026/03/23/nx-s1-5757478/inside-a-secret-pentagon-effort-to-bring-ai-to-the-battlefield) |
| 2026-05-28 | FY2027 预算申请：超过 15 亿美元扩大 MSS 访问；"MSS + 联合火力网"合计 23 亿美元 | [DefenseScoop](https://defensescoop.com/2026/05/28/dod-fy27-budget-cjadc2-maven-smart-system-palantir/); [FY2027 预算概览](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2027/FY2027_Budget_Request_Overview_Book.pdf) |
| 2026-06-22 | MSS NATO 达到全面作战能力（FOC），在北约机密网络、北约自有数据中心运行 | [SHAPE](https://shape.nato.int/news-releases/Maven-System-achieves-full-capability) |
| 2026-08-05 | 陆军上校 Molly（Melissa）Solsbury 任 CDAO 内 MSS 项目主任 | [DefenseScoop](https://defensescoop.com/2026/08/05/pentagon-appoints-new-maven-smart-system-program-director/) |
| 2026-09-22 | 用户数从 1 月约 5 万增至 10 万以上；CDAO Stanley 称 38 天打击 13,000 个目标 | [DefenseScoop](https://defensescoop.com/2026/09/22/maven-smart-system-ai-james-mazol-cameron-stanley-defensetalks/) |
| 2026-09-30 | 转为采购项目的截止日；**截至本报告未见官方确认完成** | — |

Palantir 成为 MSS 主承包商的路径是一步步加深锁定的：先作为在位原型开发商（约 2022–2024 年，"只面向有限数量的操作员"），然后获得国防部的唯一供应商认证 ([Jack Poulson](https://jackpoulson.substack.com/p/pentagon-certified-palantir-as-only))，再拿到 4.8 亿美元 IDIQ、上限提至约 13 亿美元，最后在 2026 年 3 月备忘录下把所有 MSS 合同并入陆军 EA。治理权的变化路线是：OUSD(I)（国防部负责情报的副部长办公室）下的探路项目（2017–2022）→ FY2023 拆分（NGA 负责模型流水线，MSS 由 NGA 代管、陆军负责签约）→ 2026 年 3 月起集中到 CDAO MSS 项目办公室。JAIC 从来不是 Maven 的主管单位，它只是带走了 Maven 的首任负责人，二者后来一同并入 CDAO。

### 2.2 功能设计：多源融合、看板式目标工作流与大模型代理

MSS 是一个"传感器到射手"的决策支持平台。北约对它的官方描述是"AI 赋能的作战系统"：用大语言模型、生成式 AI 和机器学习做情报融合、目标定位、战场感知、作战计划和加速决策；把涉密和公开、结构化和非结构化的多源数据汇入统一、可搜索的平台；开放架构可接入第三方 AI 模型、仿真工具和应用 ([SHAPE](https://shape.nato.int/news-releases/nato-acquires-aienabled-warfighting-system-))。

**表 2-2　MSS / NGA Maven 功能模块拆解**

| 模块 | 功能描述 | 证据等级与来源 |
|---|---|---|
| 多源情报融合 | CENTCOM 2024 年部署时接入 **179 个数据源**（另有 150 个以上的说法），包括国家侦察卫星、商业 SAR（ICEYE、Capella Space）和信号情报（截获通信、电子辐射） | 智库 ([CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do))；二手 ([GlobalSecurity](https://www.globalsecurity.org/intell/systems/maven.htm)) |
| 计算机视觉检测与"对象化" | 外部 AI 模型的检测结果作为对象写入本体。北约演示中，Safran.AI 生成的 12,000 个检测对象组成一个对象集，可以在 COP 中直接查看，也可以交给 AIP 代理使用 | 厂商 ([Palantir Blog](https://blog.palantir.com/maven-smart-system-innovating-for-the-alliance-5ebc31709eea)) |
| 共用作战图（COP） | 地图式 COP，有描述称是三维地球视图，叠加卫星、无人机、SIGINT 和地图数据；无人机位置和视频实时回传 | 二手 ([spatialintelligence.ai](https://www.spatialintelligence.ai/p/inside-palantirs-maven-smart-system)) |
| Target Workbench（目标工作台） | **看板（Kanban）式**界面，各列对应目标定位各阶段，阶段名可按单位流程定制；集成**禁打清单（NSL，No-Strike List）** | 厂商 ([Palantir Target Workbench PDF](https://www.palantir.com/assets/xrfr7uokpv1b/1IqzwzpemtBSm98TNCczao/49bbc30cbec4d2d4d189ab27bd07376c/Palantir_Target_Workbench___1_.pdf)) |
| 资产配对（武器-目标配对） | 操作员选中 AI 检测的目标，按到达时间、距离、燃油等约束比较附近的打击资产，下令打击，再用 ISR 跟踪效果 | 智库，依据国防部演示 ([CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do)) |
| 火力交接 | 排序后的目标交给 AFATDS（先进野战炮兵战术数据系统）等火力系统；射击诸元仍由 AFATDS 和弹道计算完成，大模型在这一环几乎不起作用 | 二手 ([battlepolicy](https://www.battlepolicy.com/maven-smart-system/))；分析者 ([Ben Van Roo](https://benvanroo.substack.com/p/measuring-the-machines-that-kill)) |
| 毁伤评估（BDA） | 通过 ISR 跟踪打击效果；没有找到模块级的权威描述 | 智库 ([CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do)) |
| AIP 代理与大模型 | 自然语言查询（如"Show me detections of Tu-22s"）；据报道 Claude 用于目标排序、生成坐标、推荐武器，WaPo 还称其生成法律依据草稿（二手转述）；也有说法称主要用途只是把情报报告转成通俗语言 | 多源但有争议 ([WaPo](https://www.washingtonpost.com/technology/2026/03/04/anthropic-ai-iran-campaign/); [Vision of Humanity](https://www.visionofhumanity.org/how-ai-is-rewriting-the-rules-of-modern-warfare/)) |
| NGA 机器生成情报 | 所有 AI 产品加注"machine-generated GEOINT"标签，注明 AI 参与类型和程度，模板化产品分发时"无人工经手"；下一阶段加入"推理"能力，从识别物体走向预测威胁，向作战司令或总统汇报前仍需人工佐证 | 官方 ([Breaking Defense](https://breakingdefense.com/2025/06/no-human-hands-nga-circulates-ai-generated-intel-director-says/); [MeriTalk](https://www.meritalk.com/articles/nga-expands-maven-ai-system-in-year-of-ai-whitworth-says/)) |
| 非作战扩展 | 2026 年扩展到后勤、供应链、战备和预算数据，被称为五角大楼的"万能应用"（everything app），取代了"6、8、10 个"旧系统 | 官员 ([Defense One](https://www.defenseone.com/technology/2026/09/maven-becoming-pentagons-everything-app/415882/)) |

CSIS 提醒，Palantir 2023 年"AIP for Defense"演示展示的是计划中的未来能力和示意场景，**不能等同于已部署的功能** ([CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do))。功能层面仍不透明的部分包括：FMV 接入方式、友军跟踪（BFT）接入、BDA 实现、COA（行动方案）生成算法和武器-目标配对算法，以及联盟"可释放性"（releasability）的访问控制机制，都没有权威公开描述。可以确定的是，MSS 的"武器-目标配对"更像基于约束（时间、距离、燃油、弹药）的资产推荐与比较，最终的火力分配仍走存量火控系统。

### 2.3 架构设计：本体驱动的平台、NGA 模型流水线和三个安全域

MSS 的架构可以理解为**"Palantir 平台 + 可插拔的模型和数据"**。Palantir 控制集成层和工作流层，NGA 控制模型的标注、训练和认证，第三方的计算机视觉、SAR 和大模型供应商可以替换。2026 年有报道称 Anthropic 被 OpenAI 等公司替代，说明大模型层确实可替换 ([ACA](https://www.armscontrol.org/act/2026-05/news/ai-plays-major-role-war-iran))。

**表 2-3　Maven 分层架构**

| 层 | 组成与机制 | 证据 |
|---|---|---|
| ① 数据源层 | 国家和商业卫星（含 SAR）、无人机、SIGINT、既有数据库等 179 个以上来源 | [CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do) |
| ② NGA Maven 模型流水线 | **数据标注**：Scale AI 约 2,400 万美元的一年期过渡合同，之后是 Enabled Intelligence 最高 7.08 亿美元、最长 7 年的 SEQUOIA（美国政府迄今最大的 AI 数据标注项目）；**集成**：ECS 自 2017 年起任"AI 互操作集成商"（AI3）；**模型认证**：NGA 的 AGAIM 试点提供标准化评估和风险管理，官方明确不希望它变成"ATO 式"的排队审批 | [NGA](https://www.nga.mil/news/Contract_Announcements.html); [Breaking Defense](https://breakingdefense.com/2025/11/startup-enabled-intelligence-nabs-ngas-708-million-ai-training-contract/); [ExecutiveBiz](https://www.executivebiz.com/articles/ecs-john-heneghan-nga-maven-program); [Federal News Network](https://federalnewsnetwork.com/intelligence-community/2025/09/ngas-ai-standards-work-aims-to-avoid-ato-like-process/) |
| ③ 平台层 | **Apollo**：持续交付平台，管理承载 Foundry 和 AIP 的底层基础设施，可跨本地、边缘和涉密网络运行；**Ontology（本体）**：把数据源映射为对象、属性和链接，并对"动作"（action）建模，决策可实时写回运营系统和边缘系统，边缘端可用轻量"嵌入式本体"。（MSS 基于 Foundry 还是 Gotham 的具体组合，属于分析推断） | [Palantir Docs](https://www.palantir.com/docs/foundry/architecture-center/platforms); [Ontology Overview](https://www.palantir.com/docs/foundry/ontology/overview) |
| ④ 工作流应用层 | COP 地图、Target Workbench 看板、资产比较、BDA 跟踪；开放架构，Open DAGIR 计划（2024）把其他厂商的应用接到 MSS 数据层上 | [Breaking Defense](https://breakingdefense.com/2024/05/open-dagir-dod-plans-july-industry-day-experiments-for-new-cjadc2-command-apps/) |
| ⑤ AIP/大模型代理层 | 自然语言检索、排序、COA 草案；Claude（存在争议），OpenAI 等据报为接替者 | [Palantir Blog](https://blog.palantir.com/maven-smart-system-innovating-for-the-alliance-5ebc31709eea) |
| ⑥ 部署与安全域 | NGA 称跨"3 个安全域"运行（推测为非密、秘密、TS/SCI，但无公开来源证实 JWICS 上有实例）；陆战队通过 **SIPRNet IL6 云**访问；MSS NATO 在北约机密网络和北约自有数据中心运行；托管在哪家云厂商没有公开信息 | [Breaking Defense](https://breakingdefense.com/2025/05/ai-unchained-ngas-maven-tool-significantly-decreasing-time-to-targeting-agency-chief-says/); [USMC](https://www.marines.mil/News/Press-Releases/Press-Release-Display/Article/4305728/marine-corps-partners-with-chief-digital-and-artificial-intelligence-office-and/); [SHAPE](https://shape.nato.int/news-releases/Maven-System-achieves-full-capability) |
| ⑦ 治理与合同层 | CDAO MSS 项目办公室（2026 起，CDAO 隶属 USD(R&E)）；合同经陆军 EA；R&E 任商业云授权官；CTO Emil Michael 负责评估是否把 MSS 放进拟设的 CJADC2 项目办公室 | [DefenseScoop](https://defensescoop.com/2026/04/15/palantir-maven-smart-system-pentagon-program-transition-feinberg/) |

两种数据模型可以对照来看。Palantir 本体以"对象—属性—链接—动作"为核心，面向企业级的长周期数据整合和决策回写。Lattice 实体以"实体—组件—任务"为核心，面向实时航迹和对效应器的控制。两者在 NGC2 中如何映射（例如实体与对象之间的转换），**没有公开文档**。另一个已知风险是 Maven 的数据投毒问题，CSET 明确表示不公开 MSS 的具体作战细节 ([CSET](https://cset.georgetown.edu/wp-content/uploads/CSET-Building-the-Tech-Coalition-1.pdf))。

### 2.4 能力评估：已证实的是"省人、提速"，不是"更准"

MSS 公开的指标可以分为五类，彼此**不能直接比较**。**吞吐**：资深目标官 Temple 估计，用 Maven 每小时可签批多达 80 个目标，不用时约 30 个 ([Bloomberg](https://www.bloomberg.com/features/2024-ai-warfare-project-maven/))。**人力**：XVIII 空降军约 20 人的目标单元达到了 2003 年伊拉克战争中 2,000 多人时敏目标单元的效能 ([CSET](https://cset.georgetown.edu/wp-content/uploads/CSET-Building-the-Tech-Coalition-1.pdf))。**识别准确率**：测试中 Maven 识别物体的正确率约 60%，人类分析员约 84%；遇到雪天图像或西伊拉克那种天气多变的沙漠地形，可降到 30% 以下 ([The Batch](https://www.deeplearning.ai/the-batch/maven-a-system-that-analyzes-satellite-data-to-identify-targets-in-real-world-conflicts); [Airwars](https://airwars.org/the-first-civilian-confirmed-killed-in-an-ai-assisted-strike/))。**时延**：Scarlet Dragon 中，"数据传输加打击"从 12 小时以上缩短到 1 分钟以内（二手）([Army Recognition](https://armyrecognition.com/news/army-news/army-news-2024/us-army-explores-an-ai-system-capable-of-targeting-1-000-objectives-per-hour-2))；Stanley 在国会证词中称目标周期"从数天压缩到数秒" ([国会证词](https://www.congress.gov/119/meeting/house/119184/witnesses/HHRG-119-AS35-Wstate-StanleyC-20260514.pdf))。**愿景**：陆军希望达到"每小时 1,000 个高质量决策"，这是目标，不是实测 ([Breaking Defense](https://breakingdefense.com/2025/05/ai-unchained-ngas-maven-tool-significantly-decreasing-time-to-targeting-agency-chief-says/))。

**表 2-4　Maven 能力：已证实、声称与争议**

| 维度 | 已证实（多源/官方） | 声称或未验证 | 反证或争议 |
|---|---|---|---|
| 规模化目标工作流 | 史诗怒火行动中被大规模使用；38 天 13,000 个目标（官方总量）；用户超过 10 万 | "从数天到数秒" | 13,000 统计的是"打击的目标"，不是 Maven 独立识别的目标，也不是命中率 |
| 多源融合与联盟共享 | 覆盖全部 COCOM、陆战队、国民警卫队局；北约 FOC | 179 个以上数据源（智库转述） | 乌克兰效果"好坏参半"，难以把"21 世纪的数据送进 19 世纪的战壕" ([Kyiv Independent 转述 NYT](https://kyivindependent.com/nyt-project-maven-ai-having-mixed-results-on-ukraines-battlefields/)) |
| 目标识别准确性 | 60% 对 84%（2023–24 年测试） | 2026 版（含大模型）无公开准确率数据 | 雪天或沙漠天气下低于 30%；"每平方公里 10 个误检"等二手数字无原始出处，不宜引用 |
| 大模型赋能 | 战事期间按 token 计的日峰值增长 4,425%，最高约 200 亿 token/天；非密网使用量环比增长 38%，涉密网增长 89% ([Breaking Defense](https://breakingdefense.com/2026/05/insatiable-appetite-for-ai-maven-usage-surged-for-strikes-on-iran-pentagon-ai-chief-says/)) | Claude 生成坐标、推荐武器、起草法律依据 | Claude 已被禁用还是仍在运行，说法相互矛盾 |
| 人在回路 | CENTCOM 称"每一步都以人工验证结束"；司令称最终打击决定由人作出 | 定位为"决策支持" | 批评者称已退化为"附带人类副署以满足法律合规的决策系统" ([Strategy International](https://strategyinternational.org/2026/04/06/publication258/))；Minab 案 |

政策层面，DoDD 3000.09（2012 年发布，2023 年更新）要求自主和半自主武器系统让指挥官施加"适当程度的人类判断" ([GAO-22-104765](https://www.gao.gov/assets/gao-22-104765.pdf))。但 MSS 本身不发射武器，更接近"目标选择支持系统"，因此 3000.09 规定的高级审查未必直接适用，问责主要依靠交战规则、联合目标定位流程（JP 3-60）中的人工签批和法律审查（分析推断）。没有找到针对 MSS 的正式"负责任 AI"评估或 3000.09 审查记录。Lawfare 书评指出，Maven 预算属于机密，且不适用《信息自由法》（FOIA）([Lawfare](https://www.lawfaremedia.org/article/how-the-u.s.-military-learned-to-embrace-ai-warfare))。商业层面，Palantir 2026 年二季度营收约 19.4 亿美元，同比增长 93%，管理层称"首个采购项目本季度在平台上启动" ([CNBC](https://www.cnbc.com/2026/08/03/palantir-pltr-earnings-q2-2026.html))。"Maven 年化经常性收入接近 10 亿美元"只有单一低可信来源。

### 2.5 案例目录：从反 ISIS 视频识别到伊朗战役

**表 2-5　Maven 主要案例**

| # | 日期 | 用户/单位 | 地点 | Maven 做了什么 | 结果/数据 | 可信度与来源 |
|---|---|---|---|---|---|---|
| 1 | 2017-12 | SOCOM 情报分析员 | 中东（反 ISIS） | 在 ScanEagle FMV 中识别物体，Shanahan 称之为"原型战" | 初始部署，无性能数据 | 官方/媒体 ([Nextgov](https://www.nextgov.com/artificial-intelligence/2017/12/pentagons-new-artificial-intelligence-already-hunting-terrorists/144769/)) |
| 2 | 2017-12 至 2018-05 | AFRICOM 及多个中东地点 | 非洲、中东 | 扩展部署 | 官员称自 2017-12 起使用 | 媒体 ([Breaking Defense](https://breakingdefense.com/2018/05/pentagons-big-ai-program-maven-already-hunts-data-in-middle-east-africa/)) |
| 3 | 早期测试 | 海豹突击队无人机视频 | 索马里 | 用实拍视频测试多家供应商的识别工具 | — | 媒体 ([Bloomberg](https://www.bloomberg.com/features/2024-ai-warfare-project-maven/)) |
| 4 | 2020 起（年度） | XVIII 空降军 Scarlet Dragon | 美国本土 | 整合传感器、目标识别和火力分配，孵化出 MSS；GAO 称其为使用 Maven 数据的陆军目标识别能力 | 20 人顶 2,000 人；每小时 30 → 80 个目标 | 智库/GAO ([CSET](https://cset.georgetown.edu/wp-content/uploads/CSET-Building-the-Tech-Coalition-1.pdf); [GAO](https://www.gao.gov/assets/gao-22-104765.pdf)) |
| 5 | 2022 起 | XVIII 空降军（前沿部署欧洲） | 乌克兰 | 生成目标情报分享给乌军，乌方使用不依赖美国敏感情报的版本 | Manson 书称发送了"数以万计"的目标；NYT 称"好坏参半"：打击俄军炮兵更有效，但没能把战场图像送到前线士兵手里 | 书、NYT ([Willis Strategy](https://willis-strategy.com/insights/review-project-maven.html); [Kyiv Independent](https://kyivindependent.com/nyt-project-maven-ai-having-mixed-results-on-ukraines-battlefields/)) |
| 6 | 2024-02-02 | CENTCOM | 伊拉克、叙利亚 | 机器学习目标识别"缩小目标范围"，起因是约旦 Tower 22 遇袭致 3 名美军死亡 | 参与 85 次以上打击（7 处设施）；CTO Schuyler Moore 称每一步都以人工验证结束 | 官方 ([The Register](https://www.theregister.com/2024/02/27/us_military_maven_ai_used/)) |
| 7 | 2024 | CENTCOM | 也门、红海 | 定位火箭发射器和水面船只 | 无数量 | 官方 ([Bloomberg](https://www.bloomberg.com/features/2024-ai-warfare-project-maven/)) |
| 8 | 2024-05 起 | 5 个 COCOM 与联合参谋部 | 全球 | MSS 原型推广到"数千用户" | 4.8 亿美元 IDIQ | 官方 ([DefenseScoop](https://defensescoop.com/2024/05/29/palantir-480-million-army-contract-maven-smart-system-artificial-intelligence)) |
| 9 | 2025-04 至 2026-06 | 北约 ACO（SHAPE、JFC Brunssum、JFC Norfolk） | 欧洲 | 情报融合、目标定位、战场感知和规划；经 Steadfast Deterrence 2026 演习检验 | 6 个月完成采购；2026-06-22 达到 FOC | 官方 ([SHAPE](https://shape.nato.int/news-releases/Maven-System-achieves-full-capability); [Janes](https://www.janes.com/osint-insights/defence-news/security/natos-jfc-norfolk-to-receive-palantirs-maven-smart-system-by-end-of-may)) |
| 10 | 2025-09 | 美国海军陆战队 | 全军 | 定为跨 COCOM 的标准火力与效果集成平台 | IL6 企业许可 | 官方 ([DefenseScoop](https://defensescoop.com/2025/09/12/marine-corps-maradmin-maven-smart-system-mss-palantir-rollout/)) |
| 11 | 2026-01-03 | 美军抓捕马杜罗行动 | 委内瑞拉 | WSJ 称 Claude 经 Palantir 平台参与，**没有来源确认用的是 Maven** | 机密 | 媒体（匿名信源）([Small Wars Journal](https://smallwarsjournal.com/2026/02/17/ai-enabled-decapitation-strike-maduro-raid/)) |
| 12 | 2026-02-28 起 | CENTCOM 史诗怒火行动 | 伊朗 | 目标排序、生成坐标、推荐武器 | 头 24 小时约 1,000 个目标（WaPo）；至 3-3 近 2,000 个（CENTCOM）；38 天 13,000 个（CDAO）；白宫 4-8 统计其中指挥控制目标超过 2,000 个、防空目标 1,500 个 | 官方数字+媒体 ([Breaking Defense](https://breakingdefense.com/2026/05/insatiable-appetite-for-ai-maven-usage-surged-for-strikes-on-iran-pentagon-ai-chief-says/); [defence-industry.eu](https://defence-industry.eu/operation-epic-fury-u-s-forces-strike-over-13000-targets-in-38-days/)) |
| 13 | 2026-02-28 | CENTCOM | 伊朗 Minab | **事故**：学校在旧数据库中仍标为伊斯兰革命卫队设施，被 Maven 列为"第一天推荐目标"后遭打击 | 死亡人数说法不一（见第四章）；据报道五角大楼内部调查称是"一连串可预防的失败" | 媒体（匿名官员），有争议 ([Bloomberg](https://www.bloomberg.com/graphics/2026-iran-school-attack/); [Gizmodo](https://gizmodo.com/pentagon-investigators-say-overreliance-on-palantir-ai-tech-contributed-to-u-s-strike-that-killed-123-iranian-children-2000814477)) |
| 14 | 2026 | 陆军联合兵种司令部 | 训练体系 | 把"Maven C2 智能系统"纳入训练和院校教育 | — | 官方 ([army.mil](https://www.army.mil/article/290958/armys_combined_arms_command_to_integrate_maven_c2_smart_system_into_training_and_education)) |
| 15 | 2026-09 | 全军 | 全球 | 推广到全部 COCOM 和国民警卫队局，扩展到后勤和预算 | 用户超过 10 万 | 官方 ([DefenseScoop](https://defensescoop.com/2026/09/22/maven-smart-system-ai-james-mazol-cameron-stanley-defensetalks/)) |

Minab 案是 AI 辅助目标定位中"自动化偏见"最具体的公开例证，需要单独说明。据 Bloomberg 引述的五角大楼内部调查：卫星图像显示该地点近十年前已改建，2018 年的图像上能看到足球场；CENTCOM 的平民伤害评估团队从约 10 人减到 1 人；部分用户误以为 Maven 会自动发现过期记录 ([Bloomberg](https://www.bloomberg.com/graphics/2026-iran-school-attack/))。Palantir 称自己"不对底层数据负责"，之后增加了对底层情报中"取消资格因素"的复核 ([Responsible Statecraft](https://responsiblestatecraft.org/ai-palantir-weapons/))。前军官对媒体表示，责任在人而不在 AI ([Military Times](https://www.militarytimes.com/news/your-military/2026/03/24/deadly-iran-school-strike-casts-shadow-over-pentagons-ai-targeting-push/))。也有分析指出，目前没有公开的一手材料能把某个具体的 AI 输出和这次打击直接对应起来 ([Substack 分析](https://brendonbeebe.substack.com/p/the-minab-school-strike-what-we-know))。2026-03-12，120 多名众议院民主党议员致信国防部长 Hegseth。**完整调查报告截至 2026 年 10 月仍未公开**。在 Operation Rough Rider（2025 年打击胡塞）、Midnight Hammer（2025-06 打击伊朗核设施）、Southern Spear（加勒比海打击船只）中，都没有找到 Maven 参与的公开报道。

---

## 三、对比与融合：Palantir 管企业决策，Anduril 管边缘执行

### 3.1 两套系统的本质区别

**表 3-1　Lattice 与 Maven 全维度对比**

| 维度 | Maven Smart System（Palantir） | Lattice（Anduril） |
|---|---|---|
| 出身 | 政府项目（Project Maven，2017），后由 Palantir 商业平台承载 | 企业自研产品（Anduril 2017 年成立），与公司同时诞生 |
| 所有者/主管 | 国防部 CDAO MSS 项目办公室；NGA 负责 GEOINT 模型流水线 | Anduril 拥有知识产权；SDK 许可"开放接口、封闭实现" |
| 第一用例 | 反 ISIS 无人机视频识别 | 美墨边境监视塔 |
| 杀伤链位置 | 发现—定位—目标定位—评估（F2T2EA 前段与末段）；目标提名、工作流、COP | 感知—跟踪—传输—交战（F2T2EA 中后段）；传感器到射手，给自主平台派任务 |
| 指挥层级 | 联合/COCOM/军/师，以及北约 ACO | 战术边缘至师（NGC2），也上探到战区（Thunderforge、金穹、北约 eAirC2） |
| 数据模型 | 本体：对象—属性—链接—动作 | 实体：实体—组件—任务（航迹、资产、地理区域、信号、关注点） |
| 部署形态 | 企业级、云端，3 个安全域，SIPR IL6，北约机密网 | 边缘网格，在坚固套件和车辆（Voyager、Menace）上运行，按 DDIL 设计 |
| AI 角色 | 计算机视觉检测、目标推荐、大模型代理 | 传感器融合、航迹关联、自主行为，并为 AI 训练采集数据 |
| 自主程度 | 决策支持，不直接控制武器 | 直接给效应器下发任务；武器释放由人批准 |
| 合同模式 | IDIQ（上限约 13 亿美元）+ 陆军 EA（上限 100 亿美元）；FY27 申请超过 15 亿美元 | 陆军 EA（上限 200 亿美元，软硬件加服务）；NGC2 上限 18 亿美元 |
| 规模 | 用户超过 10 万（2026-09） | 数百座边境塔；NGC2 2,500 余台终端（公司口径），计划推广到 11 个师 |
| 最大争议 | Minab 误炸与自动化偏见 | 网络安全"极高风险"、电子战下失效、厂商锁定 |

"Maven 负责作战/战略层情报融合与目标定位，Lattice 负责战术边缘的传感器到射手和自主"，这种说法**大体成立，但有例外**：在 NGC2 中，Palantir 的 Foundry 和 Target Workbench 也运行在师一级；在 Thunderforge 和金穹中，Lattice 也进入了战区和联合层级。更准确的划分是：**Palantir 是企业级数据与决策平台，Anduril 是边缘网格与效应器控制层**。

### 3.2 Anduril–Palantir 联盟：一个双边合作，一个"传闻中的财团"

2024 年 12 月有两件事常被混为一谈。**第一件已经证实**：2024-12-06，两家宣布合作"加速国家安全 AI 能力"。机制是由 Lattice 和 Menace 收集、传输来自传感器、车辆、机器人和武器的战场数据，再导入 Palantir AIP，为 AI 训练做准备，覆盖到 SCI/SAP 最高密级；报道还称会把 Lattice、Menace 与 **Maven Smart System** 结合，称之为"从边缘到企业" ([BNN Bloomberg](https://bnnbloomberg.ca/business/technology/2024/12/06/defense-startups-palantir-anduril-to-save-data-from-battlefield-to-train-ai-models); [DefenseScoop](https://defensescoop.com/2024/12/06/palantir-anduril-consortium-ai-new-alliance-merge-capabilities/))。**第二件只是报道**：2024-12-22，FT/路透称两家正与 SpaceX、OpenAI、Scale AI、Saronic 洽谈组建联合投标团体，挑战洛克希德、RTX、波音等传统主承包商 ([TechCrunch](https://techcrunch.com/2024/12/22/palantir-and-anduril-reportedly-building-a-tech-consortium-to-bid-on-defense-contracts/))。此后没有找到任何正式成员名单或章程，L3Harris 也从未出现在相关报道中。所以更准确的描述是"稳定的 Anduril–Palantir 双边组队模式"，而不是一个正式的多公司投标实体。另外，没有找到 Lattice 与 MSS 之间正式 API 集成的公告，2024 年的意向声明和 NGC2 中的实际使用是目前仅有的证据。

### 3.3 陆军 NGC2：两家集成落地最具体的地方

NGC2 是目前**两套系统集成最具体、记录最完整的案例**。2025-07-18，陆军 PEO C3N 授予 Anduril 9,960 万美元 OTA，团队成员包括 Palantir、微软、Striveworks、Govini、Instant Connect Enterprise、Research Innovations ([Defense News](https://www.defensenews.com/land/2025/07/21/anduril-wins-100m-deal-to-build-us-armys-next-gen-c2-ecosystem/))。在 Ivy Sting 1 中，**Lattice Mesh 运行在坚固的 Voyager 边缘套件上，作为数据骨干；Palantir Target Workbench 负责逐个目标的管理、跟踪和资源分配** ([Breaking Defense](https://breakingdefense.com/2025/10/in-ngc2-first-army-uses-beta-artillery-data-tool-in-howitzer-strike-at-ivy-sting-1/))。Ivy Sting 2（2025-10）把范围扩大到火力前的空域管理/冲突消解，以及司令部 C2 ([Defense One](https://www.defenseone.com/technology/2025/10/army-test-next-gen-c2-prototype-second-time-july-contract-award/408895/))。竞争方面，洛克希德·马丁牵头的团队以 2,600 万美元、16 个月的 OTA 为第 25 步兵师做数据层原型，在 Lightning Surge 系列演习中测试 ([Tectonic](https://www.tectonicdefense.com/lockheed-wins-26m-ota-for-ngc2/))。2026-06-22，陆军指定 Anduril 牵头**通用数据层基线**，内容是"Anduril Lattice + Palantir Foundry"的边缘到云数据网格，**Raft** 提供注册表、数据转换和联邦工具，洛克希德继续负责第 25 步兵师的全栈实施 ([Breaking Defense](https://breakingdefense.com/2026/06/army-picks-anduril-to-lead-next-gen-c2-common-data-layer-baseline/))。2026-10-05/06，上限 18 亿美元的部署合同落地，从 I 军开始，目标是推广到全部 11 个师；一家行业媒体称洛克希德将协助实施 Anduril 的基线 ([DefenseScoop](https://defensescoop.com/2026/10/06/army-awards-anduril-1-8b-contract-expand-ngc2/))。Raft 从竞争者变成合作伙伴，洛克希德从对手原型牵头方变成实施方，说明陆军正在向 Anduril/Palantir 基线收拢。

NGC2 也暴露了联合体最严重的风险。2025-09-05，陆军 CTO Gabriele Chiulli 在备忘录中写道，鉴于对手可能获得"持续且无法察觉的访问"，原型必须视为"**极高风险**"，并称"我们无法控制谁看到什么，无法看到用户在做什么，也无法核实软件本身是否安全"。备忘录据报发现一个应用有 25 个高危漏洞，另有三个应用各有 200 多个缺陷待审 ([Reuters via TradingView](https://de.tradingview.com/news/reuters.com,2025:newsml_L2N3VK0G9:0-anduril-and-palantir-battlefield-communication-system-very-high-risk-us-army-memo-says))。Anduril 称这是"过时的快照"，Palantir 称其平台"未发现漏洞"，陆军则表示关键缺陷已经缓解 ([Breaking Defense](https://breakingdefense.com/2025/10/army-says-its-mitigated-critical-cybersecurity-deficiencies-in-early-ngc2-prototype/))。

### 3.4 CJADC2、金穹、Thunderforge 与空军：联合层级的分工

**Maven 是 CJADC2（联合全域指挥控制）的事实骨干。** 时任常务副部长 Hicks 要求 CDAO 通过 GIDE（全球信息主导实验）在 2023 年底前交付最小可行能力（MVC）；MVC 于 2023-12 认证、2024-02 公布，重点是 11 个作战司令部之间的信息共享，应用包括联合火力网（Joint Fires Network）([DefenseScoop](https://defensescoop.com/2024/02/26/dod-cdao-ai-cjadc2-minimum-viable-capability/))。Palantir 自己把 Maven 描述为"驱动 CDAO CJADC2 计划的云基础设施、软件能力和 AI" ([DefenseScoop](https://defensescoop.com/?p=86457))。Feinberg 备忘录则把 AI 赋能决策定为 CJADC2 的"基石"。FY2027 预算把"MSS + 联合火力网"合并申请 23 亿美元，进一步说明 MSS 已经和联合火力管理绑在一起。**Lattice 在联合层级的角色小一些，也更偏试验性质**：它是 DIU Thunderforge 项目的数据共享层（与微软、Scale 的大模型配合，"始终在人类监督下"）([DefenseScoop](https://defensescoop.com/2025/03/05/diu-thunderforge-scale-ai-combatant-commands-indopacom-eucom/))，并曾在一次 ABMS 演习中连接 F-16、NASAMS、MQ-9 和陆军榴弹炮（日期未确定，可能是 2020–21 年的 ABMS on-ramp）。空军 ABMS 云端 C2 的软件集成商是 SAIC（1.12 亿美元）([af.mil](https://www.mildenhall.af.mil/News/Article-Display/Article/3262645/abms-moves-forward-on-cloud-based-c2/))；2025–26 年空军作战网络（DAF Battle Network）没有找到给两家中任何一家的授标。

**金穹是两家首次被报道在联合级项目中共同开发核心 C2 层。** 2026-03-24，路透社援引知情人士称，Anduril 与 Palantir 正在为金穹导弹盾开发软件，属于一个产业联盟，平台要融合各类传感器数据，让指挥官能够控制武器，计划 2026 年夏季测试；同时点名的还有 Aalyria、Scale AI、Swoop Technologies。金穹负责人 Guetlein 上将称 C2 是"我们的秘方"，是连接雷达、传感器和导弹连的"胶水层" ([US News/Reuters](https://www.usnews.com/news/top-news/articles/2026-03-24/anduril-palantir-developing-golden-dome-missile-shields-software-source-says))。Anduril 还是太空军 12 个天基拦截器团队之一（奖励总额上限 32 亿美元，目标 2028 年完成演示）([Airforce Technology](https://www.airforce-technology.com/news/anduril-us-golden-dome/))。金穹的总成本估算差异很大：白宫 1,750 亿美元，广泛报道 1,850 亿美元，CBO 8,310 亿美元，AEI 3.6 万亿美元。**金穹中两家的合同金额、具体分工和夏季测试结果都没有一手来源**；MSS 在金穹中的角色也没有任何来源提及。

### 3.5 北约：两家在同一买家面前既合作又竞争

北约是观察两家竞合关系的窗口。Palantir 先进入：2025-03 NCIA 为盟军作战司令部采购 MSS NATO，2026-06-22 达到全面作战能力 ([SHAPE](https://shape.nato.int/news-releases/Maven-System-achieves-full-capability))。Anduril 随后跟进：2026-07-07，NCIA 选择 Lattice 用于空中 C2 数据平台计划 eAirC2，这是 Anduril 的首个北约合同，从 9 个月评估期起步；据报道竞争对手包括 Palantir 等 ([Anduril](https://www.anduril.com/news/anduril-secures-first-nato-contract-lattice-for-eairc2-data-platform-initiative); [BattlePolicy](https://www.battlepolicy.com/nato-picks-andurils-lattice-for-air-command-trial-against-palantir-and-athea/))。也就是说，两家在美国陆军 NGC2 里分层合作，在北约空中 C2 的招标中却直接竞争。欧洲评论人士则担心"美国软件正在替欧洲做决定" ([Escudo Digital](https://www.escudodigital.com/en/defense/europe/foreign-software-europes-war-how-maven-and-palantir-are-already-making-decisions-for-europe.html))。

### 3.6 批评、风险与竞争者

三类批评最突出。第一是 **AI 目标定位造成的伤害**（Minab，只涉及 Maven）。第二是**网络安全**（NGC2"极高风险"备忘录，涉及两家）。第三是**集中与锁定**：两份企业合同上限分别为 100 亿和 200 亿美元，全陆军又统一到同一数据层。陆军自己也承认，避免厂商锁定、给传感器和升级留出空间是通用数据层的关键考量 ([Breaking Defense](https://breakingdefense.com/2026/06/army-picks-anduril-to-lead-next-gen-c2-common-data-layer-baseline/))。Lattice 方面没有找到与 Minab 同等级别的伤害事件，对它的批评集中在自主性、网络安全和锁定上，例如有评论认为 Lattice"为比人类判断更快而生"，且没有说清自主致命决策的问责 ([Free Press](https://freepress.org/article/anduril-s-lattice-now-army-s-drone-killing-brain-and-it-s-built-act-faster-human-judgment))。竞争格局方面：洛克希德（第 25 步兵师 NGC2）、Scale AI（Thunderforge 牵头方，但使用 Lattice）、Shield AI Hivemind（CCA 自主，与 LMA 可互换）、SAIC（ABMS CBC2），以及 Raft（已转为合作伙伴）。

---

## 四、数据冲突与待核实清单

下表集中列出调研中发现的口径冲突和未经证实的条目。**引用前应逐项回到原文核对。**

| 条目 | 冲突或存疑内容 | 来源 |
|---|---|---|
| Anduril 成立日 | 2017-04-20（注册）还是 2017 年 6 月（公开） | [Wikipedia](https://en.wikipedia.org/wiki/Anduril_Industries); [TechCrunch](https://techcrunch.com/?p=1654777) |
| SOCOM 反无人机合同 | 9.676 亿、9.68 亿还是"约 10 亿"美元；授标日 2022-01-19，报道日 01-24 | [AFCEA](https://www.afcea.org/signal-media/contracting/socom-selects-anduril-integration-partner-967-million-counter-unmanned) |
| Area-I / Dive 收购日期 | 2021-04 还是 2022-10；2022-02 还是 2023-03 | [Contrary Research](https://research.contrary.com/company/anduril) |
| JIATF 401 首个任务单 | 8,770 万还是 8,700 万美元 | [DefenseScoop](https://defensescoop.com/2026/03/14/anduril-20-billion-dollar-army-contract/) |
| Lattice 在 CCA 中的角色 | "空军选定 LMA 用于下一阶段"，还是"三家各获 6 个月自主 CLIN 后择优"，顺序与日期互相矛盾 | [Defence Industry EU](https://defence-industry.eu/u-s-air-force-selects-anduril-lattice-mission-autonomy-software-for-next-collaborative-combat-aircraft-program-phase/); [Simple Flying](https://simpleflying.com/software-deal-put-anduril-inside-every-cca-air-force-buys/) |
| YFQ-44A 投产 | 2026-03 已批量生产，还是 2026-07-28 首架下线 | [The Aviationist](https://theaviationist.com/2026/03/24/yfq-44a-fury-cca-is-now-in-production/); [Military Times](https://www.militarytimes.com/industry/techwatch/2026/07/28/first-anduril-yfq-44a-rolls-off-production-line-for-us-cca-program/) |
| 边境塔总数（所有供应商） | 803 座还是约 830 座；均未与 GAO 原文核对 | [MIT TR](https://www.technologyreview.com/2026/09/21/1144166/border-towers-surveillance-investigation/) |
| XRST 合同性质 | 一年期 SBIR Phase III 还是多年扩展 | [State of Surveillance](https://stateofsurveillance.org/news/anduril-border-surveillance-monopoly-big-beautiful-bill-2026/) |
| 海军无人艇失灵时间 | 2025 年 5 月/夏季还是 2024 年 | [TechBuzz](https://www.techbuzz.ai/articles/anduril-s-autonomous-weapons-fail-in-tests-ukraine-combat) |
| Ghost Shark 开发经费 | 约 1.4 亿澳元还是约 9,250 万美元 | [Wikipedia](https://en.wikipedia.org/wiki/Ghost_Shark_(submarine)) |
| 台湾 Altius-600M | 3 亿还是 11 亿美元；"追加 2,032 套"仅有单一来源 | [The Defense Post](https://thedefensepost.com/2026/03/20/anduril-altius-600m-taiwan/) |
| Anduril 估值 | Tracxn 的 1,110 亿美元为离群值；1,000 亿美元一轮未确认交割 | [Tracxn](https://tracxn.com/d/companies/anduril/__qqOI0HKR47lFXorj9FAQlDfmJOqfOpDNWiW3JcO--ss/funding-and-investors) |
| 谷歌抗议规模 | 签名 4,000、4,600 还是近 5,000；辞职约 12 人、13 人还是"数十人" | [Gizmodo AU](https://www.gizmodo.com.au/2018/05/google-employees-resign-in-protest-against-pentagon-contract/) |
| 2024-02 打击 | "85 次以上打击"还是"85 个目标" | [The Register](https://www.theregister.com/2024/02/27/us_military_maven_ai_used/) |
| MSS 数据源数 | 179 个（CSIS）还是 150 个以上（GlobalSecurity） | [CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do) |
| Palantir 陆军 EA 日期 | 2025-07-31 还是 2025 年 8 月 | [Washington Technology](https://washingtontechnology.com/contracts/2025/08/palantir-signs-10b-enterprise-agreement-army/407153) |
| Feinberg 备忘录日期 | 2026-03-09（签署）还是 03-20 至 03-23（路透报道日） | [GovConWire](https://www.govconwire.com/articles/pentagon-palantir-maven-ai-program-of-record) |
| MSS 转为采购项目 | 截止 2026-09-30；Motley Fool 称"已成为"，其他来源仍说在过渡中，没有官方确认 | [Motley Fool](https://www.fool.com/investing/2026/08/25/palantirs-maven-is-now-an-official-pentagon-progra/) |
| FY2027 预算 | 超过 15 亿美元（扩大访问）与 23 亿美元（MSS + 联合火力网，部分媒体称为 5 年合计）口径不同，尚未厘清 | [DefenseScoop](https://defensescoop.com/2026/05/28/dod-fy27-budget-cjadc2-maven-smart-system-palantir/); [SpaceNews](https://spacenews.com/pentagon-seeks-2-3-billion-for-maven-ai-battlefield-system/) |
| 伊朗战役打击数 | 24 小时约 1,000 个、至 3-3 近 2,000 个、10 天约 5,000 个（Wikipedia）、38 天 13,000 个；"每天 3,000 个""11,000 次以上打击"仅见于低可信站点，不宜采信 | [Wikipedia: AI warfare](https://en.wikipedia.org/wiki/AI_warfare) |
| Minab 死亡人数 | 约 123 名儿童、175–180 人、150–170 余人、"至少 186 名学生和教师"（伊方）；Bloomberg 调查报道日期 9-18 还是 9-20 | [Bloomberg](https://www.bloomberg.com/graphics/2026-iran-school-attack/); [ACA](https://www.armscontrol.org/act/2026-05/news/ai-plays-major-role-war-iran) |
| Claude 在 Maven 中的状态 | 2026-03-04 被列为供应链风险、6 个月内淘汰；另一说法提到 02-28 的行政令；Palantir CEO 则称 Claude 仍在目标系统中运行；最终是否完成替换、由谁接替，均无一手确认 | [Interesting Engineering](https://interestingengineering.com/military/claude-ai-iran-us-military-targeting) |
| MSS 用户数 | 2025 年 2 万以上（NGA），另有"130 个站点、约 2.5 万人"的二手说法 | [Hvylya](https://en.hvylya.net/news/1529-130-sites-1-billion-detections-the-silent-global-spread-of-america-s-ai-war-machine) |

---

## 结论

这项调研最重要的发现是：**美军数字化杀伤链的事实标准不是靠技术规范定下来的，而是靠两份企业合同**（Palantir 100 亿美元、Anduril 200 亿美元）**和一次战争**（史诗怒火行动）定下来的。Maven 用九年时间从一个视频识别小组变成用户超过 10 万的"万能应用"，Lattice 从边境塔软件变成陆军 11 个师的数据层。两者的扩张都先于独立评估：可公开核实的硬证据几乎只有采购决策和官方给出的总量数字，准确率、虚警率、电子战生存力和网络安全仍然是黑箱。少数能看到的独立证据（乌克兰的失效、Minab 的过期数据、"极高风险"备忘录）都指向同一个问题：**瓶颈和风险集中在数据质量、人机协作的密度和对抗环境中的鲁棒性上，而不是算法本身**。Maven 的价值在于把杀伤链"工业化"，代价是人工审查密度下降。Lattice 的价值在于让任何传感器或效应器在数小时内接入并被调度，代价是全军对单一私有数据层的依赖。

往后看，最值得跟踪的是三个节点。一是 MSS 是否在 2026 财年底真正完成采购项目转换，以及它会不会被并入拟设的 CJADC2 项目办公室。二是 NGC2 推广到 I 军后，Lattice 实体模型与 Palantir 本体之间的接口是否公开、是否形成政府拥有的标准；这决定了"避免厂商锁定"是一句口号还是一项可执行的架构。三是金穹 C2 和北约 eAirC2 的评估结果，它们将检验两家在联合和联盟层级上是继续分层协作，还是走向正面竞争。对研判者来说，读到今后的"打击 N 个目标""缩短 90%"一类数字时，应先问三件事：计的是什么，谁报的数，是否有独立审计。本报告的结论都建立在搜索摘要之上，关键数字须回到原文核对后再引用。
