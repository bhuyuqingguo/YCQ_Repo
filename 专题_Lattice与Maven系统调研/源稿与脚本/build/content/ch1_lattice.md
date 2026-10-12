# 一、Lattice：从边境监视塔到军种级战场数据层

:::lead
Lattice 由边境监视塔融合软件演进为美陆军 NGC2 通用数据层。功能与架构依据官方 SDK 源码，效能数据多为公司口径。数据截至 2026 年 10 月 10 日。
:::

## （一）前世今生：九年间的四次身份转换

:::lead
Lattice 历经边境监视软件、反无人机集成内核、命名产品族、开放平台与军种级数据层四个阶段，每个阶段对应一类新增用户和一次估值跃升。
:::

### 公司缘起与边境起家（2017—2020）

Anduril Industries 成立于 2017 年，联合创始人为 Oculus 创始人 Palmer Luckey 及 Trae Stephens、Brian Schimpf、Matt Grimm、Joe Chen，其中三人出自 Palantir 公司[@la_wiki_anduril]。成立日期一说 4 月 20 日注册，TechCrunch 称 6 月低调成立，前者较可能为注册日[@la_tc_founding]。Stephens 兼任 Founders Fund 合伙人，该基金领投 2024 年 F 轮和 2025 年 G 轮。公司采取软件定义、硬件承载的路线，自研的传感器塔、无人机和拦截器均经同一软件内核 Lattice 完成感知、通信和任务接收；公司每进入一个新领域，Lattice 便增加一类可接入节点。

!photo luckey_ted_2025|联合创始人帕尔默·勒基，2025 年 4 月 TED 大会|TED Conferences（经 Flickr），CC BY 2.0

!photo trae_stephens_2024|联合创始人、董事长特雷·斯蒂芬斯，2024 年|TechCrunch（经 Flickr），CC BY 2.0

Lattice 的首个用例是为美国海关与边境保护局（CBP）构建美墨边境"虚拟墙"。2017 年 6 月 Anduril 向国土安全部加州办公室推介边境方案，2018 年 6 月在德克萨斯州私人牧场非正式测试监视塔[@la_wiki_anduril]。FedScoop 称 Anduril 同月获首个国土安全部合同，金额 480 万美元，在圣迭戈和尤马部署 10 座塔；该金额未能在官方记录中核实[@la_fedscoop_towers]。

2020 年，自主监视塔（AST）成为边境巡逻队正式采购项目（Program of Record）[@la_cbp_por]。合同金额说法不一：AI Business 称 8,500 万美元；FedScoop 称未披露，高管仅称"数亿美元"；Privacy International 称 5 年 2.5 亿美元[@la_aibusiness]。采购对象是监视塔而非单独的软件。塔上的 Lattice 以 AI 处理雷达和光电/红外数据，识别潜在威胁并自动告警；CBP 官员称塔跟踪"物体和活动"，不做人脸识别。**Lattice 自始即为与硬件无关的融合层，这是其日后扩展至反无人机、指挥控制和集群自主的基础。**

!photo sentry_bfsp|圣迭戈边境州立公园内的 Sentry 自主监视塔，2024 年|Toyonbro（Wikimedia Commons），CC0

!photo ast_bigbend_dvids|边境巡逻队在大本德地区运行的自主监视塔，2021 年 12 月|CBP Office of Public Affairs（DVIDS），美国政府作品

同期，Lattice 进入美空军视野。2020 年 9 月先进作战管理系统（ABMS）第二次"上匝道"演示中，空军人员在安德鲁斯联合基地监控运行 Lattice 的计算机；10 月一次 AFRL/ABMS 演示中，操作员确认 Lattice 正在跟踪巡航导弹替代目标后，向效应器下达交战指令[@la_dn_cruise]。另有材料称 Lattice 曾在一次 ABMS 演习中连接 F-16、NASAMS、MQ-9 和陆军榴弹炮，日期未确定[@la_af_abms]。

!photo lattice_abms_onramp2|2020 年 9 月 ABMS 演示中监控运行 Lattice 的计算机|U.S. Air Force photo by Senior Airman Daniel Hernandez，美国政府作品

!photo lattice_demo_mittr|2024 年 12 月 Lattice 反无人机与基地防御演示界面|Anduril Industries / MIT Technology Review，公司图片，仅作评论引用

### 进入国防部与产品化（2021—2024）

2021 年 9 月，英国国防部战略司令部授予 Anduril 380 万英镑、最长 2 年的 TALOS 基地防御试验合同，系统基于 Lattice，以 Sentry 塔、地面传感器和无人机检测、跟踪地面与空中入侵[@la_edr_talos]。2022 年 1 月，美国特种作战司令部（SOCOM）从 12 份提案中选定 Anduril 为反无人系统集成伙伴，合同为 10 年期 IDIQ，上限 9.676 亿美元，授予时实拨约 110 万美元，期限至 2032 年 1 月；Lattice 负责自主检测、分类、跟踪目标并向操作员提供交战选项，合同明确要求集成第三方传感器与效应器[@la_wt_socom]。**SOCOM 合同使 Lattice 首次以系统集成内核的身份进入国防部。**

2023 年 5 月 3 日，Anduril 发布首个命名产品 Lattice for Mission Autonomy（LMA，任务自主），目标是由多人操控一个系统转为一人操控多个[@la_dn_lma]。SOCOM 随后选定 Anduril 为任务自主系统集成伙伴[@la_monch_mas]。2024 年的其他节点包括：2 月海军与国防创新单元（DIU）选定 Anduril 等三家研制 Dive-LD 大型无人潜航器原型；4 月在空军协同作战飞机（CCA）第一增量中胜出；9 月部署第 300 座 AST；11 月获陆战队约 2 亿美元 MADIS 反无人机交战系统合同。

2024 年 11 月，太空军授予约 9,970 万美元的太空监视网（SSN）现代化合同，以 Lattice 为弹性网状网络，要求 2026 年底完成部署[@la_ds_ssn]。12 月 3 日，国防部首席数字与人工智能办公室（CDAO）授予 1 亿美元、3 年期（另有 4 年一说）生产型 OTA，推广基于 Lattice Mesh 的边缘数据网格，属联合全域指挥控制（CJADC2）组成部分[@la_ds_cdao]。

2024 年 12 月 6 日，Anduril 与 Palantir 宣布合作，由 Lattice 和 Menace 设备采集战场边缘数据送入 Palantir AIP，覆盖 SCI/SAP 等最高密级[@la_bw_palantir]。12 月 10 日，Lattice SDK 公开发布，同步推出合作伙伴计划，首批 10 余家伙伴包括 Impulse Space、Saronic、Scale AI、Spire Global 和 Textron Systems 等[@la_ocbj_partners]。Lattice for C2 同期出现，被描述为 AI 战斗管理平台；Lattice 无公开的版本号体系。

收购围绕为 Lattice 补齐末端节点展开：Area-I 带来 ALTIUS 系列空射效应器，Dive Technologies 带来水下节点，Blue Force Technologies 带来 Fury（后发展为 YFQ-44A），另有 Numerica 雷达与 C2 业务和 Klas 边缘计算硬件，部分收购日期各来源冲突[@la_contrary]。2024 年 12 月，英国《金融时报》和路透社报道两家公司正与 SpaceX、OpenAI 等商谈组建联合投标集团，此后未见正式成立的证据[@la_tc_consortium]。

### 估值、产能与 2025—2026 年的转型

Anduril 估值由 2019 年 B 轮约 10 亿美元升至 2026 年 5 月 H 轮 610 亿美元（见{fig:c_anduril_funding}）[@la_andurilnews_funding,la_tc_seriesh]。2026 年 7 月路透社报道的约 1,000 亿美元估值洽谈未见交割确认；Tracxn 所列 1,110 亿美元按离群值处理。营收 2024 年约 10 亿美元、2025 年 22 亿美元，均为公司口径，未经审计；公司尚未公布 IPO 时间表。**我部研判，资本市场将 Anduril 作为软件平台型主承包商定价，Lattice 是这一定价的核心依据。**

!fig c_anduril_funding|c_anduril_funding.png|Anduril 历轮估值、融资额与营收（2017—2026）|本报告依据 andurilnews、Sacra、TechCrunch、CNBC 数据绘制；营收为公司口径|160

产能方面，俄亥俄州"武库-1"（Arsenal-1）工厂建筑面积 500 万平方英尺，2026 年 3 月投产 Fury，计划扩展至 Roadrunner、Barracuda 等产品[@la_bd_arsenal1]。2026 年 10 月 6 日，海军授予上限 29 亿美元的弗吉尼亚级潜艇部件合同，Anduril 将在巴尔的摩建设"武库-2"船厂，自投 37 亿美元[@la_cnbc_sub]。

!photo arsenal1_rendering|"武库-1"俄亥俄州工厂效果图（2025 年 1 月发布）|Anduril Industries 效果图，公司图片，仅作评论引用

!photo roadrunner_idex2025|IDEX 2025 展出的 Roadrunner 拦截器，2025 年 2 月|Mztourist（Wikimedia Commons），CC BY 4.0

2025 年起，Lattice 相关合同由为自家硬件配套转向为整个军种提供数据层。反无人机线方面，2025 年 3 月陆战队授予以 Lattice 为 C2 的设施反小型无人机（I-CsUAS）IDIQ 合同，上限 6.42 亿美元，Anduril 从 9 家（另记 10 家）竞标者中胜出；11 月陆军选定 Lattice 为机动型一体化作战指挥系统（IBCS-M）的反无人机火控与 C2 平台[@la_ds_icsuas]。2026 年 3 月 13—14 日，陆军授予 10 年期企业合同，上限 200 亿美元，将 120 余项采购行动并入以 Lattice 为中心的框架；陆军强调这是"没有附带资金的合同载体"，首个任务单用于联合跨机构特遣部队 401（JIATF 401）通用反无人机 C2，约 8,700 万美元（另记 8,770 万美元）[@la_army_20b]。

指挥控制线方面，2025 年 7 月 18 日，陆军授予 9,960 万美元、11 个月的 OTA，由 Anduril 牵头 Palantir、Microsoft、Striveworks 等组成的团队为第 4 步兵师交付下一代指挥控制（NGC2）原型[@la_army_ngc2_award]。2026 年 6 月 22 日，陆军指定 Anduril 牵头 NGC2 通用数据层基线，数据网格由 Lattice 与 Palantir Foundry 共同构成；10 月 5—6 日授予 5 年期、上限 18 亿美元（基础期 1.628 亿美元）的推广合同，自第 1 军开始，Anduril 称 Lattice 是连接应用、数据、AI 模型、传感器和载具的"分布式数据层"[@la_ds_icorps]。原型转生产仅用约 15 个月。

其他方向同步推进。2026 年 2 月 24 日，LMA 首次在 YFQ-44A 上飞行；6 月，CBP 以 3.63 亿美元采购 200 余座增程型 Sentry 塔，国务院批准向科威特出售含 Lattice、估值 19.8 亿美元的反无人机系统；7 月 7 日，北约通信与信息局（NCIA）选定 Lattice 参加增强型空中指挥控制（eAirC2）数据平台评估，这是 Anduril 首个北约合同[@la_anduril_nato]。开发者平台 2026 年先后上线 Developer Console、Schema Registry、面向 AI 编程智能体的 SDK skills 和 Video API 预览，10 月 5 日发布 Rust SDK，日期取自更新日志摘要[@la_changelog]。

!fig c_anduril_contracts|c_anduril_contracts.png|Anduril 主要合同金额（按时间，对数坐标）|本报告依据各合同公告与行业媒体整理；上限、已拨付与 FMS 估值口径不同，不可简单相加|160

合同结构经历三次变化：2018—2021 年以试点为主；2022 年起出现 IDIQ 和 OTA 形式的大额上限合同；2026 年进入企业协议加任务单模式，后续订单单独公告可能减少[@la_bd_jiatf]。C2、反无人机和传感器网络类合同几乎都明确以 Lattice 为核心，固体火箭发动机、CCA 机体、潜艇部件等硬件类合同通常不提及 Lattice。下表合同上限合计约 22 亿美元（不含 200 亿美元企业协议），上限、已拨付和军售估值口径不同，JIATF 401 任务单已含在企业协议内，不能直接相加。

!table la_lcontracts|来源明确提到 Lattice 的主要合同|本报告依据合同公告与行业媒体整理；上限、已拨付与 FMS 估值口径不同|22,40,34,64
时间|客户与项目|金额|Lattice 的作用
2021-09|英国国防部 TALOS 试验|380 万英镑|检测、分类、跟踪地面与空中入侵[@la_blog_talos]
2022-01|SOCOM 反无人系统集成|上限 9.676 亿美元|集成 Sentry、Anvil、Pulsar、FoxHound[@la_wt_socom]
2024-02|海军与 DIU Dive-LD 原型|未披露|实时跟踪和共享潜航器位置[@la_globalsec_diveld]
2024-11|太空军 SSN 现代化|约 9,970 万美元|弹性网状网络[@la_ds_ssn]
2024-12|CDAO 边缘数据集成|1 亿美元|基于 Lattice 的边缘数据网格[@la_ds_cdao]
2025-03|陆战队 I-CsUAS|上限 6.42 亿美元|核心 C2 软件[@la_ius_madis]
2025-09|陆军 SBMC 第一阶段|1.59 亿美元（硬件）|数据与 AI 架构建于 Lattice C2[@la_bd_eagleeye]
2025-11|陆军 IBCS-M|未披露|反无人机火控与集成骨干[@la_mes_ibcsm]
2026-03|陆军企业协议|上限 200 亿美元|Lattice 软件、硬件、数据、算力与服务[@la_army_20b]
2026-03|JIATF 401 首个任务单|约 8,700 万美元|反无人机 C2 骨干[@la_d1_jiatf]
2026-06|CBP 增程 Sentry 塔|3.63 亿美元|新塔与 Lattice 及既有塔网集成[@la_execbiz_xrst]
2026-07|北约 NCIA eAirC2 评估|未披露|在北约环境中部署 Lattice[@la_die_nato]
!end

**截至 2026 年 10 月，Lattice 已是美陆军反无人机和 NGC2 的核心数据层，竞争格局由对抗传统主承包商转为与 Palantir 分层合作、局部竞争。**

## （二）功能设计：以实体为中心的作战图与军事化任务链

:::lead
官方 SDK 可直接还原 Lattice 功能：以实体为中心的共用作战图，加实体、任务、对象三类接口。**数据模型写入大量军事概念，按作战软件设计。**
:::

### 实体与共用作战图

SDK 将实体（Entity）定义为"作战环境中的一个已知对象"，数据存于 30 余个可选组件，覆盖位置、运动学、航迹质量、敌我属性、轨道、信号、应答机代码、军标符号、补给、密级和能力目录等[@la_sdk_entity]。实时订阅接口 StreamEntities 用于"维护共用作战图（COP）的实时视图"[@la_sdk_ref]。地图、列表和告警均为同一实体集合的不同呈现；任何传感器或平台只要将输出转为实体即可入图，这是硬件无关的技术基础。结合 orbit、signal 组件和 Impulse Space、Saronic 等伙伴，我部推断该模型按陆海空天电全域设计。

location 与 kinematics 二选一，航迹优先使用 kinematics，后者是航迹外推和火控解算的输入。发布时 expiry_time 必填且距当前时间少于 30 天，陈旧信息自动退出作战图，直接针对依据过期情报实施打击的风险。本体模板共五类：航迹、传感器关注点、资产、地理形状、关注信号；限入区、禁飞区等地理围栏以带 geo_shape 组件的实体表示，可像目标一样发布、订阅和随任务下发（推断）[@la_sdk_ontology_tpl]。

!fig d_lattice_entity_task|d_lattice_entity_task.png|Lattice 实体组件模型与任务生命周期状态机|本报告依据 Anduril 官方 lattice-sdk-python 源码（entity.py、task_status_status.py 等）绘制|160

### 军事化字段：敌我、航迹、密级与溯源

敌我属性（disposition）枚举为不明、友、敌、可疑、假定友、中立、待定，与北约和美军分类基本一致[@la_sdk_milview_disp]。tracked 组件含 0—15 级航迹质量、传感器命中数和雷达截面积，并注明目标数"在某些语境下称为强度（Strength），见 Link 16"[@la_sdk_tracked]。

correlation 组件实现 N 对 1 主从航迹关联，并设显式去关联：用户判定两条航迹不同后，系统"防止关联器再次把它们关联起来"[@la_sdk_correlation]。这证实内部存在自动关联器，且人工结论对其有约束力。indicators 组件含模拟、演习、紧急、可外发等标识，支持真实与演习数据混合运行；health 组件记录连接状态和当前告警，监视塔掉线、无人机电量告急均表现为资产实体上的告警[@la_sdk_health]。

data_classification 组件设默认密级并允许逐字段设置，分非密至绝密五级，另有 NOFORN 等附加标记；egressable 标识注明"由各集成决定如何外发"[@la_sdk_classification,la_sdk_indicators]。同一目标的位置与型号判断可定为不同密级，向盟军外发时只放行可放行字段（推断）。**数据模型能够表达多密级，不等于系统已获准跨密级运行**，公开资料未见经认证的跨域解决方案。

经 API 发布的实体归发布者所有，UI 不得编辑或删除；操作员可覆写标为可覆写的字段（如 mil_view.disposition），采用后写者胜规则[@la_sdk_ref]。传感器事实与人的判断由此分层存放，位置、速度由数据源独占，属性、优先级由人覆写，何人何时将哪个目标定为敌对均有溯源记录（推断）。

### 任务链：沿用战术通信的确认语义

任务状态共 14 种，自 CREATED 经 SENT、MACHINE_RECEIPT、ACK、WILCO（将遵照执行）至 EXECUTING，终态为 DONE_OK 或 DONE_NOT_OK，沿用战术数据链和语音指挥的确认语义（推断）[@la_sdk_task_status_status]。任务以 initial_entities 指向目标实体和限入区实体，状态更新采用乐观并发控制；取消请求发出后"由代理决定能否取消"，与弹药发射后未必能召回的实际情况相符[@la_sdk_ref]。

资产实体以 task_catalog 声明自身能力，新平台接入即列入可调度资源，指挥端无需为每种平台编写专门代码；IBCS-M 试验中"数小时内接入一个此前未公开的传感器和效应器"即为例证[@la_sdk_task_catalog]。手动控制接口以带纪元号和序号的帧流传送摇杆动作，支持操作员随时接管单个平台。对象接口可在整个 Mesh 中同步最大 1 GiB 的文件；Video API 支持 RTSP、SRT 和 MPEG-TS 接入，2026 年 9 月进入预览[@la_changelog]。

### 任务自主与杀伤链

LMA 是硬件无关、端到端的集群任务平台，覆盖风险建模、任务规划、指挥控制至任务后复盘，公司称可在人类监督下管理"数百个"异构无人系统[@la_blog_lma]。陆军 EDGE23 演习中，一名士兵控制多家厂商无人机，将地空导弹阵地定为敌对并授权 ALTIUS-600M 打击，随后 Lattice 自动改派 ALTIUS ISR 无人机执行毁伤评估[@la_blog_edge23]。

将 SDK 数据结构与 EDGE23、Falcon Peak 25.2 演示对照，可还原七步交战流程（推断，见{fig:d_lattice_killchain}）：边缘 AI 探测目标，节点发布航迹实体，关联器融合多源航迹，操作员将属性改定为 HOSTILE，向声明相应能力的效应器派发任务，代理回报 ACK、WILCO 至完成，自主模块改派 ISR 资产评估毁伤。Falcon Peak 25.2 中，Mobile Sentry 探测并跟踪一架"敌方"无人机，由 Anvil 以动能方式击毁[@la_ius_falconpeak]。

!fig d_lattice_killchain|d_lattice_killchain.png|Lattice 探测—评估七步交战流程与人机关系（推断）|本报告依据 lattice-sdk-python 数据结构、EDGE23 与 Falcon Peak 公开报道绘制|160

陆军 NGC2 中，Lattice 由控制自家硬件扩展为师级数据层。2025 年 9 月 Ivy Sting 1 中，第 4 步兵师从师部到炮位的目标处理全部运行于 Lattice Mesh 和 Palantir Target Workbench；炮兵数据工具 AXS 运行于 Mesh，引导 M777 榴弹炮射击，据报道使用 AXS 的炮组 30 秒内完成数字化准备，使用 AFATDS 的炮组则常须先排查连接问题[@la_bd_ivysting1]。Lattice 负责战术边缘的数据传输与实体层，Target Workbench 负责目标管理与逐目标资源分配。

### 人机关系与功能空白

公开交战案例中，开火决定均由人作出：2020 年巡航导弹演示中操作员先确认目标再下令交战，陆战队明确 Anvil"只在人工操作员下令后才拦截"，EDGE23 中亦由人授权打击[@la_marines_gbad]。**我部研判，Lattice 的机动、感知和资源调度属"人在回路上"，武器释放属"人在回路中"（推断）。** 公开资料未见交战规则配置、小型无人机自动交战模式及落实国防部第 3000.09 号指令的文件；公司称 AI"识别威胁比人类操作员更准确"，无独立测试数据；批评者认为 Lattice"为比人类判断更快地行动而设计"[@la_freepress]。

具体任务定义、可覆写字段清单、计算机视觉模型的训练数据与准确率指标、Roadrunner 集成方式均未公开，空白集中于杀伤链中机器决定多少这一敏感问题。以基地反无人机为例（示例推断）：Sentry 塔调用 publish_entity 发布航迹实体，属性暂为不明；另一部雷达的航迹被关联器合并；指挥所以 stream_entities 按地理过滤订阅；值班员调用 override_entity 改定为敌对，再调用 create_task 指派一架声明拦截能力的 Anvil；Anvil 经 stream_as_agent 受领并逐级回报至完成[@la_sdk_ref]。谁看到了什么、谁作了何种判断、谁下达了何种命令均转为结构化记录，可供复盘，但其保存方式、期限和能否独立调阅未见说明。

## （三）架构设计：节点联邦、网状网格与 protobuf 内核

:::lead
Lattice 是由 Mesh 连接的节点联邦，面向链路拒止、降级、时断时续（DDIL）环境，可分六层；④⑤层依据 SDK 源码，①—③层部分为推断。
:::

### 总体形态与末端节点

据 SDK 推断，每个节点运行本地实体存储、任务管理、对象存储、视频服务和关联器，Mesh 以点对点方式复制实体和对象并按优先级选路，客户端连接本地节点；Video API 区分边缘封闭网络与经公共互联网访问的云部署（推断）[@la_sdk_ref]。

!fig d_lattice_arch|d_lattice_arch.png|Lattice 六层架构与部署形态示意|本报告依据 Anduril SDK 源码、Lattice Mesh 专利与公开报道绘制；①—③层及"每节点完整栈"含推断|160

公开确认由 Lattice 控制或融合的平台包括 Sentry 塔（固定、机动、增程型）、Wisp、Pulsar 电子战系统、Anvil、ALTIUS-600/600M、Ghost-X、YFQ-44A，以及 IBCS-M 下接入的第三方雷达和效应器[@la_ds_ibcsm]。增程型塔高 80 英尺，自主探测距离超过 5 英里。公司称每件产品内置"Lattice AI Core"，在边缘完成融合、分类与多航迹调和，体现了将处理能力下放到节点的取向[@la_airrec_socom]。Ghost Shark、Barracuda、Roadrunner 与 Lattice 的集成方式无公开来源。

!photo anvil_press|Anvil 动能拦截无人机，人工下令后才拦截（公司图）|Anduril Industries，公司图片，仅作评论引用

!photo pulsar_l_press|Pulsar-L 轻型电子战系统，2025 年 4 月发布（公司图）|Anduril Industries，公司图片，仅作评论引用

### 边缘计算与 Lattice Mesh

2025 年 5 月发布的 Menace-T 是两箱式 C4 套件，一名操作员数分钟即可架设，基于 Klas Voyager 坚固计算硬件运行 Lattice Mesh，可承载第三方边缘 AI，同时是 Palantir Edge 软件的首选硬件[@la_tc_menace,la_dc_menace]。NGC2 原型被描述为"在共同数据层上的一体化软硬件 C2 套件"，计算节点部署于多种车辆。**Anduril 在 C2 领域提供的是软件、计算与通信一体的边缘节点，而非单纯软件。**

!photo sentry_imperial|加州帝国县公路旁的 Sentry 塔（末端节点），2022 年 7 月|Electronic Frontier Foundation（EFF），CC BY 4.0

!photo menace_t_press|Menace-T C4 边缘计算套件，运行 Lattice Mesh（公司图）|Anduril Industries，公司图片，仅作评论引用

Mesh 专利（US 10,506,436）有三个要点：实时数据优先，回填只用剩余带宽；点对点授权路由；普通节点密钥只存于内存、不落盘，以降低节点被缴获时的泄密风险[@la_patent_436]。SDK 印证了存储转发式复制，并有断线续传、客户端落后过多即终止会话、按组件与过滤器订阅等面向 DDIL 的设计[@la_sdk_ref]。gossip 协议一说仅见个人博客，传输层、同步模型和冲突消解机制无公开描述。

部署证据方面，CDAO 授予合同时该网格已"在多个军种和作战司令部运行"[@la_ds_cdao]；Anduril 英国公司在英国陆军阿斯加德计划中演示了边缘数据网格[@la_die_asgard]。公司称 Ivy Sting 5 将网格扩大至 3 倍，连接 65 个以上战术边缘节点，并在卫星和商用通信失效时持续工作。

### 核心服务、SDK 与应用

核心服务为 gRPC 的实体管理器和任务管理器，v2 接口采用 OpenAPI/REST 加 SSE，大量使用 protobuf Any 封装，据此判断内部以 protobuf/gRPC 为原生，REST 只是外层封装（推断）[@la_docs_overview]。SDK 覆盖 Python、TypeScript、Java、Go、C++ 和 Rust；2025 年 7 月 C++ 仓库归档，protobuf 定义改由 Buf Schema Registry 托管[@la_github_anduril]。v2 公开接口分实体、任务、对象、认证、视频五组。

接入模式分三种：传感器为生产者，发布航迹或资产实体；用户界面与分析程序为消费者，订阅实体流；无人平台与武器为可受领任务的代理，接收执行、取消和完成请求并回报状态。2026 年 10 月 ORIGIN 公司 BLAZE 拦截器即按代理模式接入；中央司令部沙漠守护者 1.0 演习中，参演官兵依据 SDK 文档将各自系统接入 Lattice，部分为现场实时完成[@la_overt_blaze,la_ocbj_partners]。

SDK 许可为有限、可撤销、免版税许可，仅可为"兼容的 Lattice 实现"开发应用，禁止构建其他 SDK 或不兼容实现[@la_sdk_license]。**Lattice 属于开放接口、封闭实现，并非开源软件。** 应用层包括 LMA、Lattice for C2、反无人机 C2 和 NGC2 师级应用；DIU 于 2025 年 3 月启动、由 Scale AI 牵头的 Thunderforge 战役规划项目以 Lattice 为数据共享层，陆军单兵携行任务指挥（SBMC）的数据与 AI 架构也建于 Lattice C2 之上[@la_diu_thunderforge]。

### 互操作、Palantir 对接与安全

政府参考自主架构（A-GRA）是唯一有明确记录的标准：YFQ-44A 曾在单次飞行中经 A-GRA 在 Shield AI 的 Hivemind 与 LMA 之间切换，Anduril 称 LMA 完全符合 A-GRA[@la_aviationist_hivemind]。Link 16 仅有数据模型层面的间接证据，Menace 经 Link 16 运行一说为弱源；TAK/CoT 仅有 ATAK 工程师招聘，OMS/UCI 未找到可靠来源[@la_builtin_atak]。egressable 注释指向一个将实体转换为外部格式的适配层（推断）；Lattice 与诺斯罗普·格鲁曼 IBCS 核心的对接细节未公开。

NGC2 中 Lattice 承担战术边缘网格与实体层，Foundry 为企业数据平台，Target Workbench 承担目标处理；2026 年 6 月基线将两者定为一张边缘到云的数据网格，由 Raft 提供注册与联邦服务[@la_bd_cdl]。这种分工并非严格的层级切分，Palantir 工具也部署到师一级，Lattice 也进入战区和联合层级。Lattice 实体模型与 Palantir 本体的映射未见公开说明。

SDK 采用 OAuth2 客户端凭证认证，但授权运行（ATO）等级、IL5/IL6、SIPR/JWICS 运行与跨域方案均无公开资料。2025 年 9 月 5 日，陆军首席技术官 Gabriele Chiulli 在备忘录中称 NGC2 原型应视为"极高风险"，"无法验证软件本身是安全的"，一个应用有 25 个高危漏洞，另三个应用有 200 余个缺陷待审查[@la_reuters_memo]。Anduril 称其为"过时的快照"，Palantir 称其平台中没有发现漏洞，陆军称关键缺陷已缓解；备忘录针对原型整体而非专指 Lattice[@la_bd_memo]。**我部研判，多厂商、快速迭代数据层的安全认证是现实短板。**

## （四）能力评估：采购决策是硬证据，效能数据几乎全由公司提供

:::lead
多军种竞标采购是最硬的证据；定量效能数据几乎全为公司口径；唯一可公开核实的实战使用（乌克兰）结果为负面。
:::

### 总体判断与分项评估

SOCOM、陆战队 I-CsUAS、陆军 IBCS-M、200 亿美元企业合同、NGC2 原型转推广和北约 eAirC2 评估，均为经竞争作出的采购选择[@la_ds_icorps]。**上述决策表明美军认可 Lattice 作为集成层和数据层的价值。** 但采购决策证明的是用户认为其有用，不证明实战效能；"火力时间缩短 90%""2,500 余台终端""完美击杀"等定量数据均出自公司或演习组织方，未见独立评估[@la_milleak_ivymass]。

态势感知方面，AST 是连续使用时间最长、规模最大的场景，但检测概率、虚警率和可用率从未公开。MIT Technology Review 2026 年 9 月估计，2021 年以来有 110 余人在 Anduril 塔覆盖范围内死亡，该数字为该刊自行估算[@la_mittr_towers]。一家倡导类网站称 GAO 于 2024 年按六项隐私保护措施评估 CBP 塔项目，CBP 全部未达标，未与原文核对（弱源）[@la_sos]。

反无人机合同规模最大。IBCS-M 尤马 7 天试验中，Lattice 数小时内接入一个此前未公开的传感器和效应器，实弹拦截 4 中 4，直接检验了快速集成这一核心卖点[@la_ds_ibcsm]。但未见可独立核实的实战击落记录；2026 年对伊朗的"史诗怒火行动"中，Anduril 总裁称公司是对抗"沙希德"无人机的"主要"系统，拒绝透露具体部署[@la_aol_epicfury]。

!photo madis_mk1_mk2|陆战队 MADIS Mk2 与 Mk1 在尤马集成测试，2023 年 9 月|Neil Mabini（PEO Land Systems，经 DVIDS），美国政府作品

!photo ibcs_tent|陆军 IBCS 指挥帐篷，2021 年；Lattice 后入选 IBCS-M|U.S. Army（DVIDS），美国政府作品

集群自主方面，EDGE23 演示了完整流程，Ghost Shark 原型按期、按预算完成。据《华尔街日报》报道，海军一次加州近海演习中十余艘由 Lattice C2 控制的无人艇失灵或停机，水兵警告存在"安全违规和潜在人员伤亡"，时间有 2025 年和 2024 年两说[@la_sherwood_wsj]。2025 年 7 月另一起海军无人艇掀翻支援船事故未点名 Anduril，不应混同。

CCA 角色口径冲突：Defence Industry Europe 称空军 2026 年 6 月为 CCA 下一阶段选定 LMA；另有报道称 Anduril、Shield AI 和 Collins 各获 6 个月自主软件合同条目，之后再择优[@la_die_cca,la_simpleflying]。Shield AI Hivemind 也在 Fury 上飞行，表明政府有意保持自主软件可互换。可确认的仅是 LMA 已在 Fury 上飞行，空军所有 CCA 均使用 Lattice 一说证据不足。

C2 数据层证据集中于 NGC2，陆军官方报道证实 Ivy Sting 1 运行于 Lattice Mesh[@la_army_ivysting1]；未见陆军或 GAO 对 NGC2 网络安全和可靠性的独立评估。跨域方面，Lattice 已有陆、空、水下和太空的合同或演示，盟军项目覆盖英国、新加坡、北约和澳大利亚，但跨密级能力无公开认证。

抗干扰方面，专利和 SDK 证明了 DDIL 设计，Ivy Sting 5 在通信失效下运行仅有公司说法。乌克兰是唯一可公开核实的实战场景：2022 年交付的约 40 架 Ghost 受俄方严重干扰，士兵很快失去信心；乌克兰安全局使用的 Altius 坠毁、脱靶，2024 年停用[@la_tc_wsj]。失败主要在飞行平台与数据链，未见 Lattice 在乌克兰作为 C2 层的证据。**Lattice 宣传的边缘自主与抗干扰能力迄今没有实战结果支撑。**

!photo altius600_valkyrie|XQ-58A 在尤马试验场投放 ALTIUS-600，2021 年 3 月|U.S. Air Force courtesy photo，美国政府作品

!photo ghostx_romania_flight|第 10 山地师官兵在罗马尼亚操作 Ghost-X，2024 年 11 月|U.S. Army photo by Pfc. Nathan Arellano Tlaczani，美国政府作品

!table la_cap|Lattice 能力评估：已证实、公司声称与存疑或反证|本报告依据研究笔记综合评估；"已证实"指合同、官方或独立媒体对事件的报道|26,46,44,44
能力维度|已证实|公司声称|存疑或反证
态势感知与融合|CBP 正式采购项目；SDK 证实自动关联与人工去关联[@la_cbp_por]|覆盖边境约 30%；AI 识别比人准确|无检测率与虚警率；覆盖区内 110 余人死亡（MIT TR 估算）
反无人机|多军种合同；尤马 4 中 4；Falcon Peak 拦截成功[@la_ds_ibcsm]|"完美击杀"；伊朗冲突中的"主要系统"|无可核实的实战击落；Anvil 测试引发 22 英亩野火
集群自主|EDGE23 演示；Ghost Shark 原型按期交付[@la_blog_edge23]|LMA 管理"数百个"平台|海军无人艇演习失灵；CCA 角色口径冲突
C2 数据层|NGC2 原型转入 18 亿美元推广；数据层基线[@la_ds_icorps]|火力时间缩短 90%；65 个节点|CTO"极高风险"备忘录；无独立评估
跨域与盟军|陆海空天均有合同或演示；英、新、北约、澳项目[@la_ncia_nato]|Mesh 连接全球数千系统|无经认证的跨密级方案；北约仍在评估
抗干扰|专利与 SDK 中的 DDIL 设计[@la_patent_436]|Ivy Sting 5 通信失效仍运行|乌克兰 Ghost 受干扰、Altius 停用
!end

### 竞争、锁定与负面证据

竞争方包括 NGC2 第 25 步兵师原型牵头方洛克希德·马丁、CCA 自主软件的 Shield AI、Thunderforge 牵头方 Scale AI、ABMS 云端 C2 集成商 SAIC，以及北约评估中的 Palantir 和 Athea[@la_tectonic_lockheed]。2026 年陆军向 Anduril 与 Palantir 基线收拢，据单一来源，洛克希德·马丁转为协助实施 Anduril 基线[@la_defblog_icorps]。陆军亦将"避免厂商锁定"列为通用数据层的关键考虑，但未见讨论 NGC2 数据权利的 GAO 报告或国会听证。**当反无人机、师级 C2 和企业采购都以同一数据层为中心时，SDK 许可条款将决定未来替换成本。**

其他负面记录包括：一架 Altius 在埃格林空军基地投放后垂直坠地约 8,000 英尺，一次 Anvil 测试在俄勒冈州引发 22 英亩野火，一台 Fury 发动机在地面测试中受损，多出自同一组《华尔街日报》报道的转述，原文未能读取[@la_sherwood_wsj]。Anduril 称这是武器研发的正常现象，"我们确实会失败……而且很多"，并否认存在根本性技术缺陷[@la_conard]。

## （五）案例：从边境到师级战场

:::lead
案例涵盖边境、反无人机、NGC2、空军、海上、盟国、演习和事故八类，结果多为合同或演示层面，并非实战效能数据。
:::

### 边境与反无人机

CBP 自主监视塔是 Lattice 部署时间最长、规模最大的应用，2024 年 9 月部署第 300 座，公司称覆盖约 30% 的南部陆地边境[@la_asdnews_300]。2026 年 6 月的增程塔合同属 SBIR 第三阶段 IDIQ 下的任务，新塔须与 350 余座标准塔组成的网络及 Lattice 集成；2025 年 7 月《大而美法案》为边境技术拨款，外界普遍认为该业务线将因此受益[@la_intercept_bbb]。

反无人机案例还包括 2025 年 10 月北方司令部 Falcon Peak 25.2 套件交付、2026 年 5 月陆军原型 C2 导弹防御系统合同、ORIGIN BLAZE 拦截器接入，以及华盛顿州国民警卫队第 10 民事支援队列装含 Lattice 的反无人机系统（仅有图片说明支撑）[@la_ius_falconpeak,la_bd_missiledef]。

!photo sentry_luna_nm_2|新墨西哥州卢纳县 9 号州道旁的 Sentry 塔，2022 年|Electronic Frontier Foundation（EFF），CC BY 4.0

!photo wa_ng_cuas|华盛顿州国民警卫队 2026 年列装的 Anduril 反无人机系统|Washington National Guard，美国政府作品

### 陆军 NGC2

第 4 步兵师自 2025 年 9 月 Ivy Sting 1 起持续扩展，公司称 Ivy Sting 2—5 用例超过 50 个；2026 年 5 月 Ivy Mass 中全师上线，这是项目融合—顶点 6（PC-C6）前的最后一次整师活动，特种部队同月加入 NGC2 原型实验[@la_anduril_scaling,la_milleak_ivymass]。陆军目标是 2026 年底前以 NGC2 同步两个师。

!photo ivysting1_aes|Ivy Sting 1 期间讲解 NGC2 火炮执行套件，2025 年 9 月|4th Infantry Division Public Affairs（DVIDS），美国政府作品

!photo ivysting2_ngc2|第 4 步兵师 Ivy Sting 2 演习，2025 年 10 月|4th Infantry Division Public Affairs（DVIDS），美国政府作品

作为对照，第 25 步兵师 NGC2 原型由洛克希德·马丁牵头，获 2,600 万美元、16 个月的 OTA，经"闪电涌动"系列演习验证，与 Lattice 无关[@la_army_lockheed]。**两条路线竞争的结果是 Anduril 基线成为全陆军标准，这是 Lattice 与 Foundry 组合形成锁定的关键节点。** 2024 年 3 月项目融合—顶点 4 期间，士兵与 Anduril 开展人机融合试验，但无 Lattice 作用的文字记录。

!photo pcc6_c100|PC-C6 期间第 4 步兵师士兵检查无人机，2026 年 7 月|U.S. Army（DVIDS），美国政府作品

!photo pcc4_hmi|PC-C4 期间士兵与 Anduril 开展人机融合试验，2024 年 3 月|U.S. Army（DVIDS），美国政府作品

### 空中、海上与盟国

YFQ-44A 于 2025 年 10 月 31 日首飞，2026 年 6 月获生产合同，比原计划提前约 4 个月；首架俄亥俄制造的飞机下线日期有 7 月 28 日和 7 月 30 日两种记载，该机已完成以惰性 AIM-120 对模拟目标的端到端超视距打击[@la_ds_cca_prod,la_militarytimes_rolloff]。Hermeus 为 Quarterhorse Mk 2 选用 Lattice 一说出自聚合站点（弱源）。

!photo yfq44_captive_carry|YFQ-44A 挂载 AIM-120 进行系留挂飞试验，2026 年 2 月|U.S. Air Force，美国政府作品

!photo yfq44_creech_1|克里奇空军基地空军操作的 YFQ-44A，2026 年 7 月|U.S. Air Force，美国政府作品

海上方面，Dive-LD 竞速测试中以 Lattice 实时共享位置，首台于 2025 年 4 月交付[@la_globalsec_diveld]。澳大利亚 Ghost Shark 于 2025 年 9 月转入 5 年 17 亿澳元生产合同，首批交付由 2026 年 1 月推迟至 4 月前后；Lattice 管理其自主功能一说仅见于弱源[@la_tdn_masu]。

!photo dive_ld_uuvgru1|海军无人潜航器第 1 大队训练使用 Dive-LD，2024 年 12 月|U.S. Navy（DVIDS），美国政府作品

!photo ghost_shark_minister|首艘"幽灵鲨"超大型无人潜航器原型，2024 年 4 月|© Commonwealth of Australia（Department of Defence），仅作评论引用

盟国方面，英国 2023 年 11 月授予 TALOS 第三阶段合同 1,700 万英镑（可增至 2,400 万英镑），Lattice 为核心指挥层[@la_gov_uk_17m]。北约 eAirC2 评估期约 9 个月，之后择一长期实施。科威特一揽子系统含 Roadrunner-M、Anvil、多型 Sentry 塔、电子战和 C2，由 Lattice 连接，19.8 亿美元仅为估算上限，未见签约[@la_bd_kuwait]。

台湾于 2024 年 6 月获批 291 套 ALTIUS-600M，据报道 2026 年 8 月再签约 1,554 套 Altius-700M 和 478 套 Altius-600ISR，合同金额另有 3 亿美元与 11 亿美元之争，来源均未提及 Lattice[@la_dsca_taiwan]；日本仅有 2023 年谅解备忘录，未见防卫省正式合同。

联合层级方面，路透社援引消息人士称，Anduril 与 Palantir 作为产业联合体成员共同开发"金穹"导弹防御 C2 软件平台，Lattice 的具体角色无一手来源[@la_usnews_goldendome]。关岛"勇敢之盾 2026"中基于 Lattice 的防御作战管理器仅见于二手聚合来源（弱源）。

!table la_cases|Lattice 主要演示、演习与事故|本报告依据研究笔记整理；"结果"多为合同或演示层面，非实战效能；弱源已标注|24,40,50,46
时间|用户与场合|Lattice 作用|结果
2020-09/10|空军 ABMS、AFRL 演示|巡航导弹替代目标探测与交战引导|人工确认后交战，演示成功[@la_dn_cruise]
2023|陆军 EDGE23|单兵指挥多机，自动改派 ISR|演示成功（公司博客）[@la_blog_edge23]
约 2024—2025|中央司令部沙漠守护者 1.0|第三方 C2，现场依 SDK 集成|仅有定性描述[@la_ocbj_partners]
2025-09|第 4 步兵师 Ivy Sting 1|师级目标处理，AXS 引导 M777|30 秒完成数字化准备（报道）[@la_bd_ivysting1]
2025-10|北方司令部 Falcon Peak 25.2|反无人机套件融合与交战|拦截成功，套件交付[@la_ius_falconpeak]
2025-11|陆军 IBCS-M 尤马试验|反无人机火控|数小时接入新传感器与效应器；4 中 4[@la_ds_ibcsm]
2025-10 至 2026 初|Ivy Sting 2—5|扩展网格与用例|50 余用例、65 个以上节点（公司声称）[@la_anduril_scaling]
2026-02|空军 YFQ-44A|LMA 飞行，经 A-GRA 切换|获生产合同；角色口径冲突[@la_die_cca]
2026-05|第 4 步兵师 Ivy Mass|整师上线|2,500 余台终端（公司声称）[@la_milleak_ivymass]
约 2026-08|关岛"勇敢之盾"|防御作战管理器（弱源）|未见后续合同[@la_venture_atlas]
2022—2024|乌克兰|Ghost、Altius，未见 Lattice 作为 C2|受干扰失效，Altius 停用[@la_tc_wsj]
2025 或 2024|美国海军加州近海|十余艘无人艇的 C2|失灵停机，存在安全风险[@la_sherwood_wsj]
!end

:::judge 研判要点
- **核心竞争力在实体加任务数据模型与第三方接入能力，已转化为陆军军种级锁定。**
- 证据上强下弱：采购决策为硬证据，定量效能多为公司口径，乌克兰实战结果负面。
- 强电子对抗与网络安全是短板：未经实战检验，ATO 与跨域方案未公开。
- 武器释放一贯由人批准，但交战规则配置与 3000.09 号指令的落实方式不透明。
- 与 Palantir 转向分层合作、局部竞争；建议跟踪其向金穹、CJADC2 与盟军延伸。
:::
