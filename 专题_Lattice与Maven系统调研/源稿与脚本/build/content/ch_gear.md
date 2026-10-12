# 三、装备与节点图谱：接入两系统的“传感器—射手”家族

:::lead
Lattice 一侧几乎全为 Anduril 自研或收购的硬件，软硬同源；MSS 没有自有硬件，节点是卫星、无人机视频、信号情报与存量打击平台。截至 2026 年 10 月。
:::

本章把“接入 Lattice”分为三级：合同或官方材料明确写到的记为确认，架构上基于 Lattice 但来源未点名的记为推定，只见于套件清单的记为未确认。公开确认的有 Sentry 塔、Wisp、Pulsar、Anvil、ALTIUS-600/600M、Ghost-X、YFQ-44A 及 IBCS-M 下的第三方雷达和效应器；Ghost Shark、Barracuda 和 Roadrunner 的集成方式没有公开来源[@la_andurilnews_lattice,la_ds_ibcsm]。合同金额区分上限、已拨付和军售批准估值，不能相加。

## （一）边境与基地防护传感节点

Sentry 自主监视塔是 Anduril 的起家产品，也是 Lattice 部署最久、数量最多的节点。塔体集成雷达、光电/红外和射频传感器，太阳能供电，塔端 AI 完成检测分类后把航迹传给指挥控制节点；CBP 官员称其跟踪“物体和活动”，不做人脸识别[@la_fedscoop_towers]。型号分固定型、2022 年 10 月推出的机动型和 2024 年 5 月推出的增程型，增程型塔高 80 英尺，自主探测距离超过 5 英里[@la_execbiz_xrst]。

!photo sentry_luna_nm_1|新墨西哥州卢纳县 9 号州道旁的 Sentry 塔及底座（2022 年）|Electronic Frontier Foundation（EFF），CC BY 4.0
!photo sentry_tecate|加州特卡特山脊上的 Sentry 塔远景（2022 年）|Electronic Frontier Foundation（EFF），CC BY 4.0

CBP 于 2020 年把自主监视塔（AST）列为正式采购项目，计划总数 200 座；Anduril 2024 年 9 月宣布部署第 300 座，称覆盖南部陆地边境约 30%，系地理覆盖口径，与拦截效果无关[@la_asdnews_300]。2026 年 6 月，CBP 以 362,974,500 美元采购 200 余座增程型塔，要求与已有 350 余座标准塔和 Lattice 集成[@la_execbiz_xrst]。检测概率、虚警率从未公开；MIT Technology Review 估算 2021 年以来有 110 多人死在塔的覆盖范围内，系该刊自行估算。

Sentry 与 Lattice 进入美军演训的时间早于反无人机大合同。2020 年 1 月，Anduril 人员在加州二十九棕榈镇演习中协助部队组装 Sentry 哨塔；同年 9 月空军“先进作战管理系统”（ABMS）第二次“上匝道”演示中，人员在安德鲁斯联合基地监控运行 Lattice 的计算机，10 月演示中操作员确认巡航导弹替代目标后向效应器下达交战指令[@la_dn_cruise]。

!photo cuas_fire_control_dvids|Anduril 人员在二十九棕榈镇协助组装 Sentry（2020 年 1 月）|U.S. Army（DVIDS），美国政府作品
!photo lattice_abms_onramp2_crop|ABMS“上匝道”演示中运行 Lattice 的屏幕（2020 年 9 月）|U.S. Air Force photo by Senior Airman Daniel Hernandez，美国政府作品

此后 Sentry 转向基地防护。英国 TALOS 基地防御试验 2021 年以 380 万英镑起步，2023 年 11 月第三阶段 1,700 万英镑；2025 年 10 月北方司令部“猎鹰峰 25.2”演示中，机动型 Sentry 与 Wisp、Pulsar 协同探测，交 Anvil 拦截，整套设备随后交付北方司令部[@la_ius_falconpeak]。华盛顿州国民警卫队第 10 民事支援队 2026 年列装的 Anduril 反无人机系统同样包括摄像塔、Wisp、Pulsar 与 Lattice，Wisp 已进入国民警卫队一级的本土防护部队[@gp_dvids_wang]。

雷达主要靠收购补齐，2025 年 1 月 Anduril 宣布收购 Numerica 雷达与指挥控制业务。太空域，2024 年 11 月太空系统司令部授予约 9,970 万美元太空监视网（SSN）现代化合同，以 Lattice 连接地面监视传感器，要求 2026 年底部署[@la_ds_ssn]。

## （二）反无人机效应器与火控

反无人机是 Lattice 合同规模最大的领域。SOCOM 2022 年系统集成伙伴合同上限 967,599,957 美元，配套 Sentry、Anvil、Pulsar 和 FoxHound[@la_wt_socom]。Anvil 是动能拦截无人机，陆战队地基防空项目办公室记录其可自主跟踪目标，但只在人工下令后拦截，这是目前对其交战规则最权威的记录[@la_marines_gbad]。在 Lattice 中，Anvil 属“可受领任务的代理”，通过 task_catalog 声明拦截能力，受领任务后依次回报确认、执行和结果状态。

陆战队设施反小型无人机（I-CsUAS）项目为 10 年期 IDIQ，上限 6.42 亿美元，内容为 Lattice 加 Anvil 和 Pulsar[@la_ds_icsuas]。Pulsar 是电磁战系统，2025 年 4 月推出轻量化 Pulsar-L。陆战队 MADIS 车载防空系统以 JLTV 为底盘，2024 年 11 月 Anduril 获约 2 亿美元合同承包其反无人机交战系统，来源未点名 Lattice，按推定处理[@la_ius_madis]。

!photo pulsar_press|Anduril Pulsar 电磁战系统（公司图，2024 年 5 月）|Anduril Industries，公司图片，仅作评论引用
!photo madis_mk1|陆战队 MADIS Mk1（JLTV 底盘）在测试中（2023 年 9 月）|PEO Land Systems（经 DVIDS），Public Domain Mark 1.0

Roadrunner 是可回收双涡喷拦截器。2024 年 10 月一份 249,978,466 美元的合同采购 500 发 Roadrunner-M 及 Pulsar；2026 年 6 月获批的科威特军售方案估值 19.8 亿美元，含 Roadrunner-M、Anvil 和多型 Sentry[@la_dn_roadrunner,la_bd_kuwait]。Roadrunner 的实战拦截记录未见公开。据《华尔街日报》报道，一次 Anvil 测试在俄勒冈引发 22 英亩野火。

2025 年 11 月 10 日，陆军选定 Lattice 作为机动型一体化作战指挥系统（IBCS-M）的反无人机火控平台；尤马 7 天试验中，Lattice 数小时内接入一型未公开的传感器和效应器，实弹拦截 4 中 4，金额未披露[@la_ds_ibcsm]。2026 年 3 月，陆军企业合同下首个任务单（约 8,700 万美元）交给 JIATF-401，以 Lattice 作通用反无人机指挥控制[@la_bd_jiatf]；该部队同期采购的 Fortem、Perennial 等效应器多非 Anduril 产品，10 月 ORIGIN BLAZE 拦截器完成集成。**我部研判，Lattice 在反无人机领域正从自家硬件的操作系统转为多厂商设备的火控总线。**

## （三）小型无人机与巡飞弹

Ghost 是早期直升机式侦察无人机，2022 年约 40 架援乌，据《华尔街日报》报道受俄方干扰严重[@la_tc_wsj]。后继型 Ghost-X 2024 年秋入选陆军连级小型无人机首批（1,441.7 万美元）和“复制者 1.2”，公司称其指挥控制运行在 Lattice 上[@co_ius_ghostx]。ALTIUS 系列来自收购的 Area-I，ALTIUS-600 为管射无人机，谱系含侦察型 600ISR、打击型 600M 和更大的 700M。

!photo ghostx_romania_prep|美陆军士兵在罗马尼亚为 Ghost-X 做起飞前准备（2024 年 11 月）|U.S. Army（DVIDS），美国政府作品
!photo altius600_area_i|ALTIUS-600 管射无人机在尤马试验场飞行（2020 年 3 月）|U.S. Army photo by Jose Mejia-Betancourth（CCDC AvMC），美国政府作品

2023 年 EDGE23 演习中，士兵用 Lattice for Mission Autonomy 把地空导弹阵地定为敌对并授权 ALTIUS-600M 打击，系统随即自动改派侦察型做毁伤评估，这是“人做决策、机器做调度”最完整的公开记录[@la_blog_edge23]。合同主要在美国以外：2024 年 6 月美方批准对台出售最多 291 套 ALTIUS 600M-V，估值 3 亿美元；2026 年 8 月据报台湾再采购 1,554 套 700M 和 478 套 600ISR[@la_dsca_taiwan]。

ALTIUS 是负面记录最多的一型：乌克兰安全局 2024 年停用，埃格林一架投放后坠地，2025 年 11 月空军测试又坠毁两架[@co_bnn_crashes]。问题出在平台、导航和数据链，恰处于 Lattice 宣传的“边缘自主、抗干扰”环节。Bolt-M 是单兵便携巡飞弹，2024 年 10 月前后公开，参数、正式合同及与 Lattice 的关系均未检索到[@gp_twz_boltm]。陆军“无人机主导权”计划拟两年内采购约 34 万架小型攻击无人机，单价降至约 2,300 美元，对其成本结构构成压力。

!photo bolt_m_press|Anduril Bolt-M 单兵巡飞弹（公司图，2024 年 10 月前后）|Anduril Industries，公司图片，仅作评论引用

## （四）协同作战飞机：YFQ-44A“狂怒”与 YFQ-42A

YFQ-44A 源自 Anduril 2023 年 9 月收购的 Blue Force Technologies Fury。2024 年 4 月，Anduril 与通用原子在空军 CCA 第一增量中胜出；2025 年 10 月 31 日首飞，2026 年 2 月 24 日 Lattice for Mission Autonomy（LMA）首次随机飞行[@la_die_cca]，6 月 17 日与通用原子 FQ-42A 同时转入生产，比原计划提前约 4 个月[@la_ds_cca_prod]。

!photo yfq44_ground_test|YFQ-44A 生产代表型在科斯塔梅萨测试舱内地面试验（2025 年 5 月）|U.S. Air Force（DVIDS），美国政府作品
!photo yfq44_paris2025|2025 年 6 月巴黎航展上展出的 YFQ-44“狂怒”|Artvill（Wikimedia Commons），CC BY 4.0

YFQ-44A 的机体与武器属效应器，机载 LMA 属 Lattice 应用层。同一次飞行中，Fury 先后运行 Shield AI 的 Hivemind 和 LMA，经“政府参考自主架构”（A-GRA）切换[@la_aviationist_hivemind]；该机已完成以惰性 AIM-120 对模拟目标的端到端超视距打击。LMA 地位存在口径冲突：一说空军 2026 年 6 月为下一阶段选定 LMA；一说 Lattice 与多家同在自主软件池竞争至 2027 年[@la_simpleflying]。空军以 A-GRA 保持软件可替换，Anduril 拥有机体不等于软件独占。

通用原子 YFQ-42A 于 2025 年 8 月 27 日试飞，Lattice 在该机上没有公开角色[@gp_dvids_yfq42]；空军部长米因克 2026 年 9 月把目标提高到 2032 年前至少 500 架 CCA（二手来源）。CCA 合同金额、产量和单价均未披露；据《华尔街日报》报道，一台 Fury 发动机在地面测试中受损[@la_sherwood_wsj]。

!photo yfq42_cca_dvids|通用原子 YFQ-42A 试飞（2025 年 8 月 27 日），作对比参照|U.S. Air Force（DVIDS），美国政府作品

## （五）水下与水面节点

Dive-LD 大型无人潜航器源自收购的 Dive Technologies。2024 年 2 月，海军与 DIU 选定 Anduril 等三家研制原型；竞速测试中 Lattice 实时跟踪并共享其位置，是 Lattice 接入水下平台唯一有明确记载的案例，2025 年 4 月首台交付[@la_globalsec_diveld]。澳大利亚 Ghost Shark 超大型潜航器 2025 年 9 月签订 5 年 17 亿澳元生产合同，2026 年 4 月首批生产艇交付新成立的海上自主系统部队，较原定的 1 月推迟；由 Lattice 管理其自主功能的说法只见弱源[@la_minister_ghostshark]。

水面方向，据《华尔街日报》报道，海军加州近海演习中十余艘由 Lattice 指挥控制的无人艇失灵或停机，水兵警告存在潜在人员伤亡，演习时间说法不一，Anduril 称属迭代开发[@la_sherwood_wsj]。2026 年 10 月 6 日，海军授予 Anduril 上限 29 亿美元的弗吉尼亚级潜艇部件合同，由“武库-2”船厂生产，属工业供给，与 Lattice 无关[@la_cnbc_sub]。

## （六）远程打击与工业基础

Barracuda 是低成本巡航导弹系列，地面发射型 Barracuda-500M 采用集装箱式发射。据 Sandboxx 报道，陆军将采购 3,000 枚，2027 年起每年 1,000 枚，金额未披露[@co_sandboxx_barracuda]。“金穹”方面，2026 年 4 月 24 日太空系统司令部向 12 家公司授出 20 份天基拦截器原型 OTA，合计上限 32 亿美元，Anduril 牵头其中一个团队；路透社称 Anduril 与 Palantir 同属开发金穹指挥控制平台的产业联合体，金穹负责人盖特莱因称之为“胶水层”[@la_usnews_goldendome]。两者与 Lattice 的集成方式、金额和测试结果均无一手来源。

!photo barracuda_500m_press|Anduril Barracuda-500 地面发射构型试射（公司图）|Anduril Industries，公司图片，仅作评论引用
!photo golden_dome_map|“美国金穹”示意图板（2025 年 5 月 20 日，白宫椭圆形办公室，裁切）|The White House，美国政府作品

产能方面，俄亥俄“武库-1”工厂 2025 年 1 月宣布建设，建筑面积 500 万平方英尺，2026 年 3 月开始生产 Fury，计划年底前加产 Roadrunner 和 Barracuda[@la_bd_arsenal1]；2023 年收购的 Adranos 承担固体火箭发动机。我部研判，陆军 3,000 枚 Barracuda 的采购若属实，Lattice 任务链将首次延伸到数百公里级火力，而这一延伸目前没有公开的接口与交战规则说明。

## （七）边缘计算与指挥节点

Lattice Mesh 运行在 Menace 系列硬件上。2025 年 5 月 Anduril 签约收购 Klas，同月发布基于其 Voyager 坚固边缘计算硬件的两箱式 C4 套件 Menace-T，单人几分钟可架设，可承载第三方边缘 AI 软件[@la_tc_menace]。Menace 同时是 Palantir 边缘软件的首选硬件：2024 年 12 月两家宣布合作时，设想由 Lattice 和 Menace 采集战场边缘数据，再送入 Palantir AIP 准备训练数据，覆盖至 SCI/SAP 密级[@la_bw_palantir]。**我部研判，Menace 是目前唯一同时承载两家软件的实物节点，两家分工在这一层已固化为硬件配套关系。**

接入规则由 SDK 定义：传感器厂商做“生产者”，应用开发者做“消费者”，无人平台和武器厂商做“代理”[@la_sdk_ref]。2024 年 12 月 SDK 公开发布时，首批合作伙伴包括 Numerica、Oracle、Saronic、Scale AI、Textron Systems 等十余家，覆盖地面、水面、太空和数据服务[@la_dd_sdk]。

陆军下一代指挥控制（NGC2）把计算节点装上多型机械化车辆。2025 年 9 月“常春藤之刺 1”实弹演习中，第 4 步兵师的目标处理流程从师部到炮位运行在 Lattice Mesh 和 Palantir Target Workbench 上，运行于 Lattice Mesh 的 AXS 炮兵数据工具用于 M777 射击[@la_bd_ivysting1]。按公司口径，2026 年 5 月全师上线，接入 2,500 多台士兵终端；10 月陆军以上限 18 亿美元合同把 NGC2 推向第 1 军[@la_ds_icorps]。

NGC2 节点的安全问题有官方记录：陆军首席技术官 2025 年 9 月备忘录称原型属“极高风险”，一个应用有 25 个高危漏洞，陆军随后称关键缺陷已缓解[@la_reuters_memo]。单兵一端，2025 年 9 月 Anduril 与 Meta 合作的 EagleEye 头显获 1.59 亿美元 SBMC 原型合同，其数据架构建立在 Lattice 之上[@la_uploadvr]。头显列装后，每名士兵既是网格的消费者，也是位置与图像的生产者。

## （八）Maven 的数据源与平台侧“节点”

MSS 的节点分三部分：上游的传感器与情报数据源，中游的模型流水线，下游的打击与火控平台，均不属于 Palantir。2017 年 12 月，首个算法部署中东，识别 ScanEagle 无人机视频中的物体，从立项到上线约 8 个月，ScanEagle 本身未做改装[@mv_nextgov_2017]。中央司令部 2024 年的 MSS 部署接入 179 个数据源，包括国家侦察卫星、商业雷达卫星和信号情报；GEOINT 模型上游是 NGA Maven 流水线，SEQUOIA 标注合同上限 7.08 亿美元[@mv_csis]。

数据源也是 MSS 最大的风险来源。2026 年 2 月 28 日伊朗 Minab 学校遇袭，据彭博社引述五角大楼内部调查，该地点在旧数据库中仍标为革命卫队设施，被 Maven 列为“第一天推荐目标”；Palantir 称“不对底层数据负责”[@mv_bloomberg_minab,mv_gizmodo_minab]。

下游方面，2024 年 2 月对伊拉克、叙利亚的报复性打击中，B-1B 由戴斯空军基地出击，中央司令部称 Maven 参与 85 次以上打击，每一步以人工验证结束[@mv_register_2024]。2026 年“史诗怒火”行动中，CDAO 称 38 天内打击约 13,000 个目标，该数字统计的是被打击目标而非 Maven 识别量，公开资料也没有把任何具体架次与 Maven 的某一输出对应[@mv_ds_mazol]。

MSS 不直接控制武器，排序后的目标交由 AFATDS 等火力支援系统解算；陆战队 2025 年把 MSS 定为跨作战司令部的标准火力与效果集成平台[@mv_ds_maradmin]。两系统在实物层面的交汇有三处：Menace 边缘硬件；“常春藤之刺 1”中 AXS 与 Target Workbench；陆军 TITAN 地面站，2026 年 9 月生产合同合计 1.92 亿美元，其中 Palantir 1.27 亿美元、Anduril 6,500 万美元[@co_bd_2609_titan]。

## （九）装备—角色—合同总表

{tab:t_gp_gear}汇总本章主要装备与节点，“Lattice 关系”按本章开头的三级口径标注。

!table t_gp_gear|接入或依托两系统的装备与节点总表|本报告整理；金额为上限、授予额或批准估值，不可相加|34,26,30,70
装备/节点|角色|Lattice 关系|部署与合同（摘要）
Sentry 塔|传感|确认|CBP 正式项目；增程型 3.63 亿美元（2026-06）[@la_execbiz_xrst]
Anvil、Pulsar|拦截、电子战|确认|SOCOM、I-CsUAS（上限 6.42 亿美元）[@la_ds_icsuas]
IBCS-M、JIATF-401|火控、指挥控制|确认|尤马 4 中 4；首单约 8,700 万美元[@la_bd_jiatf]
Ghost-X|传感、任务资产|确认（公司口径）|连级首批 1,441.7 万美元[@co_ius_ghostx]
ALTIUS 系列|传感、打击|确认（EDGE23）|对台 291 套，估值 3 亿美元[@la_dsca_taiwan]
YFQ-44A|打击、LMA 载体|确认（LMA 飞行）|2026-06 转入生产[@la_ds_cca_prod]
Dive-LD、Ghost Shark|水下平台|前者确认，后者弱源|Ghost Shark 17 亿澳元[@la_minister_ghostshark]
Roadrunner、Barracuda、天基拦截器|拦截、远程打击|未确认|500 发 2.5 亿美元；3,000 枚（据报）[@la_dn_roadrunner]
Menace、NGC2 节点|计算、通信|前者确认，后者推定|NGC2 推广上限 18 亿美元[@la_ds_icorps]
MSS 数据源与打击平台|数据源、效应|—|179 个数据源；85 次以上打击[@mv_csis]
TITAN 地面站|情报到目标节点|—|生产 1.92 亿美元[@co_bd_2609_titan]
!end

Lattice 一侧，确认接入的节点集中在传感器、近程拦截器和指挥计算设备，远程打击、水下和大型空中平台多为未确认或仅有演示，硬件扩张快于软件接入的公开证据。MSS 一侧，节点全是政府既有资产或第三方模型，Palantir 控制的是把它们组织成目标流程的数据与工作流层。

:::judge 研判要点
- 确认接入 Lattice 的节点集中在反无人机与基地防护，Roadrunner、Barracuda 等尚无集成证据。
- 反无人机领域，Lattice 正转为多厂商火控总线，决定其地位的是接入能力而非单一拦截器性能。
- 负面记录集中在飞行与水面平台：ALTIUS 坠毁停用、Ghost 受干扰、无人艇失灵，恰在“边缘自主”环节。
- 空军以 A-GRA 保持 CCA 软件可替换，Anduril 拥有 YFQ-44A 机体不保证 LMA 独占。
- MSS 风险集中在数据源时效；Menace、AXS 与 Target Workbench、TITAN 三个交汇点应重点跟踪。
:::
