# 二、Maven：从无人机视频识别到全军"目标工厂"与"万能应用"

:::lead
Maven 是一条持续九年、几经改组的政府项目线，并非单一软件产品。项目起步于 2017 年反 ISIS 作战中无人机视频判读人力不足的问题，先后经历谷歌退出风波、XVIII 空降军"猩红之龙"演习和 2022 年拆分改组，现已演变为以 Palantir 软件为主体、用户逾 10 万、覆盖全部作战司令部和北约盟军作战司令部的 AI 赋能指挥控制与目标定位平台，即 Maven 智能系统（MSS）。本章依次梳理其沿革、功能设计、架构设计、能力评估和实战案例，并对官方口径、媒体报道与弱源说法分别标注。
:::

【阅读提示】本章事实均取自公开报道、官方文件、智库报告与厂商资料的检索摘要。受调研条件限制，相当一部分原文未能逐页核读；数字口径存在冲突的，并列写明；仅见于聚合站、博客或倡导团体的说法，标注"（弱源，待核）"；我部的分析与推断，以"我部分析""我部研判"或"推断"标明。

## （一）前世今生：从算法战跨职能小组到全军正式项目

:::lead
Maven 九年历程可分四个阶段。2017—2018 年为探路阶段，一个小团队用数月时间把商业计算机视觉送上反 ISIS 战场。2019—2021 年为生态扩张阶段，谷歌退出后由 ECS、Clarifai、微软、AWS、Palantir 等公司填补，XVIII 空降军开始借演习把 Maven 改造为目标工作流平台。2022—2025 年为拆分与规模化阶段，GEOINT 模型流水线划归 NGA，作战平台 MSS 由 Palantir 主承包并迅速推向各作战司令部和北约。2026 年起进入制度化阶段，Feinberg 备忘录要求 MSS 转为全军正式项目，伊朗战事使其用户在一年内翻番。
:::

### 三个名字：Project Maven、NGA Maven 与 MSS

Maven 相关讨论中常混用三个名称，须先行区分。**Project Maven** 是 2017 年 4 月成立的算法战跨职能小组（AWCFT，Algorithmic Warfare Cross-Functional Team）的通称，属政府项目，最初隶属国防部负责情报的副部长办公室（OUSD(I)，后为 OUSD(I&S)）[@mv_work_memo,mv_wiki_maven]。**NGA Maven** 是 2022 年起由国家地理空间情报局（NGA）接管的地理空间情报（GEOINT）AI 服务与模型流水线，2023 年 11 月列为 NGA 正式采购项目（program of record）[@mv_bd_2022_nga,mv_dd_por]。**Maven 智能系统（Maven Smart System，MSS）**是以 Palantir 商业软件为主体、面向指挥控制与目标定位的作战平台，2024 年起由陆军代为签约并向各作战司令部扩展，2026 年起归首席数字与人工智能办公室（CDAO）新设的 MSS 项目办公室管理[@mv_ds_2024_05,mv_ds_feinberg2]。

三者同出一源、此后分流。Project Maven 是母体；NGA Maven 继承其计算机视觉模型、数据标注与模型评估流水线；MSS 继承其面向作战司令部的数据融合与目标工作流应用。北约 2025 年采购 MSS NATO 时专门说明，该系统"不应与 NGA Maven 作战人员支援系统（NGA Maven Warfighter Support System）相混淆"[@mv_shape_2025,mv_ds_nato]，可佐证两条线并行存在。本报告不加限定时所称 Maven 指整条项目线，涉及具体系统时分别写明 NGA Maven 或 MSS。

### 2017 年的问题：反 ISIS 作战与无人机视频积压

Project Maven 诞生于打击"伊斯兰国"（ISIS）作战的高峰期。当时美军在伊拉克、叙利亚等地大量使用战术级和中空无人机执行持续监视，产生海量全动态视频（FMV）。沃克备忘录交给 AWCFT 的第一项任务，即对战术和中空无人机 FMV 进行处理、利用和分发（PED）[@mv_globalsec]，目标是用深度学习从情报数据中提取洞见，支援击败 ISIS 的作战[@mv_trajectory]。

我部分析，FMV 的 PED 属于典型的人力瓶颈问题。传感器数量和飞行小时可随装备采购同步增加，能够逐帧判读、标注车辆与人员并撰写情报产品的分析员却增长有限。计算机视觉可以承担"有无目标、属何目标"这一步的大部分重复劳动，分析员只需处理机器提示的片段。Maven 以 FMV 为切入点，主要考虑其问题边界清楚、数据现成、效果直观，适合作为国防部引入商业 AI 的示范项目，并非因为 FMV 是最重要的情报来源。

### 立项：沃克备忘录与 AWCFT

2017 年 4 月 26 日，时任国防部常务副部长罗伯特·沃克（Robert O. Work）签署《成立算法战跨职能小组（Project Maven）》备忘录，宣布成立 AWCFT，以"加速国防部整合大数据和机器学习"[@mv_work_memo]。该备忘录扫描件后由美国国家安全档案馆（NSArchive）公开。经费方面，Maven 成立后约两个月内即从国会获得约 7,000 万美元[@mv_wiki_maven,mv_globalsec]。

!photo work_portrait|罗伯特·沃克（Robert O. Work）官方肖像。沃克时任国防部常务副部长，于 2017 年 4 月 26 日签署成立算法战跨职能小组（Project Maven）的备忘录|美国国防部，公有领域

AWCFT 的组织形式本身是一项制度创新。跨职能小组有别于传统项目办公室，不走需求论证、研制、试验、列装的长周期流程，由小团队直接对接作战用户、商业供应商和经费渠道，按"先上线、再迭代"的方式推进。我部分析，这一模式后被称为"探路者"（pathfinder）模式：Maven 的根本任务是证明国防部能在数月内把商业 AI 用于战场，FMV 识别只是验证手段，这也是其日后能够从视频识别扩展到数据融合和指挥控制的原因[@mv_wiki_maven,mv_trajectory]。

### 沙纳汉与库科：探路团队的做法

Maven 的两名关键人物是空军中将杰克·沙纳汉（Jack Shanahan）和海军陆战队上校德鲁·库科（Drew Cukor）。沙纳汉于 2017 年 4 月至 2018 年 12 月负责 Maven 总体指导，此后调任新成立的联合人工智能中心（JAIC）首任主任；库科任 AWCFT 负责人，承担大量日常领导工作[@mv_wiki_maven,mv_globalsec]。2017 年 7 月，项目方公开表示将于"年底前"向战区部署算法[@mv_techsparx]。

!photo shanahan_2020|空军中将杰克·沙纳汉官方肖像。沙纳汉 2017 年 4 月至 2018 年 12 月负责指导 Project Maven，随后出任联合人工智能中心（JAIC）首任主任|美国国防部，公有领域

!photo maven_2017_dod_article|国防部 2017 年报道页面截图：Maven 计划于当年年底前向战区部署算法，图为库科上校在 Defense One 技术峰会上介绍项目|美国国防部网站截图，公有领域

JAIC 从未担任 Maven 的主管单位。JAIC 于 2018 年成立后，Maven 仍隶属 OUSD(I)，只是首任负责人沙纳汉转任 JAIC 主任；二者于 2022 年一并划入 CDAO[@mv_wiki_maven]。2026 年 3 月，彭博社记者凯特琳娜·曼森（Katrina Manson）出版专著《Project Maven：一位陆战队上校、他的团队与 AI 战争的黎明》（W. W. Norton），书名中的"陆战队上校"推测指库科，检索结果未直接确认[@mv_npr_book]。该书是迄今关于 Maven 内部运作最详细的公开叙述，本章多处引用其书评和摘要。

### 首批部署：ScanEagle 视频与"原型战"

2017 年 12 月，Maven 首个达到任务就绪状态的产品部署至中东，即用于识别 ScanEagle 小型无人机视频中物体的算法[@mv_trajectory,mv_nextgov_2017]，从立项到上线约 8 个月。使用者为特种作战司令部（SOCOM）情报分析员，沙纳汉称这种做法为"原型战"（prototype warfare）[@mv_nextgov_2017]。2018 年 5 月，官员透露非洲司令部（AFRICOM）自 2017 年 12 月起也在使用 Maven，部署范围扩展到中东多个地点[@mv_bd_2018_africa]。《原子科学家公报》于 2017 年 12 月以"Project Maven 把 AI 带进对 ISIS 的战斗"为题作了报道[@mv_bulletin_2017]。

!photo scaneagle_mkv|ScanEagle 小型无人机从 MK V 特种作战艇上发射。Maven 于 2017 年 12 月首批部署的算法用于识别 ScanEagle 全动态视频中的物体|美国国防部，公有领域

!photo scaneagle_catapult|伊拉克阿萨德空军基地弹射器上待发的 ScanEagle 无人机。此类战术无人机在反 ISIS 作战中产生了大量需人工判读的视频|美国国防部，公有领域

据彭博社 2024 年长篇报道，Maven 早期曾用美国海军"海豹"突击队在索马里拍摄的无人机视频，测试多家供应商的识别工具[@mv_bloomberg_2024]。GlobalSecurity 还提到更多早期作战使用，未获其他来源佐证（弱源，待核）[@mv_globalsec]。

### 早期供应商与合同体系：ECS 渠道下的多供应商格局

Maven 早期合同大多经集成商 ECS Federal 下达，采购渠道之一是陆军研究实验室（ARL）"基础与应用科学研究"广泛机构公告（BAA）合同；谷歌、微软、AWS、Clarifai 等均以 ECS 分包商身份参与[@mv_fedsavvy,mv_itpro]。ECS 自 2017 年起担任 Maven 的 AI 互操作集成商（AI3）[@mv_execbiz_ecs]，此后陆续持有 3 份与 Maven 相关、总额约 3.64 亿美元的合同[@mv_itpro,mv_poulson_budget]。ECS 本身于 2018 年 4 月被 ASGN 以 7.75 亿美元收购[@mv_fedsavvy]。

主要供应商情况如下。谷歌经 ECS 分包参与 FMV 目标检测 AI 开发；谷歌云负责人对内称合同"只有约 900 万美元"，泄露的内部邮件则写明"总交易 2,500—3,000 万美元，其中 1,500 万美元在 18 个月内归谷歌"，并提到"项目扩大后预算为每年 2.5 亿美元"[@mv_intercept_emails,mv_gizmodo_google]。我部分析，三个数字分属三个层次：900 万美元是对外口径的初始合同额，1,500 万美元是 18 个月的内部预期，2.5 亿美元是整个 Maven 项目的年度预算展望，并非谷歌合同上限。Clarifai 作为 ECS 分包商累计获得 2,500 万美元以上，其中一项人脸识别任务为 560 万美元[@mv_forbes_startups,mv_itpro]。微软（约 3,000 万美元，约 2019 年起）和 AWS（约 2,000 万美元，约 2020 年起）也获得 ECS 分包，但分包合同未直接点名 Maven，二者与 Maven 的关联系调查记者杰克·波尔森（Jack Poulson，Tech Inquiry）的推断[@mv_forbes_2021,mv_poulson_budget]。泄露邮件还显示，2017 年 9 月亚马逊、IBM、微软均在与谷歌竞争 Maven 工作[@mv_intercept_emails,mv_itpro]。

金额最大的是代号 Pavement 的 ECS 主合同，计 1.42 亿美元；另有一份关联 ECS 合同 5,225 万美元，用于 SUNet 开源数据聚合。五角大楼后依据《联邦采购条例》FAR 4.606 将上述记录从公开采购数据库中删除，国防部长办公室发言人确认了删除行为[@mv_poulson_pavement,mv_poulson_erasure]。我部分析，由于记录被删，2017—2021 年 Maven 支出中可公开核查的部分，很可能明显低于实际规模。GlobalSecurity 另称谷歌通过与诺斯罗普·格鲁曼的安排提供基于 TensorFlow 的模型，L3Harris、内华达山脉公司等 20 余家公司参与，Palantir 提供数据集成层并后来发展为 MSS，上述说法未获一手来源证实（弱源，待核）[@mv_globalsec]。2023 年，NGA 专门发布征询，评估 Maven 的 AI/ML 供应链风险，理由是对主承包商以下各级供应商缺乏可见度[@mv_bd_supplychain_2023]。

!table t_mv_vendors|Project Maven 早期（2017—2021）主要供应商与合同|本报告据 The Intercept、Forbes、ITPro、Tech Inquiry 等整理|24,30,46,60
供应商|身份|金额（据报）|说明与证据等级
ECS Federal|主承包商、AI 互操作集成商（AI3）|3 份相关合同约 3.64 亿美元；Pavement 合同 1.42 亿美元|Pavement 记录已依据 FAR 4.606 删除；数字来自 Tech Inquiry 调查[@mv_poulson_pavement,mv_itpro]
谷歌|ECS 分包商|对外约 900 万美元；内部预期 1,500 万美元/18 个月|FMV 目标检测；2018-06 宣布 2019-03 合同到期后不续约[@mv_intercept_emails,mv_nbc_google]
Clarifai|ECS 分包商|累计 2,500 万美元以上|含 560 万美元人脸识别任务[@mv_forbes_startups]
微软|ECS 分包商（推断）|约 3,000 万美元，约 2019 年起|分包合同未点名 Maven，关联系推断[@mv_forbes_2021]
AWS|ECS 分包商（推断）|约 2,000 万美元，约 2020 年起|同上[@mv_forbes_2021]
Palantir|数据集成层（二手说法）|未披露|GlobalSecurity 称其后发展为 MSS（弱源，待核）[@mv_globalsec]
!end

### 谷歌员工抗议：硅谷与五角大楼关系的转折

2018 年春，谷歌参与 Maven 一事在公司内部引发大规模抗议，成为 Maven 早期影响最大、最为人知的事件。员工联名请愿，要求谷歌取消合同并承诺不再从事军事工作。签名人数说法不一：Gizmodo 报道"近 4,000 人"，其他报道称 4,600 人以上，带有倡导色彩的 Jacobin 后称近 5,000 人[@mv_gizmodo_au_resign,mv_fortune_2018]。辞职人数同样口径不一：Gizmodo 2018 年 5 月报道约十余人辞职，为谷歌已知首次因业务决策出现集体辞职；其他媒体称至少 13 人，Axios 称"数十人"[@mv_gizmodo_au_resign]。公司内部另有 700 余人组成"Maven 良心拒服者"小组[@mv_collective]。

!photo google_walkout_2018|2018 年谷歌员工在桑尼维尔罢工抗议。同年谷歌在员工反对下宣布不再续签 Maven 合同，这是硅谷科技从业者首次大规模反对军事 AI 项目|维基共享资源，CC BY-SA 4.0

2018 年 6 月 1 日前后，谷歌云首席执行官黛安·格林（Diane Greene）告知员工，谷歌不会在现有合同于 2019 年 3 月到期后寻求续约[@mv_nbc_google,mv_fortune_2018]。彭博社当时评论，此次 AI 员工抗议可能影响谷歌争取五角大楼云合同的前景[@mv_bloomberg_2018]。

我部分析，谷歌退出并未延缓 Maven 进度，ECS、Clarifai、微软、AWS 以及后来的 Palantir 等迅速填补了空缺。这场争议客观上推动了国防部此后的 AI 伦理原则建设，"科技公司是否应参与杀伤链"也由此成为此后八年反复出现的议题，2026 年 Anthropic 与五角大楼的冲突与 2018 年谷歌风波一脉相承。

### 经费演变：从 7,000 万美元到 23 亿美元申请

Maven 早期经费由国会大幅加码。据 Inside Defense 报道，FY2018 国会拨款 1.31 亿美元，而国防部请求仅约 3,100 万美元[@mv_insidedefense_fy18]；FY2020 为 2.21 亿美元，FY2021 为 2.5 亿美元（按请求拨付，项目名称改为"算法战跨职能小组软件试点项目"）[@mv_ds_2024_03,mv_dd_ndaa]。此后 Maven 的公开预算逐渐模糊：FY2022—FY2025 只有早期五年防务计划（FYDP）中的规划值，分别为 2.52 亿、1.20 亿、1.21 亿和 1.22 亿美元；FY2025 预算书将 Maven 经费调整至 CDAO 项目元素 PE 0606135D8Z 下，公开预算不再单列 Maven[@mv_ds_2024_03]。NGA 一侧经费属情报预算，处于涉密状态。Lawfare 书评指出，Maven 预算属机密，且不适用《信息自由法》（FOIA）[@mv_lawfare_book]。

FY2027 预算申请中，Maven 重新以较大数额出现在公开文件里。国防部 FY2027 预算概览列出约 23 亿美元用于"Maven 智能系统与联合火力网"（Joint Fires Network），用于交付 CJADC2 能力[@mv_fy27_book,mv_gtlaw]。DefenseScoop 给出的拆分是：其中 15 亿美元以上用于"联合部队 AI 赋能司令部倡议"（Joint Force AI-Enabled Headquarters initiative），以扩大 MSS 用户访问；另有 6,000 万美元用于"虚拟联合作战中心"[@mv_ds_fy27]。{red:口径冲突}：ISS Tracker、SpaceNews 等称 23 亿美元为"未来五年"合计，DefenseScoop 和预算概览则表述为 FY2027 单年申请[@mv_isstracker,mv_spacenews_23]。本报告以官方预算概览为准；该 23 亿美元包含联合火力网，不能全部计为 Palantir MSS 收入。

!table t_mv_budget|Project Maven / MSS 各财年经费（公开口径）|本报告据 Inside Defense、DefenseScoop、FY2027 预算概览整理|26,44,90
财年|金额|性质与说明
FY2017|约 0.7 亿美元|成立后约两个月内获国会经费[@mv_wiki_maven]
FY2018|1.31 亿美元|国会拨款；国防部请求仅约 0.31 亿美元[@mv_insidedefense_fy18]
FY2019|未检索到|—
FY2020|2.21 亿美元|国会拨款[@mv_ds_2024_03]
FY2021|2.5 亿美元|按请求拨付；更名为算法战跨职能小组软件试点项目[@mv_dd_ndaa]
FY2022—FY2025|2.52 亿/1.20 亿/1.21 亿/1.22 亿美元|早期 FYDP 规划值，非实际拨款[@mv_ds_2024_03]
FY2025|不再单列|并入 CDAO 项目元素 PE 0606135D8Z；NGA 部分属情报预算[@mv_ds_2024_03]
FY2027 申请|约 23 亿美元（MSS 与联合火力网）|其中 15 亿美元以上用于扩大 MSS 访问；另有"五年合计"说法[@mv_fy27_book,mv_ds_fy27]
!end

### 猩红之龙：XVIII 空降军把 Maven 改造为目标工作流平台

2017 年的 Maven 主要是一组计算机视觉检测器，推动其发展为数据融合与目标工作流平台的，是驻布拉格堡的陆军第 XVIII 空降军。自 2020 年起，XVIII 空降军通过年度系列演习"猩红之龙"（Scarlet Dragon），在 DevSecOps 环境中与多达 70 家公司合作，把 Maven 发展为整合传感器、目标识别和火力分配的 MSS[@mv_d1_2024_08,mv_cset_coalition]。美国政府问责局（GAO）2022 年报告将"猩红之龙"描述为使用 Project Maven 数据的陆军目标识别 AI 能力[@mv_gao_22]。乔治城大学安全与新兴技术中心（CSET）2024 年 8 月发布政策简报《构建技术联盟》，系统记录了这一过程，并给出"约 20 人顶 2,000 人"的对比（详见本章第四节）[@mv_cset_coalition]。2022 年俄乌冲突爆发后，前沿部署欧洲的 XVIII 空降军又用 MSS 为乌克兰生成目标情报（详见本章第五节）。

我部分析，"猩红之龙"阶段把 Maven 的重心从提高识别精度转向加快目标流程，由此决定了 MSS 后来的形态：识别模型可由多家供应商提供并不断替换，平台的核心竞争力在于把多源数据、检测结果、目标列表、打击资产和审批流程整合在同一界面中。

### 2022 年拆分：NGA Maven 与 CDAO/陆军 MSS

2022 年是 Maven 治理结构的分水岭。当年 4 月的 GEOINT 大会上，NGA 宣布从 OUSD(I&S) 接管 Maven 的 GEOINT AI 服务，约占原项目的 80%，自 FY2023 起生效[@mv_bd_2022_nga,mv_c4isr_2022]。FY2023 预算请求据此把 Maven 拆为两部分：GEOINT 部分划归 NGA，非 GEOINT 部分划归同年成立的 CDAO[@mv_bd_2022_nga]。2022 年 10 月国会以持续决议案维持政府运转，移交一度推迟，五角大楼对此未作说明[@mv_ds_2022_cr]。

NGA 经约 9 个月的需求工作，于 2023 年 11 月 2 日宣布、11 月 7 日正式将 NGA Maven 列为采购项目，采用软件采购路径[@mv_dd_por,mv_wiki_maven]。2024 年 3 月的 FY2025 预算书将 Maven 经费调整至 CDAO 名下，CDAO 副主任表示已把整个 Maven"AI 开发流水线"交给 NGA；DefenseScoop 观察到，NGA、CDAO 和 OUSD(I&S) 自移交以来对 Maven 和 MSS"大体守口如瓶"[@mv_ds_2024_03]。DefenseScoop 引用的一份 Palantir 新闻稿，则把 Maven 描述为"支撑 CDAO 的 CJADC2 倡议的云基础设施、软件能力和 AI"[@mv_ds_86457]。

!photo nga_hq_paglen|弗吉尼亚州斯普林菲尔德的国家地理空间情报局（NGA）总部夜间航拍。NGA 自 2022 年起接管 Maven 约 80% 的 GEOINT AI 业务，2023 年 11 月将 NGA Maven 列为正式采购项目|特雷弗·帕格伦（Trevor Paglen）拍摄并公开发布

!photo whitworth_portrait|NGA 第八任局长、海军中将弗兰克·惠特沃斯（Frank Whitworth）官方肖像。惠特沃斯任内主导 Maven 在 NGA 的扩展，多次公开披露 Maven 用户规模和"机器生成情报"标注做法|美国国防部，公有领域

!photo martell_portrait|首任首席数字与人工智能官（CDAO）克雷格·马特尔（Craig Martell）官方肖像。CDAO 于 2022 年成立，承接 Maven 非 GEOINT 部分及 JAIC 等机构|美国国防部，公有领域

自 FY2023 起，Maven 形成两条线。NGA Maven 负责 GEOINT 计算机视觉模型的标注、训练、评估认证和机器生成情报产品；MSS 作为面向作战司令部的作战平台，由 CDAO 主管，NGA 承担系统管理与运行授权职责，陆军负责签约。2023 年 12 月经"全球信息主导实验"（GIDE）认证、2024 年 2 月公布的 CJADC2"最小可行能力"（MVC），即以 MSS 为事实骨干[@mv_ds_cjadc2_mvc,mv_bd_opendagir]。

!fig d_maven_governance|d_maven_governance.png|Maven 管理归属演变（2017—2026）|本报告依据 NSArchive 备忘录、Breaking Defense、Defense Daily、DefenseScoop 等公开资料绘制|160

### 前史：Palantir 在陆军"情报到目标"链条上的积累

Palantir 能在 MSS 上后来居上，与其此前在陆军和特种作战领域积累的情报数据平台业务密切相关。2016 年 5 月，SOCOM 以单一来源方式授予 Palantir 上限 2.22 亿美元的"全源信息融合"软件许可[@mv_wt_socom]。2018—2020 年，Palantir 先后进入陆军分布式通用地面系统（DCGS-A）第一能力包（与雷神共享上限 8.76 亿美元）和第二能力包（2020 年 2 月与 BAE 共享上限 8.23 亿美元的 IDIQ），并于 2021 年 10 月中标建设基于 Gotham 的跨密级情报数据织网[@mv_c4isr_dcgsa,mv_wt_dcgsa,mv_bd_dcgsa]。2019 年 12 月，Palantir 获得陆军企业数据平台 Vantage 生产合同，上限 4.58 亿美元[@mv_tipranks_vantage]。

与 Maven 关系最近的是 2020 年 10 月陆军研究实验室授予的 9,120 万美元两年期 AI/ML 研发合同，内容是用 Foundry 和 Gotham 为各作战司令部提供 AI 数据整合与模型训练，期限至 2022 年 9 月 28 日[@mv_datanami_arl,mv_bw_arl_2020]。我部分析，该合同的客户（作战司令部）、内容（数据整合与模型训练）和时间（恰在 MSS 原型阶段之前）均带有 MSS 前身特征，陆军研究实验室此后也正是 2024 年 MSS 军种扩展合同的授予方。2024 年 3 月，Palantir 击败雷神，赢得陆军下一代情报、监视与侦察地面站 TITAN 原型合同（1.784 亿美元），该项目目标即缩短"传感器到射手"时间[@mv_ds_titan,mv_army_titan]。至 2024 年 MSS 合同落地时，Palantir 已在陆军"情报—目标"链条的多个环节完成布局。

### Palantir 成为主承包商：逐步加深的锁定

Palantir 成为 MSS 主承包商经历了六个步骤，每一步都加深了国防部对其平台的依赖。第一步是在位开发原型：2024 年合同之前，Palantir 已在"面向有限数量的操作员"开发 MSS 原型，起始时间（约 2022—2023 年）未见一手来源证实[@mv_ds_2024_05]。第二步是唯一供应商认证：据 Tech Inquiry 报道，五角大楼认证 Palantir 为 MSS 唯一供应商[@mv_poulson_solesource]。

第三步是 2024 年 5 月 29 日的 4.8 亿美元合同。陆军合同司令部阿伯丁分部（ACC-APG）授予 Palantir 编号 W911QX-24-D-0012 的五年期固定价格不定期交付/不定数量（IDIQ）合同，名为"Maven 智能系统原型"，预计 2029 年 5 月 28 日完成，目的是把 MSS 扩展至中央司令部（CENTCOM）、欧洲司令部（EUCOM）、印太司令部（INDOPACOM）、北方司令部（NORTHCOM）、运输司令部（TRANSCOM）和联合参谋部的"数千名用户"[@mv_ds_2024_05,mv_dn_2024_05,mv_meritalk_480]。合同将 MSS 描述为接入卫星图像、地理定位等数据以检测潜在目标、支撑 CJADC2 的系统。对该合同的阶段定性存在分歧：合同名称为"原型"，MeriTalk 称其开启了原型阶段，Palantir 方面则称这是"从原型走向生产"[@mv_meritalk_480,mv_dn_2024_05]。

第四步是向各军种扩展。2024 年 9 月，陆军作战能力发展司令部陆军研究实验室（DEVCOM ARL）授予 Palantir 约 9,980 万美元的五年期固定价格合同，把 MSS 扩展至陆军、空军、太空军、海军和海军陆战队，新增数万名军种用户[@mv_govconwire_arl,mv_bw_2024_09]。

第五步是提高合同上限。2025 年 5 月 20 日（5 月 21 日公布），陆军对 W911QX-24-D-0012 发出第 P00005 号修改，追加 7.95 亿美元软件许可，合同上限升至约 12.75 亿美元（各方表述为"近 12.8 亿"或"约 13 亿"），期限仍至 2029 年 5 月 28 日[@mv_globalsec_contract,mv_ds_2025_05]。国防部称预计需求将"大幅涌入"，陆军官员同时强调上限只是封顶值，并非已承诺的资金[@mv_ds_2025_05]。同月，NGA 局长惠特沃斯在 GEOINT 2025 大会上披露，NGA 另授予 Palantir 2,800 万美元合同，以扩大 NGA 分析员对 MSS 的访问[@mv_meritalk_nga]。

第六步是以企业协议整合合同。2025 年 7 月 31 日（8 月 1 日公告；另有来源称 8 月），陆军与 Palantir 签订为期 10 年、上限 100 亿美元的企业协议（EA），整合 75 份合同（15 份主合同和 60 份相关合同）；陆军称 100 亿美元是上限而非"具体支出承诺"[@mv_wt_ea,mv_ds_ea]。2026 年 3 月的 Feinberg 备忘录随即规定全部 MSS 合同转入该载体（见下文）。

!table t_mv_contracts|Palantir MSS 合同链条（2024—2026）|本报告据 DefenseScoop、DoD 合同公告、GovConWire、MeriTalk、Marines.mil 等整理；上限不等于实际拨付|22,34,30,74
日期|客户与载体|金额|范围与说明
2024-05-29|陆军 ACC-APG，IDIQ W911QX-24-D-0012，固定价格|上限 4.8 亿美元|MSS 原型扩展至 5 个作战司令部和联合参谋部"数千用户"，至 2029-05-28[@mv_ds_2024_05]
2024-09|陆军 DEVCOM ARL，固定价格，5 年|约 0.998 亿美元|扩展至陆、空、天、海、陆战队五个军种[@mv_govconwire_arl]
2025-05-20|W911QX-24-D-0012 修改 P00005|追加 7.95 亿美元，上限约 12.75 亿美元|新增软件许可，未扩大范围[@mv_globalsec_contract,mv_ds_2025_05]
2025-05|NGA|0.28 亿美元|扩大 NGA 分析员 MSS 访问[@mv_meritalk_nga]
2025-07-31|陆军企业协议（EA），10 年|上限 100 亿美元（整合 75 份合同）|2026 年起为全部 MSS 合同的载体[@mv_wt_ea,mv_ds_ea]
2025-08-15 敲定|海军陆战队企业许可（经 CDAO、DIU、ARL）|未披露|在 SIPRNet（IL6 云）上无限量访问[@mv_usmc_release,mv_ds_usmc]
2026-03-09|Feinberg 备忘录（政策指令）|—|MSS 转正式项目；合同统一转入陆军 EA[@mv_ds_feinberg1]
2026-08（未证实）|据报为陆军 PEO IEW&S|"最高 6.18 亿美元、5 年"|仅见于聚合站，可能与 2024-12 陆军 Vantage 6.189 亿美元合同混淆（弱源，待核）[@mv_govly]
!end

我部分析，将已知上限相加（约 12.75 亿＋0.998 亿＋0.28 亿美元），MSS 专属合同上限约 14 亿美元，不含陆战队未披露金额和未证实的 6.18 亿美元。上限不等于拨付，也不能与陆军 EA 的 100 亿美元相加。Feinberg 备忘录之后，新的 MSS 采购将以 EA 下订单形式出现，可能不再单独发布合同公告，公开追踪难度将明显上升。财务数据方面，Palantir 美国政府收入 2025 年同比增长 55%，2026 年上半年增速升至 84%—90%，在时间上与 MSS 上限扩大、陆军 EA、陆战队许可和伊朗战事期间用户激增相吻合，但二者只是相关，因果关系未经证实[@mv_pltr_q4_2025,mv_pltr_q2_8k]。

### 北约采购：MSS NATO

2025 年 3 月 25 日，北约通信与信息局（NCIA）与 Palantir 完成"MSS NATO"采购，供盟军作战司令部（ACO，即欧洲盟军最高司令部 SHAPE）使用，4 月 14 日对外公布[@mv_ncia_2025,mv_shape_2025]。从提出需求到签约约 6 个月，北约称这是其历史上最快的采购之一；合同金额未公开，计划签约后约 30 天内部署[@mv_shape_release,mv_defupdate]。北约公布的用途为情报融合与目标定位、战场态势感知与规划、加速决策，系统包含大语言模型、生成式 AI 和机器学习，SHAPE 还计划接入新的 AI 模型和建模仿真工具[@mv_shape_release,mv_defensepost_nato]。Breaking Defense 指出，此次采购发生在跨大西洋关系紧张的背景下[@mv_bd_nato_2025]。

此后 MSS NATO 先后部署至 SHAPE 和布林森联合部队司令部（JFC Brunssum），诺福克联合部队司令部（JFC Norfolk）预计于 2026 年 4—5 月接入[@mv_janes_norfolk]。2026 年 6 月 22 日，MSS NATO 达到全面作战能力（FOC），获准在北约机密网络上运行，数据存放于北约自有数据中心；系统于 2025 年全年进行测试，并经"坚定威慑 2026"（Steadfast Deterrence 2026）演习检验，6 月 30 日对外公布[@mv_shape_foc,mv_janes_foc]。欧洲有评论认为，MSS NATO 表明美国软件正在影响欧洲军事决策，涉及主权问题[@mv_escudo_europe]。

### Feinberg 备忘录：从原型转为全军正式项目

2026 年 3 月 9 日，国防部常务副部长史蒂夫·范伯格（Steve Feinberg）签发备忘录，对 MSS 的地位作出根本调整，主要内容有四点[@mv_ds_feinberg1,mv_ds_feinberg2,mv_csis]：一是 MSS 须在 2026 财年结束（2026 年 9 月 30 日）前成为正式采购项目；二是由负责研究与工程的副部长（USD(R&E)）和负责情报与安全的副部长（USD(I&S)）牵头，在 30 天内把 MSS 的系统管理、监督、支持活动及相关职责从 NGA 移交至 CDAO 新设的 MSS 项目办公室；三是全部 MSS 合同转入"现有的陆军企业协议（EA）合同载体"，此后对 Palantir 的合同行动由陆军负责；四是由 USD(R&E) 接替 NGA，担任 MSS 及其商业云基础设施的授权官（AO）。备忘录还要求国防部首席技术官埃米尔·迈克尔（Emil Michael）评估是否将 MSS 纳入拟设的 CJADC2 项目办公室[@mv_ds_feinberg1]。

据 DefenseScoop 报道，该指令把"AI 赋能决策"定为 CJADC2 的"基石"[@mv_ds_feinberg1]。各部门面临"激进"的过渡时间表，有官员认为运行授权（ATO）是瓶颈，全面完成可能需要 18 个月；专家表示此次重大调整的"全部影响仍不清楚"[@mv_ds_feinberg2]。{red:日期冲突}：DefenseScoop 和 CSIS 给出的签署日期为 3 月 9 日，路透社约在 3 月 20—23 日报道了这份备忘录，倡导团体 Capture Cascade 的时间线写作 3 月 21 日，后者应为报道日期而非签署日期[@mv_govconwire_por,mv_capture]。

2026 年 8 月 5 日，陆军上校莫莉·索尔斯伯里（Molly Solsbury，ai.mil 简历页写作 Melissa）被任命为 CDAO 内的 MSS 项目主任。她此前任职于陆军参谋长办公室，此项任命旨在推动 MSS 成为核心指挥控制资产[@mv_ds_solsbury,mv_aimil_solsbury]。据其简历，CDAO 此时已隶属 USD(R&E)。外界评论认为，国防部对如何结束"碎片化部署"披露甚少[@mv_ds_solsbury]。

关于转制是否按期完成，{red:截至 2026 年 10 月未见国防部或 CDAO 的正式确认}。Motley Fool（2026 年 8 月 25 日）称 Maven"现已成为"正式项目[@mv_motley_por]；Palantir 管理层在 2026 年二季度财报电话会上称"首个正式项目本季度在平台上启动"[@mv_cnbc_q2,mv_fool_q2]；其他媒体仍以"过渡中"描述[@mv_govconwire_por]。

### 2026 年现状：全军"万能应用"

至 2026 年秋，MSS 已成为国防部事实上的 AI 赋能指挥控制与目标定位骨干。用户规模方面，2025 年 5 月 NGA 局长惠特沃斯称，Maven 已向所有军种和作战司令部开放，活跃用户逾 2 万，覆盖 35 个以上工具、3 个安全域，为 2024 年 3 月的四倍以上（另一报道口径为"自 2025 年 1 月以来翻了一倍多"[@mv_ds_2025_05]），模型时延在列为正式项目后一年内改善 80%[@mv_bd_geoint2025,mv_ecs_maven]。2026 年 9 月 22 日，负责研究与工程的副次长詹姆斯·马佐尔（James Mazol）在 DefenseTalks 会议上表示，MSS 用户从 2026 年 1 月的约 5 万人增至"史诗怒火"行动开始后的 10 万人以上，并正推广至所有作战司令部和国民警卫局；CDAO 卡梅伦·斯坦利（Cameron Stanley）称，Maven 在"史诗怒火"行动 38 天中协助打击了 13,000 个目标，并正扩展至后勤、供应链、战备和预算数据[@mv_ds_mazol,mv_defpost_2026]。《国防一号》据此称 Maven 正在成为五角大楼的"万能应用"（everything app），据 CDAO 称已取代"6、8、10 个"旧系统[@mv_d1_everything]。陆军联合兵种司令部也已将"Maven C2 智能系统"纳入训练和院校教育体系[@mv_army_cac]。

!fig c_maven_scale|c_maven_scale.png|MSS 用户数增长与 Palantir MSS 合同上限/预算|本报告依据 Breaking Defense、DefenseScoop、FY2027 预算文件绘制|160

【用户口径说明】上述用户数存在口径差异。2025 年的"2 万以上"是 NGA 所称活跃用户；另有二手来源称 2025 年 Maven 覆盖 130 余个站点、约 2.5 万人（弱源，待核）[@mv_hvylya]；还有聚合站称 2026 年 3 月活跃用户 2 万余人[@mv_govly]，与马佐尔所称"1 月约 5 万"冲突，差异可能源于注册用户与活跃用户之分。图 {fig:c_maven_scale} 采用官方口径。

MSS 的大模型层同期出现重大不确定性。据报道，Anthropic 的 Claude 于 2024 年末经 Palantir 接入 Maven[@mv_aca_iran]。2026 年 3 月 4 日，国防部据报将 Anthropic 列为"供应链风险"，要求 6 个月内淘汰其工具，起因是 Anthropic 拒绝将模型用于大规模国内监控和完全自主武器；Palantir 首席执行官卡普随后在 CNBC 上表示，Claude 仍在目标系统中运行[@mv_aca_iran,mv_ie_claude]。替换是否完成、由谁接替，截至本报告未见一手确认（详见本章第二节）。

### 大事年表

!table t_mv_chronology|Project Maven / MSS 大事年表（2017—2026.10）|本报告据各条所列来源整理|24,100,36
日期|事件|来源
2017-04-26|常务副部长沃克签署备忘录，成立算法战跨职能小组（Project Maven），首项任务为无人机 FMV 的处理、利用和分发|[@mv_work_memo,mv_globalsec]
2017 年中|成立约两个月内获国会约 7,000 万美元|[@mv_wiki_maven]
2017-07|项目方宣布年底前向战区部署算法|[@mv_techsparx]
2017-12|首个算法（ScanEagle FMV 物体识别）部署中东，供 SOCOM 分析员使用；AFRICOM 同期开始使用|[@mv_nextgov_2017,mv_bd_2018_africa]
2017—2018|谷歌经 ECS 分包参与；Clarifai 为 ECS 分包商|[@mv_intercept_emails,mv_forbes_startups]
2018-03 至 06|谷歌员工请愿（约 4,000—4,600 人签名）并有员工辞职|[@mv_gizmodo_au_resign,mv_fortune_2018]
2018-06-01 前后|谷歌云 CEO 格林宣布合同 2019-03 到期后不续约|[@mv_nbc_google]
2018-12|沙纳汉调任 JAIC 首任主任|[@mv_wiki_maven]
2019—2020|微软（约 3,000 万美元）、AWS（约 2,000 万美元）获 ECS 分包（关联系推断）|[@mv_forbes_2021]
2020 起|XVIII 空降军开展"猩红之龙"系列演习，与多达 70 家公司把 Maven 发展为 MSS|[@mv_d1_2024_08,mv_cset_coalition]
2022-04|NGA 宣布接管 Maven 的 GEOINT AI 服务（约 80%），FY2023 生效|[@mv_bd_2022_nga,mv_c4isr_2022]
2022 起|XVIII 空降军用 MSS 为乌克兰生成目标情报|[@mv_lawfare_book,mv_kyivind]
2022-10|移交因持续决议案推迟|[@mv_ds_2022_cr]
2023-11-02 / 11-07|NGA 宣布并正式将 NGA Maven 列为采购项目（软件采购路径）|[@mv_dd_por]
2023-12 / 2024-02|CJADC2 最小可行能力经 GIDE 认证并公布，MSS 为事实骨干|[@mv_ds_cjadc2_mvc]
2024-02-02|CENTCOM 在伊拉克、叙利亚 85 次以上打击中用 Maven 缩小目标范围|[@mv_register_2024]
2024-03|FY2025 预算将 Maven 经费调整至 CDAO PE 0606135D8Z；AI 开发流水线全部交给 NGA|[@mv_ds_2024_03]
2024-05-29|陆军授予 Palantir 4.8 亿美元 MSS 原型 IDIQ|[@mv_ds_2024_05]
2024-07-29|NGA 授予 Scale AI 约 2,400 万美元 Maven 数据标注过渡合同|[@mv_nga_contracts]
2024-09|ARL 授予 Palantir 约 9,980 万美元合同，MSS 扩展至五个军种|[@mv_govconwire_arl]
2024 年末|据报 Claude 经 Palantir 接入 Maven|[@mv_aca_iran]
2024-12-06|Anduril 与 Palantir 宣布合作，拟将 Lattice 与 MSS、AIP 结合|[@mv_ds_anduril_palantir]
2025-03-25 / 04-14|北约 NCIA 采购 MSS NATO，历时约 6 个月|[@mv_ncia_2025,mv_shape_2025]
2025-05|惠特沃斯称活跃用户 2 万以上、工具 35 个以上、安全域 3 个；MSS 上限追加 7.95 亿美元至约 13 亿美元|[@mv_bd_geoint2025,mv_ds_2025_05]
2025-07-31|陆军与 Palantir 签订 10 年、上限 100 亿美元企业协议|[@mv_wt_ea]
2025-09-10 / 09-12|陆战队企业许可公布，MSS 定为标准火力与效果集成平台|[@mv_ds_usmc,mv_ds_maradmin]
2025-11|Enabled Intelligence 赢得 NGA 最高 7.08 亿美元 SEQUOIA 数据标注合同|[@mv_bd_sequoia]
2026-02-28 起|"史诗怒火"行动（对伊朗），MSS 大规模用于目标定位；首日发生 Minab 学校遇袭事件|[@mv_aca_iran,mv_bloomberg_minab]
2026-03-04|据报国防部将 Anthropic 列为供应链风险，要求 6 个月内淘汰|[@mv_aca_iran]
2026-03-09|Feinberg 备忘录：FY2026 末转正式项目；管理权移交 CDAO；合同并入陆军 EA|[@mv_ds_feinberg1,mv_ds_feinberg2]
2026-03-23/24|曼森专著《Project Maven》出版|[@mv_npr_book]
2026-05-14|CDAO 斯坦利向众议院提交书面证词|[@mv_stanley_testimony]
2026-05-28|FY2027 预算申请：MSS 与联合火力网约 23 亿美元|[@mv_ds_fy27,mv_fy27_book]
2026-06-22|MSS NATO 达到全面作战能力|[@mv_shape_foc]
2026-08-05|索尔斯伯里上校任 CDAO MSS 项目主任|[@mv_ds_solsbury]
2026-09-22|用户超过 10 万；38 天打击 13,000 个目标|[@mv_ds_mazol]
2026-09-30|转正式项目截止日；截至本报告未见官方确认|[@mv_govconwire_por]
!end

## （二）功能设计：多源融合、看板式目标工作流与大模型代理

:::lead
MSS 的主要功能是把分散在上百个数据源中的情报转化为对象并呈现在同一张地图上，再通过看板把每个目标从发现推进到评估，各环节由人逐一批准。其核心在于把检测、目标管理、资产比较、火力交接和效果评估串成一条可追踪、可加速的流程，而非某一识别算法；2024 年后又叠加了以大模型为核心的自然语言代理。公开资料对各模块的描述详略悬殊：看板与资产比较有厂商和智库资料支撑，武器—目标配对算法、毁伤评估和行动方案生成几乎没有权威细节。
:::

### 总体定位：从"传感器到射手"的决策支持平台

北约对 MSS NATO 的官方描述，是目前关于 MSS 功能最权威的概括：该系统是"AI 赋能的作战系统"，用大语言模型、生成式 AI 和机器学习开展情报融合、目标定位、战场态势感知、作战计划和加速决策；它把多个来源（涉密和公开）的结构化与非结构化数据汇入统一、可搜索的平台，开放架构可接入第三方 AI 模型、仿真工具和应用[@mv_shape_release,mv_bd_nato_2025]。2024 年陆军合同公告对美方 MSS 的描述更侧重目标定位，即接入卫星图像、地理定位等数据，检测潜在目标，支撑 CJADC2[@mv_ds_2024_05]。海军陆战队 2025 年 MARADMIN 电报将 MSS 定为跨多个作战司令部的标准"火力与效果集成平台"（fires and effects integration platform）[@mv_ds_maradmin]。

综合上述表述，MSS 的功能定位可归纳为融合、目标和决策支持三点：把多源数据汇聚到一个平台，围绕目标定位流程组织工作，由系统给出检测、排序和建议、由人作出打击决定。官方和主流报道一致将 MSS 定位为决策支持工具，目标由人类指挥官批准[@mv_csis]。

!photo mss_ngb|国民警卫局人员在培训中学习使用 Maven 智能系统，画面可见 MSS 地图界面。MSS 自 2026 年起推广至国民警卫局|美国国民警卫局，公有领域

### 多源情报融合：179 个数据源

据 CSIS 报道，中央司令部 2024 年部署的 MSS 接入了 **179 个不同数据源**，业内人士称此后数量仍在增加[@mv_csis]。卫星来源既有国家侦察卫星，也有 ICEYE、Capella Space 等商业合成孔径雷达（SAR）卫星，此外还接入信号情报，包括截获的通信和电子辐射[@mv_csis]。GlobalSecurity 根据 Palantir 公开演示给出的数字为"150 个以上数据源"（弱源，待核）[@mv_globalsec]。

数据融合的作用在于打通各自独立的系统。传统流程中，图像情报、信号情报、人力情报和友军态势分属不同系统、密级和部门，目标分析员须在多个终端间切换并人工比对。MSS 将这些数据统一映射到平台数据模型（见本章第三节"本体"），同一目标的图像、信号、历史记录和地理信息可在一个对象下关联查询。有描述称，无人机执行任务时，其位置数据和视频实时回传至 Maven（二手）[@mv_spatial]。{red:全动态视频（FMV）和友军跟踪（BFT）的接入方式，均未找到权威公开说明}。

### 计算机视觉检测与对象化

MSS 的计算机视觉能力有两个来源：NGA Maven 流水线训练和认证的 GEOINT 模型，以及通过开放架构接入的第三方模型。检测结果无论来源，均以对象形式写入平台，而非停留在标有方框的图片上。Palantir 在北约工业日所作演示说明了这一机制：外部 AI 系统 Safran.AI 生成的目标检测导入 MSS 后，既可在共用作战图中直接调查，也可交给 AIP 代理使用；用户以自然语言提问，例如"Show me detections of Tu-22s"（显示图-22 的检测结果），代理随即在由 12,000 个 Safran.AI 检测对象组成的对象集中查询[@mv_palantir_blog_nato,mv_csis]。

我部分析，对象化是理解 MSS 的关键。检测结果成为对象后，可带有类型、置信度、时间、来源模型等属性，可与其他对象建立链接（如某检测对应某已知设施、某车辆隶属某部队），并成为提名目标、分配打击资产等后续工作流动作的作用对象。识别模型因此可以替换：Palantir 掌控对象模型和工作流，模型供应商只需按接口输出检测对象。这种"平台加可插拔模型"的结构，是 MSS 能在 2024 年后迅速吸纳第三方模型、并在 2026 年更换大模型供应商的技术前提。

### 共用作战图（COP）

MSS 提供地图式共用作战图。二手描述称，其 COP 为三维地球视图，叠加卫星、无人机、信号情报和既有地图数据[@mv_spatial]。北约演示中，第三方检测对象可在 COP 中直接调查[@mv_palantir_blog_nato]。COP 是 MSS 各类对象的空间呈现层，检测结果、已知设施、禁打目标、友军打击资产显示在同一张图上，便于目标分析员判断目标与资产之间的距离和关系。

### Target Workbench：看板式目标工作流

MSS 中辨识度最高的模块是 Target Workbench（目标工作台）。Palantir 产品资料称，其界面按 **看板（Kanban）** 形式组织，各列对应目标定位流程的各个阶段，阶段名称可按单位自身流程术语定制，并支持集成 **禁打清单（No-Strike List，NSL）**[@mv_target_workbench]。每个目标是一张卡片，随分析、核查、审批、交战和评估的推进在各列之间流转，指挥员和参谋可直接看到各阶段积压的目标数量以及卡在各环节的目标。

!fig d_maven_workflow|d_maven_workflow.png|Target Workbench 看板式目标工作流（按 F2T2EA 阶段对照）|本报告依据 Palantir Target Workbench 产品说明、CSIS、CSET 资料整理绘制|160

有分析描述了看板的实际运作：检测结果被提名上板，再从看板为目标分派最合适的资产，优化因素包括到达目标时间、燃油、弹药和距离；整条传感器到射手链路可概括为"检测 → 行动方案（COA）→ 资产选择 → 打击 → BDA"（弱源，待核）[@mv_cybershafarat,mv_battlepolicy]。看板的使用不限于 MSS：在陆军下一代指挥控制（NGC2）"常春藤之刺 1"实弹演习（2025 年 9 月）中，第 4 步兵师在 Anduril 的 Lattice 网格上运行 Palantir Target Workbench，用以管理、跟踪每个目标并为其分配资源[@mv_bd_ivysting]。

我部分析，看板式设计具有直接的作战含义。在传统联合目标定位流程（JP 3-60）中，目标从提名到批准须经多级会议和文书；看板把这一流程可视化、并行化，使小团队能够同时处理大量处于不同阶段的目标，这是"20 人顶 2,000 人""每小时 30 个到 80 个"等效率数字背后的机制。并行化同时使单个目标获得的人工关注减少，本章后文关于自动化偏差风险的讨论即由此展开。

### 资产比较与武器—目标配对

CSIS 根据国防部演示描述了一个典型操作流程：操作员选中 AI 检测到的目标，按到达时间、距离、燃油等约束比较附近打击资产，下令打击，再通过情报、监视与侦察（ISR）跟踪打击效果[@mv_csis]。这即是 MSS 的资产比较或武器—目标配对功能。据美国官员称，2026 年伊朗战事中五角大楼依靠 Maven 识别最高优先级目标并协助选择武器[@mv_aca_iran]。

我部分析，从现有描述看，MSS 的武器—目标配对更接近基于时间、距离、燃油、弹药等约束的资产推荐与比较，与传统意义上的武器—目标分配优化算法有别。{red:配对算法的具体实现，以及是否考虑毁伤概率和附带损伤估计，均无权威公开说明}。

### 火力交接：与 AFATDS 等火控系统的衔接

目标排序和资产选择完成后，打击任务须交由实际火力系统执行。有二手分析称，Target Workbench 对目标排序后，将数据传给先进野战炮兵战术数据系统（AFATDS）等火力支援系统（弱源，待核）[@mv_battlepolicy]。分析人士本·范鲁（Ben Van Roo）认为，在"分配并射击"环节，射击诸元由 AFATDS 和弹道计算完成，大模型在这部分几乎不起作用[@mv_vanroo]。据此判断，MSS 不直接控制武器，而是把打击对象和打击手段的决策结果交给现有火控系统。{red:MSS 与 AFATDS、TAK 的官方接口说明均未找到}。

### 毁伤评估（BDA）

在 CSIS 描述的流程中，打击后通过 ISR 跟踪效果，即毁伤评估（BDA）[@mv_csis]。BDA 对应看板最后一列，目标卡片获得评估结果后关闭，或退回前列重新打击。{red:BDA 模块的具体实现未见描述}，例如是否由计算机视觉自动比对打击前后图像、评估结论如何回写目标对象等。

### AIP 大模型代理与 Claude 争议

2023 年起，Palantir 将其人工智能平台（AIP）的大模型代理能力引入防务产品。CSIS 特别提示，Palantir 2023 年的"AIP for Defense"演示展示的是计划中的能力和示意场景，不等同于已部署功能[@mv_csis]。已证实的情况是：北约演示中，AIP 代理可用自然语言检索检测对象集[@mv_palantir_blog_nato]；北约也明确称 MSS NATO 包含大语言模型和生成式 AI[@mv_shape_release]。

大模型在美军 MSS 中的具体作用，各方报道分歧较大。多家媒体报道，Anthropic 的 Claude 经 Anthropic 与 Palantir 的合作，于 2024 年末接入 Maven，用于目标优先级排序和分析[@mv_rs_iran,mv_aca_iran]。《华盛顿邮报》2026 年 3 月 4 日报道，对伊朗作战中内嵌 Claude 的 MSS 为目标排序、生成坐标并建议武器[@mv_wapo_2026]；二手转述还称其生成法律依据草稿[@mv_wapo_2026]，以及"Claude 提出了数百个目标，进行优先排序并给出精确坐标，再由人类指挥官批准"（转述华邮和《自然》）[@mv_strat_intl]。"和平愿景"（Vision of Humanity）的说法则审慎得多，称 Claude 主要用于把情报报告转写为通俗语言[@mv_voh]。

Claude 的现状同样说法不一。据报道，国防部于 2026 年 3 月 4 日将 Anthropic 列为"供应链风险"，要求 6 个月内淘汰，起因是 Anthropic 拒绝将模型用于大规模国内监控和完全自主武器，OpenAI 等公司据报接替其角色；Palantir 首席执行官卡普则在 CNBC 上称 Claude 仍在目标系统中运行[@mv_aca_iran,mv_ie_claude]。另有说法提及 2026 年 2 月 28 日的行政令要求六个月内完成过渡[@mv_ie_claude]。倡导团体 Capture Cascade 在 MSS 转正式项目的条目标题中直接写有"Claude 依赖"（弱源，待核）[@mv_capture]。{red:Claude 在 MSS 中的具体角色、是否已被替换、由谁接替，均无法从五角大楼或 Anthropic 的一手文件中证实}。

我部研判，无论 Claude 具体承担何种角色，以下两点可以确认。第一，MSS 的大模型层可以替换，这与"平台加可插拔模型"的架构一致。第二，大模型在 MSS 中的作用集中于检索、摘要、排序、生成草案等信息整理环节，在射击诸元解算环节几乎不起作用。战事期间按 token 计的使用量激增（日峰值增长 4,425%，最高约 200 亿 token/天，见本章第四节），表明大模型已深度嵌入日常参谋工作[@mv_bd_insatiable]。

### NGA 机器生成情报标注与"推理"能力

NGA Maven 一侧的功能重点是 AI 情报产品的生产与治理。NGA 局长惠特沃斯 2025 年 6 月称，NGA 在所有 AI 生成的产品上加注"machine-generated GEOINT"（机器生成的地理空间情报）模板标签，此类模板化产品在分发过程中"没有人工经手"（no human hands）；标签注明 AI 参与的类型和程度，NGA 可能是情报界 18 个成员中首个常规使用此类标签的机构[@mv_bd_nohands]。惠特沃斯还表示，Maven 下一阶段将加入"推理"能力，从识别物体发展到预测和发现威胁，但向作战司令或总统汇报前仍须有人工佐证[@mv_meritalk_nga,mv_execgov_predict]。

我部分析，机器生成标签是目前公开可见的、为数不多的针对 AI 情报产品的制度化治理措施。它把 AI 参与程度作为产品元数据随情报流转，下游用户可据此调整信任程度。该措施主要适用于 NGA 的 GEOINT 产品；MSS 目标卡片上的 AI 贡献是否有类似标注，未见公开信息。

### 非作战扩展：五角大楼的"万能应用"

2026 年，MSS 的应用范围已明显超出目标定位。CDAO 斯坦利称，MSS 正扩展至后勤、供应链、战备和预算数据[@mv_ds_mazol]。《国防一号》称 Maven 正在成为五角大楼的"万能应用"，据 CDAO 称已取代"6、8、10 个"旧系统[@mv_d1_everything]。陆军联合兵种司令部已把"Maven C2 智能系统"纳入训练和院校教育[@mv_army_cac]，国民警卫局也在推广范围之内[@mv_ds_mazol]。

!photo mss_contracting|萨姆休斯顿堡合同人员在作战演习中使用 AI 与 Maven 智能系统开展仿真。MSS 的使用者已从目标分析员扩展至后勤、合同等保障领域|美国陆军，公有领域

我部分析，MSS 从目标定位扩展到全部门业务，与 Palantir 平台的通用性直接相关：本体既可描述目标和打击资产，也可描述零备件、预算科目和战备状态。对国防部而言，一个平台同时承载作战与管理数据，可降低跨领域关联分析的门槛；对供应商而言，锁定范围也由作战领域延伸至整个部门的业务系统。

### 跨梯队与联盟协同

MSS 用户覆盖作战司令部、军种和联盟各层级。2025 年 5 月，NGA 称 Maven 通过 35 个以上军种和作战司令部工具、跨三个安全域服务约 2 万名活跃用户[@mv_bd_geoint2025]。联盟层面，MSS NATO 部署于 SHAPE 和布林森联合部队司令部，诺福克联合部队司令部随后接入[@mv_janes_norfolk]。乌克兰是美方目标情报的接收方，并非 MSS 的直接用户；据《纽约时报》报道，乌方使用的是不依赖美国敏感情报的版本[@mv_kyivind]。{red:MSS 的联盟可释放性（releasability）机制，即按标签控制哪些数据可共享给哪些盟友，未找到公开细节}。

### 功能模块拆解

!table t_mv_modules|MSS / NGA Maven 功能模块拆解|本报告据北约、CSIS、Palantir 资料及媒体报道整理|26,74,30,30
模块|功能描述|证据等级|主要来源
多源情报融合|CENTCOM 2024 年部署接入 179 个数据源（另有 150 个以上说法），含国家侦察卫星、ICEYE/Capella 商业 SAR、信号情报|智库；二手|[@mv_csis,mv_globalsec]
CV 检测与对象化|外部模型检测结果作为对象写入平台；北约演示中由 12,000 个 Safran.AI 检测对象组成对象集|厂商|[@mv_palantir_blog_nato]
共用作战图（COP）|地图式 COP，据称为三维地球视图，叠加卫星、无人机、SIGINT 与地图数据|二手|[@mv_spatial]
Target Workbench|看板式界面，各列对应目标定位阶段，阶段名可定制；集成禁打清单|厂商|[@mv_target_workbench]
资产比较与配对|按到达时间、距离、燃油等约束比较附近打击资产并下令打击|智库（据国防部演示）|[@mv_csis]
火力交接|排序后的目标交 AFATDS 等火力系统；射击诸元由 AFATDS 解算|二手；分析人士|[@mv_battlepolicy,mv_vanroo]
毁伤评估（BDA）|通过 ISR 跟踪打击效果；无模块级细节|智库|[@mv_csis]
AIP 大模型代理|自然语言检索、排序、COA 草案；Claude 角色存在争议|厂商；多源说法不一|[@mv_palantir_blog_nato,mv_wapo_2026,mv_voh]
机器生成情报标注|NGA 产品加注 machine-generated GEOINT 标签，注明 AI 参与程度|官方|[@mv_bd_nohands]
推理与威胁预测|从识别物体发展到预测威胁；汇报前须人工佐证|官方（规划）|[@mv_meritalk_nga]
非作战扩展|后勤、供应链、战备、预算；取代 6—10 个旧系统|官员|[@mv_d1_everything,mv_ds_mazol]
联盟协同|MSS NATO 在北约机密网络运行；乌克兰为情报接收方|官方；媒体|[@mv_shape_foc,mv_kyivind]
!end

### 与 F2T2EA 杀伤链对照

美军通用的动态目标定位流程为"发现—定位—跟踪—瞄准—交战—评估"（F2T2EA）六步。将 MSS 已知功能逐一对照，可见其覆盖了杀伤链从发现到评估的全部环节，但各环节的自动化程度和证据充分程度差别很大（见{tab:t_mv_f2t2ea}）。

!table t_mv_f2t2ea|MSS 功能与 F2T2EA 杀伤链对照|本报告分析整理，各环节证据见所列来源|20,52,40,48
F2T2EA 环节|MSS 对应功能|自动化程度（分析）|证据情况
发现（Find）|179 个以上数据源融合；CV 模型自动检测并对象化|高：检测由机器完成|智库与厂商资料较充分[@mv_csis,mv_palantir_blog_nato]
定位（Fix）|地理定位、生成坐标；据报 Claude 生成精确坐标|中高：机器给出坐标，人工核对|坐标生成见于媒体报道，存在争议[@mv_wapo_2026,mv_strat_intl]
跟踪（Track）|COP 持续显示目标与活动；无人机位置与视频回传|中：依赖传感器持续覆盖|仅有二手描述[@mv_spatial]
瞄准（Target）|看板上的目标核查、禁打清单比对、优先级排序；人工逐一批准|中：机器排序，人工审批|厂商资料与一线访谈[@mv_target_workbench,mv_bloomberg_2024]
交战（Engage）|按时间、距离、燃油比较打击资产；交 AFATDS 等火控系统|低到中：推荐资产，射击诸元由火控系统解算|智库与二手资料[@mv_csis,mv_vanroo]
评估（Assess）|ISR 跟踪打击效果，目标卡片关闭或回流|未知|无模块级细节[@mv_csis]
!end

我部分析，对照表显示，MSS 的自动化重心在杀伤链前段（发现、定位）和中段的组织与排序，交战环节仍依靠现有火控系统，评估环节公开信息最少。MSS 压缩的主要是人工搜索目标、排列目标和比较资产的时间，武器飞行和毁伤所需时间基本不受影响，因此其效率指标多以"每小时批准多少目标""多少人完成多少工作"来表述。

### 功能层面的公开空白

以下功能未找到权威公开描述：全动态视频的接入方式；友军跟踪的接入方式；BDA 模块实现；COA 生成算法；武器—目标配对算法；联盟可释放性与标签化数据访问控制机制；MSS 与 TAK、AFATDS 的官方接口[@mv_csis]。CSET 在报告中明确表示不公开 MSS 的具体作战细节[@mv_cset_coalition]。本节对上述模块的描述，均应视为"已知存在、细节不明"。

## （三）架构设计：本体驱动的平台、NGA 模型流水线与三个安全域

:::lead
MSS 的架构可概括为"Palantir 平台加可插拔的模型与数据"。Palantir 掌控数据集成、本体与工作流应用；NGA 掌控模型的标注、训练与认证；计算机视觉、商业 SAR 和大模型等第三方供应商可以替换；国防部通过 CDAO 项目办公室和陆军企业协议实施治理。本节按七层逐层拆解，并简要对比 Palantir 本体与 Anduril Lattice 实体模型的差异。公开资料足以勾勒架构层次，但 MSS 采用 Foundry 与 Gotham 的何种组合、托管于哪家云、是否存在绝密网络实例等关键细节均未得到证实。
:::

!fig d_maven_arch|d_maven_arch.png|Maven / MSS 七层架构|本报告依据 Palantir 官方文档、NGA 合同公告、CSIS、DefenseScoop、SHAPE 等资料整理绘制|160

如图 {fig:d_maven_arch} 所示，本报告将 Maven/MSS 划分为七层：数据源层、NGA Maven 模型流水线、Palantir 平台层、工作流应用层、AIP/大模型代理层、部署与安全域层、治理与合同层。前五层为技术栈，后两层为运行环境与制度框架。该分层是本报告依据公开资料所作的归纳，并非官方架构文件。

### 第一层：数据源

数据源层是 MSS 的输入端。已知来源包括国家侦察卫星和 ICEYE、Capella Space 等商业 SAR 卫星，截获通信、电子辐射等信号情报，无人机及其全动态视频，以及既有数据库和地图数据；CENTCOM 2024 年部署时共接入 179 个数据源[@mv_csis]。北约版本同样强调接入涉密与公开、结构化与非结构化的多源数据[@mv_shape_release]。

数据源层也是 MSS 的主要风险来源之一。2026 年 Minab 学校遇袭事件表明，平台不会自动发现底层数据库中的过期记录：该地点在旧数据库中仍标为伊斯兰革命卫队设施，输入 Maven 后被列为推荐目标（详见本章第五节）[@mv_bloomberg_minab]。Palantir 事后表示自己"不对底层数据负责"[@mv_gizmodo_minab]。我部分析，在 MSS 架构中，数据质量责任仍分散于各情报来源单位，平台只负责汇聚和呈现，二者之间缺少系统性的数据时效核验机制。

### 第二层：NGA Maven 模型流水线

2022 年拆分后，整个 Maven"AI 开发流水线"交由 NGA 管理[@mv_ds_2024_03]。该流水线包括数据标注、系统集成与模型互操作、模型评估认证三个环节。

**数据标注**是计算机视觉模型的基础。2024 年 7 月 29 日，NGA 授予 Scale AI 约 2,400 万美元、为期一年的固定价格合同"NGA Maven 数据标注服务过渡"（合同号 HM047624C0047）；NGA 另一条公告写作"修改 2,400 万美元后总值 1.3 亿美元"，两者关系不明[@mv_nga_contracts]。2024 年 9 月，NGA 宣布约 7 亿美元的数据标注竞标，同时推动标准化建模[@mv_bd_2024_09_label,mv_d1_2024_09]。2025 年 11 月，初创公司 Enabled Intelligence 赢得名为 SEQUOIA 的"AI/ML 数据标注即服务"合同，该合同为单一授标 IDIQ，上限 7.08 亿美元，订货期最长 7 年，用于 GEOINT 计算机视觉的目标检测、跟踪和分类标注，合作方包括 BAE、Vantor 和 Whiteboard Federal；这是美国政府迄今规模最大的 AI 数据标注项目，也是 Maven 的基础能力[@mv_bd_sequoia,mv_ei_release]。落标的 Scale AI 先向 GAO 提出抗议，于 2026 年 1 月下旬被驳回，后起诉至联邦索赔法院，法院未推翻授标[@mv_orangeslices]。

**系统集成与模型互操作**由 ECS 承担。ECS 自 2017 年起担任 NGA Maven 项目的 AI 互操作集成商（AI3）[@mv_execbiz_ecs]。

**模型评估认证**由 NGA 的 AGAIM 试点（GEOINT AI 模型认证/评估）承担，提供一套标准的评估和风险管理流程。NGA 官方明确表示，不希望 AGAIM 变成"运行授权（ATO）式"的排队审批[@mv_fnn_agaim]。


我部分析，模型流水线归 NGA、作战平台归 CDAO 和 Palantir，形成了"模型由政府掌握、平台由商业公司提供"的分工。其好处是政府对训练数据和模型评估保有控制权，不完全依赖单一平台厂商；代价是两条线之间需要稳定的接口（检测对象写入本体），两个机构之间也存在协调成本。2026 年 MSS 管理权由 NGA 移交 CDAO 后，NGA 仍保留模型流水线，这一分工未变。

### 第三层：Palantir 平台（Apollo、Ontology、Foundry、Gotham、AIP）

平台层是 MSS 的核心，由 Palantir 的多个产品构成。

**Apollo** 是持续交付平台，负责管理承载 Foundry 和 AIP 服务的底层基础设施[@mv_palantir_platforms,mv_apollo_wp]。二手资料称，Apollo 可运行于本地数据中心、边缘硬件和涉密网络[@mv_mlq]。对军事用户而言，Apollo 可使同一套软件在非密云、秘密网、北约网络等多个隔离环境中保持版本一致并持续更新，无须为每个环境单独开发和认证。

**Ontology（本体）** 把数据源映射为对象、属性和链接，并对动作（action）建模，支持把决策实时写回业务系统和边缘系统；边缘端可用轻量的嵌入式本体（Embedded Ontology）记录决策，平台也能接入物联网和边缘数据流[@mv_palantir_ontology,mv_palantir_ontology_system]。在 MSS 中，检测结果、设施、目标、打击资产、禁打对象均可作为本体对象，提名目标、批准打击、分配资产则是作用于对象的动作。

**Foundry、Gotham 与 AIP** 分别是 Palantir 的数据集成与分析平台、情报与防务平台、人工智能平台。{red:MSS 具体采用 Foundry 与 Gotham 的何种组合，公开资料未证实}。本报告的分层推断是：数据和本体层在 Foundry/Gotham 中把传感器数据和检测结果转为对象，AIP 提供大模型代理[@mv_csis]。Palantir 在 Maven 之外长期为陆军提供情报数据平台，DCGS-A 第二能力包（2021 年中标建设基于 Gotham 的跨密级情报数据织网）和 2024 年 TITAN 地面站原型（1.784 亿美元）均处于"情报到目标"链条上，与 MSS 相衔接[@mv_bd_dcgsa,mv_ds_titan]。

### 第四层：工作流应用

工作流应用层是用户直接操作的界面，包括 COP 地图、Target Workbench 看板、资产比较与配对、BDA 跟踪等（见本章第二节）。该层对外开放：CDAO 于 2024 年启动 Open DAGIR 计划，旨在把其他厂商的应用接入 MSS 数据层，使 CJADC2 不必全部依赖 Palantir 自有应用[@mv_bd_opendagir]。Breaking Defense 还指出，2024 年公布的 CJADC2 最小可行能力属于"最低限度"[@mv_bd_opendagir]。

我部分析，Open DAGIR 是国防部针对平台锁定的制度回应，数据层由 Palantir 提供，应用层向第三方开放。第三方应用读写的仍是 Palantir 本体，平台层锁定并未消除。

### 第五层：AIP / 大模型代理

AIP 层提供自然语言检索与问答、目标排序、行动方案草案和报告生成等能力[@mv_palantir_blog_nato,mv_csis]。该层模型供应商可以替换：据报道，Claude 自 2024 年末接入，2026 年起因供应链风险认定被要求淘汰，OpenAI 等公司据报接替[@mv_aca_iran]。我部分析，从架构看，大模型不直接操作武器，而是作用于本体中的对象与动作：它可以查询对象集、生成排序和草案，批准打击等动作仍须由人在界面上执行。该层的主要风险在于生成内容的可追溯性，排序依据、坐标来源、法律依据草稿能否审计，公开资料没有说明。

### 第六层：部署与安全域

NGA 称 Maven 跨"三个安全域"运行[@mv_bd_geoint2025]。原文未说明具体网络，推测为非密、秘密和绝密/敏感隔离信息（TS/SCI）三级，{red:但无公开来源证实 MSS 在联合全球情报通信系统（JWICS）上部署有实例}。可确认的部署形态有两种：一是海军陆战队通过企业许可，在 SIPRNet 影响等级 6（IL6）云上"无限量访问"MSS[@mv_ds_maradmin,mv_usmc_release]；二是 MSS NATO 在北约机密网络上运行，数据存放于北约自有数据中心[@mv_shape_foc]。伊朗战事期间，五角大楼发言人称非密网使用量环比增长 38%、涉密网增长 89%，亦可印证 MSS 同时运行于不同密级的网络[@mv_bd_insatiable]。

{red:MSS 托管于哪家商业云（AWS、微软、甲骨文、谷歌）、是否经由联合作战云能力（JWCC）合同，均无公开信息}。Feinberg 备忘录提到 USD(R&E) 将接任 MSS"商业云基础设施"的授权官，说明 MSS 至少部分运行于商业云[@mv_ds_feinberg2]。MSS 在前沿战术节点和断连条件下的边缘部署，也未找到权威公开描述。

### 第七层：治理与合同

治理层决定系统的归属、经费来源和运行授权。截至 2026 年 10 月，MSS 的治理框架为：CDAO 新设的 MSS 项目办公室负责系统管理与监督，项目主任为索尔斯伯里上校，CDAO 隶属 USD(R&E)[@mv_ds_solsbury,mv_aimil_solsbury]；全部合同经由陆军企业协议执行[@mv_ds_feinberg1]；USD(R&E) 担任商业云授权官[@mv_ds_feinberg2]；首席技术官评估是否将 MSS 纳入拟设的 CJADC2 项目办公室[@mv_ds_feinberg1]。北约一侧由 NCIA 采办、SHAPE 运行 MSS NATO[@mv_ncia_2025]。NGA 保留 NGA Maven 模型流水线和 GEOINT 产品治理职能（机器生成标签、AGAIM）[@mv_bd_nohands,mv_fnn_agaim]。

!table t_mv_layers|Maven / MSS 七层架构要点|本报告据各层所列来源整理|28,82,50
层级|组成与机制|主要证据
① 数据源|国家与商业卫星（含 ICEYE、Capella SAR）、无人机 FMV、SIGINT、既有数据库；CENTCOM 2024 年接入 179 个数据源|[@mv_csis]
② NGA Maven 模型流水线|标注：Scale AI 过渡合同 → Enabled Intelligence SEQUOIA（上限 7.08 亿美元）；集成：ECS（AI3）；认证：AGAIM|[@mv_nga_contracts,mv_bd_sequoia,mv_execbiz_ecs,mv_fnn_agaim]
③ Palantir 平台|Apollo 持续交付；Ontology 对象—属性—链接—动作，可回写；Foundry/Gotham/AIP（具体组合未证实）|[@mv_palantir_platforms,mv_palantir_ontology]
④ 工作流应用|COP、Target Workbench、资产比较、BDA 跟踪；Open DAGIR 第三方应用|[@mv_target_workbench,mv_bd_opendagir]
⑤ AIP/大模型代理|自然语言检索、排序、COA 草案；Claude（有争议）→ OpenAI 等（据报）|[@mv_palantir_blog_nato,mv_aca_iran]
⑥ 部署与安全域|3 个安全域（NGA 口径）；陆战队 SIPRNet IL6 云；北约机密网与自有数据中心；云厂商未公开|[@mv_bd_geoint2025,mv_ds_maradmin,mv_shape_foc]
⑦ 治理与合同|CDAO MSS 项目办公室；陆军 EA；USD(R&E) 任授权官；北约 NCIA/SHAPE|[@mv_ds_feinberg1,mv_ds_feinberg2,mv_ncia_2025]
!end

### MSS 在 CJADC2 体系中的位置

在体系层面，MSS 是美军联合全域指挥控制（CJADC2）的事实骨干。时任国防部常务副部长希克斯曾要求 CDAO 在 2023 年底前通过"全球信息主导实验"（GIDE）交付 CJADC2 最小可行能力；该能力于 2023 年 12 月获认证、2024 年 2 月公布，重点是 11 个作战司令部之间的信息共享，应用包括联合火力网和一个"全球集成"工具[@mv_ds_mvp_2023,mv_ds_cjadc2_mvc,mv_nextgov_mvc]。此后 CDAO 推动 GIDE 吸纳更多工业界参与者，构建全球作战网络[@mv_bd_gide]。Breaking Defense 在 2024 年末的盘点中，将 CJADC2 与军事 AI 的进展概括为"安静的进步"[@mv_bd_killerapps]。

2026 年 Feinberg 备忘录把"AI 赋能决策"定为 CJADC2 的基石，并要求评估将 MSS 纳入拟设的 CJADC2 项目办公室[@mv_ds_feinberg1]；FY2027 预算将"Maven 智能系统与联合火力网"作为交付 CJADC2 的预算项列出[@mv_fy27_book]。我部研判，在联合层级，MSS 承担数据与决策平台角色，联合火力网承担火力协调角色，二者共同构成 CJADC2 的作战核心。{red:目前没有任何来源把 MSS 与"金穹"导弹防御直接挂钩}；有关"金穹"的报道仅提到 Anduril 与 Palantir 共同开发其指挥控制软件层[@mv_reuters_goldendome]。

### Palantir 本体与 Lattice 实体模型的差异

Palantir 与 Anduril 在陆军 NGC2 等项目中深度合作，两家的数据模型常被对照讨论。Palantir 本体以"对象—属性—链接—动作"为核心，面向企业级、长周期的数据整合和决策回写[@mv_palantir_ontology]。Lattice 以实体为核心，每个航迹、资产、地理区域和信号都是一个实体，其全部数据由位置、运动学、军事视图（敌我属性）、本体模板、来源（provenance）、密级标记等可选的类型化组件承载；实体之上，再通过任务对可受领任务的资产下达指令[@mv_lattice_entity]。

!table t_mv_onto_vs_entity|Palantir 本体与 Lattice 实体模型对比|本报告依据 Palantir Ontology 文档与 Lattice SDK 公开 schema 分析整理|30,65,65
维度|Palantir 本体（MSS）|Lattice 实体（Anduril）
基本单元|对象（object），带属性与链接|实体（entity），由类型化组件构成
行为建模|动作（action），可写回业务系统与边缘系统|任务（task），下达给可受领任务的资产
设计重心|企业级数据整合、长周期分析与决策流程|实时航迹、传感器与效应器控制
典型层级|作战司令部、军种、联盟|战术边缘、师级以下网格节点
在 NGC2 中的角色|Foundry 数据平台与 Target Workbench 目标应用|Lattice Mesh 边缘数据网格与实体层
互相映射|无公开文档|无公开文档
!end

在 NGC2 中，Lattice 担任战术边缘网格、数据传输和实体层，Palantir 担任企业数据平台（Foundry）和目标与决策应用（Target Workbench）[@mv_bd_ivysting,mv_ds_anduril_palantir]。2024 年 12 月两家宣布合作时，设想由 Lattice 和 Menace 采集、传输边缘数据，导入 Palantir AIP 用于 AI 训练准备，并与 MSS 结合，形成从边缘到企业的链路[@mv_ds_anduril_palantir,mv_pltr_ir_anduril]。有分析将二者分工概括为：MSS 处理历史和近实时情报、形成目标包，Lattice 以机器速度实时执行目标包、协调传感器和效应器[@mv_faf]。{red:实体与对象之间如何转换、两套模型如何保持一致，没有任何公开文档}，这是两系统集成中最需关注的技术空白（两系统的比较详见第五章）。

## （四）能力评估：已证实省人、提速，未证实更准

:::lead
有关 MSS 能力的公开数字较多，但分属吞吐、人力、准确率、时延、战役总量、用户规模等不同口径，不能直接相互比较。经多源证实的是，MSS 能以很少的人力支撑很高的目标处理吞吐，并已扩展至全军和北约。目标识别准确率没有证据显示优于人类，测试数据反而明显偏低。"每小时 1,000 个决策""从数天压缩到数秒"等属于愿景或官方声称。我部研判，主要风险来自数据过期、自动化偏差和人工审查密度下降，模型本身的识别错误居于次要位置。
:::

### 速度与吞吐：从每小时 30 个到 80 个

彭博社 2024 年长篇报道援引 XVIII 空降军资深目标官 Temple 的估计：借助 Maven，他每小时可签批多达 **80 个目标**，不用 Maven 时约 **30 个**；他同时表示，完全信任机器会更快，但会引入错误[@mv_bloomberg_2024,mv_techmeme]。这是目前引用最多的人机协同吞吐数字。该数字是一名目标官的个人估计，衡量的是审批环节速度，不代表从发现到打击的全流程。

时延方面，二手报道称在"猩红之龙"演习中，数据传输加打击的时间从 **12 小时以上缩短到 1 分钟以内**（二手）[@mv_armyrec]。NGA 局长惠特沃斯 2025 年也提到，某目标单元在一次演习中把时间线从数小时缩短到数分钟[@mv_bd_geoint2025]。2026 年 5 月，CDAO 斯坦利在国会书面证词中称，MSS 把目标周期"从数天压缩到数秒"[@mv_stanley_testimony]。我部分析，"数秒"是官方在申请预算和推动转正式项目背景下的表述，未公开方法说明，应视为官方声称。

### 人力：约 20 人顶 2,000 人

CSET 与 CSIS 均引用了一组对比：XVIII 空降军借助 MSS，以约 **20 人**的目标单元达到了 2003 年伊拉克战争（OIF）时一个 **2,000 余人**时敏目标单元的效能，后者被视为美军史上效率最高的目标单元[@mv_cset_coalition,mv_csis]。这是 MSS 节省人力最有力的公开证据，也是其支持者最常引用的数字。我部分析，该对比来自演习而非实战，两者面对的目标数量、情报环境、通信条件均不相同，只能作为数量级参考，不宜视为严格的效能比。

### 愿景：每小时 1,000 个高质量决策

陆军为 MSS 设定的远期目标是使一个单位"每小时做出 **1,000 个高质量决策**"，即选择或剔除目标[@mv_bd_geoint2025]。CSET 同样将其表述为最终目标：系统与士兵协助指挥官每小时处理 1,000 个战术决策[@mv_cset_coalition]。Army Recognition 以"每小时 1,000 个目标"为题报道了这一设想[@mv_armyrec]。{red:这是愿景指标，并非实测结果}。

### 战役总量：伊朗 38 天 13,000 个目标

2026 年对伊朗的"史诗怒火"行动，提供了 MSS 首个大规模实战总量数据。按时间顺序，已知口径包括：《华盛顿邮报》称头 24 小时打击约 1,000 个目标[@mv_wapo_2026,mv_rs_iran]；中央司令部 3 月 3 日称已打击近 2,000 个目标[@mv_defind_13000]；维基百科条目称 10 天约 5,000 个目标（二手）[@mv_wiki_aiwarfare]；白宫 4 月 8 日统计称其中指挥控制目标逾 2,000 个、防空目标 1,500 个[@mv_defind_13000]；CDAO 斯坦利称 38 天打击 13,000 个目标[@mv_ds_mazol,mv_stanley_testimony]。

【口径提醒】13,000 个是打击目标总数，既不等于 Maven 独立识别的目标数，也不代表命中率或准确率；MSS 在其中的贡献比例未公开。仅见于低可信站点的"每天 3,000 个目标""11,000 次以上打击""25,000 个以上账户"等说法，本报告不予采信（弱源，待核）[@mv_arturmarkus]；"86 秒完成决策"等说法同样未经证实[@mv_aca_iran]。

### 准确率：60% 对 84%，恶劣条件下低于 30%

与效率数字相比，准确率数据既少且不利。彭博社援引 XVIII 空降军军官的说法：测试中 Maven 识别物体的正确率约 **60%**，与 XVIII 空降军合作的人类分析员约 **84%**；遇到某些物体或雪天图像时，Maven 的正确率"可能低于 30%"[@mv_bloomberg_2024,mv_batch]。Airwars 报道称，在西伊拉克等天气多变的沙漠地形中，准确率可降至 30% 以下[@mv_airwars_first]。二手转述常将这组数字写作"雪天 30%"或"识别坦克 60%"。

另有两组数字流传较广但无法溯源：一是 Maven 在乌克兰"每平方公里约 10 个错误检测"，二是准确率"从 70% 降到 30%，有时 10%"（据称出自曼森）。{red:两者均未找到原始出处，不建议引用}（弱源，待核）[@mv_douwe,mv_escudo_failing]。

我部分析，60%/84% 是 2023—2024 年单项物体识别测试的结果，早于加入大模型的 2026 版本，不能直接套用于"史诗怒火"行动；2026 版本未公开任何准确率或误报率数据，AGAIM 评估结果也无公开数据。"30 → 80 个/小时"衡量人机协同的审批吞吐，"60% 对 84%"衡量机器单独识别的正确率，二者并不矛盾：MSS 的价值主要来自流程组织和人力节省，与检测精度关系不大。

### 规模：用户从 2 万到 10 万以上

用户规模的增长轨迹为：2024 年 5 月合同扩展至 5 个作战司令部的"数千用户"[@mv_ds_2024_05]；2025 年 5 月活跃用户逾 2 万，覆盖 35 个以上工具、3 个安全域[@mv_bd_geoint2025]；2026 年 1 月约 5 万；2026 年 9 月超过 10 万[@mv_ds_mazol]。我部分析，约 16 个月内用户增长约 5 倍，主要推动因素是伊朗战事以及向全部作战司令部和国民警卫局的推广。

伊朗战事期间的使用强度同样大幅上升。五角大楼发言人称，非密网使用量环比增长 38%，涉密网增长 89%；按 token 计的日峰值增长 4,425%，最高约 200 亿 token/天[@mv_bd_insatiable]。Breaking Defense 引用 CDAO 的说法，称军方对 AI 的需求"贪得无厌"[@mv_bd_insatiable]。

### 可靠性与风险

**数据投毒。** Maven 的数据投毒风险早已受到关注[@mv_techmeme]。MSS 汇聚上百个数据源，任一来源遭篡改或污染，都可能经本体关联传导至目标列表。CSET 明确表示不公开 MSS 的具体作战细节[@mv_cset_coalition]。2023 年，NGA 就 Maven 的 AI/ML 供应链风险发布征询，理由是对下级供应商缺乏可见度[@mv_bd_supplychain_2023]。

**自动化偏差。** 高吞吐的人机协同天然存在人类仅作背书的风险。目标官 Temple 本人即指出，完全信任机器会引入错误[@mv_bloomberg_2024]。批评者认为，MSS 已从决策支持系统变为"附带人类副署以满足法律合规的决策系统"[@mv_strat_intl]；也有文章讨论"橡皮图章问题"，即 AI 的速度超出了其所承诺的监督能力[@mv_medium_rubber]。中央司令部司令则表示，最终打击决定由人作出[@mv_letsdata]。

**Minab 学校事件。** 2026 年 2 月 28 日"史诗怒火"行动首日，伊朗 Minab 一所学校遭打击。据彭博社引述五角大楼内部调查，该地点在旧数据库中仍标为伊斯兰革命卫队设施，输入 Maven 后被列为"第一天推荐目标"；部分用户以为 Maven 会发现过期记录；中央司令部平民伤害评估团队已从约 10 人缩减至 1 人[@mv_bloomberg_minab,mv_gizmodo_minab]。我部分析，这是 AI 辅助目标定位中数据过期与自动化偏差叠加的最具体公开案例：模型并未识别出错，平台如实呈现了一条过期记录，人工未加核查。案例详情与各方说法见本章第五节。

**透明度与问责。** 国防部指令 DoDD 3000.09（2012 年发布，2023 年 1 月更新）要求自主和半自主武器系统的设计使指挥官和操作员能对武力使用施加"适当程度的人类判断"，正式开发前须经高级官员审查[@mv_gao_22,mv_dodd3000]。我部分析，MSS 本身不发射武器，更接近目标选择支持系统，3000.09 的高级审查未必直接适用，问责主要依赖交战规则、联合目标定位流程（JP 3-60）中的人工签批和法律审查。{red:未找到针对 MSS 的正式"负责任 AI"评估或 3000.09 审查记录，也未找到 GAO 或国防部监察长针对 MSS 的独立评估}。Maven 预算属机密，不适用 FOIA[@mv_lawfare_book]。

### 商业侧指标：Palantir 美国政府收入

MSS 的规模化也反映在 Palantir 的财务数据上。据公司披露，Palantir 美国政府收入 2022 年为 8.263 亿美元，2023 年为 9.212 亿美元，2024 年约 12 亿美元，2025 年为 18.55 亿美元（同比增长 55%），2026 年上半年约 14.96 亿美元（一季度 6.87 亿、二季度 8.09 亿，同比分别增长 84% 和 90%）[@mv_pltr_10k_2023,mv_pltr_10k_2024,mv_pltr_q4_2025,mv_pltr_q2_8k]。2026 年二季度公司总营收约 19.4 亿美元，同比增长 93%[@mv_cnbc_q2]。

!table t_mv_revenue|Palantir 美国政府收入（2022—2026H1）|Palantir 10-K、季度新闻稿；与 MSS 的对应关系为相关性分析|26,40,94
年份|美国政府收入|同期与 Maven 相关的事件
2022|8.263 亿美元|Maven 拆分，MSS 原型面向有限操作员[@mv_pltr_10k_2023]
2023|9.212 亿美元|NGA Maven 转正式项目；CJADC2 最小可行能力获认证[@mv_pltr_10k_2023]
2024|约 12 亿美元|4.8 亿美元 MSS 原型合同；ARL 军种扩展合同[@mv_pltr_10k_2024]
2025|18.55 亿美元（+55%）|MSS 上限增至约 13 亿美元；陆军 EA；陆战队许可；北约采购[@mv_pltr_q4_2025]
2026 上半年|约 14.96 亿美元（+84%/+90%）|"史诗怒火"行动；Feinberg 备忘录；用户突破 10 万[@mv_pltr_q2_8k]
!end

我部分析，时间上的吻合不等于因果关系，Palantir 未单独披露 MSS 收入。有分析师认为 MSS 正"冲刺"10 亿美元年化经常性收入，另有报道称 Maven 年化经常性收入接近 10 亿美元，两种说法均只有单一来源，可信度低（弱源，待核）[@mv_bitget,mv_simplywall]。

### 能力评估总表

!table t_mv_capability|MSS 能力评估：已证实、官方声称与存疑|本报告综合 Bloomberg、CSET、CSIS、DefenseScoop、Breaking Defense 等整理|24,46,46,44
维度|已证实（多源/官方）|官方声称或愿景|存疑或反证
目标处理吞吐|一名目标官估计每小时 30 → 80 个目标[@mv_bloomberg_2024]|每小时 1,000 个高质量决策（愿景）[@mv_bd_geoint2025]|"完全信任机器会引入错误"
人力节省|约 20 人达到 OIF 时 2,000 余人目标单元的效能[@mv_cset_coalition]|—|演习对比，非实战；条件不同
时延|演习中从数小时缩短到数分钟[@mv_bd_geoint2025]|"从数天到数秒"[@mv_stanley_testimony]；12 小时以上 → 1 分钟以内（二手）[@mv_armyrec]|无方法说明
战役规模|38 天打击 13,000 个目标（官方总量）[@mv_ds_mazol]|头 24 小时约 1,000 个（媒体）[@mv_wapo_2026]|统计的是打击目标，非 Maven 识别量；"每天 3,000 个"等不予采信
识别准确率|测试中约 60%，人类约 84%[@mv_bloomberg_2024]|2026 版无公开数据|恶劣天气、雪天低于 30%[@mv_airwars_first]；"每平方公里 10 个误检"无出处
用户规模|2 万以上（2025-05）→ 约 5 万（2026-01）→ 10 万以上（2026-09）[@mv_bd_geoint2025,mv_ds_mazol]|推广至全部作战司令部和国民警卫局|注册与活跃口径不一[@mv_govly]
使用强度|涉密网使用量增长 89%；日峰值约 200 亿 token[@mv_bd_insatiable]|—|无独立审计
联盟能力|北约 MSS NATO 达到 FOC[@mv_shape_foc]|—|乌克兰效果"好坏参半"[@mv_kyivind]
人在回路|CENTCOM 称每一步均以人工验证结束[@mv_register_2024]|定位为决策支持|Minab 事件；"橡皮图章"批评[@mv_bloomberg_minab,mv_strat_intl]
!end

【综合判断】**MSS 经多源证实的核心能力，是多源情报融合和目标工作流管理，以及由此实现的以少量人力支撑大规模目标吞吐。**目标识别准确性、"每小时 1,000 个决策"、"数秒完成目标周期"以及 AI 对每个具体目标的实际贡献，仍属声称或未经验证。13,000 个目标、10 万用户、token 增长等数字均出自官员，未经独立审计；官方在申请 23 亿美元预算和推动转正式项目时，亦有强调成效的动机。

### 口径冲突一览

!table t_mv_conflicts|Maven 相关数据口径冲突与待核清单|本报告整理，引用前应逐项回到原文核对|30,82,48
条目|冲突或存疑内容|来源
谷歌抗议规模|签名约 4,000、4,600 还是近 5,000 人；辞职约 12 人、13 人还是"数十人"|[@mv_gizmodo_au_resign,mv_fortune_2018]
谷歌合同额|约 900 万美元（对外口径）、1,500 万美元（18 个月内部预期）、2.5 亿美元/年（项目预算展望，非谷歌合同额）|[@mv_intercept_emails]
2024-02 打击|"85 次以上打击"还是"85 个目标"|[@mv_register_2024]
MSS 数据源数|179 个（CSIS）还是 150 个以上（GlobalSecurity）|[@mv_csis,mv_globalsec]
陆军 EA 日期|2025-07-31 还是 2025 年 8 月|[@mv_wt_ea,mv_ds_ea]
MSS 合同上限|约 12.75 亿、"近 12.8 亿"还是"约 13 亿"美元；另有"10 亿美元上限"的低可信说法|[@mv_globalsec_contract,mv_ds_2025_05]
Feinberg 备忘录日期|3 月 9 日（签署）还是 3 月 20—23 日（报道）|[@mv_govconwire_por,mv_capture]
转正式项目|截止 2026-09-30；有媒体称"已成为"，无官方确认|[@mv_motley_por]
FY2027 预算|23 亿美元为单年还是五年合计；其中 15 亿美元以上用于扩大 MSS 访问|[@mv_ds_fy27,mv_isstracker]
用户数|2025 年 2 万以上（NGA）与"130 个站点、约 2.5 万人"（二手）；2026-03"2 万多活跃用户"与 2026-01"约 5 万"|[@mv_bd_geoint2025,mv_hvylya,mv_govly]
伊朗打击数|24 小时约 1,000 个、至 3-3 近 2,000 个、10 天约 5,000 个、38 天 13,000 个；"每天 3,000 个"等不予采信|[@mv_wapo_2026,mv_wiki_aiwarfare,mv_ds_mazol]
Minab 死亡人数|约 123 名儿童、175—180 人、150—170 余人、至少 186 名学生和教师|[@mv_gizmodo_minab,mv_aca_iran,mv_wiki_minab]
Claude 状态|3-4 被列为供应链风险、6 个月内淘汰，或依据 2-28 行政令；卡普称仍在运行|[@mv_aca_iran,mv_ie_claude]
Scale AI 标注合同|2,400 万美元与"修改后总值 1.3 亿美元"的关系不明|[@mv_nga_contracts]
!end

## （五）案例：从反 ISIS 视频识别到伊朗战役

:::lead
有公开数据支撑的 Maven 实战案例不多，主要包括 2017—2018 年反 ISIS 作战中的 FMV 识别、2024 年 2 月对伊拉克和叙利亚的空袭、2024 年也门和红海作战，以及 2026 年对伊朗的"史诗怒火"行动。前三者只有官员的定性说法；"史诗怒火"有官方总量数字，也发生了与 Maven 相关的最严重平民伤亡事件。演习、盟国和军种推广类案例以采购和部署信息为主。本节逐案记录时间、单位、战区、Maven 的作用、结果和来源，并单列"未找到关联证据"的行动清单，避免在无据情况下将 Maven 与近年美军各项行动相挂钩。
:::

### 案例一：反 ISIS 首次部署（2017—2018）

2017 年 12 月起至 2018 年，特种作战司令部情报分析员在中东反 ISIS 作战中使用 Maven，非洲司令部及中东多个地点随后跟进。Maven 用于在 ScanEagle 小型无人机全动态视频中自动识别物体，辅助分析员完成 PED[@mv_nextgov_2017,mv_trajectory]，沙纳汉称之为"原型战"[@mv_nextgov_2017]。2018 年 5 月，官员称非洲司令部自 2017 年 12 月起也在使用，部署范围扩展至中东多个地点[@mv_bd_2018_africa]。早期还曾用海豹突击队在索马里拍摄的无人机视频测试多家供应商的识别工具[@mv_bloomberg_2024]。

此次属初始部署，无公开性能数据，主要意义在于证明国防部能在约 8 个月内把商业计算机视觉送上战场[@mv_bulletin_2017]。GlobalSecurity 提到的其他早期作战使用未获佐证（弱源，待核）[@mv_globalsec]。

### 案例二：XVIII 空降军"猩红之龙"系列演习（2020 年起）

自 2020 年起，驻布拉格堡的陆军第 XVIII 空降军在美国本土逐年开展"猩红之龙"系列演习，在 DevSecOps 环境中与多达 70 家公司合作，把 Maven 从视频识别工具发展为整合传感器、目标识别和火力分配的 MSS[@mv_d1_2024_08,mv_cset_coalition]。GAO 将"猩红之龙"描述为使用 Project Maven 数据的陆军目标识别 AI 能力[@mv_gao_22]。

据 CSET 记录，约 20 人的目标小组达到了 2003 年伊拉克战争时时敏目标单元（约 2,000 人）的产出；一名目标军官估计，使用 Maven 每小时可处理 80 个目标，不用时为 30 个[@mv_cset_coalition,mv_bloomberg_2024]。二手报道称数据传输加打击的时间从 12 小时以上缩短到 1 分钟以内[@mv_armyrec]。"每小时 1,000 个高质量决策"仅为目标，未经验证[@mv_interesting_eng_army]。

!photo scarlet_dragon_26_1|XVIII 空降军"猩红之龙"演习（编号 26-1）中，参演人员通过 Maven 智能系统共享目标数据。该系列演习是 MSS 从视频识别工具发展为目标工作流平台的主要试验场|美国陆军，公有领域

!photo scarlet_dragon_c_uas|XVIII 空降军在"猩红之龙"系列活动中开展反无人机训练，以应对未来战争中的无人机威胁|美国陆军，公有领域

### 案例三：支援乌克兰（2022 年起）

2022 年起，前沿部署欧洲的 XVIII 空降军用 MSS 生成目标情报并提供给乌军，乌方使用的是不依赖美国敏感情报的版本[@mv_lawfare_book,mv_kyivind]。

曼森专著称，美方向乌克兰发送了"数以万计"的目标[@mv_willis_book,mv_lawfare_book]。《纽约时报》2024 年 4 月报道称效果"好坏参半"：该系统帮助乌军更有效地打击俄军炮兵，但未能把战场图像送到前线士兵手中，难以把"21 世纪的数据送进 19 世纪的战壕"[@mv_kyivind,mv_defender_nyt]。

【说明】乌克兰是美方目标情报的接收方，不是 MSS 的直接用户。曼森书中有关威斯巴登方面的细节，因无法查阅原文书摘而未能核实。

### 案例四：中央司令部 2024 年 2 月空袭伊拉克、叙利亚

约旦"22 号塔"（Tower 22）前哨遇袭致 3 名美军死亡后，中央司令部于 2024 年 2 月 2 日对伊拉克和叙利亚境内目标实施报复性打击[@mv_register_2024,mv_national_2024]。中央司令部首席技术官舒伊勒·摩尔（Schuyler Moore）对彭博社表示，机器学习目标识别帮助"缩小目标范围"，每一步均以人工验证结束[@mv_register_2024,mv_bnn_2024]。

Maven 参与了 85 次以上打击，涉及 7 处设施[@mv_register_2024]。{red:口径冲突}：彭博社原文为 85 次以上"打击"，部分媒体写作 85 个"目标"[@mv_register_2024]。这是官方首次公开确认 Maven 用于实际打击的目标筛选。

!photo b1b_feb2024_ellsworth|2024 年 2 月 1 日，戴斯空军基地停机坪上的 B-1B"枪骑兵"轰炸机（含埃尔斯沃思基地机组），次日由此出击，对伊拉克、叙利亚境内 85 处目标实施打击；据中央司令部首席技术官向彭博社透露，Maven 在此轮打击中用于缩小目标范围|美国空军 Senior Airman Leon Redfern 摄，公有领域（240201-F-MI946-1067）

### 案例五：也门与红海（2024）

据摩尔介绍，2024 年中央司令部在也门和红海方向使用 Maven 定位也门境内的火箭发射器和红海上的水面船只[@mv_bloomberg_2024,mv_batch]，具体数量未公开。2024 年 1 月起美英对胡塞武装的系列打击是这一时期的主要作战背景，{red:但无公开来源把某一次具体打击与 Maven 直接对应}。

!photo centcom_jan2024_1|2024 年 1 月 12 日美英对也门胡塞武装目标实施打击（中央司令部发布）。Maven 于 2024 年用于定位也门境内火箭发射器和红海水面船只，公开资料未将本次打击与 Maven 直接对应|美国中央司令部，公有领域

!photo gravely_tomahawk|2024 年 1 月 12 日，美国海军"格雷夫利"号驱逐舰发射"战斧"巡航导弹打击胡塞目标。红海方向的海上打击是 Maven 2024 年实战使用的背景之一|美国海军，公有领域

### 案例六："史诗怒火"行动：对伊朗作战（2026）

"史诗怒火"行动自 2026 年 2 月 28 日开始，由中央司令部对伊朗实施，官方统计口径为 38 天。美国官员称，五角大楼依靠 Maven 识别最高优先级目标并协助选择武器[@mv_aca_iran]。《华盛顿邮报》报道，内嵌 Claude 的 MSS 为目标排序、生成坐标并建议武器，二手转述还称其生成法律依据草稿[@mv_wapo_2026]。中央司令部司令表示，最终打击决定由人作出[@mv_letsdata]。

行动结果存在多种口径（见本章第四节）：头 24 小时约 1,000 个目标（华邮）；至 3 月 3 日近 2,000 个（中央司令部）；38 天 13,000 个（CDAO 斯坦利），斯坦利称目标周期"从数天压缩到数秒"；白宫 4 月 8 日统计其中指挥控制目标逾 2,000 个、防空目标 1,500 个[@mv_wapo_2026,mv_defind_13000,mv_stanley_testimony,mv_bd_insatiable]。战事期间 MSS 涉密网使用量增长 89%，token 日峰值增长 4,425%[@mv_bd_insatiable]，用户数从约 5 万增至 10 万以上[@mv_ds_mazol]。上述数字统计的是打击目标，不是 Maven 独立识别的目标；Claude 的具体角色仍有争议（见本章第二节）。

!photo b1b_centcom_9762139|B-1B"枪骑兵"轰炸机起飞，执行中央司令部责任区安全支援任务（2026 年 5 月）。对伊朗作战期间及其后，MSS 是中央司令部目标定位的核心平台；本照片仅作背景，不表明该架次与 Maven 直接相关|美国空军，公有领域

### 案例七：Minab 学校遇袭事件（2026-02-28）

2026 年 2 月 28 日前后，即"史诗怒火"行动首日，伊朗 Minab 一所学校遭美军打击。据彭博社引述五角大楼内部调查，该地点在旧数据库中仍标为伊斯兰革命卫队设施，输入 Maven 后被列为"第一天推荐目标"；卫星图像显示该地点近十年前已改建，2018 年的图像上可见足球场；中央司令部平民伤害评估团队已从约 10 人缩减至 1 人；部分用户以为 Maven 会发现过期记录；调查称这是"一连串可预防的失败"[@mv_bloomberg_minab,mv_gizmodo_minab,mv_theprint_minab]。《纽约时报》援引美国官员称美方对此负责，调查仍在进行[@mv_aca_iran,mv_airwars_guardian]。

{red:死亡人数说法不一}：彭博社/Gizmodo 称约 123 名儿童死亡[@mv_gizmodo_minab]；军控协会称约 175—180 人[@mv_aca_iran]；另有 150—170 余人的说法[@mv_rs_palantir]；伊方称至少 186 名学生和教师死亡[@mv_wiki_minab]。彭博社调查报道的日期也有 9 月 18 日和 9 月 20 日两种说法。

各方说法方面，Palantir 称自己"不对底层数据负责"，此后增加了对底层情报中"取消资格因素"的复核[@mv_gizmodo_minab,mv_rs_palantir]。前军官对 Semafor 等媒体表示，责任在人而不在 AI[@mv_mt_minab]。也有分析指出，目前没有公开的一手材料能把某一具体 AI 输出与此次打击直接对应[@mv_beebe_minab]。Maven 或 Claude 是否在其中起作用，仍有争议[@mv_aca_iran]。

事件发生后，2026 年 3 月 12 日，120 余名众议院民主党议员致信国防部长赫格塞斯，46 名参议员另提出类似要求；五角大楼以调查尚在进行为由作答；联合国事实调查团认为"有合理理由"相信构成战争罪[@mv_gizmodo_minab,mv_wiki_minab]。{red:截至 2026 年 10 月，完整调查报告仍未公开}。

我部研判，Minab 事件的失败链条是"数据过期 → 平台如实呈现 → 人工核查缺位"，模型识别本身并未出错。事件揭示了 MSS 规模化的代价：目标处理吞吐成倍提高，平民伤害评估人员却从 10 人减至 1 人，人在回路在形式上仍然存在，实质审查能力已被稀释。

### 案例八：北约 MSS NATO（2025—2026）

北约通信与信息局（采办方）于 2025 年 3 月 25 日签约采购 MSS NATO，4 月 14 日公布，供盟军作战司令部在欧洲使用，2026 年 6 月 22 日系统达到全面作战能力。系统用于情报融合与目标定位、战场态势感知与规划、加速决策，包含大语言模型、生成式 AI 和机器学习[@mv_shape_release,mv_ncia_2025]。

从提出需求到签约约 6 个月，北约称之为史上最快的采购之一，金额未公开[@mv_shape_2025,mv_ds_nato]。系统先后部署于 SHAPE、布林森联合部队司令部，诺福克联合部队司令部预计于 2026 年 4—5 月接入[@mv_janes_norfolk]。系统于 2025 年全年测试，经"坚定威慑 2026"演习检验后达到 FOC，获准在北约机密网络运行，数据存放于北约自有数据中心[@mv_shape_foc,mv_janes_foc]。北约强调，该系统不同于"NGA Maven 作战人员支援系统"[@mv_shape_2025]。

!photo shape_hq|比利时蒙斯北约欧洲盟军最高司令部（SHAPE）主入口。北约于 2025 年 3 月为盟军作战司令部采购 MSS NATO，SHAPE 为首批部署地点|维基共享资源

!photo jfc_brunssum|荷兰布林森北约联合部队司令部。该司令部是继 SHAPE 之后部署 MSS NATO 的单位之一|维基共享资源，CC BY-SA 2.0

!photo nato_mss_release|SHAPE 新闻稿页面《北约采购 AI 赋能作战系统》，宣布通过 NCIA 采购 Palantir MSS NATO（2025 年 4 月）|北约版权，新闻用途

### 案例九：海军陆战队企业许可（2025）

美国海军陆战队与 DIU、CDAO、ARL 合作，于 2025 年 8 月 15 日敲定 MSS 企业许可，9 月 10 日公布，9 月 11 日发布 MARADMIN 424/25，适用范围为全军种。陆战队将 MSS 定为跨多个作战司令部的标准"火力与效果集成平台"[@mv_ds_maradmin]。通过该许可，从舰队陆战队到支援机构均可在 SIPRNet（IL6 云）上无限量访问 MSS，金额未披露[@mv_usmc_release,mv_maradmin,mv_ds_usmc]。

### 其他推广与使用

在作战司令部和军种层面，4.8 亿美元合同自 2024 年 5 月起把 MSS 原型推广至中央、欧洲、印太、北方、运输五个作战司令部和联合参谋部的"数千用户"[@mv_ds_2024_05]；ARL 约 9,980 万美元合同自 2024 年 9 月起把 MSS 扩展至陆、空、天、海和陆战队[@mv_govconwire_arl]。

2026 年，陆军联合兵种司令部把"Maven C2 智能系统"纳入训练与院校教育[@mv_army_cac]；马佐尔称 MSS 正推广至国民警卫局[@mv_ds_mazol]。

2025 年 9 月陆军 NGC2"常春藤之刺 1"演习中，第 4 步兵师在 Lattice 网格上运行 Palantir Target Workbench，完成师级目标定位流程；{red:此处使用的是 Target Workbench，公开资料未说明是否即 MSS 本身}[@mv_bd_ivysting]。

2026 年 1 月 3 日委内瑞拉马杜罗抓捕行动中，《华尔街日报》称 Claude 经 Palantir 平台参与，{red:但没有来源明确说明使用的是 Maven}，具体任务属机密，Anthropic 不予置评[@mv_swj_maduro,mv_cnbc_karp]。

### 案例总表

!table t_mv_cases|Maven / MSS 主要案例|本报告据各条所列来源整理；可信度分官方、媒体、智库、二手|18,22,18,36,40,26
日期|单位|战区|Maven 作用|结果与数据|可信度与来源
2017-12 起|SOCOM、AFRICOM|中东、非洲|ScanEagle FMV 物体识别|初始部署，无性能数据|官方/媒体[@mv_nextgov_2017,mv_bd_2018_africa]
早期|海豹突击队视频|索马里|测试多家供应商识别工具|—|媒体[@mv_bloomberg_2024]
2020 起|XVIII 空降军|美国本土|"猩红之龙"演习孵化 MSS|20 人顶 2,000 人；每小时 30 → 80 个目标|智库/GAO[@mv_cset_coalition,mv_gao_22]
2022 起|XVIII 空降军|乌克兰|生成目标情报提供乌军|"数以万计"目标；效果"好坏参半"|专著、NYT[@mv_willis_book,mv_kyivind]
2024-02-02|CENTCOM|伊拉克、叙利亚|ML 目标识别缩小目标范围|85 次以上打击、7 处设施|官方[@mv_register_2024]
2024|CENTCOM|也门、红海|定位火箭发射器与水面船只|无数量|官方[@mv_bloomberg_2024]
2024-05 起|5 个作战司令部与联合参谋部|全球|MSS 原型推广|"数千用户"|官方[@mv_ds_2024_05]
2025-03 至 2026-06|北约 ACO|欧洲|情报融合、目标定位、规划|6 个月完成采购；2026-06-22 达到 FOC|官方[@mv_ncia_2025,mv_shape_foc]
2025-09|海军陆战队|全军|标准火力与效果集成平台|IL6 企业许可|官方[@mv_ds_maradmin]
2026-02-28 起|CENTCOM|伊朗|目标排序、坐标、武器建议|38 天 13,000 个目标；用户 10 万以上|官方数字＋媒体[@mv_ds_mazol,mv_wapo_2026]
2026-02-28|CENTCOM|伊朗 Minab|过期记录被列为推荐目标|学校遇袭，死亡人数说法不一|媒体，有争议[@mv_bloomberg_minab,mv_gizmodo_minab]
2026|陆军联合兵种司令部、国民警卫局|训练体系、本土|纳入训练；推广使用|—|官方[@mv_army_cac,mv_ds_mazol]
!end

### 未找到关联证据的行动

以下行动或项目常与 Maven 相提并论，但本轮调研{red:未找到将其与 Maven 直接挂钩的公开报道}。列出这些行动，是为了避免在缺乏证据的情况下外推 Maven 的作用。

!table t_mv_noevidence|未找到 Maven 关联证据的行动与项目|本报告调研结论（截至 2026-10-10）|40,60,60
行动或项目|时间与背景|调研结论
"粗骑兵"行动（Operation Rough Rider）|2025 年，对也门胡塞武装打击|未找到 Maven 参与的公开报道
"午夜之锤"行动（Midnight Hammer）|2025 年 6 月，打击伊朗核设施|未找到 Maven 参与的公开报道
"南方之矛"行动（Southern Spear）|2025 年 9 月起，在加勒比海、东太平洋打击船只|检索结果中无 Maven 或 Palantir 相关信息
马杜罗抓捕行动|2026-01-03，委内瑞拉|仅有"Claude 经 Palantir 参与"的说法，未确认使用 Maven[@mv_swj_maduro]
"金穹"导弹防御|2025 年起|未找到 MSS 角色；仅有 Anduril 与 Palantir 共同开发 C2 软件的报道[@mv_reuters_goldendome]
印太司令部专门演习|—|仅能确认印太司令部在 2024 年合同覆盖范围内[@mv_ds_2024_05]
"项目融合"（Project Convergence）|陆军年度试验|未找到 Maven 具体使用记录
太空军|—|已列入 2024-09 军种扩展范围，未找到具体使用记录[@mv_govconwire_arl]
英国国防部|2025-09 宣布与 Palantir 建立战略伙伴关系，最高 7.5 亿英镑|官方未称 MSS；最终合同签署未证实[@mv_computing_uk]
!end

### 案例综合分析

按时间排列上述案例，Maven 实战使用呈现三个演进特征。

**作用从识别转向排序。**2017 年 Maven 的作用是在视频中识别物体，属于情报处理；2024 年 2 月的作用是"缩小目标范围"，开始进入目标筛选；2026 年的作用是目标排序、生成坐标和建议武器，已深入目标定位的核心决策环节[@mv_nextgov_2017,mv_register_2024,mv_aca_iran]。

**规模从试点转向战役级。**2017 年只有少数分析员使用，2024 年 2 月参与 85 次以上打击，2026 年为 38 天 13,000 个目标、用户 10 万以上[@mv_register_2024,mv_ds_mazol]。规模扩大的同时，官方披露的信息越来越集中于总量数字，单个目标层面的 AI 贡献、误差和审批时长均无公开数据。

**风险从识别不准转向流程失守。**早期的担忧是模型准确率偏低（60% 对 84%），Minab 事件暴露的则是数据过期、平民伤害评估人员缩减和用户对系统能力的错误预期[@mv_bloomberg_2024,mv_bloomberg_minab]。我部研判，AI 目标定位系统进入战役级运用后，风险评估的重点应从模型指标转向数据治理和人机协作流程。

盟国方面，北约 ACO 是已确认的 MSS 直接用户，乌克兰是美方目标情报的接收方；英国 2025 年 9 月宣布与 Palantir 建立的战略伙伴关系涉及 AI 目标定位，但官方未称其为 MSS；其他国家的采用情况未找到证据[@mv_shape_foc,mv_kyivind,mv_computing_uk]。

:::judge 研判要点
- **Maven 的核心价值在于提高杀伤链的处理规模和速度。**经多源证实的是以少量人力支撑大规模目标吞吐（20 人顶 2,000 人、每小时 30 → 80 个、38 天 13,000 个目标），识别精度并未提高；测试中其识别率约 60%，低于人类的 84%，2026 年版本没有任何公开准确率数据。
- **MSS 已从无人机视频识别工具演变为国防部事实上的 AI 赋能 C2 与目标定位骨干和"万能应用"。**用户约 16 个月增长约 5 倍至 10 万以上，覆盖全部作战司令部、各军种、国民警卫局和北约 ACO；FY2027 申请约 23 亿美元（含联合火力网）；Feinberg 备忘录将其推向全军正式项目。
- **架构上形成政府掌握模型流水线（NGA）、商业公司掌握平台与本体（Palantir）、模型与大模型可插拔的格局。**合同全部并入陆军 100 亿美元企业协议后，平台锁定进一步加深，公开追踪难度上升；Open DAGIR 只开放了应用层。
- **主要风险在数据与人，算法居次。**Minab 事件暴露了"过期数据＋自动化偏差＋人工审查密度下降"的失败链条；大模型层（Claude）的角色与替换状态不透明；MSS 不发射武器，处于 DoDD 3000.09 高级审查范围之外，目前没有公开的负责任 AI 评估或独立审计。
- **对我方的启示：AI 目标定位系统的效能瓶颈和风险均集中在数据时效、对象化和审批流程环节。**评估同类系统时，应重点关注数据源治理、AI 贡献标注（如 NGA 的机器生成标签）和单目标人工审查时长，不宜单纯比较识别率。
:::
