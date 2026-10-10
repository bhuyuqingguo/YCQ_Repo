# 一、Lattice：从边境监视塔到军种级战场数据层

:::lead
Lattice 是 Anduril Industries 的核心软件平台，2017 年随公司一同诞生。它最早只是美墨边境监视塔上的 AI 传感器融合软件，此后依次成为反无人机系统的集成内核、无人集群的任务自主软件、对第三方开放的开发平台，到 2026 年已是美陆军"下一代指挥控制"（NGC2）的通用数据层和陆军上限 200 亿美元企业合同的核心。本章按"前世今生、功能设计、架构设计、能力评估、案例"五个部分展开。功能与架构两节主要依据 Anduril 在 GitHub 公开的官方 Python SDK 源码，这是本章证据等级最高的部分；合同、演习和效能数据主要依据行业媒体与官方公告的检索摘要，多数没有逐篇读全文，文中按"已证实""公司声称""存疑或反证"分别标注。数据截至 2026 年 10 月 10 日。
:::

## （一）前世今生：九年间的四次身份转换

:::lead
Lattice 的演进可以概括为四个阶段：边境监视软件（2017—2020），反无人机系统集成内核（2020—2022），命名产品族（2023—2024，含任务自主、指挥控制和 Mesh 数据网格），以及开放平台与军种级数据层（2024 年 12 月至今）。每个阶段都对应一类新的付费用户，也对应 Anduril 估值的一次跃升。Anduril 的路线是先在国土安全领域拿到正式采购项目地位，再进入国防部；先用自筹资金做出产品，再争取合同。Lattice 是这条路线上始终不变的"粘合剂"。
:::

### 公司缘起与创始团队

Anduril Industries 于 2017 年成立，联合创始人为 Oculus 虚拟现实头显的创始人 Palmer Luckey，以及 Trae Stephens、Brian Schimpf、Matt Grimm、Joe Chen，其中三人出自 Palantir[@la_wiki_anduril,la_builtin_luckey]。成立日期有两种说法：一说公司于 2017 年 4 月 20 日注册，TechCrunch 则称其在 2017 年 6 月"悄然成立"[@la_wiki_anduril,la_tc_founding]。较合理的解释是前者为注册日、后者为公开亮相日，但没有找到一手证据。创始团队与 Palantir 的人员渊源，是理解后来两家公司"分层合作、局部竞争"关系的一条背景线索。

资本关系上，Trae Stephens 同时是 Founders Fund 的合伙人。Founders Fund 后来领投了 Anduril 2024 年的 F 轮和 2025 年的 G 轮，并在 G 轮中出资 10 亿美元[@la_andurilnews_funding,la_sacra]。Stephens 在 Founders Fund 的身份属公开常识，但本轮检索没有找到专门的一手来源。2017 年 8 月，公司完成 1,800 万美元种子轮[@la_andurilnews_funding]。

!photo luckey_ted_2025|Anduril 联合创始人帕尔默·勒基（Palmer Luckey）在 TED 大会演讲（2025 年 4 月）。勒基此前创办 Oculus，2017 年与四位合伙人共同创立 Anduril|TED Conferences（经 Flickr），CC BY 2.0

!photo trae_stephens_2024|Anduril 联合创始人、董事长特雷·斯蒂芬斯（Trae Stephens）出席 2024 年 TechCrunch StrictlyVC 活动。斯蒂芬斯出自 Palantir，同时任 Founders Fund 合伙人|TechCrunch（经 Flickr），CC BY 2.0

从一开始，Anduril 的产品逻辑就是"软件定义、硬件为载体"。公司自己研制传感器塔、无人机和拦截器，但这些硬件都通过同一个软件内核感知、通信和接受任务，这个内核就是 Lattice。正因如此，Lattice 的历史基本就是 Anduril 的业务扩张史：每进入一个新领域，Lattice 就多一类可以接入的节点。

### 边境监视塔起家（2017—2020）

Lattice 的第一个用例是为美国海关与边境保护局（CBP）在美墨边境构建"虚拟墙"。2017 年 6 月，Anduril 高管联系国土安全部（DHS）加州办公室，推销低成本边境安全方案，CBP 圣迭戈办公室随后付费让 Anduril 测试新系统[@la_wiki_anduril]。2018 年 6 月，Lattice 监视塔在德克萨斯州一位牧场主的私人土地上做了非正式测试，由 Anduril 技术员远程操作[@la_wiki_anduril]。

首个 DHS 合同的口径存在分歧。FedScoop 和 Shadowproof 记载，2018 年 6 月 Anduril 获得首个 DHS 合同，金额 480 万美元，在圣迭戈和尤马部署 10 座塔[@la_fedscoop_towers,la_shadowproof]；另一份合同梳理则只确认 2018 年 Sentry 塔首次部署于 CBP 自主监视塔（AST）试点，"480 万美元"未能在官方记录中核实[@la_privacyintl]。2019 年，CBP 创新团队在圣迭戈区测试了 5 座塔，结果成功[@la_fedscoop_towers,la_execbiz_xrst]。

2020 年是转折点。CBP 宣布自主监视塔成为美国边境巡逻队的正式采购项目（Program of Record，即列入正式预算和采购计划的项目）[@la_cbp_por,la_nextgov_2020,la_defensedaily_por]。合同金额同样说法不一：AI Business 称获得 8,500 万美元，并扩展到埃尔帕索和格兰德河谷[@la_aibusiness]；FedScoop 称金额未披露，公司高管只说"数亿美元"；Privacy International 则称 5 年 2.5 亿美元[@la_fedscoop_towers,la_privacyintl]。按 FedScoop 的说法，计划共部署 200 座塔，即在已有 60 座基础上于 2021—2022 财年再采购 140 座[@la_fedscoop_towers]。需要注意，采购项目针对的是塔项目，而不是单独的 Lattice 软件，各来源对 Lattice 本身是否被点名说法不一[@la_govconwire_dhs]。同月（2020 年 7 月），Anduril 完成 2 亿美元 C 轮融资，估值 19 亿美元[@la_aibusiness]。

!photo sentry_bfsp|位于加州圣迭戈边境州立公园的 Anduril Sentry 自主监视塔（CBP AST），2024 年拍摄。圣迭戈是 2018—2019 年 Lattice 塔最早试点的地区之一|Toyonbro（Wikimedia Commons），CC0

!photo ast_bigbend_dvids|美国边境巡逻队在西南边境大本德（Big Bend）地区运行的自主监视塔（2021 年 12 月）。AST 于 2020 年成为 CBP 正式采购项目|CBP Office of Public Affairs（DVIDS），美国政府作品

在这些塔上，Lattice 的作用是用 AI 处理雷达、光电/红外等传感器数据，识别潜在威胁，再自动向边境人员告警[@la_govconwire_dhs]。CBP 官员表示，这些塔跟踪的是"物体和活动"，不针对个人，也不做人脸识别[@la_fedscoop_towers]。从技术谱系看，Lattice 从第一天起就是一个与硬件无关的融合层，塔只是载体。正是这一点，让它后来能横向扩展到反无人机、指挥控制和集群自主。

同一时期，Lattice 开始进入空军视野。据美空军发布的照片，2020 年 9 月"先进作战管理系统"（ABMS）第二次"上匝道"（On-ramp 2）演示中，空军人员在安德鲁斯联合基地监控运行 Lattice 的计算机（见下图）。2020 年 10 月，Defense News 报道了 Anduril 在一次 AFRL/ABMS 演示中探测巡航导弹替代目标的情况：操作员确认 Lattice 正在跟踪预期目标后，向效应器下达交战指令[@la_dn_cruise]。另有材料称，Lattice 曾在一次 ABMS 演习中连接 F-16、NASAMS、MQ-9 和陆军榴弹炮，但来源没有给出准确日期，较可能是 2020—2021 年的"上匝道"系列[@la_af_abms,la_lodi411]。

!photo lattice_abms_onramp2|2020 年 9 月 2 日，美空军 ABMS 第二次"上匝道"演示期间，空军人员在安德鲁斯联合基地监控运行 Lattice 的计算机。这是 Lattice 界面较早出现在美军官方图片中的一例|U.S. Air Force photo by Senior Airman Daniel Hernandez，美国政府作品

### 进入国防部：SOCOM 反无人机系统集成（2021—2022）

Lattice 进入国防体系的第一步，是英国而非美国。2021 年 9 月，英国国防部战略司令部的 jHub 授予 Anduril 一份 380 万英镑（约 520 万美元）、最长 2 年的 TALOS 基地防御试验合同，系统基于 Lattice，用 Sentry 塔、地面传感器和无人机检测、分类和跟踪地面与空中入侵[@la_edr_talos,la_blog_talos]。

真正的转折是 2022 年 1 月。美国特种作战司令部（SOCOM）选定 Anduril 为反无人系统（C-UxS）的系统集成伙伴（SIP）。合同为 10 年期 IDIQ（编号 H92402-22-D-0001），上限 967,599,957 美元，授予时实际拨付仅 1,096,092 美元（2022 财年运维经费），期限至 2032 年 1 月 19 日[@la_wt_socom,la_afcea_socom]。Anduril 从 12 份提案中胜出，媒体常表述为"击败另外 11 家"，金额常被约称为"10 亿美元"，Monch 记为 9.68 亿美元[@la_dn_socom,la_monch_cuxs]。GovConWire 把完成日期误写成 2023 年，应以 2032 年为准[@la_govconwire_socom]。

这份合同的内容是集成传感器与效应器，构建分层反无人机体系，交付 Lattice 软件，并配套 Sentry 塔、Anvil 拦截无人机、Pulsar 电子战系统和 FoxHound[@la_wt_socom,la_anduril_blog_socom]。合同明确要求集成第三方传感器与效应器[@la_dn_socom]。Lattice 在其中负责"自主检测、分类、跟踪目标，向操作员告警并提供处置与交战选项"[@la_afcea_socom,la_fedscoop_socom]。公司在这一时期提出："每一件 Anduril 产品都内置 Lattice AI Core，在边缘完成传感器融合、目标分类和多航迹调和"[@la_airrec_socom]。这一表述属于公司口径，但它清楚说明了 Lattice 的设计取向：智能尽量下沉到每个节点，而不是全部集中在后方。

SOCOM 合同的意义在于，Lattice 第一次以"系统集成内核"的身份进入国防部，而不只是某件硬件的附属软件。同年 Anduril 收购 Dive Technologies，2022 年还向乌克兰提供约 40 架 Ghost 侦察无人机（其表现见第四节）[@la_contrary,la_tc_wsj]。2022 年 12 月，公司完成 14.8 亿美元 E 轮融资，投后估值 84.8 亿美元[@la_andurilnews_funding,la_sacra]。

### 产品化：任务自主、Mesh 数据网格、SDK 与 Lattice for C2（2023—2024）

2023 年 5 月 3 日，Anduril 发布 Lattice for Mission Autonomy（LMA，任务自主），这是 Lattice 第一个对外命名的产品。公司把它定义为"硬件无关、端到端"的平台，可在人类监督下管理"数百个"异构无人系统，理念是从"多人操控一个自主系统"转为"一人操控多个"[@la_dn_lma,la_blog_lma]。功能覆盖风险与威胁建模、作战分析、训练与演习、任务前规划、指挥控制和任务后复盘，并包括自主驾驶、威胁识别、多平台机动编排以及电磁特征与通信管理[@la_blog_lma,la_d1_lma]。同年陆军 EDGE23 演习中，一名士兵用 LMA 协调多家厂商的无人机，定位并摧毁了地空导弹阵地[@la_blog_edge23]。SOCOM 随后还选定 Anduril 为其"任务自主系统集成伙伴"[@la_monch_mas]，另有一笔 8,600 万美元合同用于帮助 SOCOM 控制其无人机，日期未核实[@la_tectonic_86m]。

Lattice Mesh 是第二条产品线。它的技术根源可以追溯到 Anduril 的专利 US 10,506,436（公开号 US 2020/0068404），核心原则是"实时数据是系统的优先级，回填只使用剩余带宽"[@la_patent_436,la_patent_pub]。2024 年 12 月 3 日，国防部首席数字与人工智能办公室（CDAO）授予 Anduril 一份 3 年期、1 亿美元的生产型其他交易协议（OTA），推广建立在 Lattice Mesh 上的"边缘数据网格"，授予时拨付约 3,300 万美元。该协议源自"全球信息优势实验"（GIDE）的原型 OT，属于联合全域指挥控制（CJADC2）的组成部分[@la_ds_cdao,la_anduril_cdao,la_insidedef_cdao]。期限另有 4 年一说[@la_orangeslices_cdao]。授予时，这一网格已"在多个军种和作战司令部运行"[@la_ds_cdao]。2024 年 11 月 21 日，太空军太空系统司令部还授予约 9,970 万美元（另记 9,960 万美元）的太空监视网（SSN）现代化合同，以 Lattice 作为弹性网状网络，要求 2026 年底完成部署[@la_ds_ssn,la_bd_ssn,la_spaceinsider,la_execbiz_ssn]。

第三条线是平台化。2024 年 12 月 6 日，Anduril 与 Palantir 宣布合作：由 Lattice 和 Menace 系列可部署计算/通信设备采集战场边缘数据，再送入 Palantir AIP 平台，为 AI 训练准备数据，包括 SCI/SAP 等最高密级数据[@la_bw_palantir,la_bnn_palantir]。报道还称，双方计划把 Lattice、Menace 与 Palantir AIP 和 Maven 智能系统结合起来，形成"从边缘到企业"的链路[@la_ds_palantir]。2024 年 12 月 10 日，Lattice SDK 公开发布，同时推出 Lattice 合作伙伴计划，首批 10 余家伙伴包括 Apex、Forterra、Impulse Space、Numerica、Oracle、Saronic、Scale AI、Spire Global、Striveworks、Textron Systems 和 Valinor[@la_dd_sdk,la_x_sdk,la_ocbj_partners,la_bd_cdao]。SDK 面向"没有中心云、通信降级"的边缘环境，内容包括数据模型定义、API 绑定、示例代码和参考实现[@la_dd_sdk,la_ocbj_partners]。

"Lattice for Command and Control"（Lattice for C2）也在这一时期出现，被描述为 AI 战斗管理平台[@la_bd_tag,la_ua_20b]。不过，Lattice Mesh 和 Lattice for C2 的正式发布日期都没有找到，Lattice 也没有公开的版本号体系；"Lattice OS"是否经历过正式更名，同样没有一手证据。

!photo lattice_demo_mittr|2024 年 12 月 MIT Technology Review 记者现场观看的 Lattice 反无人机/基地防御演示界面截图。界面以地图为底，叠加航迹实体、己方资产和告警|Anduril Industries / MIT Technology Review，公司图片，仅作评论引用

这一阶段的其他节点包括：2024 年 2 月，海军 PMS 394 与国防创新单元（DIU）选定 Anduril 等三家研制 Dive-LD 大型无人潜航器原型，竞速测试中用 Lattice 实时跟踪和共享 Dive-LD 位置[@la_dn_diveld,la_globalsec_diveld]；2024 年 4 月 24 日，Anduril 与通用原子公司在空军"协同作战飞机"（CCA）第一增量中胜出[@la_ds_cca1,la_twz_cca1]；2024 年 9 月，第 300 座 AST 部署，公司称覆盖约 30% 的南部陆地边境[@la_asdnews_300]；2024 年 10 月，国防部一份约 2.5 亿美元合同采购 500 发 Roadrunner-M 全备弹和 Pulsar[@la_dn_roadrunner]；2024 年 11 月，陆战队授予约 2 亿美元的 MADIS 反无人机交战系统合同[@la_ius_madis,la_overt_642]。

### 收购扩展：给 Lattice 补齐末端节点

Anduril 的收购有一条清晰主线：给 Lattice 补上可以感知或可以打击的"末端节点"。每一笔收购都增加一类可被 Lattice 编排的平台，平台的锁定效应也随之加强。部分收购日期在不同来源中存在冲突，下表并列给出。

!table la_acq|Anduril 主要收购及其对 Lattice 的补强|依据 Contrary Research、Janes、Built In、PrivSource 等整理；日期冲突处并列|26,34,56,44
时间|标的|对 Lattice 的意义|备注与来源
2021-04（另记 2022-10）|Area-I|补齐空射效应器 ALTIUS 系列，可由 LMA 编组调度|保留品牌、全资子公司；日期冲突[@la_contrary,la_andurilnews_acq]
2022-02（另记 2023-03）|Dive Technologies|补齐水下节点，后改组为 Anduril Maritime，是 Ghost Shark、Dive-LD 的基础|日期冲突[@la_contrary,la_notboring]
2023-06|Adranos|固体火箭发动机，服务弹药产能|与 Lattice 无直接关系[@la_builtin_what]
2023-09-07|Blue Force Technologies|Fury 自主飞机，后发展为 YFQ-44A，成为 CCA 第一增量两家胜出方之一|[@la_janes_blueforce,la_wiki_yfq44]
2025-01（宣布）|Numerica 雷达与 C2 业务|补齐 Spyglass、Spark 雷达与 Mimir C2 软件|完成日期未核实[@la_builtin_what,la_contrary]
2025-05-05（签约）|Klas|Voyager 坚固边缘计算与战术通信硬件，成为 Menace 系列的硬件底座|完成日期未核实[@la_privsource_klas,la_builtin_what]
!end

合作层面，Anduril 与 Palantir 的联盟最为重要。2024 年 12 月 22 日，英国《金融时报》和路透社报道，两家正与 SpaceX、OpenAI、Saronic、Scale AI 等约十几家公司商谈组建联合投标集团，挑战传统主承包商，但成员名单来自匿名消息源，之后也没有找到正式成立的证据[@la_tc_consortium]。更准确的描述是：Anduril 与 Palantir 形成了一种稳定的"组队模式"，此后在陆军 NGC2 和"金穹"导弹防御 C2 软件上反复同场出现[@la_dn_ngc2_award,la_usnews_goldendome]。

### 融资与增长：估值曲线与 Lattice 地位同步上升

Anduril 的估值从 2019 年 B 轮的约 10 亿美元，涨到 2026 年 5 月 H 轮的 610 亿美元，7 年增长约 60 倍。各轮次数据见{tab:la_funding}和{fig:c_anduril_funding}。

!table la_funding|Anduril 历轮融资与估值|依据 andurilnews 融资追踪、Sacra、TechCrunch、CNBC、Defense News 整理；金额单位美元|22,20,26,30,62
时间|轮次|融资额|估值|领投方与说明
2017-08|种子轮|1,800 万|未披露|[@la_andurilnews_funding]
2018-06|A 轮|未披露|2.62 亿|Multiples.vc 记载，日期与种子轮有 2017/2018 混淆[@la_multiples]
2019-09|B 轮|未披露|约 10 亿|a16z[@la_andurilnews_funding,la_sacra]
2020-07|C 轮|2 亿|19 亿|a16z；同期获 CBP 塔合同[@la_aibusiness]
2021-06|D 轮|4.5 亿|46 亿（Sacra 记约 47 亿）|Elad Gil[@la_andurilnews_funding,la_sacra]
2022-12|E 轮|14.8 亿|84.8 亿（投后）|Valor[@la_andurilnews_funding]
2024-08|F 轮|15 亿|140 亿|Founders Fund、Sands Capital[@la_andurilnews_funding,la_sacra]
2025-06|G 轮|25 亿|305 亿|Founders Fund（出资 10 亿）[@la_andurilnews_funding,la_sacra]
2026-05-13|H 轮|50 亿|610 亿|Thrive Capital、a16z[@la_tc_seriesh,la_cnbc_seriesh]
2026-07-24|洽谈中|未披露|约 1,000 亿|路透社报道，未见交割确认[@la_dn_100b,la_tc_100b]
!end

!fig c_anduril_funding|c_anduril_funding.png|Anduril 历轮估值、融资额与营收（2017—2026）|本报告依据 andurilnews、Sacra、TechCrunch、CNBC 数据绘制；营收为公司口径|160

几组数据需要谨慎对待。估值方面，Tracxn 列出 2026 年 9 月估值 1,110 亿美元，与其他来源均不符，应视为离群值[@la_tracxn]。累计融资额有 62.6 亿、69 亿、111.3 亿和 113 亿美元等多种说法[@la_acquinox,la_fnex,la_tracxn]。营收方面，2024 年约 10 亿美元，2025 年 22 亿美元（增长 120%），2026 年目标约 43 亿美元，均为公司口径、未经审计[@la_sacra,la_cnbc_seriesh]。员工人数没有找到可靠的分年数据。截至 2026 年 10 月，公司尚未宣布 IPO 时间表[@la_yahoo_ipo,la_tc_seriesh]。

产能是另一条增长线。2025 年 1 月 16 日，Anduril 宣布在俄亥俄州皮卡韦县建设"武库-1"（Arsenal-1）工厂，占地 500 英亩、建筑面积 500 万平方英尺，承诺到 2035 年创造约 4,000 个岗位，获 JobsOhio 3.1 亿美元资助和州税收抵免 4.522 亿美元[@la_dn_arsenal1,la_ohio_arsenal1]。2026 年 3 月，Fury 在此开始生产，计划到 2026 年底同时生产 Fury、Roadrunner、Barracuda 和一种保密平台[@la_bd_arsenal1]。首架俄亥俄制造的 YFQ-44A 下线时间有 2026 年 7 月 28 日（Military Times）和 7 月 30 日（追踪站点）两种说法[@la_militarytimes_rolloff,la_andurilnews_mfg]。2026 年 10 月 6 日，海军授予上限 29 亿美元的弗吉尼亚级潜艇部件合同，在巴尔的摩建设"武库-2"船厂，Anduril 自投 37 亿美元[@la_cnbc_sub,la_janes_sub]。

!photo arsenal1_rendering|Anduril"武库-1"（Arsenal-1）俄亥俄州超大规模工厂效果图（2025 年 1 月发布，非实拍）。工厂 2026 年 3 月开始生产 Fury，计划扩展到 Roadrunner、Barracuda 等|Anduril Industries 效果图，公司图片，仅作评论引用

把估值曲线和合同节点对照起来看，可以发现两者高度同步：2022 年 SOCOM 合同后进入 E 轮；2025—2026 年 NGC2、200 亿美元企业合同和 CCA 相继落地，估值随之翻倍。这说明资本市场把 Anduril 当作"软件平台型主承包商"来定价，而不只是一家硬件公司，而 Lattice 正是这一定价的核心依据。

### 2025—2026：从"自家硬件的操作系统"到"军种级通用数据层"

2025 年起，Lattice 的合同从"给 Anduril 硬件配软件"转向"给整个军种当数据层"。主要节点如下。

反无人机线持续放大。2025 年 3 月，陆战队授予 10 年期"设施反小型无人机"（I-CsUAS）IDIQ 合同，上限 6.42 亿美元（另记 6.422 亿），期限至 2035 年 3 月，内容为 Lattice C2 加 Anvil 和 Pulsar 电子战，Anduril 在 9 家（另记 10 家）竞标者中胜出，首笔 950 万美元来自 2024 财年采购预算[@la_ds_icsuas,la_wt_icsuas,la_edr_icsuas]。2025 年 11 月 10 日，陆军选定 Lattice 作为"机动型一体化作战指挥系统"（IBCS-M）的反无人机火控与 C2 平台[@la_ds_ibcsm,la_janes_ibcsm]。2026 年 3 月 13—14 日，陆军授予 Anduril 一份 10 年期企业合同（5 年基础期加 5 年选择期，预计 2036 年 3 月 12 日完成），上限 200 亿美元，固定价格，把 120 多项采购行动并入一个以 Lattice 为中心的框架，涵盖 Lattice 软件、集成硬件、数据、算力和支持服务，其他联邦机构也可以使用[@la_ds_20b,la_army_20b,la_ius_20b]。陆军强调这是"没有附带资金的合同载体"，200 亿美元是上限，不是承诺支出[@la_army_20b,la_bd_jiatf]。首个任务单用于联合跨机构特遣部队 401（JIATF 401）的"通用反无人机 C2"，金额有 8,770 万美元和 8,700 万美元两种记法[@la_ds_20b,la_bd_jiatf,la_d1_jiatf]。2026 年 5 月，Anduril 又获得陆军原型 C2 导弹防御系统合同[@la_bd_missiledef]。

指挥控制线突破最大。2025 年 4 月 NGC2 项目办公室成立；7 月 18 日，陆军授予 Anduril 一份 9,960 万美元、为期 11 个月的 OTA，牵头为第 4 步兵师交付 NGC2 原型，"Team Anduril"成员包括 Palantir、Microsoft、Striveworks、Govini、Instant Connect Enterprise 和 Research Innovations Inc.[@la_army_ngc2_award,la_tdp_ngc2,la_ds_ngc2_award]。2025 年 9 月 Ivy Sting 1 实弹演习中，师级目标处理流程完全运行在 Lattice Mesh 和 Palantir Target Workbench 上[@la_die_ivysting1,la_ss_ivysting1]。2026 年 6 月 22 日，陆军指定 Anduril 牵头 NGC2"通用数据层基线"，数据网格由"Anduril 的 Lattice 与 Palantir 的 Foundry"共同构成[@la_ds_cdl,la_bd_cdl]。2026 年 10 月 5—6 日，陆军授予 Anduril 一份 5 年期、上限 18 亿美元（基础期 1.628 亿美元）的 NGC2 推广合同，从第 1 军（I Corps）开始；Anduril 在新闻稿中把 Lattice 描述为连接应用、数据、AI 模型、传感器和载具的"分布式数据层"[@la_anduril_ngc2_scale,la_govconwire_icorps,la_asdnews_icorps,la_ds_icorps]。

空中、联盟和边境三条线同步推进。2026 年 2 月 24 日，LMA 首次在 YFQ-44A 上飞行；2026 年 6 月，据报道空军在 CCA 下一阶段选定 LMA（这一点在不同来源中有出入，见第四节）[@la_die_cca]。2026 年 7 月 7 日，北约通信与信息局（NCIA）选择 Lattice 参加"增强型空中指挥控制"（eAirC2）数据平台评估，这是 Anduril 的首个北约合同，评估期约 9 个月，同场的还有 Palantir 和 Athea[@la_anduril_nato,la_ncia_nato,la_battlepolicy_nato]。2026 年 6 月，CBP 以 3.63 亿美元（精确为 362,974,500 美元）采购 200 余座增程型 Sentry 塔（XRST），说明边境这条起家业务仍在扩张[@la_anduril_xrst,la_execbiz_xrst]。同月，美国国务院批准向科威特出售包含 Lattice 在内、估值 19.8 亿美元的反无人机一揽子系统[@la_bd_kuwait,la_armyrec_kuwait]。

!fig c_anduril_contracts|c_anduril_contracts.png|Anduril 主要合同金额（按时间，对数坐标）|本报告依据各合同公告与行业媒体整理；上限、已拨付与 FMS 估值口径不同，不可简单相加|160

开发者平台在 2026 年也在快速迭代。按开发者更新日志的检索摘要：6 月 9 日上线 Developer Console，7 月 23 日推出 Lattice Schema Registry，8 月 3 日发布面向 AI 编程智能体的官方"Lattice SDK skills"，9 月 9 日 Video API 进入预览，9 月 17 日 Schema 自动同步到沙箱，10 月 5 日发布 Rust（REST）SDK[@la_changelog]。这些日期来自搜索摘要，没有逐条打开核实。

截至 2026 年 10 月，可以这样概括 Lattice 的地位：它是美陆军反无人机（200 亿美元企业合同和 JIATF 401）和 NGC2（I 军推广，上限 18 亿美元）的核心数据层，进入了空军 CCA 下一阶段，赢得首个北约合同，边境业务仍在扩张。它的竞争格局也随之变化，从"对抗传统主承包商"转为"与 Palantir 分层合作、在部分招标中直接竞争"，北约 eAirC2 就是两家同场竞争的例子[@la_battlepolicy_nato]。

### 合同结构的演进：从试点到"企业协议加任务单"

把 Anduril 的合同按时间排开，可以看到三次结构性变化。2018—2021 年以试点和小额试验为主，例如 CBP 塔试点和英国 TALOS 试验；2022 年起出现 IDIQ 和 OTA 形式的大额上限合同，SOCOM 的 9.676 亿美元合同是第一个接近十亿量级的；2026 年进入"企业协议加任务单"模式，陆军 200 亿美元企业合同之下，JIATF 401 这类后续订单以任务单形式出现，单独公告可能因此减少[@la_wt_socom,la_ds_20b,la_bd_jiatf]。NGC2 从 2025 年 9,960 万美元原型到 2026 年 18 亿美元推广，只用了约 15 个月，说明"原型 OTA 转生产"的路径已经打通[@la_army_ngc2_award,la_ds_icorps]。

更重要的是 Lattice 在这些合同中的位置。几乎所有 C2、反无人机和传感器网络类合同都明确以 Lattice 为核心，而硬件和弹药类合同（固体火箭发动机、Altius、Barracuda、CCA 机体、潜艇部件）的来源通常不提 Lattice。下表列出来源中明确写到 Lattice 的主要合同。

!table la_lcontracts|来源明确提到 Lattice 的主要合同|本报告依据合同公告与行业媒体整理；上限、已拨付与 FMS 估值口径不同|22,36,34,68
时间|客户与项目|金额|Lattice 在其中的作用
2021-09|英国国防部 TALOS 基地防御试验|380 万英镑|系统运行在 Lattice 上，检测、分类、跟踪地面与空中入侵[@la_blog_talos]
2022-01|SOCOM 反无人系统集成伙伴|上限 9.676 亿美元|交付 Lattice 平台，集成 Sentry、Anvil、Pulsar、FoxHound[@la_wt_socom]
2024-02|海军与 DIU Dive-LD 原型|未披露|竞速测试中用 Lattice 实时跟踪和共享位置[@la_globalsec_diveld]
2024-11|太空军 SSN 现代化|约 9,970 万美元|交付 Lattice 作为弹性网状网络[@la_ds_ssn]
2024-12|CDAO 边缘数据集成服务|1 亿美元|Lattice 驱动的边缘数据网格[@la_ds_cdao]
2025-03|陆战队 I-CsUAS|上限 6.42 亿美元|核心软件为 Lattice[@la_ius_madis]
2025-09|陆军 SBMC 第一阶段|1.59 亿美元（硬件）|SBMC-A 数据与 AI 架构建立在 Lattice C2 上[@la_bd_eagleeye,la_uploadvr]
2025-11|陆军 IBCS-M|未披露|Lattice 作为反无人机火控与集成骨干[@la_mes_ibcsm]
2026-03|陆军企业协议|上限 200 亿美元|涵盖 Lattice 软件、硬件、数据、算力与服务[@la_army_20b]
2026-03|陆军 JIATF 401 首个任务单|约 8,700 万美元|Lattice 作为反无人机 C2 骨干[@la_d1_jiatf]
2026-06|CBP 增程 Sentry 塔|3.63 亿美元|新塔与 Lattice 及既有塔网络集成[@la_execbiz_xrst]
2026-07|北约 NCIA eAirC2 评估|未披露|在北约环境中部署 Lattice[@la_die_nato]
!end

按公开上限粗算，这些明确提到 Lattice 的合同（不含 200 亿美元企业协议）合计约 22 亿美元；计入企业协议约 220 亿美元；如果把普遍被认为基于 Lattice 的两份 NGC2 合同（9,960 万美元和 18 亿美元）也算进去，还要再加约 19 亿美元。需要强调，上限、已拨付金额和对外军售批准估值是三种不同口径，不能直接相加；JIATF 401 的任务单也已包含在 200 亿美元企业协议之内，不能重复计算。

### 大事年表

!table la_timeline|Lattice 与 Anduril 大事年表（2017—2026 年 10 月）|本报告依据研究笔记整理；金额为上限或报道值，冲突处并列|24,70,34,32
时间|事件|阶段意义|来源
2017-04/06|Anduril 成立（4 月注册说与 6 月公开说并存），Lattice 同期开发；6 月向 DHS 加州办公室推销边境方案|边境监视软件起步|[@la_wiki_anduril,la_tc_founding]
2017-08|种子轮 1,800 万美元|启动资金|[@la_andurilnews_funding]
2018-06|德州私人牧场非正式测试；首个 DHS 合同（480 万美元、10 座塔，金额未经官方核实）|第一个付费用户|[@la_wiki_anduril,la_fedscoop_towers]
2019|CBP 在圣迭戈测试 5 座塔，结果成功；B 轮估值约 10 亿美元|技术验证|[@la_fedscoop_towers,la_sacra]
2020-07|AST 成为 CBP 正式采购项目；C 轮 2 亿美元，估值 19 亿美元|首个采购项目|[@la_cbp_por,la_aibusiness]
2020-09/10|ABMS 第二次"上匝道"演示；AFRL 巡航导弹替代目标探测演示，人确认后下达交战指令|进入空军与防空场景|[@la_dn_cruise]
2021-04|收购 Area-I（日期另记 2022-10）|补齐空射效应器|[@la_contrary]
2021-06|D 轮 4.5 亿美元，估值 46 亿美元|扩张|[@la_andurilnews_funding]
2021-09|英国 TALOS 基地防御试验合同 380 万英镑，基于 Lattice|首个海外国防合同|[@la_edr_talos]
2022-01|SOCOM 反无人系统集成伙伴，10 年 IDIQ，上限 9.676 亿美元|进入国防部的转折点|[@la_dn_socom,la_afcea_socom]
2022|收购 Dive Technologies；约 40 架 Ghost 交付乌克兰；E 轮估值 84.8 亿美元|水下节点与首次实战|[@la_contrary,la_tc_wsj]
2023-05-03|发布 Lattice for Mission Autonomy|首个命名产品|[@la_dn_lma,la_blog_lma]
2023|EDGE23：单兵指挥多型无人机摧毁地空导弹阵地，系统自动改派 ISR 做毁伤评估|集群自主公开演示|[@la_blog_edge23]
2023-09-07|收购 Blue Force（Fury）|进入大型自主飞机|[@la_janes_blueforce]
2023-11|英国 TALOS 第三阶段合同 1,700 万英镑（可增至 2,400 万）|海外持续|[@la_gov_uk_17m]
2024-02|Dive-LD 原型（DIU/海军），用 Lattice 实时跟踪位置|水下|[@la_dn_diveld,la_globalsec_diveld]
2024-04-24|CCA 第一增量胜出（与 GA）|进入 CCA|[@la_ds_cca1]
2024-08|F 轮 15 亿美元，估值 140 亿美元|—|[@la_andurilnews_funding]
2024-09|第 300 座 AST 部署（公司称覆盖约 30% 南部陆地边境）|边境规模化|[@la_asdnews_300]
2024-11|陆战队 MADIS 交战系统约 2 亿美元；太空军 SSN 现代化约 9,970 万美元，用 Lattice 组网|多军种、进入太空|[@la_ius_madis,la_ds_ssn]
2024-12-03|CDAO 1 亿美元生产型 OTA，推广 Lattice Mesh 边缘数据网格|Mesh 成为采购对象|[@la_ds_cdao]
2024-12-06|与 Palantir 宣布合作（Lattice/Menace 加 AIP）|两大系统结盟|[@la_bw_palantir]
2024-12-10|Lattice SDK 公开发布，合作伙伴计划首批 10 余家|平台化|[@la_dd_sdk,la_ocbj_partners]
2025-01|宣布收购 Numerica 雷达与 C2 业务；宣布建设 Arsenal-1|雷达与产能|[@la_builtin_what,la_dn_arsenal1]
2025-03|陆战队 I-CsUAS 上限 6.42 亿美元；DIU Thunderforge 以 Lattice 为数据共享层；新加坡 DSTA/RSAF 合作|多军种、国际化|[@la_ds_icsuas,la_diu_thunderforge,la_amr_singapore]
2025-05|签约收购 Klas；发布 Menace-T/X 边缘 C4 套件|边缘硬件|[@la_privsource_klas,la_tc_menace]
2025-06|G 轮 25 亿美元，估值 305 亿美元|—|[@la_andurilnews_funding]
2025-07-18|NGC2 原型 OTA 9,960 万美元（第 4 步兵师）|进入师级 C2|[@la_army_ngc2_award]
2025-09|Ivy Sting 1 实弹：师级目标处理运行在 Lattice Mesh 与 Target Workbench 上；陆军 CTO 备忘录评为"极高风险"|首次实弹杀伤链集成|[@la_die_ivysting1,la_reuters_memo]
2025-10|Falcon Peak 25.2 反无人机演示并交付北方司令部；YFQ-44A 首飞（10-31）|—|[@la_ius_falconpeak,la_twz_production]
2025-11-10|陆军选定 Lattice 为 IBCS-M 反无人机火控，尤马实弹 4 中 4|进入陆军防空体系|[@la_ds_ibcsm]
2026-02-24|LMA 首次在 YFQ-44A 上飞行|进入 CCA 自主|[@la_die_cca]
2026-03-13/14|陆军 10 年期企业合同，上限 200 亿美元；JIATF 401 首单约 8,700 万美元|军种级锁定|[@la_ds_20b,la_bd_jiatf]
2026-05|H 轮 50 亿美元，估值 610 亿美元；Ivy Mass 第 4 步兵师整师上线；陆军原型 C2 导弹防御合同|—|[@la_tc_seriesh,la_milleak_ivymass,la_bd_missiledef]
2026-06|NGC2 通用数据层基线（Lattice 加 Foundry）；CBP 增程塔 3.63 亿美元；科威特 19.8 亿美元军售获批；CCA 生产合同|三线同时扩张|[@la_ds_cdl,la_anduril_xrst,la_bd_kuwait,la_ds_cca_prod]
2026-07-07|北约 NCIA 选择 Lattice 参加 eAirC2 数据平台评估|首个北约合同|[@la_anduril_nato]
2026-10-01|ORIGIN 公司 BLAZE 拦截器集成进 Lattice|第三方效应器接入|[@la_overt_blaze]
2026-10-05/06|NGC2 推广合同，5 年上限 18 亿美元，从第 1 军开始；Rust SDK 发布|从原型转入部署|[@la_ds_icorps,la_changelog]
!end

## （二）功能设计：以实体为中心的作战图与军事化任务链

:::lead
Lattice 的功能设计可以从 Anduril 在 GitHub 公开的官方 Python SDK 直接还原。该 SDK 由 Lattice 的 OpenAPI 规范自动生成，字段名、枚举值和接口注释都是一手证据。还原的结果是：Lattice 的核心是一张以"实体"（Entity）为中心的共用作战图（COP），航迹、己方资产、地理区域、信号源都被建模为实体；其上有三类接口，"实体"负责发布、订阅与人工覆写，"任务"负责在操作员与无人平台、效应器之间流转军事化指令，"对象"负责在网格中同步文件。公开数据模型里直接写入了敌我属性、Link 16 风格的"强度"、0—15 级航迹质量、逐字段密级标记和"将遵照执行"（WILCO）这类军事概念，可见它从设计上就是一套作战软件，而不是借用民用物联网平台改出来的。
:::

### 总体思路：一张由"实体"构成的共用作战图

SDK 对 Entity 的定义是"代表 Lattice 作战环境中的一个已知对象"，实体的全部数据都放在"组件"（component）中[@la_sdk_entity]。实时订阅接口 StreamEntities 的注释写明，它"让客户端维护共用作战图（COP）的实时视图"[@la_sdk_ref]。换句话说，Lattice 不是先有一张地图、再往上叠加图层，而是先有一个实体集合，地图、列表、告警都只是对这个集合的不同呈现。

这种设计有三个直接后果。第一，任何新传感器或新平台只要能把自己的输出翻译成实体，就能进入 COP，这是"硬件无关"的技术基础。第二，所有实体都带时效和溯源，过期即消失，修改留痕，这为杀伤链上的追责提供了数据基础。第三，"任务"也是围绕实体组织的：打击任务的目标是一个实体，执行任务的平台也是一个实体，平台能做什么写在它自己的实体组件里。

!fig d_lattice_entity_task|d_lattice_entity_task.png|Lattice 实体组件模型与任务生命周期状态机|本报告依据 Anduril 官方 lattice-sdk-python 源码（entity.py、task_status_status.py 等）绘制|160

### 实体数据模型：30 余个可选组件覆盖全域

SDK 列出的实体顶层字段与组件包括：entity_id、description、is_live、created_time、expiry_time、no_expiry、status、location、location_uncertainty、kinematics、geo_shape、geo_details、aliases、tracked、correlation、mil_view、ontology、sensors、payloads、power_state、provenance、overrides、indicators、target_priority、signal、transponder_codes、data_classification、task_catalog、media、relationships、visual_details、dimensions、route_details、schedules、health、group_details、supplies、orbit、symbology[@la_sdk_entity]。

几项设计细节值得专业读者注意。

其一，位置与运动学二选一。文档要求 location 和 kinematics 只填其一，不要同时填写，航迹实体"优先使用 kinematics"[@la_sdk_entity]。这说明 Lattice 区分"静态位置描述"和"带速度、加速度的运动状态"，后者是航迹外推和火控解算的输入。

其二，强制时效。发布实体时 expiry_time 是必填项，"必须在未来，但距当前时间少于 30 天"，且发布时 is_live 必须为真[@la_sdk_entity]。这意味着 COP 中不存在"永久有效"的外部数据，陈旧信息会自动退出作战图。对于目标数据来说，这一设计直接针对"用过期情报打击"的风险。

其三，覆盖太空与电磁域。orbit 组件的注释是"空间目标的轨道信息"，signal 组件描述"关注信号"[@la_sdk_entity]。transponder_codes 用于应答机和敌我识别代码，symbology 组件"遵循既有标准"表达军标符号[@la_sdk_entity]。supplies 组件则可以表达补给状态。结合合作伙伴中有 Impulse Space、Spire（太空）和 Saronic（无人艇），可以推断这套模型面向陆海空天电全域设计（推断）[@la_ocbj_partners]。

其四，丰富的关系与编组表达。relationships、group_details、route_details、schedules 等组件让实体之间可以表达隶属、编组、航路和时间计划，sensors 与 payloads 组件描述平台挂载的传感器和载荷[@la_sdk_entity]。

### 本体模板：战场对象的五种基本类型

实体的类型由 ontology 组件决定，其中的"本体模板"规定了该类实体至少要带哪些组件。公开 SDK 中共有五种模板：TEMPLATE_TRACK（航迹）、TEMPLATE_SENSOR_POINT_OF_INTEREST（传感器关注点）、TEMPLATE_ASSET（资产，即己方可控平台）、TEMPLATE_GEO（地理形状，如地理围栏和区域）、TEMPLATE_SIGNAL_OF_INTEREST（关注信号）[@la_sdk_ontology,la_sdk_ontology_tpl]。ontology 组件还带有 platform_type 和 specific_type 两个字段，用于细化平台类别和具体型号[@la_sdk_ontology]。

这五类基本对象恰好对应一个战术 C2 系统需要处理的全部内容：别人的东西（航迹、信号）、自己的东西（资产）、空间规则（地理区域）以及需要进一步核查的线索（关注点）。值得注意的是，地理围栏在公开模型中并没有独立的接口，而是带 geo_shape 和 geo_details 组件的实体（推断）[@la_sdk_ontology_tpl]。限入区、禁飞区、交战区因此也能像目标一样被发布、订阅和随任务下发。

### 敌我属性：与美军和北约标准一致

mil_view 组件承载识别与属性信息。disposition（敌我属性）的枚举值为：UNKNOWN（不明）、FRIENDLY（友）、HOSTILE（敌）、SUSPICIOUS（可疑）、ASSUMED_FRIENDLY（假定友）、NEUTRAL（中立）、PENDING（待定）[@la_sdk_milview_disp]。mil_view 还包含 environment（所处环境，如空中、水面、地面）和 nationality（国籍）字段[@la_sdk_milview]。这套枚举与北约和美军通用的敌我属性分类基本一致，方便与战术数据链和军标符号系统对接。

在交战流程中，disposition 是最关键的字段之一：把一个航迹的属性改为 HOSTILE，就是"识别"环节的结论。SDK 示例中给出的可覆写字段路径恰好就是 mil_view.disposition，这说明"由人改定敌我属性"是系统设计时就考虑到的核心操作[@la_sdk_ref]。

### 航迹质量、融合与关联：自动关联器加人工否决

tracked 组件描述航迹本身的质量，包含 track_quality_wrapper（注释为"质量评分，0—15"）、sensor_hits（传感器命中数）、radar_cross_section（雷达截面积）和 number_of_objects。number_of_objects 的注释特意说明"在某些语境下称为强度（Strength），见 Link 16"[@la_sdk_tracked]。0—15 级的航迹质量和"强度"概念，都与美军战术数据链的习惯一致。

correlation 组件实现多传感器航迹融合。多个实体可以组成"N 对 1"的关联集合，其中一个为 primary（主航迹），其余为 secondary（从航迹）[@la_sdk_correlation]。更值得注意的是显式的 decorrelation（去关联）记录，其注释写道：当"UI 中的用户判定两条航迹实际上并不相同，尽管自动关联器已将它们关联"时，系统记录这一决定，"防止关联器再次把它们关联起来"[@la_sdk_correlation]。

这段注释证实了两件事：Lattice 内部存在一个自动关联器；人可以推翻它的结论，而且这个人工结论对自动化有约束力。这是典型的多传感器航迹融合设计，即各节点产生局部航迹，再关联成系统航迹。结合公司"Lattice AI Core 在边缘做多航迹调和"的说法，可以推断每个设备先生成本地航迹，再由关联器在 COP 中合并（推断）[@la_airrec_socom]。

### 标识位、健康与告警

indicators 组件是一组布尔标识：simulated（模拟数据）、exercise（演习数据）、emergency（紧急）、c2（指挥控制相关）、egressable（可外发）和 starred（星标）[@la_sdk_indicators]。其中 egressable 的注释是"该实体应被外发到外部来源"，并举例"例如实体需要先做模糊化处理"，同时说明"由各集成决定如何外发"[@la_sdk_indicators]。simulated 和 exercise 两个标识说明系统支持真实数据与模拟、演习数据混跑，这对训练和实兵演习很重要，但公开资料中没有找到对应的仿真器产品。

health 组件包含 connection_status（连接状态）、health_status（健康状态）、components（各部件健康）、update_time 和 active_alerts（当前告警）[@la_sdk_health]。由此可见，告警至少部分以"实体健康告警"的方式建模：一座塔掉线、一架无人机电量告急，都表现为对应资产实体上的告警。

### 密级与标识：逐字段的密级标记

data_classification 组件给每个实体一个默认密级，并允许在 fields 列表中为单个字段设置不同密级，字段级设置"始终优先于默认值"[@la_sdk_classification]。密级分为 UNCLASSIFIED（非密）、CONTROLLED_UNCLASSIFIED（受控非密）、CONFIDENTIAL（秘密）、SECRET（机密）、TOP_SECRET（绝密）五级，另有 caveats（附加控制标记）。SDK 举的例子是："TOPSECRET//NOFORN//FISA"被解析为第 5 级，附加标记为 NOFORN 和 FISA[@la_sdk_class_info,la_sdk_class_level]。

逐字段密级加上 egressable 标识，说明数据模型已经为多级安全和跨域外发预留了接口：同一个目标实体，位置可以是机密，型号判断可以是绝密，外发给盟军时只放行可放行字段（推断）。但需要强调，没有任何公开资料描述 Lattice 经认证的跨域解决方案（CDS），模型"能表达"不等于系统"已获准"跨密级运行。

### 所有权、溯源与覆写：谁改了什么都有记录

SDK 文档对实体的所有权规则写得很明确：通过 API 发布的实体归发布者"所有"，"UI 等其他来源不得编辑或删除这些实体"；只有当 provenance.sourceUpdateTime 比现有数据更新时，更新才会被接受[@la_sdk_ref]。但操作员仍然可以"覆写"（override）被标为可覆写的字段，示例字段路径就是 mil_view.disposition；覆写是最终一致的，采用"后写者胜"规则[@la_sdk_ref]。

实体事件分为五类：CREATED（创建）、UPDATE（更新）、DELETED（删除）、PREEXISTING（订阅时已存在）、POST_EXPIRY_OVERRIDE（过期后的覆写）[@la_sdk_event_type]。

这套规则解决的是多源数据下的一个老问题：传感器在持续刷新航迹，人又要修改其中的判断，两者如何不打架。Lattice 的做法是把"传感器事实"和"人的判断"分层存放：位置、速度等由数据源独占，属性、优先级等由人覆写。由此产生的副作用是一条天然的审计链，"谁在什么时候把哪个目标定为敌对"都有带溯源的覆写记录（推断）。

### 任务生命周期：照搬战术通信的确认语义

任务（Task）是 Lattice 区别于一般态势感知软件的关键。任务状态的完整枚举为：CREATED（已创建）、SCHEDULED_IN_MANAGER（已在管理器排程）、SENT（已发送）、MACHINE_RECEIPT（机器已接收）、ACK（已确认）、WILCO（将遵照执行）、EXECUTING（执行中）、WAITING_FOR_UPDATE（等待更新）、DONE_OK（成功完成）、DONE_NOT_OK（未成功完成）、REPLACED（已被替换）、CANCEL_REQUESTED（请求取消）、COMPLETE_REQUESTED（请求完成）、VERSION_REJECTED（版本被拒）[@la_sdk_task_status_status]。WILCO 是军用无线电通话中"将遵照执行"的标准用语。

任务对象包含以下要素[@la_sdk_ref]：specification（以 protobuf Any 封装的具体任务定义）；author（发起人，即 Principal）；relations（父任务和受领者）；initial_entities（任务涉及的初始实体，文档举例为"一个目标实体、一个限入区实体"）；retry_strategy（重试策略）；delivery_constraints（投递约束）；execution_constraints（执行约束）；is_executed_elsewhere（是否在别处执行）。任务状态对象另含 progress（进度）、result（结果）、estimate（预估）和 allocation（"任务已分配的代理"）[@la_sdk_task_status]。

并发与取消规则同样体现了作战逻辑。状态更新通过 status_version 实现乐观并发控制；DONE_OK 和 DONE_NOT_OK 是不可逆的终态[@la_sdk_ref]。取消请求发出后，如果任务已经交给执行代理，"由代理决定能否取消"，代理可以用 ERROR_CODE_REJECTED 拒绝[@la_sdk_ref]。这符合实战常识：导弹出膛后不一定能召回，能否中止只有执行端最清楚。

从 SENT 到 MACHINE_RECEIPT、ACK、WILCO 再到 EXECUTING 的链条，复制的是战术数据链和语音指挥的确认语义（推断）。这样做的好处是，任务状态可以直接映射到 Link 16、JREAP 一类数据链的任务消息，也容易以人能看懂的方式显示给操作员。

### 能力目录：平台自报"我能做什么"

资产实体通过 task_catalog 组件中的 task_definitions 列表声明自己能执行哪些任务[@la_sdk_task_catalog]。这一设计让调度逻辑与具体平台解耦：新平台接入网络时，只要在自己的资产实体里声明能力，就会自动出现在可调度资源中，指挥端不需要为每种平台写专门代码。IBCS-M 试验中"数小时内接入一个此前未公开的传感器和效应器"，正是这种自描述机制的直接体现[@la_ds_ibcsm]。

不过，具体的任务定义（例如目视识别、侦察、打击等）位于 SDK 之外的 tasks/v* 目录，公开的 Python 类型中没有包含，因此 Lattice 内置了哪些标准任务类型，目前无法从公开资料确认。

### 手动控制：自主与遥控随时切换

stream_manual_control_frames 接口用于手动控制任务，把"摇杆动作"以流的方式发送给执行代理，每一帧带有纪元号（epoch）和序号，用来处理多个控制会话并发和过期帧问题[@la_sdk_ref]。这意味着 Lattice 不是只能"下达任务、自主执行"，操作员也可以随时接管单个平台。纪元号和序号的设计说明，系统考虑到了控制权交接时新旧指令交错的风险。

### 对象存储与视频：情报产品在网格中流动

Objects 接口提供按路径的列出、获取、上传、删除和元数据查询，单个对象最大 1 GiB，带 expiry_time 时效[@la_sdk_ref]。默认只列出本节点上的对象；参数 all_objects_in_mesh 为真时，"列出 Lattice Mesh 中所有环境节点上的对象"；last_updated_at 记录的是"对象到达持有它的节点的时间"[@la_sdk_ref,la_dev_objects]。获取接口支持 RFC 9218 优先级头和压缩[@la_sdk_ref]。图片、文档、模型文件等情报产品因此可以像实体一样在网格中分发，并按优先级传输。

较新的 Video API 支持三种接入方式：RTSP 拉流、SRT 推流和 MPEG-TS 推流；输出可通过 RTSP 或 SRT 再发布。文档特别说明，"MPEG-TS 接入只在边缘封闭网络中支持"，当 Lattice 运行在"经公共互联网访问的云环境"时可能被禁用[@la_sdk_ref]。按开发者更新日志，Video API 于 2026 年 9 月 9 日进入预览[@la_changelog]。

### 任务自主：Lattice for Mission Autonomy

LMA 是 Lattice 在无人集群方向的应用层产品。按公司说法，它是"硬件无关、端到端"的软件平台，用于指挥由异构机器人资产组成的编队，把"多人操控一个自主系统"变为"一人操控多个"[@la_blog_lma,la_d1_lma]。功能链条覆盖：风险与威胁建模、作战分析、训练与演习、任务前规划、指挥控制、任务后复盘[@la_blog_lma]。Defense News 报道中还列出自主驾驶、威胁识别、多平台机动编排以及电磁特征与通信管理[@la_dn_lma]。Defense One 引述公司说法称，LMA 能让机器人完成更多任务，同时"仍有人在监督任务"，并能告诉监控人员突然出现的飞机是否敌对[@la_d1_lma]。

LMA 最有代表性的公开演示是陆军 EDGE23：一名士兵完成任务前规划并控制多架无人机，把一个地空导弹阵地定为"敌对"，授权 ALTIUS-600M 实施打击；随后 Lattice 自动把一架 ALTIUS ISR 无人机改派去做毁伤评估（BDA）[@la_blog_edge23]。这个演示同时展示了"人做决策"和"机器做调度"两件事。

在空中，LMA 于 2026 年 2 月 24 日首次在 YFQ-44A 上飞行[@la_die_cca]。The Aviationist 报道，Fury 在同一次飞行中既运行 Shield AI 的 Hivemind，也运行 Anduril 的 LMA，并通过早期"政府参考自主架构"（A-GRA）实现在两套自主软件之间切换，Anduril 称 LMA 完全符合 A-GRA[@la_aviationist_hivemind]。新加坡国防科技局（DSTA）与空军（RSAF）2025 年 3 月与 Anduril 的合作，是 LMA 的首个国际合作[@la_amr_singapore]。

### 反无人机杀伤链：从探测到摧毁

反无人机是 Lattice 合同规模最大的应用领域，也是其杀伤链功能最完整的体现。2025 年 11 月，陆军选定 Lattice 作为 IBCS-M 的反无人机火控与 C2 平台，由它负责传感器融合和"从探测到摧毁"的自动化火控[@la_ds_ibcsm,la_execbiz_ibcsm]。2025 年 10 月的 Falcon Peak 25.2 演示中，基于 Lattice 的套件由 Mobile Sentry 负责自主探测和跟踪，Wisp 和 Pulsar 传感器补充，Anvil 负责动能摧毁，Mobile Sentry 探测并跟踪一架"敌方"无人机后由 Anvil 将其击毁[@la_ius_falconpeak,la_tdp_falconpeak]。

把 SDK 的数据结构与这些演示对照，可以还原出 Lattice 的标准交战流程（推断，未见官方完整描述），共七步：

【第一步 探测】塔、雷达、光电/红外等传感器上的边缘 AI 检测并分类目标。

【第二步 建航迹】节点发布 TEMPLATE_TRACK 实体，附带 kinematics 和 tracked 组件中的航迹质量评分。

【第三步 融合】自动关联器把多源航迹合并为主航迹，操作员可以去关联。

【第四步 识别】操作员或规则把 mil_view.disposition 改为 HOSTILE，形成带溯源的覆写记录。

【第五步 派任务】操作员创建或批准一条打击/拦截任务，以 initial_entities 指向目标实体，发给在 task_catalog 中声明了相应能力的效应器代理。

【第六步 执行】代理依次回报 ACK、WILCO、EXECUTING，最终 DONE_OK 或 DONE_NOT_OK。

【第七步 评估】自主模块自动改派 ISR 资产做毁伤评估，EDGE23 已演示这一步[@la_blog_edge23]。

!fig d_lattice_killchain|d_lattice_killchain.png|Lattice 探测—评估七步交战流程与人机关系（推断）|本报告依据 lattice-sdk-python 数据结构、EDGE23 与 Falcon Peak 公开报道绘制|160

### 师级火力指挥控制：NGC2 中的 Lattice

在陆军 NGC2 中，Lattice 的功能从"控制自家硬件"扩展为"承载师级作战应用的数据层"。Ivy Sting 1 演习中，第 4 步兵师的师级目标处理流程从师部一直到炮位，完全运行在 Lattice Mesh 和 Palantir Target Workbench 上；一款运行在 Lattice Mesh 上的测试版炮兵数据工具 AXS 被用于 M777 榴弹炮射击[@la_ss_ivysting1,la_bd_ivysting1,la_die_ivysting1]。据报道，使用 AXS 的炮组在 30 秒内完成数字化准备，而使用传统"先进野战炮兵战术数据系统"（AFATDS）的炮组往往要先排查连接问题[@la_bd_ivysting1]。

在这一结构中，分工相当清楚：Lattice 负责战术边缘的数据传输、实体层和网格；Palantir 的 Target Workbench 负责目标管理、跟踪和每个目标的资源分配[@la_bd_ivysting1]。2026 年 6 月确定的 NGC2 通用数据层基线，则把这种分工固化为"Lattice 加 Foundry"的"边缘到云"数据网格[@la_ds_cdl,la_bd_cdl]。按公司说法，后续的 Ivy Sting 5 已在通信降级阶段于本地网格上完成"电子战定位到火力打击"的端到端流程[@la_anduril_scaling]。

### 人机关系：机动和感知"人在回路上"，武器释放"人在回路中"

所有公开记录的 Lattice 交战案例中，开火决定都由人作出。2020 年 AFRL/ABMS 巡航导弹演示中，操作员先确认 Lattice 跟踪的是预期目标，再向效应器下达交战指令[@la_dn_cruise]。陆战队地基防空项目办公室明确，Anvil 可以利用传感器航迹数据自主跟踪，但"只在人工操作员下令后才拦截"，并可通过 Lattice 界面控制[@la_marines_gbad]。EDGE23 中，由人把目标定为敌对并授权打击，由软件自动改派 ISR 做毁伤评估[@la_blog_edge23]。

SDK 中能找到一组明确的人机交互"挂钩"[@la_sdk_ref,la_sdk_correlation]：敌我属性覆写带溯源；用户去关联对自动关联器有约束力；任务创建、取消和状态变更都记录发起人（author）；执行代理可以拒绝任务；以及手动摇杆控制。综合这些设计，可以把 Lattice 的人机关系概括为：机动、感知和资源调度是"人在回路上"（human-on-the-loop，人监督、可干预），武器释放是"人在回路中"（human-in-the-loop，必须由人批准）（推断）。

但这一结论有明显边界。公开资料中没有找到交战规则（ROE）的配置方式，没有找到针对一类、二类小型无人机的"自动交战"模式说明，也没有找到 Lattice 如何满足国防部第 3000.09 号指令（武器系统自主性）要求的公开文件。公司宣称 AI"识别威胁比人类操作员更准确"，但没有找到任何独立测试数据[@la_airrec_socom,la_popsci]。批评者认为 Lattice"为比人类判断更快地行动而设计"，并指出公司材料没有解释自主致命决策的问责机制[@la_freepress]。

### 功能模块拆解

!table la_func|Lattice 功能模块拆解|本报告依据 lattice-sdk-python 源码及相关报道整理；"一手"指直接读自官方 SDK|26,58,44,32
模块|关键设计（官方 SDK 原名或公开描述）|军事含义|证据等级
实体数据模型|Entity 为"作战环境中的一个已知对象"，30 余个可选组件；location 与 kinematics 二选一；expiry_time 必填且不超过 30 天|全域对象统一建模，所有数据有时效|一手[@la_sdk_entity]
本体模板|TRACK、SENSOR_POINT_OF_INTEREST、ASSET、GEO、SIGNAL_OF_INTEREST 五类；附 platform_type、specific_type|战场对象五种基本类型，围栏即实体|一手[@la_sdk_ontology_tpl]
敌我属性|MilView：UNKNOWN、FRIENDLY、HOSTILE、SUSPICIOUS、ASSUMED_FRIENDLY、NEUTRAL、PENDING；含环境与国籍|与美军和北约标准一致|一手[@la_sdk_milview_disp]
航迹质量|tracked：0—15 质量分、传感器命中数、雷达截面积、"强度"（Link 16）|与战术数据链习惯一致|一手[@la_sdk_tracked]
航迹融合与关联|correlation：N 对 1 主从关联；显式去关联阻止自动关联器重新合并|自动融合、人可否决|一手[@la_sdk_correlation]
标识与健康|indicators：模拟、演习、紧急、c2、可外发、星标；health：连接、健康、当前告警|真实与演习数据混跑；告警挂在资产上|一手[@la_sdk_indicators,la_sdk_health]
密级标记|默认密级加逐字段密级，五级加 NOFORN 等附加标记|为多级安全和跨域外发预留接口|一手[@la_sdk_classification]
所有权与覆写|发布者独占；按 sourceUpdateTime 判新旧；可覆写字段由人修改，后写者胜|传感器事实与人的判断分层，留审计链|一手[@la_sdk_ref]
任务生命周期|CREATED 至 DONE_OK 等 14 种状态，含 ACK、WILCO；乐观并发；代理可拒绝取消|照搬战术通信确认语义|一手[@la_sdk_task_status_status]
能力目录|task_catalog 中的 task_definitions|新平台接入即可被调度|一手[@la_sdk_task_catalog]
手动控制|stream_manual_control_frames，带纪元号和序号|自主与遥控随时切换|一手[@la_sdk_ref]
对象与视频|对象最大 1 GiB，可按节点或全网格列出；视频支持 RTSP、SRT、MPEG-TS|情报产品与视频在网格中分发|一手[@la_sdk_ref]
任务自主 LMA|硬件无关、端到端，一人操控多机，覆盖规划到复盘|集群作战大脑|公司口径[@la_blog_lma]
反无人机杀伤链|IBCS-M 中"从探测到摧毁"的融合与自动火控|探测、跟踪、识别、拦截一体|合同事实[@la_ds_ibcsm]
师级火力 C2|AXS 炮兵工具运行于 Lattice Mesh，与 Target Workbench 协同|从传感器到炮位|演习事实[@la_bd_ivysting1]
!end

### 一个反无人机场景在接口层的映射（示例推断）

为了让读者直观理解上述数据结构如何协同，下面把一次典型的基地反无人机交战映射到 SDK 公开接口上。这是依据 SDK 文档所作的示例推断，不代表 Anduril 公布过的具体实现。

【传感器上报】一座 Sentry 塔作为"生产者"，对新发现的小型无人机调用 publish_entity，发布一个 TEMPLATE_TRACK 实体：kinematics 填位置和速度，tracked 填航迹质量和传感器命中数，mil_view.disposition 暂为 UNKNOWN，expiry_time 设在几分钟之后，provenance 标明数据来源[@la_sdk_ref,la_sdk_entity]。

【多源融合】另一部雷达也发布了同一目标的航迹，自动关联器把两者组成主从关联集合；如果操作员认为其实是两个目标，可以去关联，关联器此后不会再把它们合并[@la_sdk_correlation]。

【态势分发】指挥所的界面和分析程序作为"消费者"，通过 stream_entities 订阅，并用过滤语句只接收基地周边地理区域内的航迹，以节省带宽[@la_sdk_ref]。

【识别定性】值班员根据画面和规则，调用 override_entity 把 mil_view.disposition 改为 HOSTILE，这次覆写带有操作员身份和时间[@la_sdk_ref]。

【任务下达】值班员调用 create_task，specification 中写入拦截任务定义，initial_entities 指向该航迹实体，受领者是一架在 task_catalog 中声明了拦截能力的 Anvil[@la_sdk_ref,la_sdk_task_catalog]。

【执行与回报】Anvil 作为"代理"，经 stream_as_agent 收到执行请求，依次回报 MACHINE_RECEIPT、ACK、WILCO、EXECUTING，拦截后回报 DONE_OK 或 DONE_NOT_OK；如果中途收到取消请求，由 Anvil 判断是否还能中止[@la_sdk_task_status_status,la_sdk_ref]。

【复盘留痕】整个过程中，航迹的创建与更新、敌我属性的覆写、任务的发起人与每一次状态变更都有记录，可供事后复盘。

这一映射说明，Lattice 把"谁看到了什么、谁作了什么判断、谁下了什么命令、执行端如何回应"全部变成结构化数据。这既是它支持快速集成和自动化的基础，也是它在追责和审计上潜在的优势；但公开资料没有说明这些记录如何保存、保存多久、能否被独立调阅。

### 功能上的空白

功能层面的未知项同样需要列明。公开资料中没有找到：告警和地理围栏的专用接口；tasks/v* 下的具体任务定义；可覆写字段的完整清单；仿真器或测试工具产品；交战规则配置；针对小型无人机的自动交战模式；计算机视觉模型的架构、训练数据和准确率指标。Roadrunner 与 Lattice 的集成方式也没有找到公开说明。这些空白多数恰好落在"杀伤链中由机器决定多少"这一最敏感的问题上。
## （三）架构设计：节点联邦、网状网格与 protobuf 内核

:::lead
Lattice 的部署形态是一组由 Lattice Mesh 连接起来的"节点"。节点可以是一座监视塔、一套背负式边缘计算箱、一辆车、一艘无人艇，也可以是云端或本地机房。Mesh 是点对点数据网格，设计目标是在链路被拒止、降级、时断时续或带宽受限（DDIL）的条件下继续工作。本节把 Lattice 拆为六层逐层说明：传感器与效应器、边缘计算与通信、Mesh 数据网格、核心服务、API 与 SDK、应用层。第④、⑤层依据官方 SDK 源码，属一手证据；第①—③层和"每个节点运行完整服务栈"的判断，部分依据专利与公司材料推断，文中分别标明。
:::

### 总体形态：由节点组成的联邦

从 SDK 可以推断 Lattice 的基本结构：每个节点运行一套本地 Lattice 服务（实体存储、任务管理、对象存储、视频服务、本地关联器和 AI），Lattice Mesh 以点对点方式复制实体和对象，并按优先级选路；客户端（用户界面或 SDK 应用）连接自己所在的本地节点（推断）[@la_sdk_ref]。这一推断可以解释 SDK 中的两个现象：接口作用范围以"环境"（environment）为单位，对象列表默认只返回"本节点对象"。Video API 区分"边缘部署（封闭网络）"和"经公共互联网访问的云部署"，说明边缘和云两种部署都受支持[@la_sdk_ref]。

!fig d_lattice_arch|d_lattice_arch.png|Lattice 六层架构与部署形态示意|本报告依据 Anduril SDK 源码、Lattice Mesh 专利与公开报道绘制；①—③层及"每节点完整栈"含推断|160

### 第①层 传感器与效应器：内置"Lattice AI Core"的末端节点

最底层是各类可感知、可打击的平台。公开确认由 Lattice 控制或融合的系统包括：Sentry 塔（固定型、机动型和增程型）、Wisp、Pulsar 电子战系统、Anvil 拦截无人机、ALTIUS-600 与 600M、Ghost-X、YFQ-44A Fury，以及在 IBCS-M 下接入的第三方雷达和效应器、Hermeus Quarterhorse 等合作伙伴平台[@la_ds_ibcsm,la_blog_edge23,la_ius_falconpeak,la_aviationist_hivemind,la_andurilnews_lattice]。

Sentry 塔集成雷达、光电/红外和射频传感器，负责探测和跟踪目标，再把数据传给 C2 节点[@la_dn_cruise,la_c4isrnet_mobilesentry,la_execbiz_xrsentry]。2022 年 10 月推出的轮式机动型（Mobile Sentry）和 2024 年 5 月推出的增程型，扩展了部署方式[@la_c4isrnet_mobilesentry,la_execbiz_xrsentry]。增程型塔高 80 英尺，自主探测距离超过 5 英里，有人辅助可达 7.5 英里[@la_execbiz_xrst]。按公司说法，"每一件 Anduril 产品都内置 Lattice AI Core，在边缘完成传感器融合、目标分类和多航迹调和"[@la_airrec_socom]。Ghost-X 的 C2 据 Anduril 网站描述也运行在 Lattice 上[@la_cyberwarzone]。

!photo sentry_imperial|加州帝国县 CA-98 公路旁沙地中的 Anduril Sentry 塔（2022 年 7 月 29 日）。塔顶集成雷达与光电/红外传感器，太阳能供电，是 Lattice 最早的"末端节点"|Electronic Frontier Foundation（EFF），CC BY 4.0

!photo anvil_press|Anduril Anvil 动能拦截无人机（公司图，2021 年 9 月）。Anvil 可利用 Lattice 航迹数据自主跟踪，但只在人工操作员下令后实施拦截|Anduril Industries，公司图片，仅作评论引用

!photo pulsar_l_press|Anduril Pulsar-L 轻型电子战系统（公司图，2025 年 4 月发布）。Pulsar 系列在 SOCOM、陆战队 I-CsUAS 等反无人机方案中与 Lattice 配套|Anduril Industries，公司图片，仅作评论引用

!photo roadrunner_idex2025|IDEX 2025 防务展上的 Anduril Roadrunner 可回收双涡喷拦截器（2025 年 2 月 19 日，阿布扎比）。2026 年 6 月获批的科威特军售包含 Roadrunner-M 与 Lattice|Mztourist（Wikimedia Commons），CC BY 4.0

但也有一批平台与 Lattice 的关系没有得到确认。Ghost Shark、Dive-LD、Barracuda、Roadrunner 和 Pulsar 除了出现在套件清单中，没有找到说明其如何与 Lattice 集成的公开来源。Ghost Shark"由 Lattice 管理自主功能"的说法只见于二手来源（弱源，待核）[@la_speedoscience,la_engineers_ghostshark]。

### 第②层 边缘计算与通信：Menace 与 Voyager

第二层是承载 Lattice 的边缘计算硬件。2025 年 5 月，Anduril 发布 Menace-T：一套由两个箱子组成的 C4（指挥、控制、通信、计算机）套件，一名操作员几分钟即可架设，基于 Klas 公司（被 Anduril 收购）的 Voyager 坚固计算硬件，运行 Lattice Mesh，可以承载第三方边缘 AI 软件栈，已在地面车辆和舰船上使用；Menace-X 是面向远征和动中通的版本[@la_tc_menace,la_everythingrf_menace]。Menace 系统同时是 Palantir Edge 软件的首选硬件，与 Lattice Mesh 组网配套[@la_dc_menace]。

NGC2 的 Ivy Sting 1 中，Lattice Mesh 运行在坚固的 Voyager 边缘计算套件上[@la_bd_ivysting1]。NGC2 原型还被描述为"在共同数据层上的一体化软硬件 C2 套件"，计算节点部署在多种机械化车辆上[@la_ss_ngc2_award]。这说明 Anduril 在 C2 领域卖的不只是软件，而是"软件加计算加通信"的整套边缘节点。

!photo menace_t_press|Anduril Menace-T 单兵可部署 C4 边缘计算套件（公司图）。Menace-T 基于 Klas Voyager 硬件，运行 Lattice Mesh，也是 Palantir Edge 软件的首选硬件|Anduril Industries，公司图片，仅作评论引用

一份二手材料称 Menace C4 硬件通过包括 Link 16 在内的多条通信路径运行 Lattice（弱源，待核）[@la_phil_blog]。L3Harris、Silvus 等网状电台厂商与 Lattice 的关系，本轮研究没有涉及。

### 第③层 Lattice Mesh：实时优先的点对点数据网格

Lattice Mesh 是整个架构最有特色的一层。公司的描述是：它是"一个已连接全球数千个防务系统的去中心化网络，专门、独特地为在降级环境下实现安全的点对点数据共享而构建"，通过"对数据路径排定优先级"，在平台、作战域和合作伙伴之间分发数据[@la_x_mesh,la_ua_cdao]。这些是公司口径。

专利提供了更具体的线索。Anduril 的 Lattice Mesh 专利（US 10,506,436，公开号 US 2020/0068404）有三个要点[@la_patent_436,la_patent_pub]：

【实时优先】"实时数据是系统的优先级，回填只使用剩余带宽"，网络在链路性能波动时仍优先保障实时数据。

【点对点授权路由】安全路由依靠点对点授权，每条转发路径都需要授权。

【密钥不落盘】普通节点的密钥只保存在内存中，不写入永久存储，节点被缴获时降低密钥泄露风险。

SDK 从另一侧印证了"节点本地存储加跨节点复制"的结构。对象可以按单个节点或整个网格列出，last_updated_at 记录的是"副本"到达某个节点的时间，这证实了节点之间存在存储转发式复制；RFC 9218 优先级头让客户端可以设置传输优先级[@la_sdk_ref]。

SDK 还暴露了几项面向 DDIL 的工程设计[@la_sdk_ref]：长轮询会话中，如果客户端落后超过"环境中实体总数的 3 倍"，会话会被终止；SSE 流"自动从临时断连中恢复，从断点继续"；订阅时可以用 components_to_include 只取需要的组件，并用过滤语句（Statement）筛选实体以节省带宽，这个过滤器"镜像 gRPC 的 StreamEntityComponents 端点"。

有一篇个人博客称 Mesh 使用 gossip 协议，在每个节点保存资产数据库，网络可以自愈，但这一说法无法核实（弱源，待核）[@la_phil_blog]。Mesh 的传输层、同步模型（例如是否使用 CRDT）以及覆写"后写者胜"之外的冲突消解机制，都没有公开描述。

Mesh 的实际部署有几项硬证据：2024 年 12 月 CDAO 1 亿美元 OTA 授予时，网格已"在多个军种和作战司令部运行"[@la_ds_cdao]；太空军 SSN 现代化合同以 Lattice 作为弹性网状网络[@la_ds_ssn]；Anduril 英国公司在英国陆军"阿斯加德计划"（Project Asgard）中演示了边缘数据网格，把前线数据传到司令部[@la_die_asgard]；NGC2 中 Lattice Mesh 是第 4 步兵师的数据骨干[@la_bd_ivysting1]。按公司说法，Ivy Sting 5 把数据网格扩大到原来的 3 倍，连接 65 个以上战术边缘节点，并在卫星和商用通信失效时继续工作[@la_anduril_scaling,la_militaer_ivysting5]。

### 第④层 核心服务：实体管理器与任务管理器

开发者文档的概述说明，Lattice SDK 用来构建"创建、使用和改进 Lattice Mesh 数据"的应用、数据服务和硬件集成，核心是 gRPC 的 Entity Manager（实体管理器）和 Task Manager（任务管理器）接口，以及 HTTP 的 Entities 和 Tasks 接口[@la_docs_overview]。结合 SDK，可以确认核心服务至少包括：实体管理（发布、订阅、覆写、过期）、任务管理（创建、分派、状态跟踪、取消）、对象存储、视频服务以及自动航迹关联器[@la_sdk_ref,la_sdk_correlation]。"每个节点都运行完整服务栈"是推断，没有公开文件证实。

运行时技术栈（操作系统、是否使用 Kubernetes、主要编程语言）没有公开文档。从 v2 REST 接口大量使用 google.protobuf.Any、STATUS_ 和 TEMPLATE_ 这类枚举前缀，以及过滤器"镜像 gRPC 端点"的注释，可以判断 Lattice 内部是 protobuf/gRPC 原生的，REST 只是外层封装（推断）[@la_sdk_ref]。

### 第⑤层 API 与 SDK：开放接口、封闭实现

Lattice SDK 于 2024 年 12 月 10 日公开发布[@la_dd_sdk]。开发者文档说明，v1 原生支持 gRPC，v2 使用 OpenAPI，Anduril 建议升级到 v2；v2 SDK 新增了 StreamEntities，并提供 Go、Java、Python 和 TypeScript 示例[@la_changelog_20250724,la_docs_java,la_dev_watch,la_docs_publish]。Python 包名为 anduril-lattice-sdk，客户端以 client_id 和 client_secret 认证，支持异步客户端、重试、超时、分页和流式接收[@la_sdk_readme]。该 SDK 由 Fern 工具从 OpenAPI 规范生成，GitHub 上另有 Fern 维护的镜像[@la_fern_mirror]。

SDK 语言覆盖 Python、JavaScript/TypeScript、Java、Go、C++ 和 Rust。2025 年 7 月 24 日，C++ 仓库归档，protobuf 定义改由 Buf Schema Registry 托管；2026 年 10 月 5 日发布 Rust（REST）SDK[@la_github_anduril,la_sdk_cpp,la_changelog]。

v2 公开接口分为五组[@la_sdk_ref]：

【Entities 实体】publish_entity、get_entity、override_entity、remove_entity_override、long_poll_entity_events、stream_entities（SSE）。

【Tasks 任务】create_task、get_task、update_task_status、cancel_task、query_tasks、stream_tasks、listen_as_agent、stream_as_agent、stream_manual_control_frames。

【Objects 对象】list_objects、get_object、upload_object、delete_object、get_object_metadata。

【OAuth 认证】get_token。

【Video 视频】接入流和输出流各自的列出、创建、获取、删除。

SDK 定义了三种标准接入模式[@la_sdk_ref]：

【生产者】传感器或 C2 适配器调用 PublishEntity，发布航迹或资产实体。

【消费者】用户界面或分析程序调用 StreamEntities，先收到全部 PREEXISTING 事件，再接收创建、更新、删除事件，默认每 30 秒一次心跳。

【可受领任务的代理】机器人或效应器先发布带 task_catalog 的资产实体，再用 EntityIdsSelector 调用 StreamAsAgent 或 ListenAsAgent，接收执行（ExecuteRequest）、取消（CancelRequest）和完成（CompleteRequest）请求，并通过 UpdateTaskStatus 回报进度。

这三种模式清楚地划分了第三方接入 Lattice 的路径：传感器厂商做生产者，应用开发者做消费者，无人平台和武器厂商做代理。2026 年 10 月 1 日 ORIGIN 公司 BLAZE 拦截器集成进 Lattice，就是"代理"模式的一个实例[@la_overt_blaze]。中央司令部"沙漠守护者 1.0"（Desert Guardian 1.0）演习中，Lattice 作为第三方 C2 系统，参演官兵依靠 API 和 SDK 文档集成自己的系统，部分是实时完成的[@la_ocbj_partners]。

许可条款决定了这套 SDK 的性质。许可是有限、可撤销、免版税的，只能用于为"兼容的 Lattice 实现"开发应用，明确禁止用它构建其他 SDK 或不兼容的实现[@la_sdk_license,la_buf_license]。因此，Lattice 是"开放接口、封闭实现"，不是开源软件。SDK 是否收费、开发者沙箱的准入方式和其中的模拟资产，本轮均未查明；开发者计划提供"运行 Lattice Mesh、带模拟数据的环境"[@la_docs_overview]。Anduril 的招聘信息显示，其合作伙伴"从创新初创公司到防务巨头和世界各国军事组织"都有[@la_gc_jobs]。

### 第⑥层 应用层

最上层是面向用户的应用：LMA（任务自主）、Lattice for C2（AI 战斗管理）、反无人机 C2、NGC2 中的师级应用（例如 AXS 炮兵数据工具），以及合作伙伴应用[@la_blog_lma,la_bd_tag,la_bd_ivysting1]。2026 年开发者平台新增的 Developer Console、Schema Registry、Video API 和面向 AI 编程智能体的"SDK skills"，说明 Anduril 正在把应用层的开发门槛进一步降低[@la_changelog]。

在更大的体系中，Lattice 还被嵌入其他系统的应用层。DIU 2025 年 3 月启动的 Thunderforge 项目由 Scale AI 牵头，为印太司令部和欧洲司令部开发 AI 辅助的战役规划，Lattice 在其中提供数据共享层，配合微软和 Scale 的大模型，采用"始终在人类监督下"的智能体工作流[@la_ds_thunderforge,la_diu_thunderforge,la_scale_thunderforge]。陆军"单兵携行任务指挥"（SBMC，原 IVAS Next）项目中，SBMC-A 的数据与 AI 架构也建立在 Lattice C2 之上[@la_bd_eagleeye]。

!table la_arch|Lattice 六层架构要点|本报告依据 SDK 源码、专利与公开报道整理；证据栏区分一手、专利、公司口径与推断|28,58,44,30
层|主要组成|关键事实|证据
①传感器与效应器|Sentry 塔、Wisp、Pulsar、Anvil、ALTIUS、Ghost-X、YFQ-44A、第三方雷达与拦截器|每件产品内置 Lattice AI Core，边缘融合、分类、多航迹调和|公司口径[@la_airrec_socom]
②边缘计算与通信|Menace-T、Menace-X，Klas Voyager 坚固计算|运行 Lattice Mesh，可承载第三方 AI；Palantir Edge 首选硬件|事实[@la_tc_menace,la_dc_menace]
③Lattice Mesh|点对点、按优先级选路、存储转发|实时优先、回填用剩余带宽；点对点授权；密钥不落盘|专利[@la_patent_436]
④核心服务|实体管理器、任务管理器、对象存储、视频服务、自动关联器|gRPC 与 HTTP 两套接口|文档事实；完整栈为推断[@la_docs_overview]
⑤API 与 SDK|v1 gRPC，v2 REST 加 SSE；OAuth2；多语言 SDK|三种接入模式；断线续传；按组件与过滤器订阅|一手[@la_sdk_ref]
⑥应用层|LMA、Lattice for C2、反无人机 C2、NGC2 应用、伙伴应用|Developer Console、Schema Registry、Video API、AI skills|更新日志摘要[@la_changelog]
!end

### 互操作标准：只有 A-GRA 有明确记录

在军用标准与开放架构方面，公开证据的强弱差别很大，必须分开看。

【已证实：A-GRA】政府参考自主架构（A-GRA）是唯一有明确记录的标准。Anduril 称 LMA 完全符合 A-GRA，YFQ-44A 在一次飞行中通过两套软件上的早期 A-GRA 实现，在 Shield AI 的 Hivemind 与 Anduril 的 LMA 之间切换[@la_aviationist_hivemind]。

【间接证据：Link 16】Link 16 概念直接写进了数据模型：tracked 组件的"强度"注释引用 Link 16，实体带有 transponder_codes（应答机与敌我识别代码）和"遵循既有标准"的 symbology 组件[@la_sdk_tracked,la_sdk_entity]。但 Lattice 是否原生收发 Link 16 消息，只有一份二手来源称 Menace 通过 Link 16 等多条链路运行（弱源，待核）[@la_phil_blog]。

【未证实：TAK】Anduril 在招聘"高级 ATAK 工程师"（电子战团队），负责为实时遥测构建界面和接口，说明公司有 ATAK 方面的工作，但不能证明存在 Lattice 与 TAK/CoT 之间的桥接产品[@la_builtin_atak]。

【未证实：OMS/UCI】没有找到可靠来源证实 Lattice 支持开放任务系统/通用指挥接口（OMS/UCI）消息标准。

【开放架构表述】IBCS-M 被描述为连接传感器、效应器和决策中心的开放架构，Lattice 是其机动火控层[@la_uasmag_ibcsm,la_armyrec_ibcsm]。Anduril 公开主张"边缘互操作"和开放接口[@la_anduril_contours]。

从架构上看，egressable 标识的注释"由各集成决定如何外发"，指向一个适配器或"集成"层，负责把实体翻译成 CoT/TAK、Link 16/JREAP、IBCS 等外部格式（推断）[@la_sdk_indicators]。这与 Lattice 在"沙漠守护者"演习中接入第三方 C2 的做法一致。Lattice 与 IBCS 核心（诺斯罗普·格鲁曼）在"爱国者"、LTAMDS 层面如何对接，没有公开细节；《星条旗报》标题称其缩短了"爱国者"操作员的反应时间，但正文未能读取[@la_stripes_ibcsm]。

!table la_std|Lattice 与主要军用标准的关系|本报告依据 SDK 源码、The Aviationist、招聘信息等整理|30,34,56,40
标准或接口|结论|证据|来源
A-GRA 政府参考自主架构|已证实|Fury 单次飞行在 Hivemind 与 LMA 间切换；公司称完全符合|[@la_aviationist_hivemind]
Link 16|部分间接证据|数据模型含"强度"、应答机代码；Menace 支持 Link 16 仅见二手来源|[@la_sdk_tracked,la_phil_blog]
TAK/CoT|未证实|仅有 ATAK 工程师招聘，无桥接产品记录|[@la_builtin_atak]
OMS/UCI|未证实|未找到任何可靠来源|无
MOSA 模块化开放系统|部分|主要通过公开接口、SDK 和飞机上的 A-GRA 体现|[@la_anduril_contours]
IBCS 开放架构|部分|Lattice 为 IBCS-M 机动火控层，与 IBCS 核心对接细节未公开|[@la_uasmag_ibcsm]
!end

### 与 Palantir 体系的架构对接

Lattice 与 Palantir 的组合在架构上是"边缘采集与传输"加"企业级数据准备与决策应用"。2024 年 12 月的合作声明描述的链路是：传感器、载具、机器人和武器的战场数据由 Lattice 和 Menace 采集和传输，再进入 Palantir 的安全平台 AIP，为 AI 训练做准备，覆盖 SCI/SAP 等最高密级[@la_bnn_palantir,la_bw_palantir]。在 NGC2 中，Lattice 是战术边缘的网格、数据传输和实体层，Palantir 的 Foundry 是企业数据平台，Target Workbench 承担目标处理与决策应用；2026 年 6 月的通用数据层基线把两者定义为"边缘到云"的一张数据网格，Raft 提供注册与联邦服务[@la_bd_ivysting1,la_bd_cdl,la_ds_cdl]。硬件层面，Menace 同时是两家软件的首选承载平台[@la_dc_menace]。

但需要指出，这种分工并不是严格的层级切分：在 NGC2 中，Palantir 的工具也部署在师一级，而不只在战役和战略层级；在 Thunderforge 和"金穹"中，Lattice 也进入了战区和联合层级[@la_diu_thunderforge,la_usnews_goldendome]。更关键的空白是，公开资料中没有找到 Lattice 实体模型与 Palantir 本体之间的映射说明，也没有找到两者之间正式的接口集成公告，2024 年的合作声明和 NGC2 实践之外，具体如何对接仍不透明。

### 安全与认证：最大的公开空白

SDK 层面可以确认两项安全设计：认证采用 OAuth2 客户端凭证流程，令牌短时有效；每个实体带逐字段密级标记[@la_sdk_ref,la_sdk_classification]。专利层面还有点对点授权路由和密钥不落盘[@la_patent_436]。

但系统级认证信息几乎全部缺失：Lattice 的授权运行（ATO）等级、是否达到 IL5/IL6、能否在 SIPR/JWICS 上运行、使用何种跨域解决方案，均无公开资料。与此形成对照的是一条负面证据：2025 年 9 月 5 日，陆军首席技术官 Gabriele Chiulli 在一份备忘录中写道，NGC2 原型应被视为"极高风险"，因为对手很可能获得"持续、无法察觉的访问"；他写道："我们无法控制谁看到什么，无法看到用户在做什么，也无法验证软件本身是安全的。"备忘录称一个应用有 25 个高危漏洞，另有三个应用有 200 多个缺陷待审查[@la_reuters_memo,la_yahoo_memo]。Anduril 称这是"过时的快照"，Palantir 称"在 Palantir 平台中没有发现漏洞"，陆军首席信息官 Leonel Garciga 称备忘录属于分诊流程的一部分，陆军表示关键缺陷已经缓解[@la_bd_memo]。这份备忘录针对的是 NGC2 原型整体，而不是专门针对 Lattice，但它说明在多厂商、快速迭代的数据层上，安全认证是一个真实的短板。
## （四）能力评估：采购决策是硬证据，效能数据几乎全由公司提供

:::lead
评估 Lattice 的能力，需要先区分三类证据。第一类是"已证实"：政府合同、官方公告、独立媒体对事件的报道，以及官方 SDK 源码。第二类是"公司声称"：Anduril 新闻稿、高管表态，以及只有公司来源的演习数据。第三类是"存疑或反证"：相互冲突的口径、只有弱源支撑的说法，以及失败和事故记录。按这一标准，Lattice 最可靠的证据是多个军种通过竞标作出的采购选择；几乎所有定量效能数据都来自公司；唯一可公开核实的实战使用（乌克兰）结果是负面的；强电子对抗环境下的表现是最大的未证实领域。
:::

### 评估方法与总体判断

最能说明 Lattice 能力的，是用户用钱投出的票。SOCOM 在 12 份提案中选中它（2022），陆战队 I-CsUAS 在 9 家（另记 10 家）竞标者中选中它（2025），陆军为 IBCS-M 选中它（2025），陆军把 120 多项采购行动并入以它为中心的 200 亿美元企业合同（2026），陆军 NGC2 从 9,960 万美元原型直接转入 18 亿美元推广（2026），北约在三家竞争者中把它列入 eAirC2 评估（2026）[@la_wt_socom,la_ds_icsuas,la_ds_ibcsm,la_ds_20b,la_ds_icorps,la_ncia_nato]。这一连串决策说明，美军用户确实认可 Lattice 作为集成层、数据层和 C2 软件的价值。这是比任何公司宣传都更硬的信号。

但采购决策证明的是"用户相信它有用"，不等于"它在实战中达到了某个效能指标"。几乎所有定量数据，包括"火力时间缩短 90%"、"炮组 30 秒完成数字化准备"、"2,500 余台终端"、"65 个以上边缘节点"、IBCS-M 测试"完美击杀"，都来自 Anduril 或演习组织方的表述，没有找到独立评估[@la_milleak_ivymass,la_anduril_scaling,la_tdp_ibcsm]。下面逐项评估。

### 态势感知与传感器融合

【已证实】Lattice 的传感器融合能力在边境场景中经过了最长时间、最大规模的连续使用。AST 于 2020 年成为 CBP 正式采购项目，部署数百座塔[@la_cbp_por]；2026 年 6 月 CBP 又追加 200 余座增程型塔，新塔要与已有 350 余座标准塔组成的网络和 Lattice 集成[@la_execbiz_xrst,la_orangeslices_xrst]。官方 SDK 证实了多传感器航迹关联、0—15 级航迹质量评分和人工去关联机制[@la_sdk_tracked,la_sdk_correlation]。

【公司声称】"覆盖约 30% 的南部陆地边境"是公司口径，指的是地理覆盖，不是检测或拦截效果[@la_asdnews_300,la_anduril_300]。"AI 识别威胁比人类操作员更准确"同样只有公司说法[@la_popsci,la_airrec_socom]。

【存疑或反证】检测概率、虚警率、系统可用率等效能指标从未公开，也没有找到 GAO 或 DHS 监察长办公室的相关数据。MIT Technology Review 2026 年 9 月的调查估计，2021 年以来有 110 多人死在 Anduril 现代自主监视塔的覆盖范围内，并质疑数十亿美元的监视投入为何没能及早发现处于危险中的人员；这一数字是该刊自行估算的[@la_mittr_towers]。一个倡导类网站称 GAO 2024 年按六项隐私保护措施评估 CBP 塔项目，CBP 全部不达标，但未与 GAO 原文核对（弱源，待核）[@la_sos]。全部边境塔的数量也有 803 座和约 830 座两种说法，且都涵盖所有供应商[@la_mittr_towers,la_sos]。

### 反无人机

【已证实】以合同计，反无人机是 Lattice 最大的应用领域：SOCOM 上限 9.676 亿美元、陆战队 I-CsUAS 上限 6.42 亿美元、MADIS 约 2 亿美元、陆军 IBCS-M 选型、JIATF 401 首单约 8,700 万美元，以及科威特 19.8 亿美元拟议军售[@la_afcea_socom,la_ds_icsuas,la_ius_madis,la_ds_ibcsm,la_bd_jiatf,la_bd_kuwait]。较有说服力的单项证据是 IBCS-M 在尤马试验场为期 7 天的试验：Lattice 在数小时内接入了一个此前未公开的传感器和效应器，实弹拦截 4 中 4[@la_ds_ibcsm]。这直接检验了"硬件无关、快速集成"的核心卖点。Falcon Peak 25.2 中，套件成功探测、跟踪并动能摧毁一架无人机，随后交付北方司令部[@la_ius_falconpeak]。2026 年 10 月 ORIGIN 公司的 BLAZE 拦截器集成进 Lattice，说明第三方效应器在持续接入[@la_overt_blaze]。

【公司声称】The Defense Post 标题称 Lattice 在 IBCS-M 测试中取得"完美击杀纪录"，细节来自公司[@la_tdp_ibcsm]。2026 年对伊朗的"史诗怒火行动"中，Anduril 总裁称公司是对抗"沙希德"无人机的"主要"系统和"大量"参与者，但拒绝透露具体部署了哪些系统；报道同时指出，并不清楚相关系统近期是否在中东部署过[@la_aol_epicfury]。

【存疑或反证】没有找到任何可独立核实的、由 Lattice 引导的实战击落记录；中央司令部基地防御的具体部署、红海相关使用也没有可靠来源。IBCS-M 的合同金额、期限和"完美击杀"的测试条件都未披露。据《华尔街日报》报道，一次 Anvil 反无人机测试在俄勒冈州引发了 22 英亩的野火[@la_sherwood_wsj]。

!photo madis_mk1_mk2|海军陆战队 MADIS Mk2（左）与 Mk1（右）在尤马试验场进行系统集成测试（2023 年 9 月）。Anduril 承包 MADIS 的反无人机交战系统，2024 年 11 月获约 2 亿美元合同|Neil Mabini（PEO Land Systems，经 DVIDS），美国政府作品

### 集群自主与无人平台控制

【已证实】EDGE23 演示了单兵指挥多型无人机、人工授权打击、系统自动改派 ISR 做毁伤评估的完整流程[@la_blog_edge23]。澳大利亚 Ghost Shark 项目原型阶段按期、按预算完成，2025 年 9 月转入 17 亿澳元生产合同，2026 年 4 月交付首批生产艇[@la_bd_ghostshark_first,la_minister_ghostshark,la_tdn_masu]。YFQ-44A 已完成以惰性 AIM-120 对模拟目标实施的端到端超视距打击[@la_militarytimes_rolloff]。

【公司声称】LMA 可管理"数百个"异构平台[@la_dn_lma]；Ghost Shark 的自主功能由 Lattice 管理（只见于二手来源，弱源，待核）[@la_speedoscience]。

【存疑或反证】据《华尔街日报》报道，美国海军一次加州近海演习中，十余艘由 Lattice C2 控制的无人艇失灵或停机，对其他船只构成危险，水兵警告存在"安全违规和潜在人员伤亡"。演习时间有冲突：多数来源称 2025 年 5 月或夏季，TechBuzz 称 2024 年[@la_sherwood_wsj,la_techbuzz]。Anduril 回应称这是迭代开发的一部分[@la_conard]。

Lattice 在 CCA 中的角色口径也不一致，需要并列：

【口径一】Defence Industry Europe 称空军在 2026 年 6 月为 CCA 下一阶段选定了 LMA[@la_die_cca]；Simple Flying 的标题称这笔软件交易"把 Anduril 放进了空军购买的每一架 CCA"[@la_simpleflying]。

【口径二】另有报道描述 Anduril、Shield AI 和 Collins 各获 6 个月的自主软件合同条目（CLIN），之后再择优，两类来源在日期和顺序上相互矛盾[@la_simpleflying,la_twz_f35]。

【口径三】也有研究笔记认为公开资料没有说清 Lattice 在 CCA 任务自主软件中的确切角色；2026 年 2 月 Shield AI Hivemind 被选中在 Fury 机体上做飞行演示，说明政府有意保持自主软件可互换（二手来源）[@la_robotics_hivemind]。

综合看，可以确认的是 LMA 已在 Fury 上飞行并通过 A-GRA 与 Hivemind 切换；"空军所有 CCA 都使用 Lattice"的说法目前证据不足。

### C2 数据层

【已证实】Lattice 作为战场数据层的证据集中在陆军 NGC2：9,960 万美元原型、Ivy Sting 系列演习、通用数据层基线、18 亿美元推广合同依次落地[@la_army_ngc2_award,la_ds_cdl,la_ds_icorps]。Ivy Sting 1 中师级目标处理全程运行在 Lattice Mesh 和 Target Workbench 上，有陆军官方报道[@la_army_ivysting1,la_bd_ivysting1]。CDAO 的边缘数据网格合同、太空军 SSN 网状网络合同、DIU Thunderforge 也都把 Lattice 用作数据层[@la_ds_cdao,la_ds_ssn,la_diu_thunderforge]。

【公司声称】Ivy Sting 4—5 实现 50 多个用例，网格扩大 3 倍、连接 65 个以上边缘节点[@la_anduril_scaling,la_asdnews_scaling]；Ivy Mass 中整个第 4 步兵师上线，接入 2,500 多台终端，炮兵火力时间比传统系统缩短 90%[@la_milleak_ivymass,la_meritalk]。这些数字没有陆军官方确认。

【存疑或反证】陆军首席技术官 2025 年 9 月的"极高风险"备忘录是最重要的反证（见第三节）[@la_reuters_memo]。陆军自己也把"避免厂商锁定、为传感器和升级留出空间"列为通用数据层的关键考虑[@la_bd_cdl]。没有找到陆军或 GAO 对 NGC2 网络安全、可靠性的独立评估，Project Convergence 顶点演习 6 的结果也未找到。

### 跨域与盟军

"跨域"在这里有两层含义：跨作战域（陆海空天电）和跨密级、跨国别的数据交换。

【已证实】跨作战域方面，Lattice 已有陆上（边境、NGC2）、空中（反无人机、CCA）、水下（Dive-LD 竞速测试中实时共享位置）和太空（SSN 现代化）的合同或演示[@la_globalsec_diveld,la_ds_ssn]。Varda、LeoLabs 和 Anduril 联合跟踪 Varda 返回舱的轨道机动，数据实时输入 Lattice[@la_execbiz_varda]。盟军方面，英国 TALOS 系列合同、英国陆军 Project Asgard 演示、新加坡 LMA 合作、北约 eAirC2 评估、澳大利亚 Ghost Shark 都是事实[@la_edr_talos,la_gov_uk_17m,la_die_asgard,la_amr_singapore,la_ncia_nato]。

【公司声称】Mesh"已连接全球数千个防务系统"，能在平台、作战域和合作伙伴之间分发数据[@la_x_mesh]。

【存疑或反证】跨密级方面，数据模型支持逐字段密级和"可外发"标识，但没有任何公开资料描述其经过认证的跨域解决方案[@la_sdk_classification]。北约 eAirC2 目前只是 9 个月的评估期合同，之后择一长期实施，最终能否胜出未定[@la_ncia_nato]。关岛"勇敢之盾 2026"中基于 Lattice 的防御作战管理器只见于二手聚合来源（弱源，待核）[@la_venture_atlas]。

### 抗干扰与对抗环境

【已证实】专利和 SDK 证明了 Lattice 在设计上针对 DDIL：实时优先、存储转发、断线续传、按组件订阅[@la_patent_436,la_sdk_ref]。CDAO 合同以"扩展到断连和分布式系统"为目标[@la_ds_cdao]。

【公司声称】Ivy Sting 5 在卫星和商用通信失效时继续工作，在通信降级阶段于本地网格上完成"电子战定位到火力打击"的端到端流程（只有公司和二手来源）[@la_anduril_scaling,la_militaer_ivysting5]。

【存疑或反证】乌克兰是 Anduril 系统唯一可公开核实的实战使用场景，结果总体负面。据《华尔街日报》报道（经 TechCrunch 等转述），2022 年交付乌军的约 40 架 Ghost 侦察无人机受俄方干扰严重，士兵很快感到沮丧；乌克兰安全局（SBU）使用的 Altius 坠毁、未能命中目标，问题严重到 2024 年被停用，此后未再部署；另有报道称其易受俄方干扰，已撤出战场[@la_tc_wsj,la_techbuzz]。这些失败主要出在飞行平台和导航/数据链在强电子战下的生存能力，并非专门针对 Lattice 软件本身；也没有找到 Lattice 在乌克兰作为 C2 层使用的公开证据。但 Lattice 宣传的"边缘自主、抗干扰"确实没有得到实战支持。

!photo altius600_valkyrie|XQ-58A"女武神"无人机在尤马试验场投放 ALTIUS-600（2021 年 3 月 26 日）。ALTIUS 系列由收购的 Area-I 研制，在 EDGE23 中由 LMA 调度；乌克兰 SBU 使用的 Altius 因坠毁和受干扰于 2024 年停用|U.S. Air Force courtesy photo，美国政府作品

### 能力评估总表

!table la_cap|Lattice 能力评估：已证实、公司声称与存疑或反证|本报告依据研究笔记综合评估；"已证实"指合同、官方或独立媒体对事件的报道|26,46,44,44
能力维度|已证实|公司声称|存疑或反证
态势感知与传感器融合|CBP 采购项目，数百座塔持续运行；SDK 证实自动关联与人工去关联[@la_cbp_por,la_sdk_correlation]|覆盖边境约 30%；AI 识别比人更准[@la_asdnews_300,la_popsci]|无检测率与虚警率；MIT TR 估算覆盖区内 110 余人死亡；GAO 隐私审查不达标（弱源）[@la_mittr_towers,la_sos]
反无人机|SOCOM、I-CsUAS、MADIS、IBCS-M、JIATF 401 合同；尤马 4 中 4；Falcon Peak 拦截成功[@la_ds_ibcsm,la_ius_falconpeak]|IBCS-M"完美击杀"；伊朗冲突中"主要系统"[@la_tdp_ibcsm,la_aol_epicfury]|无可核实实战击落；Anvil 测试引发 22 英亩野火[@la_sherwood_wsj]
集群自主与无人平台|EDGE23 演示；Ghost Shark 按期交付；Fury 完成惰性 AIM-120 端到端打击[@la_blog_edge23,la_tdn_masu]|LMA 管理"数百个"平台；Ghost Shark 由 Lattice 管理（弱源）[@la_dn_lma,la_speedoscience]|海军十余艘 Lattice 控制无人艇演习失灵；CCA 中角色口径冲突[@la_sherwood_wsj,la_simpleflying]
C2 数据层|NGC2 原型转入 18 亿美元推广；通用数据层基线；CDAO、SSN、Thunderforge[@la_ds_icorps,la_ds_cdl]|火力时间缩短 90%；30 秒；2,500 台终端；65 个节点[@la_milleak_ivymass,la_anduril_scaling]|陆军 CTO"极高风险"备忘录；锁定风险；无独立评估[@la_reuters_memo,la_bd_cdl]
跨域与盟军|陆海空天均有合同或演示；英国、新加坡、北约、澳大利亚项目[@la_ds_ssn,la_ncia_nato]|Mesh 连接全球数千系统[@la_x_mesh]|无经认证的跨密级方案；北约仍在评估；关岛演示仅弱源[@la_venture_atlas]
抗干扰与对抗环境|专利与 SDK 的 DDIL 设计[@la_patent_436,la_sdk_ref]|Ivy Sting 5 卫星与商用通信失效时仍运行[@la_anduril_scaling]|乌克兰 Ghost 受干扰、Altius 停用[@la_tc_wsj]
!end

### 竞争者与锁定风险

Lattice 并不是没有对手。在陆军 NGC2 中，洛克希德·马丁牵头的团队为第 25 步兵师做了竞争性数据层原型[@la_tectonic_lockheed]；在 CCA 自主软件上，Shield AI 的 Hivemind 已在 Fury 机体上飞行，政府明显希望保持自主软件可互换[@la_robotics_hivemind,la_aviationist_hivemind]；在战役规划上，Thunderforge 由 Scale AI 牵头，Lattice 只是其中的数据层[@la_ds_thunderforge]；在空军，ABMS 云端 C2 的软件集成商是 SAIC[@la_af_abms]；在北约 eAirC2 中，Lattice 与 Palantir、Athea 同场评估[@la_ncia_nato]。

但从 2026 年的走势看，陆军正在向 Anduril 与 Palantir 的基线收拢：原本属于数据层供应商的 Raft 成为 NGC2 基线的合作方，原本牵头竞争原型的洛克希德·马丁据一家行业媒体报道转为协助实施 Anduril 基线（单一来源）[@la_bd_cdl,la_defblog_icorps]。陆军自己也把"避免厂商锁定、为传感器和升级留出空间"列为通用数据层的关键考虑[@la_bd_cdl]。当一个军种的反无人机、师级 C2 和企业采购都以同一个数据层为中心时，Lattice 的许可条款（只允许为"兼容的 Lattice 实现"开发应用）就不只是一个法律细节，而是决定未来替换成本的关键因素[@la_sdk_license]。没有找到 GAO 报告、国防授权法条款或国会听证专门讨论 NGC2 的数据权利和锁定问题。

### 负面证据汇总

把分散的负面证据集中起来，可以看到它们主要集中在硬件平台和对抗环境，而不是数据层本身：

【乌克兰（2022—2024）】Ghost 受干扰、Altius 坠毁和脱靶后停用[@la_tc_wsj,la_techbuzz]。有二手页面把 Altius 的电子战失败与对台交付并列讨论（弱源，待核）[@la_drone_warfare]。

【美国海军无人艇演习（2025 年 5 月或夏季，另说 2024 年）】十余艘 Lattice C2 控制的无人艇停机，水兵警告安全风险[@la_sherwood_wsj,la_techbuzz]。另有 2025 年 7 月一艘海军无人艇在加州海峡群岛附近掀翻支援船、试验中止的事故，但该报道没有点名 Anduril，不应混为一谈[@la_ds_navyaccident]。

【Altius 埃格林坠毁】据《华尔街日报》报道，在埃格林空军基地，一架 Altius 从飞机投放后垂直坠地约 8,000 英尺[@la_midbay_eglin]。

【Anvil 野火与 Fury 发动机】一次 Anvil 测试在俄勒冈州引发 22 英亩野火；一台 Fury 发动机在地面测试中受损[@la_sherwood_wsj]。

【NGC2 网络安全】陆军首席技术官备忘录评为"极高风险"，陆军称关键缺陷已缓解[@la_reuters_memo,la_bd_memo]。

【边境效果与隐私】MIT Technology Review 的死亡人数估算和倡导类网站转述的 GAO 隐私审查[@la_mittr_towers,la_sos]。

Anduril 对上述报道的回应是，这些挑战是武器研发中的正常现象，"我们确实会失败……而且很多"，并否认存在根本性技术缺陷[@la_conard]。Anduril 创始人还公开称《华尔街日报》另一篇关于无人艇工厂的报道失实[@la_defblog_wsjfalse]。需要强调的是，这些负面证据大多来自同一组《华尔街日报》报道的转述，原文没能读取，乌方和美方官方也没有回应。

!photo ghostx_romania_flight|美陆军第 10 山地师第 3 旅 317 工兵营在罗马尼亚操作 Ghost-X 无人机飞行（2024 年 11 月 24 日）。Ghost-X 被选入陆军连级小型无人机需求和"复制者"计划；2022 年交付乌克兰的 Ghost 侦察无人机则曾受俄方干扰严重|U.S. Army photo by Pfc. Nathan Arellano Tlaczani，美国政府作品
## （五）案例：从边境到师级战场

:::lead
本节按八类整理 Lattice 的公开案例：边境监视、反无人机、陆军 NGC2、空军 CCA 与 ABMS、海上与水下、盟国与对外销售、演习与联合层级项目、失败与事故。每个案例尽量给出时间、用户、地点、Lattice 的作用、结果和来源。需要说明的是，案例中的"结果"多数是合同或演示层面的结果，而不是实战效能数据；凡只有公司来源或弱源支撑的，均单独标注。节末附案例总表。
:::

### 第一类 边境监视

【案例 1：CBP 自主监视塔（AST）】时间：2018 年试点，2020 年起成为正式采购项目，持续至今。用户：美国海关与边境保护局、边境巡逻队。地点：美墨边境，最早在圣迭戈和尤马，后扩展到埃尔帕索、格兰德河谷等地。Lattice 作用：在塔端自动检测、分类、跟踪人员和车辆，向特工推送告警。结果：2024 年 9 月部署第 300 座，公司称覆盖约 30% 南部陆地边境[@la_cbp_por,la_asdnews_300,la_govconwire_dhs]。这是 Lattice 部署时间最长、规模最大的持续应用，但效能指标从未公开，MIT Technology Review 对其实际效果提出质疑[@la_mittr_towers]。

【案例 2：增程型 Sentry 塔（XRST）】时间：2026 年 6 月 12 日公开（低可信来源称 2025 年 12 月已授予）。用户：CBP，经费来自边境巡逻队。地点：美墨边境。Lattice 作用：新塔与 Lattice 及已有 350 余座标准塔网络集成。结果：合同金额 362,974,500 美元，属自主监视塔 SBIR 第三阶段 IDIQ 下的任务，期限 1 年，采购 200 余座 80 英尺增程塔，自主探测距离超过 5 英里，有人辅助达 7.5 英里[@la_anduril_xrst,la_execbiz_xrst,la_orangeslices_xrst,la_zerog]。合同性质另有"多年扩展"一说[@la_tdn_xrst,la_sos]。2025 年 7 月的《大而美法案》为边境技术拨款，被认为将使这条业务线大幅受益[@la_intercept_bbb]。

!photo sentry_luna_nm_2|新墨西哥州卢纳县 9 号州道旁的 Anduril Sentry 塔（2022 年）。到 2026 年，Anduril 自有标准塔已超过 350 座，并追加 200 余座增程型塔|Electronic Frontier Foundation（EFF），CC BY 4.0

### 第二类 反无人机

【案例 3：SOCOM 反无人系统集成】时间：2022 年 1 月起，期限至 2032 年 1 月。用户：美国特种作战司令部。地点：美国本土内外。Lattice 作用：作为集成内核连接 Sentry、Anvil、Pulsar、FoxHound 及第三方传感器与效应器，自主检测、分类、跟踪目标，向操作员告警并提供交战选项。结果：10 年 IDIQ，上限 9.676 亿美元[@la_dn_socom,la_afcea_socom,la_wt_socom]。

【案例 4：陆战队 MADIS 与 I-CsUAS】时间：2024 年 11 月（MADIS）、2025 年 3 月（I-CsUAS）。用户：美国海军陆战队。地点：MADIS 为车载机动防空，I-CsUAS 覆盖各设施。Lattice 作用：I-CsUAS 以 Lattice 为 C2，集成 Anvil、Pulsar 等多种传感器和效应器，包括交付、安装和维护。结果：MADIS 交战系统约 2 亿美元；I-CsUAS 10 年期上限 6.42 亿美元，至 2035 年 3 月，首笔约 950 万美元，未公布具体型号和数量[@la_ius_madis,la_ds_icsuas,la_wt_icsuas,la_edr_icsuas]。陆战队地基防空项目办公室的演示明确，Anvil 只在人工下令后拦截[@la_marines_gbad]。

【案例 5：Falcon Peak 25.2】时间：2025 年 10 月。用户：美国北方司令部。地点：佛罗里达州埃格林空军基地。Lattice 作用：把 Mobile Sentry、Wisp、Pulsar 和 Anvil 组成一套反无人机套件。结果：Mobile Sentry 探测并跟踪一架"敌方"无人机，Anvil 将其动能摧毁，套件随后交付北方司令部[@la_ius_falconpeak,la_tdp_falconpeak]。另有检索摘要称 Lattice 在一次北方司令部演习中担任通用 C2，日期未核实[@la_armyrec_ibcsm]。

【案例 6：陆军 IBCS-M 反无人机火控】时间：2025 年 11 月 10 日宣布。用户：美国陆军。地点：亚利桑那州尤马试验场。Lattice 作用：作为 IBCS-M 的下一代反无人机火控与 C2，负责传感器融合和"从探测到摧毁"的自动化火控。结果：7 天试验中，数小时内接入一个此前未公开的传感器和效应器，实弹拦截 4 中 4；合同金额和期限未披露[@la_ds_ibcsm,la_janes_ibcsm,la_mes_ibcsm,la_stripes_ibcsm]。

!photo ibcs_tent|美陆军一体化防空反导作战指挥系统（IBCS）的指挥帐篷（2021 年）。2025 年 11 月，陆军选定 Lattice 作为 IBCS 机动型（IBCS-M）的反无人机火控与 C2 平台|U.S. Army（DVIDS），美国政府作品

【案例 7：JIATF 401 通用反无人机 C2】时间：2026 年 3 月。用户：陆军联合跨机构特遣部队 401。地点：全军范围。Lattice 作用：作为"通用反无人机 C2"骨干，把多种反无人机系统连接起来，内容包括 Lattice 软件、集成和培训。结果：200 亿美元企业合同下的首个任务单，约 8,700 万美元（另记 8,770 万美元）[@la_bd_jiatf,la_d1_jiatf,la_ds_20b,la_dronexl]。

【案例 8：陆军原型 C2 导弹防御系统】时间：2026 年 5 月。用户：美国陆军。Lattice 作用：报道标题为原型 C2 导弹防御系统，细节未读取。结果：获得合同[@la_bd_missiledef]。

【案例 9：ORIGIN BLAZE 拦截器集成】时间：2026 年 10 月 1 日。用户：Anduril 与 ORIGIN 公司。Lattice 作用：把第三方 BLAZE 拦截器作为效应器接入 Lattice。结果：完成集成，体现开放架构对第三方效应器的吸纳[@la_overt_blaze]。

【案例 10：国民警卫队反无人机列装】据华盛顿州国民警卫队发布的照片，2026 年其第 10 民事支援队列装了 Anduril 反无人机系统，包括远程摄像塔、Wisp、Pulsar 和 Lattice，并组织了主操作员课程。这一案例只有图片说明支撑，研究笔记中没有对应报道。

!photo wa_ng_cuas|华盛顿州国民警卫队第 10 民事支援队列装的 Anduril 反无人机系统（2026 年），图片说明称系统包括远程摄像塔、Wisp、Pulsar 与 Lattice|Washington National Guard，美国政府作品

### 第三类 陆军下一代指挥控制（NGC2）

【案例 11：NGC2 原型合同】时间：2025 年 7 月 18 日。用户：陆军 C3N 计划执行办公室、第 4 步兵师。地点：科罗拉多州卡森堡。Lattice 作用：作为原型的通用数据层基础，由 Anduril 牵头"Team Anduril"（Palantir、Microsoft、Striveworks、Govini、Instant Connect Enterprise、Research Innovations Inc.）。结果：9,960 万美元、11 个月 OTA，目标为第 4 步兵师构建原型并扩展到师级；陆军同时计划为第 25 步兵师和第 3 军另行竞争[@la_army_ngc2_award,la_ds_ngc2_award,la_dn_ngc2_award,la_ss_ngc2_award,la_insidedef_ngc2]。

【案例 12：Ivy Sting 1 实弹演习】时间：2025 年 9 月。用户：第 4 步兵师，第 77 野战炮兵团第 2 营。地点：卡森堡。Lattice 作用：师级目标处理流程从师部到炮位，完全运行在 Lattice Mesh（部署于坚固的 Voyager 边缘计算套件）和 Palantir Target Workbench 上；测试版炮兵数据工具 AXS 运行在 Lattice Mesh 上，引导 M777 榴弹炮射击。结果：据报道使用 AXS 的炮组 30 秒内完成数字化准备，而 AFATDS 炮组常需先排查连接[@la_die_ivysting1,la_ss_ivysting1,la_bd_ivysting1,la_army_ivysting1]。

!photo ivysting1_aes|"常春藤之刺 1"（Ivy Sting 1）期间，陆军将领向第 77 野战炮兵团第 2 营讲解 NGC2 火炮执行套件（2025 年 9 月 17 日，卡森堡）|4th Infantry Division Public Affairs（DVIDS），美国政府作品

【案例 13：Ivy Sting 2 至 5】时间：2025 年 10 月至 2026 年初。用户：第 4 步兵师。Lattice 作用：持续扩大数据网格和应用规模。结果：按公司说法，用例超过 50 个；Ivy Sting 5 把数据网格扩大到原来的 3 倍，连接 65 个以上战术边缘节点，在通信降级阶段于本地网格上完成"电子战定位到火力打击"的端到端流程，卫星和商用通信失效时仍能运行（公司声称）[@la_anduril_scaling,la_asdnews_scaling,la_militaer_ivysting5]。

!photo ivysting2_ngc2|第 4 步兵师在"常春藤之刺 2"（Ivy Sting II）中推进 NGC2 下一阶段（2025 年 10 月 30 日，卡森堡）|4th Infantry Division Public Affairs（DVIDS），美国政府作品

【案例 14：Ivy Mass 整师上线】时间：2026 年 5 月（春季）。用户：第 4 步兵师全师。Lattice 作用：整个师运行在 NGC2 上，这是 Project Convergence 顶点演习 6（PC-C6）前的最后一次活动。结果：接入 2,500 多台士兵终端；Anduril 称炮兵火力时间比传统系统缩短 90%，均为公司口径[@la_milleak_ivymass,la_meritalk,la_anduril_ngc2_scale]。2026 年 5 月，特种部队也加入了 NGC2 原型实验[@la_bd_sf]。

!photo pcc6_c100|"项目融合—顶点 6"（PC-C6）期间，第 4 步兵师士兵检查无人机（2026 年 7 月 20 日，加州欧文堡）。Ivy Mass 是 PC-C6 前 NGC2 的最后一次整师活动|U.S. Army（DVIDS），美国政府作品

【案例 15：通用数据层基线与 I 军推广】时间：2026 年 6 月 22 日（基线）、2026 年 10 月 5—6 日（推广合同）。用户：美国陆军，首先是第 1 军。Lattice 作用：与 Palantir Foundry 组成"边缘到云"的通用数据网格，Raft 提供注册与联邦服务；Lattice 被定义为连接应用、数据、AI 模型、传感器和载具的"分布式数据层"。结果：基线授予未披露金额，被报道为归入 Anduril 陆军企业协议；推广合同 5 年、上限 18 亿美元、基础期 1.628 亿美元；有一家行业媒体称洛克希德·马丁将协助实施 Anduril 的基线（单一来源）[@la_ds_cdl,la_bd_cdl,la_insidedef_cdl,la_ds_icorps,la_govconwire_icorps,la_defblog_icorps]。陆军目标是在 2026 年底前用 NGC2 同步两个师[@la_d1_twodiv]。

作为对照，第 25 步兵师（夏威夷）的 NGC2 原型由洛克希德·马丁牵头，获 2,600 万美元、16 个月 OTA，2026 年 1 月首次测试其数据层，并通过"闪电涌动"（Lightning Surge）系列演习验证，与 Anduril 和 Lattice 无关[@la_army_lockheed,la_tectonic_lockheed,la_bd_lockheed,la_tdp_lightning]。两条路线竞争的结果是 Anduril 基线成为全陆军标准，这是 Lattice 与 Foundry 组合形成锁定的关键节点。

### 第四类 空军 CCA 与 ABMS

【案例 16：ABMS 与 AFRL 巡航导弹演示】时间：2020 年 9—10 月。用户：美空军、空军研究实验室。地点：美国本土（安德鲁斯联合基地等）。Lattice 作用：探测和跟踪巡航导弹替代目标，操作员确认后向效应器下达交战指令。结果：演示成功[@la_dn_cruise]。另有材料称 Lattice 在一次 ABMS 演习中连接 F-16、NASAMS、MQ-9 和陆军榴弹炮，日期未确定[@la_af_abms,la_lodi411]。

【案例 17：YFQ-44A Fury 与 LMA】时间：2024 年 4 月 24 日 CCA 第一增量胜出；2025 年 10 月 31 日首飞；2026 年 2 月 24 日 LMA 首次在 Fury 上飞行；2026 年 6 月 17 日获生产合同。用户：美空军。Lattice 作用：LMA 作为任务自主软件，通过 A-GRA 可与 Hivemind 切换。结果：生产合同比原计划提前约 4 个月；投产时间有 2026 年 3 月（The Aviationist）与首架俄亥俄制造飞机 7 月 28 日下线（Military Times）两种说法；已完成以惰性 AIM-120 对模拟目标的端到端超视距打击；Anduril 称已向空军交付首架 CCA，空军操作员已自行驾驶 Fury[@la_ds_cca1,la_twz_production,la_die_cca,la_ds_cca_prod,la_aviationist_production,la_militarytimes_rolloff,la_x_cca]。Lattice 在 CCA 中的确切地位存在口径冲突（见第四节）。空军部长 Meink 2026 年 9 月 14 日将目标提高到 2032 年至少 500 架 CCA（二手来源）[@la_migflug]。

!photo yfq44_captive_carry|YFQ-44A 挂载 AIM-120 导弹进行系留挂飞试验（2026 年 2 月）。同月 24 日，Lattice for Mission Autonomy 首次在 YFQ-44A 上飞行|U.S. Air Force，美国政府作品

!photo yfq44_creech_1|YFQ-44A 在内华达州克里奇空军基地（2026 年 7 月 21 日），由空军实验作战部队操作。Anduril 称空军操作员已自行驾驶 Fury|U.S. Air Force，美国政府作品

【案例 18：Hermeus Quarterhorse】Hermeus 公司为 Quarterhorse Mk 2 选用 Lattice，有来源称这是 Anduril 自主软件首次大规模集成到第三方飞机上。该信息来自聚合追踪站点（弱源，待核）[@la_andurilnews_lattice]。

### 第五类 海上与水下

【案例 19：Dive-LD 大型无人潜航器】时间：2024 年 2 月 7 日授予，2025 年 4 月首台交付。用户：海军 PMS 394、国防创新单元、海军无人潜航器第 1 中队。Lattice 作用：竞速测试中用 Lattice 实时跟踪和共享 Dive-LD 位置。结果：与 Oceaneering、Kongsberg 共三家获原型合同，金额未披露[@la_dn_diveld,la_globalsec_diveld]。

!photo dive_ld_uuvgru1|美国海军无人潜航器第 1 大队官兵在华盛顿州基波特训练使用 Anduril Dive-LD 大型无人潜航器（2024 年 12 月 11 日）|U.S. Navy（DVIDS），美国政府作品

【案例 20：澳大利亚 Ghost Shark】时间：2022 年起联合开发，2024 年交付首艘原型，2025 年 9 月 10 日签生产合同（8 月 26 日签署，Anduril 称 9 月 9 日授予），2026 年 4 月 14—15 日交付首批生产艇。用户：澳大利亚皇家海军海上自主系统部队（MASU，SEA 1200 项目）。Lattice 作用：据二手来源，艇载自主功能由 Lattice 管理（弱源，待核）。结果：原型阶段按期按预算完成 3 艘；5 年 17 亿澳元（约 11 亿美元）生产、维护和持续开发合同，首批"数十艘"；交付时间由原定 2026 年 1 月推迟到 4 月左右[@la_minister_ghostshark,la_bd_ghostshark,la_navalnews_ghostshark,la_bd_ghostshark_first,la_tdn_masu,la_speedoscience]。开发经费有约 1.4 亿澳元和约 9,250 万美元两种说法[@la_bd_ghostshark_first,la_wiki_ghostshark]。

!photo ghost_shark_minister|澳大利亚国防部发布：首艘"幽灵鲨"（Ghost Shark）超大型无人潜航器原型完成（2024 年 4 月 18 日）|© Commonwealth of Australia（Department of Defence），仅作评论引用

【案例 21：美国海军无人艇演习失败】见第八类。Dive-LD 之外的海军合同和测试数据、"复制者"计划中 Lattice 的角色，均未能核实；Copperhead 相关海军合同也没有检索到。

### 第六类 盟国与对外销售

【案例 22：英国 TALOS 系列与本土项目】时间：2021 年 9 月（TALOS 试验，380 万英镑）；2023 年 11 月 2 日（TALOS 第三阶段"Entrelazar"，1,700 万英镑，可增至 2,400 万英镑，31 个月）。用户：英国国防部战略司令部。地点：英国及海外常设联合作战基地。Lattice 作用：基地防护、反入侵和反无人机，Lattice 作为核心指挥层。结果：第一阶段已完成，第三阶段执行中或已完成[@la_edr_talos,la_blog_talos,la_gov_uk_17m,la_shephard_talos3,la_armytech_talos3,la_anduril_uk17m]。调查媒体报道，Anduril 自 2019 年起在英国开展业务，服务过皇家海军陆战队和战略司令部[@la_tbij]。英国内政部另有一份边境与海峡监视合同（初始 3 年 1,600 万英镑，延至 2026 年累计 2,100 万英镑），是否使用 Lattice 未知[@la_privacyintl]。2025 年，Anduril 英国公司在英国陆军 Project Asgard 中演示了边缘数据网格[@la_die_asgard]。

【案例 23：新加坡 LMA 合作】时间：2025 年 3 月。用户：新加坡国防科技局与空军。结果：LMA 的首个国际合作[@la_amr_singapore]。

【案例 24：北约 eAirC2】时间：2026 年 7 月 7 日。用户：北约通信与信息局。Lattice 作用：在北约环境中部署 Lattice，作为增强型空中指挥控制的数据平台候选。结果：通过 Anduril 英国公司签约，约 9 个月评估期，与 Palantir、Athea 并列，评估后择一长期实施；这是 Anduril 首个北约合同[@la_anduril_nato,la_ncia_nato,la_die_nato,la_battlepolicy_nato]。

【案例 25：科威特对外军售】时间：2026 年 6 月 5 日批准公告，联邦公报 7 月 22 日刊登。用户：科威特。Lattice 作用：一揽子反无人机系统（Roadrunner-M、Anvil-Kinetic、多型 Sentry 塔、电子战、战术作战中心和 C2）由 Lattice 连接，Anduril 为主承包商。结果：估值 19.8 亿美元，这只是可能销售的估算上限，未见合同签署报道[@la_bd_kuwait,la_dn_kuwait,la_armyrec_kuwait,la_defmatters_kuwait]。

【案例 26：台湾与印太】台湾 2024 年 6 月获批 291 套 ALTIUS-600M（估值 3 亿美元），2025 年 8 月开始交付；2026 年 8 月据报道再签约 1,554 套 Altius-700M 和 478 套 Altius-600ISR，约新台币 269 亿元[@la_dsca_taiwan,la_tdp_taiwan_2025,la_tdp_taiwan_2026]。合同金额另有 3 亿与 11 亿美元之争[@la_tdp_taiwan,la_janes_taiwan]。这些交易的来源都没有提到 Lattice。2025 年 8 月，Anduril 扩大了在台湾和韩国的合作伙伴关系[@la_bd_indopac]；台湾共同生产 Dive-LD/Dive-XL 的说法只见于 Substack（弱源，待核）[@la_substack_taiwan]。日本方面只有 2023 年的谅解备忘录和 2026 年洽购日产工厂的报道，没有防卫省正式合同[@la_defconnect_japan,la_reuters_nissan]。

### 第七类 演习与联合层级项目

【案例 27：陆军 EDGE23】时间：2023 年。用户：美国陆军。Lattice 作用：LMA 支持单兵完成任务前规划并控制多家厂商的无人机，人把地空导弹阵地定为敌对、授权 ALTIUS-600M 打击，系统自动改派 ALTIUS ISR 做毁伤评估。结果：演示成功（公司博客）[@la_blog_edge23]。

【案例 28：Project Convergence 顶点 4】时间：2024 年 3 月。地点：加州欧文堡。据陆军发布的照片，陆军参谋长听取了 Anduril Ghost 能力简报，士兵与 Anduril 开展了人机融合试验。研究笔记中没有该演习中 Lattice 作用的文字记录。

!photo pcc4_hmi|"项目融合—顶点 4"（2024 年 3 月，欧文堡）期间，士兵与 Anduril 开展人机融合试验|U.S. Army（DVIDS），美国政府作品

【案例 29：中央司令部"沙漠守护者 1.0"】时间：约 2024—2025 年。用户：美国中央司令部。地点：中东。Lattice 作用：作为第三方 C2 系统，参演官兵依靠 API 和 SDK 文档集成自己的系统，部分实时完成。结果：定性描述，无定量数据[@la_ocbj_partners]。

【案例 30：CDAO 边缘数据网格与太空监视网】时间：2024 年 11—12 月。用户：CDAO、太空军太空系统司令部。Lattice 作用：CDAO 合同以 Lattice Mesh 为基础推广边缘数据网格，太空军 SSN 现代化以 Lattice 为弹性网状网络。结果：分别为 1 亿美元生产型 OTA 和约 9,970 万美元 IDIQ（要求 2026 年底完成部署）；此前 2022—2024 年 SSN 系列合同累计 3,350 万美元[@la_ds_cdao,la_ds_ssn,la_bd_ssn]。

【案例 31：DIU Thunderforge】时间：2025 年 3 月 5 日。用户：国防创新单元，面向印太司令部和欧洲司令部。Lattice 作用：在 Scale AI 牵头的 AI 战役规划项目中提供数据共享层。结果：项目启动[@la_ds_thunderforge,la_diu_thunderforge,la_scale_thunderforge]。

【案例 32：太空态势感知演示】Varda、LeoLabs 与 Anduril 联合跟踪 Varda 返回舱的轨道机动，数据实时输入 Lattice[@la_execbiz_varda]。

【案例 33："勇敢之盾 2026"关岛防御】时间：约 2026 年 8 月。地点：关岛。Lattice 作用：据称 Anduril 演示了基于 Lattice 的关岛防御作战管理器，融合陆军、空军、海军和导弹防御局的资产。结果：截至 2026 年 9 月 15 日未见后续部署合同。只有二手聚合来源（弱源，待核）[@la_venture_atlas]。

【案例 34："金穹"导弹防御】时间：2026 年 3 月 24 日报道。路透社援引消息人士称，Anduril 与 Palantir 作为一个产业联合体的成员，共同开发"金穹"导弹防御的 C2 软件平台，用于融合各类传感器数据并让指挥官控制武器，计划 2026 年夏季测试，同场的还有 Aalyria、Scale AI 和 Swoop Technologies[@la_usnews_goldendome,la_govconwire_goldendome]。另外，Anduril 是太空军 12 家天基拦截器原型团队之一（12 家合计上限 32 亿美元，2028 年前完成演示）[@la_aft_goldendome,la_bloomberg_sbi]。Lattice 在"金穹"中的具体角色和金额没有一手来源。

### 第八类 失败与事故

【案例 35：乌克兰 Ghost 与 Altius】时间：2022—2024 年。用户：乌克兰军队、乌克兰安全局。结果：约 40 架 Ghost 受俄方干扰严重；Altius 坠毁、脱靶，2024 年停用[@la_tc_wsj,la_techbuzz]。英国国防部另有一份 3,000 万英镑合同向乌克兰交付 Altius，年份按检索摘要推断为 2025 年[@la_privacyintl]。没有证据表明 Lattice 在乌克兰作为 C2 层使用。

【案例 36：美国海军无人艇演习】时间：2025 年 5 月或夏季（另说 2024 年）。地点：加州近海。Lattice 作用：十余艘无人艇由 Lattice C2 控制。结果：无人艇失灵或停机，对其他船只构成危险，水兵警告"安全违规和潜在人员伤亡"[@la_sherwood_wsj,la_techbuzz,la_conard]。

【案例 37：Altius 埃格林坠毁、Anvil 野火、Fury 发动机受损】一架 Altius 在埃格林空军基地从飞机投放后垂直坠地约 8,000 英尺；一次 Anvil 测试在俄勒冈州引发 22 英亩野火；一台 Fury 发动机在地面测试中受损。均据《华尔街日报》报道[@la_midbay_eglin,la_sherwood_wsj]。

【案例 38：NGC2 网络安全备忘录】时间：2025 年 9 月 5 日（路透社约 10 月 3 日报道）。用户：陆军首席技术官办公室。结果：原型被评为"极高风险"，一个应用有 25 个高危漏洞，另三个有 200 多个缺陷待审；陆军称关键缺陷已缓解[@la_reuters_memo,la_bd_memo]。

### 案例总表

!table la_cases|Lattice 主要案例总表|本报告依据研究笔记整理；"结果"多为合同或演示层面，非实战效能；弱源已标注|9,22,30,41,32,26
序号|时间|用户与地点|Lattice 作用|结果|类别与来源
1|2018 至今|CBP，美墨边境|塔端自动检测、分类、跟踪并告警|2020 年成采购项目；2024 年第 300 座|边境[@la_cbp_por,la_asdnews_300]
2|2026-06|CBP，美墨边境|新增增程塔与 Lattice 及 350 余座塔网络集成|3.63 亿美元，200 余座|边境[@la_execbiz_xrst]
3|2022-01|SOCOM，美国本土内外|反无人系统集成内核|10 年 IDIQ，上限 9.676 亿美元|反无人机[@la_afcea_socom]
4|2024-11、2025-03|陆战队，各设施与车载|MADIS 交战系统；I-CsUAS 以 Lattice 为 C2|约 2 亿美元；上限 6.42 亿美元|反无人机[@la_ius_madis,la_ds_icsuas]
5|2025-10|北方司令部，埃格林基地|Falcon Peak 套件融合与交战|拦截成功，套件交付|反无人机[@la_ius_falconpeak]
6|2025-11|陆军，尤马试验场|IBCS-M 反无人机火控，数小时接入新传感器与效应器|实弹 4 中 4，金额未披露|反无人机[@la_ds_ibcsm]
7|2026-03|陆军 JIATF 401，全军|通用反无人机 C2|首单约 8,700 万美元|反无人机[@la_bd_jiatf]
8|2026-10|ORIGIN 公司|第三方 BLAZE 拦截器接入|完成集成|反无人机[@la_overt_blaze]
9|2025-07|陆军第 4 步兵师，卡森堡|NGC2 原型数据层|9,960 万美元 OTA|NGC2[@la_army_ngc2_award]
10|2025-09|第 4 步兵师，卡森堡|Ivy Sting 1：师级目标处理与 AXS 引导 M777|30 秒完成数字化准备（报道）|NGC2[@la_bd_ivysting1]
11|2025-10 至 2026 初|第 4 步兵师|Ivy Sting 2—5 扩展网格与用例|50 余用例、65 个以上节点（公司声称）|NGC2[@la_anduril_scaling]
12|2026-05|第 4 步兵师全师|Ivy Mass 整师上线|2,500 余终端；火力时间缩短 90%（公司声称）|NGC2[@la_milleak_ivymass]
13|2026-06、2026-10|陆军，第 1 军起|通用数据层基线（Lattice 加 Foundry）与推广|5 年上限 18 亿美元|NGC2[@la_ds_cdl,la_ds_icorps]
14|2020-09/10|空军、AFRL，美国本土|ABMS 演示与巡航导弹替代目标交战引导|演示成功|空军[@la_dn_cruise]
15|2024-04 至 2026-07|空军，CCA 项目|LMA 在 YFQ-44A 上飞行，可经 A-GRA 切换|生产合同；角色口径冲突|空军[@la_die_cca,la_aviationist_hivemind]
16|2024-02|海军与 DIU|Dive-LD 竞速测试实时共享位置|2025-04 首台交付|海上[@la_globalsec_diveld]
17|2022 至 2026-04|澳大利亚皇家海军|Ghost Shark 自主功能（弱源）|17 亿澳元生产合同；首批交付推迟至 4 月|海上[@la_minister_ghostshark,la_tdn_masu]
18|2021-09、2023-11|英国国防部|TALOS 基地防护指挥层|380 万英镑；1,700 万英镑|盟国[@la_edr_talos,la_gov_uk_17m]
19|2025-03|新加坡 DSTA 与 RSAF|LMA 合作|首个国际合作|盟国[@la_amr_singapore]
20|2026-07|北约 NCIA|eAirC2 数据平台评估|9 个月评估，与 Palantir、Athea 竞争|盟国[@la_ncia_nato]
21|2026-06|科威特|反无人机一揽子系统的 C2|获批 19.8 亿美元，未见签约|对外销售[@la_bd_kuwait]
22|2023|陆军 EDGE23|单兵指挥多机，自动改派 ISR|演示成功|演习[@la_blog_edge23]
23|约 2024—2025|中央司令部，中东|沙漠守护者 1.0 第三方 C2|定性描述|演习[@la_ocbj_partners]
24|2024-11/12|CDAO、太空军|边缘数据网格；SSN 网状网络|1 亿美元；约 9,970 万美元|联合与太空[@la_ds_cdao,la_ds_ssn]
25|2025-03|DIU，印太与欧洲司令部|Thunderforge 数据共享层|项目启动|联合[@la_diu_thunderforge]
26|约 2026-08|关岛|勇敢之盾防御作战管理器（弱源）|未见后续合同|演习[@la_venture_atlas]
27|2022—2024|乌克兰|Ghost、Altius（未见 Lattice 作 C2）|受干扰失效，Altius 停用|失败[@la_tc_wsj]
28|2025 或 2024|美国海军，加州近海|十余艘无人艇由 Lattice C2 控制|失灵停机，安全风险|失败[@la_sherwood_wsj]
29|2025-09|陆军 CTO|NGC2 原型网络安全评估|"极高风险"，称已缓解|失败与风险[@la_reuters_memo,la_bd_memo]
!end

:::judge 研判要点
- Lattice 的真正护城河不是某项算法，而是"实体加任务"的数据模型和对第三方的接入能力。官方 SDK 显示，它把敌我属性、航迹质量、WILCO 确认、逐字段密级都写进了公开模式；任何传感器或武器只要按生产者或代理模式接入，就能进入杀伤链。这使它在反无人机、师级 C2 这类"多厂商拼装"场景中具有结构性优势，2026 年陆军 200 亿美元企业合同和 NGC2 通用数据层基线标志着这种优势已转化为军种级锁定。
- 证据结构明显"上强下弱"：采购决策是硬证据，定量效能数据几乎全部来自公司，唯一可公开核实的实战场景乌克兰结果负面。对"火力时间缩短 90%""4 中 4""完美击杀"等数字，应作为公司口径使用，等待陆军、GAO 或作战试验鉴定局的独立数据。
- 强电子对抗与网络安全是两大短板。Mesh 的 DDIL 设计有专利和 SDK 支撑，但没有经过公开可核实的强对抗检验；陆军 CTO"极高风险"备忘录、无公开 ATO 与跨域方案，说明快速迭代、多厂商数据层的安全认证仍是现实瓶颈。
- 人机关系在公开案例中一贯是"武器释放由人批准"，但 ROE 配置、小型无人机自动交战模式和对国防部第 3000.09 号指令的落实方式均不透明。随着"一人操控多机"和 CCA 规模化，这一空白将成为政策与伦理争议的焦点。
- Lattice 与 Palantir 的关系正在从"边缘与企业分工"走向"分层合作、局部竞争"：NGC2 中是 Lattice 加 Foundry 的组合，北约 eAirC2 中两家同场竞争。对体系对手而言，值得重点跟踪的是 Lattice 能否从陆军数据层延伸到联合层级（金穹、CJADC2）以及盟军体系（北约、澳大利亚、科威特）。
:::
