# 三、装备与节点图谱：接入两系统的“传感器—射手”家族

:::lead
本章从实物出发，逐类梳理接入或依托 Lattice 与 Maven 智能系统（MSS）的装备与节点：边境与基地防护传感器、反无人机效应器与火控、小型无人机与巡飞弹、协同作战飞机、水下与水面平台、远程打击与工业设施、边缘计算与指挥节点，以及 Maven 一侧的数据源与打击平台。每类装备给出外形与公开参数、在两系统中的角色（传感、效应、通信、计算或数据源）、部署与合同情况和已暴露的问题。我部研判，两系统的装备谱系呈明显的不对称：Lattice 一侧几乎全部是 Anduril 自研或收购的硬件，软件与硬件同源，接入关系由公司直接定义；MSS 一侧没有自有硬件，它的“节点”是国家侦察卫星、商业雷达卫星、无人机视频、信号情报和存量打击平台，接入关系由政府的数据流水线定义。参数部分仅采用研究笔记已有的公开数据，凡只见于公司材料或弱源者均注明。数据截至 2026 年 10 月 10 日。
:::

研判本章内容前需明确三条口径。第一，“接入 Lattice”有三个证据等级：合同或官方材料明确写到 Lattice 的，记为确认；系统架构上基于 Lattice 但所引来源未点名的，记为架构推定；只出现在 Anduril 套件清单、未见集成说明的，记为未确认。研究笔记的结论是，公开确认由 Lattice 控制或融合的系统包括 Sentry 塔（固定型、机动型、增程型）、Wisp、Pulsar、Anvil、ALTIUS-600/600M、Ghost-X、YFQ-44A，以及 IBCS-M 框架下的第三方雷达和效应器；Ghost Shark、Dive-LD、Barracuda 和 Roadrunner 与 Lattice 的集成方式没有公开来源[@la_andurilnews_lattice,la_ds_ibcsm,la_ius_falconpeak,la_speedoscience]。第二，合同金额区分上限、已拨付和对外军售批准估值，三者不能相加。第三，本章照片均取自美国政府公有领域图片、知识共享许可图片或公司新闻图，公司图片仅作评论性引用。

## （一）边境与基地防护传感节点

### Sentry 自主监视塔：Lattice 的第一个“末端节点”

Sentry 塔是 Anduril 的起家产品，也是 Lattice 部署时间最长、数量最多的节点。塔体集成雷达、光电/红外和射频传感器，太阳能供电，由塔端 AI 完成目标检测和分类，再把航迹传给指挥控制节点[@la_dn_cruise,la_c4isrnet_mobilesentry,la_execbiz_xrsentry,co_wiki_anduril]。CBP 官员称这些塔跟踪的是“物体和活动”，不针对个人，也不做人脸识别[@la_fedscoop_towers]。在 Lattice 的数据模型中，一座塔同时扮演两种实体：它把探测结果发布为航迹实体，自身又作为资产实体挂载传感器组件、健康状态和告警[@la_sdk_entity,la_sdk_health]。塔掉线、电量不足等状况都以资产实体告警的形式出现在共用作战图上。

!photo sentry_luna_nm_1|新墨西哥州卢纳县 9 号州道旁的 Anduril Sentry 塔及其底座（2022 年）。塔顶为传感器舱，下部为供电与通信设备，整塔可在路旁空地快速架设|Electronic Frontier Foundation（EFF），CC BY 4.0

型号沿三条线发展。固定型是 CBP 自主监视塔（AST）项目的主体；2022 年 10 月 Anduril 推出轮式机动型 Mobile Sentry；2024 年 5 月推出增程型[@la_c4isrnet_mobilesentry,la_execbiz_xrsentry]。增程型塔高 80 英尺，自主探测距离超过 5 英里，有人辅助时可达 7.5 英里[@la_execbiz_xrst]。机动型的主要用途已从边境转向军事基地防护：2025 年 10 月北方司令部“猎鹰峰 25.2”演示中，Mobile Sentry 承担自主探测与跟踪，发现并锁定一架“敌方”无人机后交由 Anvil 拦截，整套设备随后交付北方司令部[@la_ius_falconpeak,la_tdp_falconpeak]。

部署规模方面，CBP 于 2020 年将 AST 列为边境巡逻队的正式采购项目，当时计划总数 200 座，即在已有 60 座基础上于 2021—2022 财年再采购 140 座[@la_cbp_por,la_fedscoop_towers]。Anduril 2024 年 9 月宣布部署第 300 座，公司称覆盖约 30% 的南部陆地边境，这一比例指地理覆盖，与检测或拦截效果无关[@la_asdnews_300]。2026 年 6 月，CBP 以 362,974,500 美元采购 200 余座增程型塔（XRST），合同挂在自主监视塔 SBIR 第三阶段 IDIQ 下，期限 1 年，新塔须与已有 350 余座标准塔组成的网络和 Lattice 集成[@la_anduril_xrst,la_execbiz_xrst,la_orangeslices_xrst]。按这组数字，Anduril 自有标准塔加增程塔总量将超过 550 座。全部供应商的边境塔总数另有 803 座和约 830 座两种说法，均未与 GAO 原文核对[@la_mittr_towers,la_sos]。

!photo sentry_tecate|加州特卡特（Tecate）山丘上的 Anduril Sentry 塔远景（2022 年）。山地部署可扩大视距，塔体在山脊上形成连续监视链|Electronic Frontier Foundation（EFF），CC BY 4.0

Sentry 塔进入军事用途的时间早于反无人机大合同。据美国陆军发布的图片说明，2020 年 1 月 Anduril 技术运营人员已在加州二十九棕榈镇的演习中协助部队组装 Sentry 哨塔。2021 年 9 月，英国国防部战略司令部 jHub 授予 Anduril 380 万英镑的 TALOS 基地防御试验合同，系统基于 Lattice，用 Sentry 塔、地面传感器和无人机检测、分类、跟踪地面与空中入侵[@la_edr_talos,la_blog_talos]；2023 年 11 月的第三阶段合同金额 1,700 万英镑，可增至 2,400 万英镑，期限 31 个月，面向海外常设联合作战基地的固定设施防护[@la_gov_uk_17m,la_shephard_talos3]。2026 年 6 月获批的科威特军售方案中包含“多型 Sentry 塔”，由 Lattice 统一连接[@la_bd_kuwait,la_defmatters_kuwait]。

!photo cuas_fire_control_dvids|Anduril 技术运营人员马特·里德（Matt Reed）在加州二十九棕榈镇演习中协助组装 Sentry 哨塔（2020 年 1 月）。这是 Sentry 塔较早出现在美军演训场的影像记录|U.S. Army（DVIDS），美国政府作品

问题面集中在效果与隐私两项。检测概率、虚警率和系统可用率从未公开，也没有找到 GAO 或国土安全部监察长的相关数据。MIT Technology Review 2026 年 9 月的调查估算，2021 年以来有 110 多人死在 Anduril 监视塔覆盖范围内，并质疑数十亿美元的监视投入为何未能及早发现处于危险中的人员，该数字为该刊自行估算[@la_mittr_towers]。一家倡导类网站称 GAO 2024 年按六项隐私保护措施评估 CBP 塔项目，CBP 全部不达标，此说未与 GAO 原文核对[@la_sos]。2025 年 7 月的《大而美法案》为边境技术拨款，被认为将使这条业务线进一步扩张[@la_intercept_bbb]。

### Wisp 与雷达：从自研到收购补齐

Wisp 是 Anduril 套件中与 Sentry 塔配合的传感器。公开资料只记录了它的角色，没有参数：在“猎鹰峰 25.2”中，Wisp 与 Pulsar 作为补充传感器，协助 Mobile Sentry 完成探测和跟踪[@la_ius_falconpeak]。据华盛顿州国民警卫队 2026 年的发布，其第 10 民事支援队列装的 Anduril 反无人机系统包括远程摄像塔、Wisp、Pulsar 与 Lattice，同年 9 月又组织了反无人机主操作员课程，课程内容包括组装 Wisp 和 Pulsar[@gp_dvids_wang,gp_dvids_wang_course]。这说明 Wisp 已进入国民警卫队这一级的本土防护部队。

雷达方面，Anduril 主要靠收购补齐。2025 年 1 月宣布收购 Numerica 的雷达与指挥控制业务，带入 Spyglass、Spark 两型雷达和 Mimir 指挥控制软件，交易完成日期未核实[@la_builtin_what,la_contrary]。陆军 IBCS-M 试验则显示了另一条路径：在亚利桑那州尤马试验场为期 7 天的试验中，Lattice 在数小时内接入了一型此前未公开的传感器和效应器[@la_ds_ibcsm]。第三方雷达通过“生产者”模式向 Lattice 发布航迹实体，这是 SDK 定义的标准接入路径[@la_sdk_ref]。

太空域的传感节点也被纳入同一网格。2024 年 11 月，太空军太空系统司令部授予约 9,970 万美元（另记 9,960 万美元）的太空监视网（SSN）现代化合同，以 Lattice 作为弹性网状网络连接地面监视传感器，要求 2026 年底完成部署；此前 2022—2024 年的 SSN 系列升级合同累计 3,350 万美元[@la_ds_ssn,la_bd_ssn,la_spaceinsider]。Varda、LeoLabs 与 Anduril 还联合跟踪 Varda 返回舱的轨道机动，数据实时输入 Lattice[@la_execbiz_varda]。

## （二）反无人机效应器与火控

反无人机是 Lattice 合同规模最大的领域。SOCOM 2022 年的系统集成伙伴合同（上限 967,599,957 美元）把 Sentry、Anvil、Pulsar 和 FoxHound 列为配套硬件，并要求集成第三方传感器与效应器[@la_wt_socom,la_afcea_socom,la_dn_socom]。此后的陆战队、陆军项目基本沿用“Lattice 指挥控制加 Anduril 硬件加第三方设备”的结构。FoxHound 在研究笔记中只有名称，没有参数和用途说明。

### Anvil：唯一有官方人机规则记录的拦截器

Anvil 是 Anduril 的动能拦截无人机，2021 年 9 月前后公开，以动能方式摧毁目标无人机，2022 年即列入 SOCOM 反无人机配套硬件[@la_wt_socom,la_ius_falconpeak]。陆战队地基防空项目办公室的演示说明是目前对 Anvil 交战规则最权威的记录：Anvil 可利用传感器航迹数据自主跟踪目标，但只在人工操作员下令后实施拦截，并可通过 Lattice 界面控制[@la_marines_gbad]。在 Lattice 体系中，Anvil 属于“可受领任务的代理”，通过 task_catalog 声明拦截能力，接收拦截任务后依次回报确认、执行和结果状态[@la_sdk_task_catalog,la_sdk_task_status_status]。

Anvil 出现在 SOCOM、陆战队设施反小型无人机（I-CsUAS）、“猎鹰峰 25.2”和科威特军售方案（Anvil-Kinetic）中[@la_ds_icsuas,la_ius_falconpeak,la_bd_kuwait]。I-CsUAS 合同为 10 年期 IDIQ，上限 6.42 亿美元（另记 6.422 亿），内容为 Lattice 指挥控制加 Anvil 和 Pulsar，首笔约 950 万美元，未公布型号和数量[@la_ds_icsuas,la_wt_icsuas]。问题面方面，据《华尔街日报》报道，一次 Anvil 测试在俄勒冈州引发 22 英亩的野火[@la_sherwood_wsj]。

### Roadrunner：可回收拦截弹

据 2025 年阿布扎比 IDEX 防务展的展品说明，Roadrunner 为可回收的双涡喷拦截器。2024 年 10 月 8 日，国防部一份 249,978,466 美元的生产合同采购 500 发 Roadrunner-M 全备弹，同时包括 Pulsar 电子战系统，客户未具名[@la_dn_roadrunner]。2026 年 6 月获批的科威特军售包含 Roadrunner-M，估值 19.8 亿美元的一揽子方案以 Anduril 为主承包商[@la_bd_kuwait,la_dn_kuwait]。Anduril 计划 2026 年底前在俄亥俄“武库-1”工厂生产 Roadrunner[@la_bd_arsenal1]。

Roadrunner 与 Lattice 的集成方式没有公开来源，研究笔记将其列为未确认[@la_andurilnews_lattice]。实战拦截记录同样没有找到。2026 年对伊朗作战期间，Anduril 总裁称公司是对抗“沙希德”无人机的“主要”系统，但拒绝透露部署了哪些系统；报道同时指出，并不清楚相关系统是否近期在中东部署过[@la_aol_epicfury]。

### Pulsar：电子战传感与干扰

Pulsar 是 Anduril 的电磁战系统。“猎鹰峰 25.2”中它与 Wisp 一起作为传感器使用，陆战队 I-CsUAS 合同则把它列为电子战手段[@la_ius_falconpeak,la_ds_icsuas]。它是 SOCOM、I-CsUAS、2024 年 Roadrunner 合同和华盛顿州国民警卫队列装方案的组成部分[@la_wt_socom,la_ds_icsuas,la_dn_roadrunner,gp_dvids_wang]。2025 年 4 月，Anduril 发布轻量化的 Pulsar-L，定位为“快速部署”型电子战系统[@gp_anduril_pulsarl]。

!photo pulsar_press|Anduril Pulsar 电磁战系统（公司图，2024 年 5 月发布）。Pulsar 在 SOCOM、陆战队 I-CsUAS 和“猎鹰峰”演示中与 Lattice 配套|Anduril Industries，公司图片，仅作评论引用

在 Lattice 数据模型中，Pulsar 的输出最可能落在 signal 组件和“关注信号”模板上，这两者是 SDK 为电磁域预留的对象类型[@la_sdk_entity,la_sdk_ontology_tpl]。这一对应关系是我部依据 SDK 结构作出的推断，Anduril 没有公开 Pulsar 的数据接口。

### MADIS：陆战队车载防空中的 Anduril 部分

陆战队防空一体化系统（MADIS）是陆战队的车载近程防空与反无人机系统，陆战队 2024 年将其作为提升空中优势的新型防空系统对外介绍[@gp_marines_madis]。据陆军陆地系统项目执行办公室发布的图片说明，Mk1 型以联合轻型战术车（JLTV）为底盘，2023 年 9 月 Mk1 与 Mk2 在尤马试验场进行系统集成测试。2024 年 11 月，Anduril 获得约 2 亿美元合同，承包 MADIS 的反无人机交战系统[@la_ius_madis,la_overt_642]。据报道，2025 年 4 月陆战队在菲律宾“肩并肩 25”演习中展示了新型 MADIS 反无人机系统[@gp_armyrec_madis]。

!photo madis_mk1|陆战队 MADIS Mk1（JLTV 底盘）在测试中（2023 年 9 月）。车顶集成传感器与武器站，Anduril 承包其反无人机交战系统|PEO Land Systems（经 DVIDS），Public Domain Mark 1.0

MADIS 合同在所引来源中没有点名 Lattice，研究笔记按架构推定处理[@la_ius_madis]。MADIS 的意义在于它把 Anduril 的交战软件放进了一型由传统车辆和武器构成的正式装备，这与 Sentry、Anvil 那类自研硬件的路径不同。

### IBCS-M 火控与 JIATF-401 通用指挥控制

2025 年 11 月 10 日，陆军选定 Lattice 作为机动型一体化作战指挥系统（IBCS-M）的反无人机火控与指挥控制平台，负责传感器融合和“从探测到摧毁”的自动化火控[@la_ds_ibcsm,la_execbiz_ibcsm]。陆军与国防创新单元（DIU）此前已联合选定 Anduril 推进下一代反无人机火控能力[@gp_dvids_cuas_fc]。尤马 7 天试验中，Lattice 在数小时内接入一型未公开的传感器和效应器，实弹拦截 4 中 4；合同金额和期限未披露[@la_ds_ibcsm,la_janes_ibcsm]。The Defense Post 以“完美击杀纪录”为题报道，细节来自公司[@la_tdp_ibcsm]。IBCS 核心由诺斯罗普·格鲁曼承制，Lattice 与 IBCS 核心在“爱国者”和 LTAMDS 层面如何对接没有公开细节[@la_uasmag_ibcsm,la_stripes_ibcsm]。

在 IBCS-M 中，Lattice 第一次以“火控节点”而非“传感器节点”或“效应器节点”的身份进入陆军防空体系。2026 年 3 月，陆军 200 亿美元企业合同下的首个任务单（约 8,700 万美元，另记 8,770 万美元）交给联合跨机构特遣部队 401（JIATF-401），以 Lattice 作为“通用反无人机指挥控制”，把多种反无人机系统连接起来[@la_bd_jiatf,la_d1_jiatf]。JIATF-401 同期采购的效应器多数并非 Anduril 产品：2026 年 1 月首笔“复制者 2”采购为 Fortem DroneHunter F700，2 月采购 Perennial Autonomy Bumblebee V2（520 万美元）[@co_soldiersys_jiatf,co_defpost_bumblebee]。2026 年 10 月 1 日，ORIGIN 公司的 BLAZE 拦截器完成与 Lattice 的集成[@la_overt_blaze]。我部研判，Lattice 在反无人机领域的地位正从“自家硬件的操作系统”转为“多厂商设备的火控总线”，其护城河在接入能力，单一拦截器的性能已居次要位置。

## （三）小型无人机与巡飞弹

### Ghost 与 Ghost-X：从侦察直升机到陆军连级无人机

Ghost 是 Anduril 早期的小型直升机式侦察无人机。2021 年英国部队防护技术演示中使用的是 Ghost 4 加 Lattice 的组合[@la_tbij]。2022 年，Anduril 向乌克兰提供约 40 架 Ghost，据《华尔街日报》报道（经 TechCrunch 转述），这批无人机受俄方干扰严重，士兵很快感到沮丧[@la_tc_wsj]。

Ghost-X 是其后继型。2024 年秋，陆军“连级小型无人机定向需求”第一批次选定 Anduril Ghost-X 与 PDW C-100，经国防后勤局合同载体授出，金额 1,441.7 万美元，来源未说明是否为两家合计[@co_ius_ghostx]。2024 年 10—11 月，Ghost-X 入选“复制者 1.2”[@co_ds_ghostx_replicator,co_ius_replicator2]。Anduril 网站称 Ghost-X 的指挥控制运行在 Lattice 上，这一说法经检索摘要转述，属公司口径[@la_cyberwarzone]。陆军方面，据陆军发布的图片说明，2024 年 3 月“项目融合—顶点 4”期间陆军参谋长听取了 Anduril Ghost 能力简报[@gp_dvids_pcc4_csa]；2024 年 11 月，第 10 山地师第 3 旅第 317 工兵营在罗马尼亚米哈伊尔·科格尔尼恰努空军基地附近操作 Ghost-X 飞行。

!photo ghostx_romania_prep|美陆军士兵在罗马尼亚米哈伊尔·科格尔尼恰努空军基地附近为 Ghost-X 无人机做起飞前准备（2024 年 11 月）。Ghost-X 为陆军连级小型无人机需求首批选型之一|U.S. Army（DVIDS），美国政府作品

在 Lattice 体系中，Ghost-X 属于既能感知又能接受任务的资产：作为传感器发布关注点和航迹，作为资产在 task_catalog 中声明侦察能力，可被 Lattice for Mission Autonomy 调度[@la_sdk_task_catalog,la_blog_lma]。问题面上，Reuters 2025 年 11 月报道 Anduril Ghost 在乌克兰难以对抗俄方电子战，这一记录与 Ghost-X 的电子战韧性直接相关，尚无公开的 Ghost-X 抗干扰测试数据[@co_bnn_crashes]。

### ALTIUS 系列：管射无人机与巡飞弹

ALTIUS 系列来自 Anduril 收购的 Area-I，收购日期有 2021 年 4 月和 2022 年 10 月两种记法[@la_contrary,la_andurilnews_acq]。系列基本型 ALTIUS-600 为管射无人机，可从地面发射器或无人机上发射；2020 年 3 月陆军航空导弹中心在尤马试验场对其进行了飞行试验，2021 年 3 月空军 XQ-58A“女武神”在尤马投放了 ALTIUS-600。型号谱系包括侦察型 ALTIUS-600（600ISR）、打击型 ALTIUS-600M，以及更大的 ALTIUS-700M[@la_blog_edge23,la_tdp_taiwan_2026]。

!photo altius600_area_i|ALTIUS-600 管射无人机在尤马试验场飞行（2020 年 3 月，陆军作战能力发展司令部航空导弹中心试验）。ALTIUS 系列由 Anduril 收购的 Area-I 研制|U.S. Army photo by Jose Mejia-Betancourth（CCDC AvMC），美国政府作品

ALTIUS 是 Lattice 杀伤链演示中出镜最多的效应器。2023 年陆军 EDGE23 演习中，一名士兵用 Lattice for Mission Autonomy 把地空导弹阵地定为“敌对”，授权 ALTIUS-600M 实施打击，随后系统自动把一架 ALTIUS 侦察型改派去做毁伤评估[@la_blog_edge23]。这是 Lattice“人做决策、机器做调度”最完整的公开记录。

合同与部署主要在美国以外。2024 年 6 月 18 日，美国国务院批准向台湾出售最多 291 套 ALTIUS 600M-V，估值 3 亿美元，含发射器和地面控制站，2025 年 8 月开始交付[@la_dsca_taiwan,la_tdp_taiwan_2025]；台湾陆军称 2025 年共收到 131 架[@co_bnn_crashes]。2026 年 8 月，据报道台湾又采购 1,554 套 ALTIUS-700M 和 478 套 ALTIUS-600ISR，约新台币 269 亿元，是否属对外军售未确认[@la_tdp_taiwan_2026]。美方一侧，ALTIUS-600 入选“复制者 1.2”，用于陆战队“建制精确火力”，不同来源对承担项目的军种说法不一[@co_ius_replicator2,co_axios_replicator]。英国国防部另有约 3,000 万英镑合同向乌克兰交付 ALTIUS[@la_privacyintl]。台湾、乌克兰相关交易的来源均未提到 Lattice。

ALTIUS 是 Anduril 产品中负面记录最多的一型。据《华尔街日报》报道，乌克兰安全局使用的 ALTIUS 坠毁、未命中目标，2024 年停用；在埃格林空军基地，一架 ALTIUS 从飞机投放后垂直坠地约 8,000 英尺[@la_tc_wsj,la_midbay_eglin]。Reuters 报道 2025 年 11 月空军测试中又坠毁两架[@co_bnn_crashes]。这些失败出在飞行平台、导航和数据链，与 Lattice 软件本身无直接关系，但它们发生在 Lattice 宣传最重的“边缘自主、抗干扰”环节。

### Bolt-M：单兵便携巡飞弹

Bolt-M 是 Anduril 的单兵便携巡飞弹，2024 年 10 月前后公开，TWZ 的报道将其定位为“让自杀式无人机攻击更易用、更有效”的产品[@gp_twz_boltm]。研究笔记没有取得其重量、航程、战斗部等参数，SOCOM 相关 Bolt 合同也未检索到[@gp_twz_boltm]。

!photo bolt_m_press|Anduril Bolt-M 单兵便携巡飞弹（公司图，2024 年 10 月前后发布）。Bolt-M 面向班排级打击任务，公开资料未见其参数与正式合同|Anduril Industries，公司图片，仅作评论引用

Bolt-M 与 Lattice 的关系没有公开说明。我部研判，Bolt-M 所在的单兵巡飞弹市场是 2025 年后美军“无人机主导权”计划的重点：该计划拟在两年内采购约 34 万架小型攻击无人机，单价从约 5,000 美元降到 2,300 美元[@co_army_dd,co_ds_2602_dd]。这一价格区间对 Anduril 的成本结构构成压力，Bolt-M 能否进入这一批量采购尚无公开信息。

## （四）协同作战飞机：YFQ-44A“狂怒”与 YFQ-42A

YFQ-44A 是 Anduril 体量最大的空中平台。其前身是 Blue Force Technologies 的 Fury 自主飞机，Anduril 于 2023 年 9 月 7 日收购该公司[@la_janes_blueforce,la_wiki_yfq44]。2024 年 4 月 24 日，Anduril 与通用原子公司在空军 CCA 第一增量中胜出，进入详细设计、制造和试验阶段，洛克希德·马丁、诺斯罗普·格鲁曼和波音出局；项目层面的经费为 2025 财年申请 5.57 亿美元，2029 财年前计划约 90 亿美元[@la_ds_cca1,la_twz_cca1]。2025 年 5 月，生产代表型试验机在科斯塔梅萨的测试舱内进行地面试验[@gp_afmc_yfq44]。

!photo yfq44_ground_test|YFQ-44A 生产代表型试验机在加州科斯塔梅萨测试舱内进行地面试验（2025 年 5 月）。CCA 第一增量生产代表型机体由此进入地面综合试验|U.S. Air Force（DVIDS），美国政府作品

!photo yfq44_paris2025|2025 年 6 月巴黎航展上展出的 Anduril YFQ-44“狂怒”协同作战飞机。该机是 Anduril 在欧洲防务展会上展示的重点平台|Artvill（Wikimedia Commons），CC BY 4.0

试飞与交付节奏很快。YFQ-44A 于 2025 年 10 月 31 日首飞；2026 年 2 月进行挂载 AIM-120 的系留挂飞试验，同月 24 日 Lattice for Mission Autonomy 首次在该机上飞行[@la_twz_production,la_die_cca]。The Aviationist 报道，Fury 在同一次飞行中先后运行 Shield AI 的 Hivemind 和 Anduril 的 LMA，通过早期“政府参考自主架构”（A-GRA）在两套软件之间切换[@la_aviationist_hivemind]。该机已完成以惰性 AIM-120 对模拟目标实施的端到端超视距打击[@la_militarytimes_rolloff]。2026 年 6 月 17 日，空军选定 Anduril（FQ-44A）和通用原子（FQ-42A）进入第一增量生产，比原计划提前约 4 个月[@la_ds_cca_prod,la_twz_production]。投产时间有 2026 年 3 月（The Aviationist）和首架俄亥俄造机 7 月 28 日下线（Military Times）两种说法[@la_aviationist_production,la_militarytimes_rolloff]。Anduril 称已向空军交付首架 CCA，空军操作员已自行驾驶 Fury[@la_x_cca]。

在两系统体系中，YFQ-44A 的位置有两层。机体与武器属于效应器；机载 LMA 属于 Lattice 的应用层。Lattice 在 CCA 中的地位存在口径冲突：一说空军 2026 年 6 月为 CCA 下一阶段选定 LMA，一说 Lattice 与通用原子、洛克希德、诺斯罗普、RTX Collins 和 Shield AI 同在自主软件池中竞争至 2027 年[@la_die_cca,co_circleville_cca,la_simpleflying]。空军以 A-GRA 保持自主软件可替换，Anduril 拥有机体并不保证其软件独占[@la_robotics_hivemind]。

YFQ-42A 是通用原子的方案，2025 年 8 月 27 日试飞，2026 年 6 月与 FQ-44A 同时获得生产合同[@gp_dvids_yfq42,la_ds_cca_prod]。两型机分别以“复仇”和“狂怒”命名，空军部长米因克 2026 年 9 月把目标提高到 2032 年前至少 500 架 CCA（二手来源）[@la_migflug]。YFQ-42A 的自主软件同样受 A-GRA 约束，Lattice 在该机上的角色没有公开记录。Palantir 在 CCA 中没有公开角色[@co_ds_2606_cca]。

!photo yfq42_cca_dvids|通用原子 YFQ-42A 在试飞中（2025 年 8 月 27 日）。YFQ-42A 与 YFQ-44A 同为 CCA 第一增量入选机型，2026 年 6 月两型同时转入生产，本图作对比参照|U.S. Air Force（DVIDS），美国政府作品

问题面方面，据《华尔街日报》报道，一台 Fury 发动机在地面测试中受损[@la_sherwood_wsj]。CCA 合同金额未披露，第一增量产量、单价和 Lattice 在其中的软件收入都无公开数据。

## （五）水下与水面节点

### Dive-LD：Lattice 确认接入的水下平台

Dive-LD 是大型无人潜航器，源自 Anduril 收购的 Dive Technologies，收购日期有 2022 年 2 月和 2023 年 3 月两种记法，被收购方后改组为 Anduril Maritime[@la_contrary,la_notboring]。2024 年 2 月 7 日，海军 PMS 394 与 DIU 选定 Anduril、Oceaneering 和 Kongsberg 三家研制大型无人潜航器原型，合同金额未披露[@la_dn_diveld]。竞速测试中，Anduril 用 Lattice 实时跟踪和共享 Dive-LD 位置，这是 Lattice 接入水下平台唯一有明确记载的案例[@la_globalsec_diveld]。2025 年 4 月首台交付海军无人潜航器第 1 中队[@co_gs_divel]。

水下平台与 Lattice 的连接受物理条件限制（推断）。潜航时难以维持射频链路，Lattice 的“实时优先、回填使用剩余带宽”设计在水下只能体现为上浮或经水面中继时的批量同步[@la_patent_436]。公开资料没有说明 Dive-LD 的通信方式。台湾共同生产 Dive-LD/Dive-XL 的说法只见于 Substack（弱源）[@la_substack_taiwan]。

### Ghost Shark：澳大利亚的超大型无人潜航器

Ghost Shark 是 Anduril 澳大利亚公司与澳大利亚海军联合开发的超大型自主潜航器（XL-AUV）。2022 年启动联合开发，原型阶段生产 3 艘，2024 年交付首艘原型，原型阶段按期、按预算完成[@la_bd_ghostshark_first,la_wiki_ghostshark]。2025 年 9 月 10 日，澳方签订 5 年期生产、维护和持续开发合同，金额 17 亿澳元（约 11 亿美元），首批“数十艘”[@la_minister_ghostshark,la_navalnews_ghostshark,gp_defnews_ghostshark]。悉尼 7,400 平方米的工厂计划 2026 年全面量产，官方将其定位为 AUKUS 核潜艇的补充，经批准后可出口[@co_minister_ghostshark,co_sldinfo_ghostshark]。2026 年 4 月，澳海军海上自主系统部队（MASU）成立并接收首批生产艇，交付时间由原定 2026 年 1 月推迟到 4 月左右[@la_tdn_masu]。开发经费有约 1.4 亿澳元和约 9,250 万美元两种说法[@la_bd_ghostshark_first,la_wiki_ghostshark]。

Ghost Shark 由 Lattice 管理自主功能的说法只见于二手来源，研究笔记标为弱源[@la_speedoscience,la_engineers_ghostshark]。这一点决定了 Ghost Shark 在本章中的定位：它是 Anduril 硬件出口最成功的样板，却不能作为 Lattice 已进入盟国水下作战体系的证据。

### 无人艇编队与潜艇工业

水面方向，Lattice 有一次重要的负面记录。据《华尔街日报》报道，美国海军一次加州近海演习中，十余艘由 Lattice 指挥控制的无人艇失灵或停机，对其他船只构成危险，水兵警告存在“安全违规和潜在人员伤亡”；演习时间有 2025 年 5 月或夏季、2024 年两种说法，Anduril 称这是迭代开发的一部分[@la_sherwood_wsj,la_techbuzz,la_conard]。2025 年 7 月另有一起海军无人艇在海峡群岛附近掀翻支援船的事故，该报道没有点名 Anduril[@la_ds_navyaccident]。研究笔记没有检索到 Copperhead 等水下弹药的海军合同。

2026 年 10 月 6 日，海军授予 Anduril 上限 29 亿美元的弗吉尼亚级潜艇部件合同，由 Anduril 自投 37 亿美元在巴尔的摩建设的“武库-2”船厂生产鱼雷管等部件，2030 年投产[@la_cnbc_sub,la_janes_sub]。该合同属工业供给，与 Lattice 无关。

## （六）远程打击与工业基础

### Barracuda：低成本巡航导弹

Barracuda 是 Anduril 的低成本巡航导弹系列。地面发射型 Barracuda-500M 采用集装箱式发射，The Aviationist 2026 年 5 月 16 日以“Anduril 将向美陆军供应地面发射型 Barracuda-500M”为题作了报道[@gp_aviationist_barracuda]。据 Sandboxx 报道，陆军将采购 3,000 枚 Barracuda-500M，2027 年起每年 1,000 枚，合同金额未披露，分析师推测单价 15 万至 30 万美元，合同日期未核实[@co_sandboxx_barracuda]。“武库-1”计划在 2026 年底前生产 Barracuda[@la_bd_arsenal1]。

!photo barracuda_500m_press|Anduril Barracuda-500 地面发射构型试射（公司图）。地面发射型 Barracuda-500M 采用集装箱式发射，据报道陆军拟采购 3,000 枚|Anduril Industries，公司图片，仅作评论引用

Barracuda 与 Lattice 的集成方式没有公开来源[@la_andurilnews_lattice]。另有弱源称台湾中山科学研究院与 Anduril 于 2025 年 9 月同意合作生产 Barracuda-500 和水下无人机[@co_eurasian_taiwan]。我部研判，Barracuda 是 Anduril 从“传感器与近程拦截”走向“纵深打击”的关键一步；如果陆军 3,000 枚的采购属实，Lattice 的任务链将首次延伸到数百公里级的火力，而这一延伸目前没有任何公开的接口与交战规则说明。

### 固体火箭发动机

2023 年 6 月 Anduril 收购固体火箭发动机企业 Adranos[@la_builtin_what]。此后获得海军 SM-6 二级 21 英寸发动机演示合同（1,900 万美元，2024 年 6 月）、陆军 4.75 英寸发动机研发合同（2025 年 3 月）和《国防生产法》第三章产能资助 4,370 万美元（日期待核）[@co_wdam_srm,co_dn_srm475,co_tectonic_dpa]。这条线服务于弹药产能，与 Lattice 无直接关系。

### “武库-1”“武库-2”与金穹天基拦截器

2025 年 1 月 16 日，Anduril 宣布在俄亥俄州皮卡韦县建设“武库-1”工厂，占地 500 英亩、建筑面积 500 万平方英尺，承诺 2035 年前创造约 4,000 个岗位，获 JobsOhio 3.1 亿美元资助和州税收抵免 4.522 亿美元[@la_dn_arsenal1,la_ohio_arsenal1]。2026 年 3 月 Fury 在此开始生产，计划年底前同时生产 Fury、Roadrunner、Barracuda 和一种保密平台[@la_bd_arsenal1]。武库系列工厂是 Anduril“先投产能、再拿订单”模式的物质载体[@co_dn_arsenal1,co_cnbc_sub]。

“金穹”导弹防御是 Anduril 硬件与软件同时介入的联合级项目。2026 年 4 月 24 日，太空系统司令部向 12 家公司授出 20 份天基拦截器原型 OTA，合计上限 32 亿美元，Anduril 牵头一个由 Impulse、Inversion、K2、Sandia、Voyager 组成的团队，目标 2028 年前完成演示，Anduril 份额未披露[@la_bloomberg_sbi,la_aft_goldendome,co_fortune_sbi]。另有二手来源称该团队 8 月通过首次设计评审[@gp_flyingmag_gd]。软件层面，路透社 2026 年 3 月援引知情人士称，Anduril 与 Palantir 同属一个产业联合体，开发连接雷达、卫星、传感器和拦截弹的指挥控制平台，金穹负责人盖特莱因上将称之为“胶水层”[@la_usnews_goldendome,co_cxo_gd]。

!photo golden_dome_map|“美国金穹”导弹防御系统示意图板（2025 年 5 月 20 日，白宫椭圆形办公室，裁切）。Anduril 牵头天基拦截器原型团队之一，并据报与 Palantir 共同开发金穹指挥控制软件层|The White House，美国政府作品

金穹中 Lattice 的具体角色、合同金额和测试结果都没有一手来源，MSS 本身在金穹中的角色也没有任何来源提及[@mv_reuters_goldendome]。

## （七）边缘计算与指挥节点

### Menace 与 Voyager：Lattice Mesh 的硬件底座

Lattice Mesh 需要运行在可部署的计算硬件上，这一层由 Menace 系列承担。2025 年 5 月 5 日，Anduril 签约收购 Klas，将其 Voyager 坚固边缘计算与战术通信硬件纳入自主系统和 Lattice[@la_privsource_klas]。同月发布的 Menace-T 是两箱式 C4 套件，单名操作员几分钟即可架设，基于 Voyager 硬件，运行 Lattice Mesh，可承载第三方边缘 AI 软件栈，已用于地面车辆和舰船；Menace-X 是面向远征和动中通的版本[@la_tc_menace,la_everythingrf_menace]。

Menace 同时是 Palantir 边缘软件的首选硬件，与 Lattice Mesh 组网配套[@la_dc_menace]。2024 年 12 月两家宣布合作时，设想由 Lattice 和 Menace 采集战场边缘数据，再送入 Palantir AIP 准备 AI 训练数据，覆盖至 SCI/SAP 密级[@la_bw_palantir,la_bnn_palantir]。我部研判，Menace 是目前唯一一类同时承载两家软件的实物节点，两家的分工在这一层已固化为硬件配套关系。一份二手材料称 Menace 通过包括 Link 16 在内的多条通信路径运行 Lattice，属弱源[@la_phil_blog]。

### NGC2 套件：车载计算节点、炮兵工具与士兵终端

陆军下一代指挥控制（NGC2）原型被描述为“在共同数据层上的一体化软硬件指挥控制套件”，计算节点装在多型机械化车辆上[@la_ss_ngc2_award]。2025 年 9 月“常春藤之刺 1”实弹演习中，Lattice Mesh 运行在 Voyager 坚固边缘计算套件上，第 4 步兵师的师级目标处理流程从师部到炮位完全运行在 Lattice Mesh 和 Palantir Target Workbench 上；一款运行在 Lattice Mesh 上的测试版炮兵数据工具 AXS 被用于 M777 榴弹炮射击，据报道使用 AXS 的炮组 30 秒内完成数字化准备[@la_bd_ivysting1,la_ss_ivysting1]。

节点规模此后快速扩大。按 Anduril 说法，“常春藤之刺 5”把数据网格扩大到原来的 3 倍，连接 65 个以上战术边缘节点，每辆车、每个指挥所和每名士兵都是网格节点[@la_anduril_scaling,co_anduril_scaling]；2026 年 5 月“常春藤集结”中整个第 4 步兵师上线，接入 2,500 多台士兵终端[@la_milleak_ivymass]。这些数字均为公司口径。2026 年 10 月，陆军以 5 年、上限 18 亿美元的合同把 NGC2 推向第 1 军，Anduril 把 Lattice 描述为连接应用、数据、AI 模型、传感器和载具的“分布式数据层”[@la_ds_icorps,la_anduril_ngc2_scale]。

NGC2 节点的安全问题有官方记录。陆军首席技术官 2025 年 9 月的备忘录称原型应被视为“极高风险”，一个应用有 25 个高危漏洞，另有三个应用各有 200 多个缺陷待审；陆军随后称关键缺陷已缓解[@la_reuters_memo,la_bd_memo]。节点数量从几十个增至数千台终端，攻击面随之线性放大。

### Lattice 界面：操作员看到的指挥节点

据 MIT Technology Review 2024 年 12 月观摩演示的报道，Lattice 用户界面以地图为底，叠加航迹实体、己方资产和告警[@gp_mittr_demo]。美空军 2020 年 9 月“先进作战管理系统”（ABMS）第二次“上匝道”演示期间，空军人员在安德鲁斯联合基地监控运行 Lattice 的计算机，这是 Lattice 界面较早出现在美军官方图片中的一例；同年 10 月的演示中，操作员确认 Lattice 跟踪的是巡航导弹替代目标后，向效应器下达交战指令[@la_dn_cruise]。

!photo lattice_abms_onramp2_crop|ABMS 第二次“上匝道”演示中运行 Lattice 的计算机屏幕（2020 年 9 月 2 日，安德鲁斯联合基地，裁切）。界面以地图为底，叠加航迹与资产图标|U.S. Air Force photo by Senior Airman Daniel Hernandez，美国政府作品

界面背后是 SDK 定义的三类接入角色：传感器厂商做“生产者”，应用开发者做“消费者”，无人平台和武器厂商做“代理”[@la_sdk_ref]。2024 年 12 月 SDK 公开发布时首批合作伙伴包括 Apex、Forterra、Impulse Space、Numerica、Oracle、Saronic、Scale AI、Spire Global、Striveworks、Textron Systems 和 Valinor，覆盖地面、水面、太空和数据服务[@la_dd_sdk,la_ocbj_partners]。另有聚合站称 Hermeus 为 Quarterhorse Mk 2 高速试验机选用 Lattice，属弱源[@la_andurilnews_lattice]。

### 单兵头显：SBMC 与 EagleEye

单兵是 Lattice 节点谱系的最末端。2025 年 2 月或 4 月，陆军把 IVAS 头显生产合同从微软转由 Anduril 管理[@co_bd_eagleeye]。2025 年 9 月，陆军“单兵携行任务指挥”（SBMC，原 IVAS Next）第一阶段原型硬件授予 Anduril 1.59 亿美元（与 Meta 合作的 EagleEye），Rivet 另获 1.95 亿美元；SBMC-A 的数据与 AI 架构建立在 Lattice 指挥控制之上，规模化交付预计 2027 年[@la_uploadvr,la_bd_eagleeye]。头显一旦列装，每名士兵既是 Lattice 网格的消费者，也是位置与图像的生产者。

## （八）Maven 的数据源与平台侧“节点”

MSS 没有自有硬件，它的节点由三部分构成：上游的传感器与情报数据源，中游的模型流水线，下游接受目标数据的打击与火控平台。三部分都不属于 Palantir，MSS 通过数据集成和本体把它们串起来[@mv_csis,mv_palantir_ontology]。

### ScanEagle：Maven 的第一个接入对象

Project Maven 的第一个任务是战术和中空无人机全动态视频的处理、利用和分发[@mv_work_memo,mv_globalsec]。2017 年 12 月，首个达到任务就绪状态的算法部署到中东，用于识别 ScanEagle 小型无人机视频中的物体，使用者为 SOCOM 情报分析员，从立项到上线约 8 个月[@mv_trajectory,mv_nextgov_2017]。非洲司令部自同月起也在使用[@mv_bd_2018_africa]。ScanEagle 本身没有为 Maven 做任何改装，Maven 处理的是它回传的视频流。这一“只接数据、不碰平台”的方式决定了此后 MSS 的扩展路径。

### 卫星、信号情报与无人机视频

据 CSIS 报道，中央司令部 2024 年的 MSS 部署接入了 179 个数据源，包括国家侦察卫星、ICEYE 和 Capella Space 等商业合成孔径雷达卫星，以及截获通信、电子辐射等信号情报[@mv_csis]。另有二手描述称，无人机执行任务时的位置和实时视频会回传到 Maven[@mv_spatial]。全动态视频和友军跟踪的接入方式没有权威公开说明[@mv_csis]。

第三方识别模型是另一类“软节点”。Palantir 在北约工业日的示例中，把外部 AI 系统 Safran.AI 生成的 12,000 个检测对象导入 MSS，用户可在共用作战图中调查，也可用自然语言让 AIP 代理检索[@mv_palantir_blog_nato]。GEOINT 模型的上游是 NGA Maven 流水线：Scale AI 2024 年 7 月获约 2,400 万美元数据标注过渡合同，Enabled Intelligence 2025 年 11 月赢得上限 7.08 亿美元的 SEQUOIA 标注合同，ECS 自 2017 年起担任 AI 互操作集成商，模型认证由 NGA 的 AGAIM 试点承担[@mv_nga_contracts,mv_bd_sequoia,mv_execbiz_ecs,mv_fnn_agaim]。

数据源层也是 MSS 最大的风险来源。2026 年 2 月 28 日伊朗 Minab 学校遇袭事件中，据彭博社引述五角大楼内部调查，该地点在旧数据库中仍标为伊斯兰革命卫队设施，输入 Maven 后被列为“第一天推荐目标”[@mv_bloomberg_minab,mv_gizmodo_minab]。Palantir 称自己“不对底层数据负责”[@mv_gizmodo_minab]。

### 打击平台：B-1B 与海上打击力量

MSS 的下游是存量打击平台，它们与 MSS 之间隔着目标审批和火力分配环节。2024 年 2 月 2 日，中央司令部对伊拉克、叙利亚境内目标实施报复性打击，据美国空军发布的图片说明，B-1B 轰炸机由戴斯空军基地出击；中央司令部首席技术官舒伊勒·摩尔对彭博社表示，机器学习目标识别帮助“缩小目标范围”，Maven 参与了 85 次以上打击，涉及 7 处设施，每一步以人工验证结束[@mv_register_2024,mv_bnn_2024]。2024 年 Maven 还被用于定位也门境内的火箭发射器和红海上的水面船只[@mv_bloomberg_2024]。2026 年“史诗怒火”行动中，美国官员称五角大楼依靠 Maven 识别最高优先级目标并帮助选择武器，CDAO 称 38 天内打击约 13,000 个目标，这一数字统计的是被打击目标，不是 Maven 识别量[@mv_aca_iran,mv_ds_mazol]。公开资料没有把任何具体打击架次与 Maven 的某一输出直接对应。

### 火力交接：AFATDS、M777 与两系统的交汇点

MSS 不直接控制武器。有二手分析称，Target Workbench 排序后的目标交给先进野战炮兵战术数据系统（AFATDS）等火力支援系统，射击诸元由 AFATDS 和弹道计算完成[@mv_battlepolicy,mv_vanroo]。陆战队 2025 年的 MARADMIN 电报把 MSS 定为跨作战司令部的标准“火力与效果集成平台”，并通过企业许可在 SIPRNet 影响等级 6 云上向舰队陆战队开放[@mv_ds_maradmin,mv_usmc_release]。

“常春藤之刺 1”提供了两系统在实物层面交汇的唯一公开实例：M777 榴弹炮的射击数据由运行在 Lattice Mesh 上的 AXS 工具传递，师级目标处理在 Palantir Target Workbench 上完成[@la_bd_ivysting1,mv_bd_ivysting]。该演习使用的是 Target Workbench，公开资料没有说明是否就是 MSS 本身。

### TITAN 地面站：两家共同承制的情报节点

陆军“战术情报目标接入节点”（TITAN）是下一代情报、监视与侦察地面站，目标是缩短传感器到射手的时间。2024 年 3 月 6 日，陆军授予 Palantir 1.784 亿美元原型 OTA，建造 10 套原型（5 套高级型、5 套基本型），合作方包括诺斯罗普·格鲁曼、L3Harris 和 Anduril[@mv_ds_titan,mv_army_titan,co_army_titan_2403]。2026 年 9 月，陆军授出合计 1.92 亿美元的 TITAN 生产合同，其中 Palantir 1.27 亿美元、Anduril 6,500 万美元[@co_bd_2609_titan]。TITAN 是唯一一型由两家共同承制、专门服务“情报到目标”链路的硬件节点，Anduril 在其中承担的具体分系统没有公开。

## （九）装备—角色—体系位置—合同总表

{tab:t_gp_gear}汇总本章涉及的主要装备与节点。“Lattice 关系”一栏中，“确认”指合同或官方材料明确写到 Lattice，“推定”指架构上基于 Lattice 但所引来源未点名，“未确认”指未见集成说明。

!table t_gp_gear|接入或依托两系统的装备与节点总表|本报告依据第一、二、四、五章与研究笔记整理；金额为上限、授予额或批准估值，口径不同不可相加|26,18,32,26,58
装备/节点|角色|体系位置|Lattice 关系|部署与合同（摘要）
Sentry 塔（固定/机动/增程）|传感|Lattice 第①层末端节点|确认|CBP 正式采购项目，第 300 座（2024-09）；XRST 3.63 亿美元，200 余座（2026-06）[@la_asdnews_300,la_execbiz_xrst]
Wisp|传感|反无人机套件补充传感器|确认|“猎鹰峰 25.2”；华盛顿州国民警卫队列装[@la_ius_falconpeak,gp_dvids_wang]
Spyglass/Spark 雷达|传感|收购补齐的雷达节点|未确认|2025-01 宣布收购 Numerica 雷达与 C2 业务[@la_builtin_what]
SSN 地面传感网|传感、通信|太空域网格|确认|约 9,970 万美元，2026 年底部署[@la_ds_ssn]
Anvil|效应|可受领任务的拦截代理|确认|SOCOM、I-CsUAS（上限 6.42 亿美元）、科威特方案；人工下令才拦截[@la_marines_gbad,la_ds_icsuas]
Roadrunner-M|效应|可回收拦截弹|未确认|500 发加 Pulsar，249,978,466 美元（2024-10）[@la_dn_roadrunner]
Pulsar/Pulsar-L|传感、效应（电子战）|电磁域节点|确认|SOCOM、I-CsUAS、Roadrunner 合同配套[@la_wt_socom,gp_anduril_pulsarl]
MADIS 交战系统|效应、火控|陆战队车载防空|推定|约 2 亿美元（2024-11）[@la_ius_madis]
IBCS-M 反无人机火控|火控、计算|陆军防空体系中的 Lattice 火控层|确认|尤马实弹 4 中 4，金额未披露[@la_ds_ibcsm]
JIATF-401 通用 C2|指挥控制|多厂商反无人机总线|确认|首单约 8,700 万美元（企业合同下）[@la_bd_jiatf]
Ghost/Ghost-X|传感、可受领任务资产|小型无人机节点|确认（公司口径）|连级无人机首批 1,441.7 万美元；“复制者 1.2”[@co_ius_ghostx,la_cyberwarzone]
ALTIUS-600/600M/700M|传感、效应|管射无人机与巡飞弹|确认（EDGE23）|台湾 291 套（估值 3 亿美元）及 2026 年新订单；乌克兰停用[@la_dsca_taiwan,la_tdp_taiwan_2026]
Bolt-M|效应|单兵巡飞弹|未确认|未检索到正式合同[@gp_twz_boltm]
YFQ-44A Fury|效应、LMA 载体|CCA 平台与 Lattice 应用层|确认（LMA 飞行）|2026-06 转入生产，金额未披露[@la_ds_cca_prod,la_die_cca]
YFQ-42A|效应|CCA 对照机型|无公开记录|2026-06 转入生产[@la_ds_cca_prod]
Dive-LD|传感、平台|水下节点|确认|海军/DIU 原型，2025-04 首台交付[@la_globalsec_diveld,co_gs_divel]
Ghost Shark|传感、效应平台|超大型无人潜航器|未确认（弱源）|17 亿澳元生产合同（2025-09）[@la_minister_ghostshark]
Barracuda-500M|效应|远程打击|未确认|据报陆军 3,000 枚，金额未披露[@co_sandboxx_barracuda]
天基拦截器|效应|金穹拦截层|未确认|12 家合计上限 32 亿美元[@la_bloomberg_sbi]
Menace-T/X（Voyager）|计算、通信|Lattice 第②层；Palantir 边缘软件首选硬件|确认|2025-05 发布；Klas 收购[@la_tc_menace,la_dc_menace]
NGC2 车载节点与终端|计算、通信|师级数据网格|推定|原型 9,960 万美元；I 军推广上限 18 亿美元[@la_army_ngc2_award,la_ds_icorps]
SBMC/EagleEye 头显|传感、显示|单兵节点|确认（SBMC-A）|1.59 亿美元原型（2025-09）[@la_uploadvr]
ScanEagle FMV|数据源|Maven 首个处理对象|—|2017-12 首个算法部署中东[@mv_nextgov_2017]
国家与商业卫星、SIGINT|数据源|MSS 数据源层|—|CENTCOM 2024 年接入 179 个数据源[@mv_csis]
NGA Maven 模型流水线|计算（模型）|MSS 上游|—|SEQUOIA 上限 7.08 亿美元[@mv_bd_sequoia]
B-1B 等打击平台|效应|MSS 下游|—|2024-02 85 次以上打击使用 Maven 缩小目标范围[@mv_register_2024]
AFATDS/M777|火控、效应|两系统火力交接点|AXS 运行于 Lattice Mesh|“常春藤之刺 1”实弹[@la_bd_ivysting1]
TITAN 地面站|计算、数据源|情报到目标节点|—|生产 1.92 亿美元（Palantir 1.27 亿、Anduril 6,500 万）[@co_bd_2609_titan]
!end

把总表按角色归并，可以读出两条结论。Lattice 一侧，确认接入的节点集中在传感器、近程拦截器和指挥计算设备，远程打击、水下和大型空中平台的接入多为未确认或仅有演示；Anduril 硬件谱系的扩张速度明显快于 Lattice 公开接入证据的积累速度。MSS 一侧，节点全部是政府既有资产或第三方模型，Palantir 控制的是把这些节点组织成目标流程的数据与工作流层。两系统在实物层面只有三个公开交汇点：Menace 边缘硬件、NGC2 中的 AXS 与 Target Workbench，以及 TITAN 地面站。

:::judge 研判要点
- Lattice 的装备谱系以 Sentry、Anvil、Pulsar、ALTIUS 和 Menace 为骨干，确认接入的节点集中在反无人机和基地防护；Roadrunner、Barracuda、Ghost Shark 等新平台与 Lattice 的集成尚无公开证据，Anduril 硬件扩张快于其软件接入的公开证明。
- 反无人机领域，Lattice 的角色正从“自家硬件的操作系统”转为多厂商火控总线：IBCS-M 数小时接入第三方传感器与效应器、JIATF-401 连接 Fortem、Perennial 等非 Anduril 设备、ORIGIN BLAZE 完成集成，决定其地位的是接入能力而非单一拦截器性能。
- 负面记录高度集中在飞行与水面平台：ALTIUS 在乌克兰停用并在埃格林、空军测试中坠毁，Ghost 受俄方干扰，十余艘 Lattice 控制的无人艇演习失灵，Anvil 测试引发野火。这些问题出在平台和数据链，恰处于 Lattice 宣传的“边缘自主、抗干扰”环节。
- YFQ-44A 是 Anduril 最重要的空中平台，但空军以 A-GRA 保持自主软件可替换，LMA 需与 Hivemind 等长期竞争，Anduril 拥有机体并不保证其软件独占。
- MSS 没有自有硬件，节点全部是卫星、无人机视频、信号情报、第三方模型和存量打击平台；其风险集中在数据源时效，Minab 事件即源于数据库过期记录。两系统在实物层面的交汇点只有 Menace、NGC2 中的 AXS 与 Target Workbench，以及两家共同承制的 TITAN 地面站，应作为后续跟踪的重点。
:::
