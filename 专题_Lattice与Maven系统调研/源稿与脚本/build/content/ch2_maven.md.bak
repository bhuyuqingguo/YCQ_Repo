# 二、Maven：从无人机视频识别到全军"目标工厂"与"万能应用"

:::lead
Maven 不是一个单一的软件产品，而是一条持续九年、几经改组的政府项目线。它起步于 2017 年反 ISIS 战场上"看不完的无人机视频"，经过谷歌退出风波、XVIII 空降军"猩红之龙"演习的打磨、2022 年的拆分改组，最终演变为以 Palantir 软件为主体、用户超过 10 万、覆盖全部作战司令部和北约盟军作战司令部的 AI 赋能指挥控制与目标定位平台——Maven 智能系统（MSS）。本章依次梳理其前世今生、功能设计、架构设计、能力评估和实战案例，并对官方口径、媒体报道与弱源说法分别标注。
:::

【阅读提示】本章所述事实均来自公开报道、官方文件、智库报告与厂商资料的检索摘要。由于调研环境限制，相当一部分原文未能逐页核读，凡数字口径存在冲突的，均并列写明；只见于聚合站、博客或倡导团体的说法，标注为"（弱源，待核）"；作者自己的推断明确标注为"分析"或"推断"。

## （一）前世今生：从算法战跨职能小组到全军正式项目

:::lead
Maven 的九年可以分为四段：2017—2018 年是"探路者"阶段，一个小团队用几个月时间把商业计算机视觉送上反 ISIS 战场；2019—2021 年是"生态扩张"阶段，谷歌退出后由 ECS、Clarifai、微软、AWS、Palantir 等填补，XVIII 空降军开始用演习把它改造成目标工作流平台；2022—2025 年是"拆分与规模化"阶段，GEOINT 模型流水线归 NGA、作战平台 MSS 由 Palantir 主承包并快速推向各作战司令部和北约；2026 年起是"制度化"阶段，Feinberg 备忘录要求 MSS 转为全军正式项目，伊朗战事使其用户在一年内翻番。
:::

### 三个名字：Project Maven、NGA Maven 与 MSS

讨论 Maven 首先要分清三个经常被混用的名字。**Project Maven** 是 2017 年 4 月成立的"算法战跨职能小组"（AWCFT，Algorithmic Warfare Cross-Functional Team）的俗称，是一个政府项目，最初隶属国防部负责情报的副部长办公室（OUSD(I)，后为 OUSD(I&S)）[@mv_work_memo,mv_wiki_maven]。**NGA Maven** 是 2022 年起由国家地理空间情报局（NGA）接管的地理空间情报（GEOINT）AI 服务与模型流水线，2023 年 11 月成为 NGA 的正式采购项目（program of record）[@mv_bd_2022_nga,mv_dd_por]。**Maven 智能系统（Maven Smart System，MSS）**则是以 Palantir 商业软件为主体、面向指挥控制与目标定位的作战平台，2024 年起由陆军代为签约、向各作战司令部扩展，2026 年起归首席数字与人工智能办公室（CDAO）新设的 MSS 项目办公室管理[@mv_ds_2024_05,mv_ds_feinberg2]。

三者的关系可以概括为"同源而分流"：Project Maven 是母体，NGA Maven 继承了它的计算机视觉模型、数据标注与模型评估流水线，MSS 继承了它在作战司令部一侧的数据融合与目标工作流应用。北约在 2025 年采购 MSS NATO 时专门强调，该系统"不应与 NGA Maven 作战人员支援系统（NGA Maven Warfighter Support System）相混淆"[@mv_shape_2025,mv_ds_nato]，这从侧面印证了两条线并行存在。本报告在不加限定时所说的"Maven"，指的是这一整条项目线；凡涉及具体系统，均分别写明 NGA Maven 或 MSS。

### 2017 年的问题：反 ISIS 战场与"看不完的视频"

Project Maven 诞生于打击"伊斯兰国"（ISIS）的战事高峰期。当时美军在伊拉克、叙利亚等地大量使用战术级和中空无人机执行持续监视，产生了海量全动态视频（FMV）。沃克备忘录给 AWCFT 布置的第一项任务，正是对战术和中空无人机 FMV 进行"处理、利用和分发"（PED）[@mv_globalsec]；其目标是用深度学习从情报数据中提取洞见，支援击败 ISIS 的作战[@mv_trajectory]。

【分析】从业务逻辑看，FMV 的 PED 是一个典型的"人力瓶颈"问题：传感器数量和飞行小时可以按装备采购的节奏增加，但能盯着屏幕逐帧判读、标注车辆与人员、再把结论写成情报产品的分析员数量增长有限。计算机视觉恰好可以把"有没有目标、是什么目标"这一步的大部分重复劳动交给机器，让分析员只处理机器提示的片段。Maven 选择 FMV 作为切入点，是因为它问题边界清楚、数据现成、效果直观，适合作为国防部引入商业 AI 的"示范工程"，而不是因为 FMV 本身是最重要的情报来源。

### 立项：沃克备忘录与 AWCFT

2017 年 4 月 26 日，时任国防部常务副部长罗伯特·沃克（Robert O. Work）签署题为《成立算法战跨职能小组（Project Maven）》的备忘录，宣布成立 AWCFT，以"加速国防部整合大数据和机器学习"[@mv_work_memo]。这份备忘录后来由美国国家安全档案馆（NSArchive）公开了扫描件。经费方面，Maven 成立后大约两个月内就从国会获得约 7,000 万美元[@mv_wiki_maven,mv_globalsec]。

!photo work_portrait|罗伯特·沃克（Robert O. Work）官方肖像。沃克时任国防部常务副部长，2017 年 4 月 26 日签署成立算法战跨职能小组（Project Maven）的备忘录|美国国防部，公有领域

AWCFT 的组织形式本身就是一项制度创新。"跨职能小组"意味着它不是传统意义上的项目办公室，没有长周期的需求论证—研制—试验—列装流程，而是由一个小团队直接对接作战用户、商业供应商和经费渠道，以"先上线、再迭代"的方式推进。【分析】这一模式后来被概括为"探路者"（pathfinder）：Maven 的真正使命，是证明国防部能够在几个月内把商业 AI 用上战场；FMV 识别只是证明这一点的手段。也正因如此，它后来才能从视频识别自然地扩展到数据融合和指挥控制[@mv_wiki_maven,mv_trajectory]。

### 沙纳汉与库科：探路者团队的打法

Maven 的两位关键人物是杰克·沙纳汉（Jack Shanahan）空军中将和海军陆战队上校德鲁·库科（Drew Cukor）。沙纳汉自 2017 年 4 月至 2018 年 12 月负责 Maven 的总体指导，此后调任新成立的联合人工智能中心（JAIC）首任主任；库科是 AWCFT 的负责人，承担了大量日常领导工作[@mv_wiki_maven,mv_globalsec]。2017 年 7 月，项目方已公开表示要在"年底前"把算法部署到战区[@mv_techsparx]。

!photo shanahan_2020|杰克·沙纳汉空军中将官方肖像。沙纳汉 2017 年 4 月至 2018 年 12 月负责指导 Project Maven，随后出任联合人工智能中心（JAIC）首任主任|美国国防部，公有领域

!photo maven_2017_dod_article|国防部 2017 年报道页面：Maven 计划于当年年底前向战区部署算法，图为库科上校在 Defense One 技术峰会上介绍项目|美国国防部网站截图，公有领域

需要说明的是，JAIC 从来不是 Maven 的主管单位。JAIC 于 2018 年成立后，Maven 仍留在 OUSD(I) 之下，只是首任负责人沙纳汉转去领导 JAIC；二者后来在 2022 年一同并入 CDAO[@mv_wiki_maven]。2026 年 3 月，彭博社记者凯特琳娜·曼森（Katrina Manson）出版专著《Project Maven：一位陆战队上校、他的团队与 AI 战争的黎明》（W. W. Norton），书名中的"陆战队上校"推测指库科，但检索结果未直接确认[@mv_npr_book]。该书是迄今关于 Maven 内部运作最详细的公开叙事，本章多处引用其书评和摘要。

### 首批部署：ScanEagle 视频与"原型战"

2017 年 12 月，Maven 第一个达到任务就绪状态的产品部署到中东：一个用于识别 ScanEagle 小型无人机视频中物体的算法[@mv_trajectory,mv_nextgov_2017]。从立项到上线大约只用了 8 个月。使用者是特种作战司令部（SOCOM）的情报分析员，沙纳汉把这种做法称为"原型战"（prototype warfare）[@mv_nextgov_2017]。到 2018 年 5 月，官员透露非洲司令部（AFRICOM）自 2017 年 12 月起也在使用 Maven，部署范围扩展到中东多个地点[@mv_bd_2018_africa]。《原子科学家公报》在 2017 年 12 月即以"Project Maven 把 AI 带进对 ISIS 的战斗"为题做了报道[@mv_bulletin_2017]。

!photo scaneagle_mkv|ScanEagle 小型无人机从 MK V 特种作战艇上发射。Maven 2017 年 12 月首批部署的算法即用于识别 ScanEagle 全动态视频中的物体|美国国防部，公有领域

!photo scaneagle_catapult|ScanEagle 无人机在伊拉克阿萨德空军基地的弹射器上待发。此类战术无人机在反 ISIS 作战中产生了大量需要人工判读的视频|美国国防部，公有领域

据彭博社 2024 年的长篇报道，Maven 早期曾用美国海军"海豹"突击队在索马里拍摄的无人机视频测试多家供应商的识别工具[@mv_bloomberg_2024]。GlobalSecurity 还提到更多早期作战使用，但这些说法未获其他来源佐证（弱源，待核）[@mv_globalsec]。

### 早期供应商与合同体系：ECS 渠道下的"多供应商拼盘"

Maven 早期的合同大多通过集成商 ECS Federal 下达，采购渠道之一是陆军研究实验室（ARL）的"基础与应用科学研究"广泛机构公告（BAA）合同；谷歌、微软、AWS、Clarifai 等均以 ECS 分包商身份参与[@mv_fedsavvy,mv_itpro]。ECS 自 2017 年起担任 Maven 的"AI 互操作集成商"（AI3）[@mv_execbiz_ecs]，此后陆续持有 3 份与 Maven 相关、总额约 3.64 亿美元的合同[@mv_itpro,mv_poulson_budget]。ECS 本身于 2018 年 4 月被 ASGN 以 7.75 亿美元收购[@mv_fedsavvy]。

几家主要供应商的情况如下。谷歌通过 ECS 分包参与 FMV 目标检测 AI 的开发，谷歌云负责人对内称合同"只有约 900 万美元"，但泄露的内部邮件写的是"总交易 2,500—3,000 万美元，其中 1,500 万美元在 18 个月内归谷歌"，并提到"项目扩大后预算为每年 2.5 亿美元"[@mv_intercept_emails,mv_gizmodo_google]。【分析】这三个数字分属三个层次：900 万美元是对外口径的初始合同额，1,500 万美元是 18 个月的内部预期，2.5 亿美元是整个 Maven 项目的年度预算展望，不是谷歌的合同上限。Clarifai 作为 ECS 分包商累计获得超过 2,500 万美元，其中一项人脸识别任务为 560 万美元[@mv_forbes_startups,mv_itpro]。微软（约 3,000 万美元，约 2019 年起）和 AWS（约 2,000 万美元，约 2020 年起）也获得 ECS 分包，但这些分包合同并未直接点名 Maven，二者与 Maven 的关联是调查记者杰克·波尔森（Jack Poulson，Tech Inquiry）的推断[@mv_forbes_2021,mv_poulson_budget]。泄露邮件还显示，2017 年 9 月亚马逊、IBM、微软都在与谷歌竞争 Maven 工作[@mv_intercept_emails,mv_itpro]。

最大的一笔是代号"Pavement"的 ECS 主合同，金额 1.42 亿美元，另有一份关联的 ECS 合同 5,225 万美元，用于 SUNet 开源数据聚合。这些记录后来被五角大楼依据《联邦采购条例》FAR 4.606 从公开采购数据库中删除，国防部长办公室发言人确认了删除行为[@mv_poulson_pavement,mv_poulson_erasure]。【分析】由于记录被删除，2017—2021 年 Maven 实际支出中可公开核查的部分，很可能明显低于真实规模。GlobalSecurity 还称谷歌是通过与诺斯罗普·格鲁曼的安排提供基于 TensorFlow 的模型、L3Harris、内华达山脉公司等 20 多家公司参与，Palantir 提供数据集成层并后来发展为 MSS，这些说法未获一手来源证实（弱源，待核）[@mv_globalsec]。2023 年 NGA 还专门发布征询，评估 Maven 的 AI/ML 供应链风险，理由是对主承包商以下各级供应商缺乏可见度[@mv_bd_supplychain_2023]。

!table t_mv_vendors|Project Maven 早期（2017—2021）主要供应商与合同|本报告据 The Intercept、Forbes、ITPro、Tech Inquiry 等整理|24,30,46,60
供应商|身份|金额（据报）|说明与证据等级
ECS Federal|主承包商、AI 互操作集成商（AI3）|3 份相关合同约 3.64 亿美元；"Pavement" 1.42 亿美元|"Pavement"记录已被依据 FAR 4.606 删除；数字来自 Tech Inquiry 调查[@mv_poulson_pavement,mv_itpro]
谷歌|ECS 分包商|对外约 900 万美元；内部预期 1,500 万美元/18 个月|FMV 目标检测；2018-06 宣布 2019-03 合同到期后不续约[@mv_intercept_emails,mv_nbc_google]
Clarifai|ECS 分包商|累计超过 2,500 万美元|含 560 万美元人脸识别任务[@mv_forbes_startups]
微软|ECS 分包商（推断）|约 3,000 万美元，约 2019 年起|分包合同未点名 Maven，关联系推断[@mv_forbes_2021]
AWS|ECS 分包商（推断）|约 2,000 万美元，约 2020 年起|同上[@mv_forbes_2021]
Palantir|数据集成层（据二手说法）|未披露|GlobalSecurity 称其后来发展为 MSS（弱源，待核）[@mv_globalsec]
!end

### 谷歌员工抗议：硅谷与五角大楼关系的转折点

2018 年春，谷歌参与 Maven 的消息在公司内部引发大规模抗议，成为 Maven 早期最著名、也最具长远影响的事件。员工联名请愿，要求谷歌取消合同并承诺今后不再从事军事工作。签名人数有多种说法：Gizmodo 报道"近 4,000 人"，其他报道称 4,600 人以上，后来带有倡导色彩的 Jacobin 称近 5,000 人[@mv_gizmodo_au_resign,mv_fortune_2018]。辞职人数同样口径不一：Gizmodo 2018 年 5 月报道约十余人辞职，这是谷歌首次因业务决策出现已知的集体辞职；其他媒体称至少 13 人，Axios 称"数十人"[@mv_gizmodo_au_resign]。内部还有 700 多人组成"Maven 良心拒服者"小组[@mv_collective]。

!photo google_walkout_2018|2018 年谷歌员工罢工抗议现场（桑尼维尔）。同年谷歌在员工反对下宣布不再续签 Maven 合同，这是硅谷科技工作者首次大规模反对军事 AI 项目|维基共享资源，CC BY-SA 4.0

2018 年 6 月 1 日前后，谷歌云首席执行官黛安·格林（Diane Greene）告知员工，谷歌不会在现有合同于 2019 年 3 月到期后寻求续约[@mv_nbc_google,mv_fortune_2018]。彭博社当时评论，这场 AI 员工反抗可能危及谷歌争取五角大楼云合同的前景[@mv_bloomberg_2018]。

【分析】谷歌退出并没有让 Maven 放慢脚步。ECS、Clarifai、微软、AWS 以及后来的 Palantir 等迅速填补了空缺；而这场争议在客观上推动了国防部此后的 AI 伦理原则建设，也使"科技公司是否应参与杀伤链"成为此后八年反复出现的议题——2026 年 Anthropic 与五角大楼的冲突，在某种意义上是 2018 年谷歌风波的延续。

### 经费演变：从 7,000 万美元到 23 亿美元申请

Maven 早期经费由国会大幅加码。按 Inside Defense 的报道，FY2018 国会拨款 1.31 亿美元，而国防部的请求只有约 3,100 万美元[@mv_insidedefense_fy18]；FY2020 为 2.21 亿美元，FY2021 为 2.5 亿美元（按请求拨付，项目名称改为"算法战跨职能小组软件试点项目"）[@mv_ds_2024_03,mv_dd_ndaa]。此后 Maven 的公开预算逐渐模糊：FY2022—FY2025 只有早期五年防务计划（FYDP）中的规划值，分别为 2.52 亿、1.20 亿、1.21 亿和 1.22 亿美元；FY2025 预算书把 Maven 经费调整到 CDAO 的项目元素 PE 0606135D8Z 下，公开预算中不再单列 Maven[@mv_ds_2024_03]。NGA 一侧的经费属于情报预算，涉密。Lawfare 的书评指出，Maven 的预算是机密的，且不适用《信息自由法》（FOIA）[@mv_lawfare_book]。

到 FY2027 预算申请，Maven 重新以显著数额出现在公开文件中。国防部 FY2027 预算概览列出约 23 亿美元用于"Maven 智能系统与联合火力网"（Joint Fires Network），交付 CJADC2 能力[@mv_fy27_book,mv_gtlaw]；DefenseScoop 的拆分是：其中超过 15 亿美元用于"联合部队 AI 赋能司令部倡议"（Joint Force AI-Enabled Headquarters initiative）以扩大 MSS 用户访问，另有 6,000 万美元用于"虚拟联合作战中心"[@mv_ds_fy27]。{red:口径冲突}：ISS Tracker、SpaceNews 等把 23 亿美元描述为"未来五年"合计，DefenseScoop 和预算概览则表述为 FY2027 单年申请[@mv_isstracker,mv_spacenews_23]；本报告以官方预算概览为准，但提醒这 23 亿美元包含联合火力网，不能全部计为 Palantir MSS 收入。

!table t_mv_budget|Project Maven / MSS 各财年经费（公开口径）|本报告据 Inside Defense、DefenseScoop、FY2027 预算概览整理|26,44,90
财年|金额|性质与说明
FY2017|约 0.7 亿美元|成立后约两个月内获国会经费[@mv_wiki_maven]
FY2018|1.31 亿美元|国会拨款；国防部请求仅约 0.31 亿美元[@mv_insidedefense_fy18]
FY2019|未检索到|—
FY2020|2.21 亿美元|国会拨款[@mv_ds_2024_03]
FY2021|2.5 亿美元|按请求拨付；更名为算法战跨职能小组软件试点项目[@mv_dd_ndaa]
FY2022—FY2025|2.52 亿/1.20 亿/1.21 亿/1.22 亿美元|早期 FYDP 规划值，非实际拨款[@mv_ds_2024_03]
FY2025|不再单列|并入 CDAO 项目元素 PE 0606135D8Z；NGA 部分属情报预算[@mv_ds_2024_03]
FY2027 申请|约 23 亿美元（MSS 与联合火力网）|其中超过 15 亿美元用于扩大 MSS 访问；另有"五年合计"说法[@mv_fy27_book,mv_ds_fy27]
!end

### 猩红之龙：XVIII 空降军把 Maven 改造成目标工作流

如果说 2017 年的 Maven 是一组"计算机视觉检测器"，那么把它变成"数据融合加目标工作流平台"的关键推手，是驻布拉格堡的陆军第 XVIII 空降军。自 2020 年起，XVIII 空降军通过年度系列演习"猩红之龙"（Scarlet Dragon），在 DevSecOps 环境中与多达 70 家公司合作，把 Maven 发展为整合传感器、目标识别和火力分配的 MSS[@mv_d1_2024_08,mv_cset_coalition]。美国政府问责局（GAO）在 2022 年的报告中把"猩红之龙"描述为使用 Project Maven 数据的陆军目标识别 AI 能力[@mv_gao_22]。乔治城大学安全与新兴技术中心（CSET）2024 年 8 月的政策简报《构建技术联盟》对这一过程做了系统记录，并给出了著名的"约 20 人顶 2,000 人"对比（详见本章第四节）[@mv_cset_coalition]。2022 年俄乌冲突爆发后，前沿部署欧洲的 XVIII 空降军又用 MSS 为乌克兰生成目标情报（详见第五节）。

【分析】"猩红之龙"阶段的意义在于，它把 Maven 的重心从"更准地识别"转向"更快地走完目标流程"。这一转向决定了 MSS 后来的形态：识别模型可以由多家供应商提供、不断替换，而平台的核心竞争力在于把多源数据、检测结果、目标列表、打击资产和审批流程串在同一个界面里。

### 2022 年拆分：NGA Maven 与 CDAO/陆军 MSS

2022 年是 Maven 治理结构的分水岭。在 2022 年 4 月的 GEOINT 大会上，NGA 宣布将从 OUSD(I&S) 接管 Maven 的 GEOINT AI 服务，约占原项目的 80%，自 FY2023 起生效[@mv_bd_2022_nga,mv_c4isr_2022]。FY2023 预算请求据此把 Maven 拆为两部分：GEOINT 部分划归 NGA，非 GEOINT 部分划归同年成立的 CDAO[@mv_bd_2022_nga]。由于 2022 年 10 月国会以持续决议案维持政府运转，移交一度被推迟，五角大楼对此"保持沉默"[@mv_ds_2022_cr]。

NGA 方面，经过约 9 个月的需求工作，NGA 于 2023 年 11 月 2 日宣布、11 月 7 日正式将"NGA Maven"列为采购项目，采用"软件采购路径"[@mv_dd_por,mv_wiki_maven]。2024 年 3 月的 FY2025 预算书中，Maven 经费被调整到 CDAO 名下，CDAO 副主任表示 CDAO 已把整个 Maven"AI 开发流水线"交给 NGA；DefenseScoop 观察到，NGA、CDAO 和 OUSD(I&S) 自移交以来对 Maven 和 MSS"大体守口如瓶"[@mv_ds_2024_03]。一份被 DefenseScoop 引用的 Palantir 新闻稿则把 Maven 描述为"支撑 CDAO 的 CJADC2 倡议的云基础设施、软件能力和 AI"[@mv_ds_86457]。

!photo nga_hq_paglen|国家地理空间情报局（NGA）位于弗吉尼亚州斯普林菲尔德的总部夜间航拍。2022 年起 NGA 接管 Maven 约 80% 的 GEOINT AI 业务，2023 年 11 月将 NGA Maven 列为正式采购项目|特雷弗·帕格伦（Trevor Paglen）拍摄并公开发布

!photo whitworth_portrait|NGA 第八任局长弗兰克·惠特沃斯（Frank Whitworth）海军中将官方肖像。惠特沃斯任内主导了 Maven 在 NGA 的扩展，并多次公开披露 Maven 用户规模与"机器生成情报"标注做法|美国国防部，公有领域

!photo martell_portrait|首任首席数字与人工智能官（CDAO）克雷格·马特尔（Craig Martell）官方肖像。CDAO 于 2022 年成立，承接 Maven 的非 GEOINT 部分及 JAIC 等机构|美国国防部，公有领域

这样，从 FY2023 起 Maven 形成两条线：NGA Maven 负责 GEOINT 计算机视觉模型的标注、训练、评估认证和机器生成情报产品；MSS 作为作战平台面向作战司令部，由 CDAO 主管、NGA 承担系统管理与运行授权职责、陆军负责签约。2023 年 12 月经"全球信息主导实验"（GIDE）认证、2024 年 2 月公布的 CJADC2"最小可行能力"（MVC），就以 MSS 为事实上的骨干[@mv_ds_cjadc2_mvc,mv_bd_opendagir]。

!fig d_maven_governance|d_maven_governance.png|Maven 管理归属演变（2017—2026）|本报告依据 NSArchive 备忘录、Breaking Defense、Defense Daily、DefenseScoop 等公开资料绘制|160

### 前史：Palantir 在陆军"情报到目标"链条上的铺垫

Palantir 能够在 MSS 上后来居上，与它此前在陆军和特种作战领域积累的情报数据平台业务密不可分。2016 年 5 月，SOCOM 以单一来源方式授予 Palantir 上限 2.22 亿美元的"全源信息融合"软件许可[@mv_wt_socom]。2018—2020 年，Palantir 先后进入陆军分布式通用地面系统（DCGS-A）的第一能力包（与雷神共享上限 8.76 亿美元）和第二能力包（2020 年 2 月与 BAE 共享上限 8.23 亿美元的 IDIQ），并在 2021 年 10 月被选中建设基于 Gotham 的跨密级情报数据织网[@mv_c4isr_dcgsa,mv_wt_dcgsa,mv_bd_dcgsa]。2019 年 12 月，Palantir 获得陆军企业数据平台 Vantage 的生产合同，上限 4.58 亿美元[@mv_tipranks_vantage]。

与 Maven 关系最近的是 2020 年 10 月陆军研究实验室授予的 9,120 万美元、两年期 AI/ML 研发合同：用 Foundry 和 Gotham 为各作战司令部提供 AI 数据整合与模型训练，期限至 2022 年 9 月 28 日[@mv_datanami_arl,mv_bw_arl_2020]。【分析】这份合同的客户（作战司令部）、内容（数据整合加模型训练）和时间（恰在 MSS 原型阶段之前），都带有 MSS 前身的特征；而陆军研究实验室此后又是 2024 年 MSS 军种扩展合同的授予方。2024 年 3 月，Palantir 又击败雷神赢得陆军下一代情报、监视与侦察地面站 TITAN 的原型合同（1.784 亿美元），其目标正是缩短"传感器到射手"的时间[@mv_ds_titan,mv_army_titan]。可以说，到 2024 年 MSS 合同落地时，Palantir 已经在陆军"情报—目标"链条的多个环节完成了布局。

### Palantir 成为主承包商：一步步加深的锁定

Palantir 走向 MSS 主承包商的路径，是一个"每一步都加深锁定"的过程。第一步是在位原型开发：在 2024 年合同之前，Palantir 已经"面向有限数量的操作员"开发 MSS 原型，但其起始时间（约 2022—2023 年）没有一手来源证实[@mv_ds_2024_05]。第二步是唯一供应商认证：据 Tech Inquiry 报道，五角大楼认证 Palantir 是 MSS 的唯一供应商[@mv_poulson_solesource]。

第三步是 2024 年 5 月 29 日的 4.8 亿美元合同。陆军合同司令部阿伯丁分部（ACC-APG）授予 Palantir 编号 W911QX-24-D-0012 的五年期、固定价格、不定期交付/不定数量（IDIQ）合同，名为"Maven 智能系统原型"，预计 2029 年 5 月 28 日完成，目的是把 MSS 扩展到中央司令部（CENTCOM）、欧洲司令部（EUCOM）、印太司令部（INDOPACOM）、北方司令部（NORTHCOM）、运输司令部（TRANSCOM）以及联合参谋部的"数千名用户"[@mv_ds_2024_05,mv_dn_2024_05,mv_meritalk_480]。合同把 MSS 描述为接入卫星图像、地理定位等数据以检测潜在目标、支撑 CJADC2 的系统。对这份合同的阶段定性也有分歧：合同名称写的是"原型"，MeriTalk 称它开启了原型阶段，Palantir 方面则称这是"从原型走向生产"[@mv_meritalk_480,mv_dn_2024_05]。

第四步是向各军种扩展。2024 年 9 月，陆军作战能力发展司令部陆军研究实验室（DEVCOM ARL）授予 Palantir 一份约 9,980 万美元、五年期固定价格合同，把 MSS 扩展到陆军、空军、太空军、海军和海军陆战队，新增数万名军种用户[@mv_govconwire_arl,mv_bw_2024_09]。

第五步是上限扩容。2025 年 5 月 20 日（5 月 21 日公布），陆军对 W911QX-24-D-0012 发出第 P00005 号修改，追加 7.95 亿美元软件许可，合同上限升至约 12.75 亿美元（各方表述为"近 12.8 亿"或"约 13 亿"），期限仍至 2029 年 5 月 28 日[@mv_globalsec_contract,mv_ds_2025_05]。国防部称预计需求会"大幅涌入"，但陆军官员同时强调上限只是封顶值，并非已承诺的资金[@mv_ds_2025_05]。同月，NGA 局长惠特沃斯在 GEOINT 2025 大会上披露，NGA 另授予 Palantir 2,800 万美元合同，以扩大 NGA 分析员对 MSS 的访问[@mv_meritalk_nga]。

第六步是企业协议整合。2025 年 7 月 31 日（8 月 1 日公告；也有来源称 8 月），陆军与 Palantir 签订为期 10 年、上限 100 亿美元的企业协议（EA），整合 75 份合同（15 份主合同和 60 份相关合同），陆军称 100 亿美元是上限而非"具体支出承诺"[@mv_wt_ea,mv_ds_ea]。2026 年 3 月的 Feinberg 备忘录随即规定所有 MSS 合同转入这一载体（见下文）。

!table t_mv_contracts|Palantir MSS 合同链条（2024—2026）|本报告据 DefenseScoop、DoD 合同公告、GovConWire、MeriTalk、Marines.mil 等整理；上限不等于实际拨付|22,34,30,74
日期|客户与载体|金额|范围与说明
2024-05-29|陆军 ACC-APG，IDIQ W911QX-24-D-0012，固定价格|上限 4.8 亿美元|MSS 原型扩展至 5 个作战司令部和联合参谋部"数千用户"，至 2029-05-28[@mv_ds_2024_05]
2024-09|陆军 DEVCOM ARL，固定价格，5 年|约 0.998 亿美元|扩展至陆、空、天、海、陆战队五个军种[@mv_govconwire_arl]
2025-05-20|W911QX-24-D-0012 修改 P00005|追加 7.95 亿美元，上限约 12.75 亿美元|新增软件许可，非新增范围[@mv_globalsec_contract,mv_ds_2025_05]
2025-05|NGA|0.28 亿美元|扩大 NGA 分析员 MSS 访问[@mv_meritalk_nga]
2025-07-31|陆军企业协议（EA），10 年|上限 100 亿美元（整合 75 份合同）|2026 年起成为全部 MSS 合同的载体[@mv_wt_ea,mv_ds_ea]
2025-08-15 敲定|海军陆战队企业许可（经 CDAO、DIU、ARL）|未披露|在 SIPRNet（IL6 云）上无限量访问[@mv_usmc_release,mv_ds_usmc]
2026-03-09|Feinberg 备忘录（政策指令）|—|MSS 转正式项目；合同统一转入陆军 EA[@mv_ds_feinberg1]
2026-08（未证实）|据报陆军 PEO IEW&S|"最高 6.18 亿美元、5 年"|仅见聚合站，可能与 2024-12 陆军 Vantage 6.189 亿美元混淆（弱源，待核）[@mv_govly]
!end

【分析】把已知上限简单相加（约 12.75 亿 + 0.998 亿 + 0.28 亿），MSS 专属合同上限约 14 亿美元，不含陆战队未披露金额和未证实的 6.18 亿美元。但上限不等于拨付，更不能与陆军 EA 的 100 亿美元相加。Feinberg 备忘录之后，新的 MSS 采购将以 EA 下订单的形式出现，可能不再有独立的合同公告，公开追踪难度会明显上升。从财务表现看，Palantir 美国政府收入 2025 年同比增长 55%，2026 年上半年增速升至 84%—90%，与 MSS 上限扩大、陆军 EA、陆战队许可和伊朗战事期间用户激增在时间上吻合，但这只是相关，不是已证实的因果[@mv_pltr_q4_2025,mv_pltr_q2_8k]。

### 北约采购：MSS NATO

2025 年 3 月 25 日，北约通信与信息局（NCIA）与 Palantir 完成"MSS NATO"采购，供盟军作战司令部（ACO，即欧洲盟军最高司令部 SHAPE）使用；4 月 14 日对外公布[@mv_ncia_2025,mv_shape_2025]。从提出需求到签约只用了约 6 个月，北约称这是其历史上最快的采购之一；合同金额未公开，计划签约后约 30 天内部署[@mv_shape_release,mv_defupdate]。北约给出的用途是情报融合与目标定位、战场态势感知与规划、加速决策，系统包含大语言模型、生成式 AI 和机器学习，SHAPE 还计划接入新的 AI 模型和建模仿真工具[@mv_shape_release,mv_defensepost_nato]。Breaking Defense 指出，这一采购发生在跨大西洋关系紧张的背景下[@mv_bd_nato_2025]。

此后 MSS NATO 先后部署到 SHAPE 和布林森联合部队司令部（JFC Brunssum），诺福克联合部队司令部（JFC Norfolk）预计在 2026 年 4—5 月接入[@mv_janes_norfolk]。2026 年 6 月 22 日，MSS NATO 达到全面作战能力（FOC），获准在北约机密网络上运行，数据存放在北约自有的数据中心；系统在 2025 年全年进行测试，并经"坚定威慑 2026"（Steadfast Deterrence 2026）演习检验，6 月 30 日对外公布[@mv_shape_foc,mv_janes_foc]。欧洲也有评论认为，MSS NATO 意味着美国软件正在影响欧洲的军事决策，涉及主权问题[@mv_escudo_europe]。

### Feinberg 备忘录：从"原型"到全军正式项目

2026 年 3 月 9 日，国防部常务副部长史蒂夫·范伯格（Steve Feinberg）签发备忘录，对 MSS 的地位作出根本性调整，主要内容有四点[@mv_ds_feinberg1,mv_ds_feinberg2,mv_csis]：一是 MSS 须在 2026 财年结束（2026 年 9 月 30 日）前成为正式采购项目；二是由负责研究与工程的副部长（USD(R&E)）和负责情报与安全的副部长（USD(I&S)）牵头，在 30 天内把 MSS 的系统管理、监督、支持活动及相关职责从 NGA 移交给 CDAO 新设的 MSS 项目办公室；三是所有 MSS 合同转入"现有的陆军企业协议（EA）合同载体"，今后对 Palantir 的合同行动由陆军负责；四是由 USD(R&E) 接替 NGA，担任 MSS 及其商业云基础设施的授权官（AO）。备忘录还要求国防部首席技术官埃米尔·迈克尔（Emil Michael）评估是否把 MSS 纳入拟设的 CJADC2 项目办公室[@mv_ds_feinberg1]。

DefenseScoop 报道称，这份指令把"AI 赋能决策"定为 CJADC2 的"基石"[@mv_ds_feinberg1]；各部门面临"激进"的过渡时间表，有官员认为运行授权（ATO）是瓶颈，全面完成可能需要 18 个月，专家也表示这次重大转变的"全部影响仍不清楚"[@mv_ds_feinberg2]。{red:日期冲突}：DefenseScoop 和 CSIS 给出的签署日期是 3 月 9 日，路透社约在 3 月 20—23 日报道了这封信，倡导团体 Capture Cascade 的时间线写作 3 月 21 日；后者应为报道日期而非签署日期[@mv_govconwire_por,mv_capture]。

2026 年 8 月 5 日，陆军上校莫莉·索尔斯伯里（Molly Solsbury，ai.mil 简历页写作 Melissa）被任命为 CDAO 内的 MSS 项目主任；她此前任职于陆军参谋长办公室，任命目标是推动 MSS 成为核心指挥控制资产[@mv_ds_solsbury,mv_aimil_solsbury]。根据其简历，CDAO 此时已隶属 USD(R&E)。外界评论称，国防部对如何走出"碎片化部署"披露甚少[@mv_ds_solsbury]。

关于转制是否按期完成，{red:截至 2026 年 10 月未见国防部或 CDAO 的正式确认}。Motley Fool（2026 年 8 月 25 日）称 Maven"现已成为"正式项目[@mv_motley_por]，Palantir 管理层在 2026 年二季度财报电话会上称"首个正式项目本季度在平台上启动"[@mv_cnbc_q2,mv_fool_q2]，但其他媒体仍以"过渡中"描述[@mv_govconwire_por]。

### 2026 年现状：全军"万能应用"

到 2026 年秋，MSS 已成为国防部事实上的 AI 赋能指挥控制与目标定位骨干。用户规模方面，2025 年 5 月 NGA 局长惠特沃斯称 Maven 已向所有军种和作战司令部开放，活跃用户超过 2 万，覆盖 35 个以上工具、3 个安全域，增至 2024 年 3 月时的四倍以上（另一报道口径为"自 2025 年 1 月以来翻了一倍多"[@mv_ds_2025_05]），模型时延在列为正式项目后一年内改善了 80%[@mv_bd_geoint2025,mv_ecs_maven]。2026 年 9 月 22 日，负责研究与工程的副次长詹姆斯·马佐尔（James Mazol）在 DefenseTalks 会议上表示，MSS 用户从 2026 年 1 月的约 5 万人增至"史诗怒火"行动开始后的 10 万人以上，并正在推广到所有作战司令部和国民警卫局；CDAO 卡梅伦·斯坦利（Cameron Stanley）称 Maven 在"史诗怒火"行动 38 天中帮助打击了 13,000 个目标，并正在扩展到后勤、供应链、战备和预算数据[@mv_ds_mazol,mv_defpost_2026]。《国防一号》据此称 Maven 正在成为五角大楼的"万能应用"（everything app），据 CDAO 称已取代"6、8、10 个"旧系统[@mv_d1_everything]。陆军联合兵种司令部也已把"Maven C2 智能系统"纳入训练和院校教育体系[@mv_army_cac]。

!fig c_maven_scale|c_maven_scale.png|MSS 用户数增长与 Palantir MSS 合同上限/预算|本报告依据 Breaking Defense、DefenseScoop、FY2027 预算文件绘制|160

【用户口径说明】上述用户数存在口径差异：2025 年的"2 万以上"是 NGA 所称"活跃用户"；另有二手来源称 2025 年 Maven 覆盖 130 多个站点、约 2.5 万人（弱源，待核）[@mv_hvylya]；还有聚合站称 2026 年 3 月有 2 万多活跃用户[@mv_govly]，与马佐尔所说"1 月约 5 万"冲突，可能是"注册用户"与"活跃用户"之别。图 {fig:c_maven_scale} 采用官方口径。

与此同时，MSS 的大模型层出现了重大不确定性。据报道，Anthropic 的 Claude 于 2024 年末通过 Palantir 接入 Maven[@mv_aca_iran]；2026 年 3 月 4 日，国防部据报把 Anthropic 列为"供应链风险"，要求 6 个月内淘汰其工具，起因是 Anthropic 拒绝把模型用于大规模国内监控和完全自主武器；但 Palantir 首席执行官卡普随后在 CNBC 上表示 Claude 仍在目标系统中运行[@mv_aca_iran,mv_ie_claude]。替换是否完成、由谁接替，截至本报告未见一手确认（详见第二节）。

### 大事年表

!table t_mv_chronology|Project Maven / MSS 大事年表（2017—2026.10）|本报告据各条所列来源整理|24,100,36
日期|事件|来源
2017-04-26|常务副部长沃克签署备忘录，成立算法战跨职能小组（Project Maven），首个任务是无人机 FMV 的处理、利用和分发|[@mv_work_memo,mv_globalsec]
2017 年中|成立约两个月内获国会约 7,000 万美元|[@mv_wiki_maven]
2017-07|项目方宣布年底前向战区部署算法|[@mv_techsparx]
2017-12|首个算法（ScanEagle FMV 物体识别）部署中东，SOCOM 分析员使用；AFRICOM 同期开始使用|[@mv_nextgov_2017,mv_bd_2018_africa]
2017—2018|谷歌经 ECS 分包参与；Clarifai 为 ECS 分包商|[@mv_intercept_emails,mv_forbes_startups]
2018-03 至 06|谷歌员工请愿（约 4,000—4,600 人签名）与辞职|[@mv_gizmodo_au_resign,mv_fortune_2018]
2018-06-01 前后|谷歌云 CEO 格林宣布合同 2019-03 到期后不续约|[@mv_nbc_google]
2018-12|沙纳汉调任 JAIC 首任主任|[@mv_wiki_maven]
2019—2020|微软（约 3,000 万美元）、AWS（约 2,000 万美元）获 ECS 分包（关联系推断）|[@mv_forbes_2021]
2020 起|XVIII 空降军"猩红之龙"系列演习，与多达 70 家公司把 Maven 发展为 MSS|[@mv_d1_2024_08,mv_cset_coalition]
2022-04|NGA 宣布接管 Maven 的 GEOINT AI 服务（约 80%），FY2023 生效|[@mv_bd_2022_nga,mv_c4isr_2022]
2022 起|XVIII 空降军用 MSS 为乌克兰生成目标情报|[@mv_lawfare_book,mv_kyivind]
2022-10|移交因持续决议案推迟|[@mv_ds_2022_cr]
2023-11-02 / 11-07|NGA Maven 宣布并正式成为采购项目（软件采购路径）|[@mv_dd_por]
2023-12 / 2024-02|CJADC2 最小可行能力经 GIDE 认证并公布，MSS 为事实骨干|[@mv_ds_cjadc2_mvc]
2024-02-02|CENTCOM 在伊拉克、叙利亚 85 次以上打击中用 Maven 缩小目标范围|[@mv_register_2024]
2024-03|FY2025 预算把 Maven 经费调整到 CDAO PE 0606135D8Z；AI 开发流水线全部交给 NGA|[@mv_ds_2024_03]
2024-05-29|陆军授予 Palantir 4.8 亿美元 MSS 原型 IDIQ|[@mv_ds_2024_05]
2024-07-29|NGA 授予 Scale AI 约 2,400 万美元 Maven 数据标注过渡合同|[@mv_nga_contracts]
2024-09|ARL 授予 Palantir 约 9,980 万美元，MSS 扩展至五个军种|[@mv_govconwire_arl]
2024 年末|据报 Claude 经 Palantir 接入 Maven|[@mv_aca_iran]
2024-12-06|Anduril 与 Palantir 宣布合作，拟把 Lattice 与 MSS、AIP 结合|[@mv_ds_anduril_palantir]
2025-03-25 / 04-14|北约 NCIA 采购 MSS NATO，约 6 个月完成|[@mv_ncia_2025,mv_shape_2025]
2025-05|惠特沃斯：活跃用户 2 万以上、35 个以上工具、3 个安全域；MSS 上限追加 7.95 亿美元至约 13 亿美元|[@mv_bd_geoint2025,mv_ds_2025_05]
2025-07-31|陆军与 Palantir 签订 10 年、上限 100 亿美元企业协议|[@mv_wt_ea]
2025-09-10 / 09-12|陆战队企业许可公布，MSS 成为标准火力与效果集成平台|[@mv_ds_usmc,mv_ds_maradmin]
2025-11|Enabled Intelligence 赢得 NGA 最高 7.08 亿美元 SEQUOIA 数据标注合同|[@mv_bd_sequoia]
2026-02-28 起|"史诗怒火"行动（对伊朗），MSS 被大规模用于目标定位；首日发生 Minab 学校遇袭|[@mv_aca_iran,mv_bloomberg_minab]
2026-03-04|据报国防部把 Anthropic 列为供应链风险，6 个月内淘汰|[@mv_aca_iran]
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
MSS 的功能可以用一句话概括：把分散在上百个数据源里的情报"对象化"后摆在同一张图上，再用一块看板把每个目标从"发现"推到"评估"，中间由人逐一批准。它的核心不是某个识别算法，而是把检测、目标管理、资产比较、火力交接和效果评估串成一条可追踪、可加速的流水线；2024 年以后又叠加了以大模型为核心的自然语言代理。需要注意的是，公开资料对各模块的描述详略悬殊，看板与资产比较有厂商和智库资料支撑，而武器—目标配对算法、BDA 和 COA 生成几乎没有权威细节。
:::

### 总体定位：从"传感器到射手"的决策支持平台

北约对 MSS NATO 的官方描述，是目前对 MSS 功能最权威的概括："AI 赋能的作战系统"，用大语言模型、生成式 AI 和机器学习进行情报融合、目标定位、战场态势感知、作战计划和加速决策；它把来自多个来源（涉密和公开）的结构化与非结构化数据汇入一个统一、可搜索的平台，开放架构可接入第三方 AI 模型、仿真工具和应用[@mv_shape_release,mv_bd_nato_2025]。2024 年陆军合同公告对美方 MSS 的描述则更偏目标定位：接入卫星图像、地理定位等数据，检测潜在目标，支撑 CJADC2[@mv_ds_2024_05]。海军陆战队 2025 年的 MARADMIN 电报把 MSS 定为跨多个作战司令部的标准"火力与效果集成平台"（fires and effects integration platform）[@mv_ds_maradmin]。

综合这三种表述，MSS 的功能定位有三个关键词：一是"融合"，即把多源数据汇到一个平台；二是"目标"，即围绕目标定位流程组织工作；三是"决策支持"，即系统给出检测、排序和建议，打击决定由人作出。官方和主流报道一致把 MSS 定位为决策支持工具，目标由人类指挥官批准[@mv_csis]。

!photo mss_ngb|国民警卫局人员在培训中学习使用 Maven 智能系统，画面中可见 MSS 地图界面。2026 年起 MSS 被推广至国民警卫局|美国国民警卫局，公有领域

### 多源情报融合：179 个数据源

据 CSIS 报道，中央司令部 2024 年的 MSS 部署接入了 **179 个不同数据源**，业内人士称此后数量还在增加[@mv_csis]。卫星来源既包括国家侦察卫星，也包括 ICEYE、Capella Space 等商业合成孔径雷达（SAR）卫星；此外还接入信号情报，包括截获的通信和电子辐射[@mv_csis]。GlobalSecurity 根据 Palantir 的公开演示给出的数字是"150 个以上数据源"（弱源，待核）[@mv_globalsec]。

数据融合的意义在于消除"烟囱"。在传统流程中，图像情报、信号情报、人力情报和友军态势分属不同系统、不同密级、不同部门，目标分析员需要在多个终端之间来回切换、人工比对。MSS 把这些数据统一映射到平台的数据模型中（见第三节"本体"），使同一目标的图像、信号、历史记录和地理信息可以在一个对象下关联查询。有描述称，无人机执行任务时，其位置数据和实时视频会实时回传到 Maven（二手）[@mv_spatial]。但{red:全动态视频（FMV）的接入方式、友军跟踪（BFT）的接入方式，均没有找到权威公开说明}。

### 计算机视觉检测与"对象化"

MSS 的计算机视觉能力有两个来源：一是 NGA Maven 流水线训练和认证的 GEOINT 模型，二是通过开放架构接入的第三方模型。无论来源如何，检测结果都以"对象"的形式写入平台，而不是停留在一张标了方框的图片上。Palantir 在北约工业日的示例说明了这一机制：一个外部 AI 系统（Safran.AI）生成的目标检测被导入 MSS，可以在共用作战图中直接调查，也可以交给 AIP 代理使用；用户用自然语言提问，例如"Show me detections of Tu-22s"（显示图-22 的检测结果），代理随后在由 12,000 个 Safran.AI 检测对象组成的对象集中查询[@mv_palantir_blog_nato,mv_csis]。

【分析】"对象化"是理解 MSS 的关键。检测结果一旦成为对象，就可以带上属性（类型、置信度、时间、来源模型）、与其他对象建立链接（某检测对应某已知设施、某车辆属于某部队），并成为后续工作流动作（提名为目标、分配打击资产）的操作对象。这意味着识别模型本身可以替换——Palantir 控制的是对象模型和工作流，模型供应商只需按接口输出检测对象。这种"平台加可插拔模型"的结构，是 MSS 能在 2024 年后迅速吸纳第三方模型、乃至在 2026 年更换大模型供应商的技术前提。

### 共用作战图（COP）

MSS 提供地图式共用作战图。有二手描述称，其 COP 是一个三维地球视图，叠加卫星、无人机、信号情报和既有地图数据[@mv_spatial]。在北约演示中，第三方检测对象可以直接在 COP 中调查[@mv_palantir_blog_nato]。COP 是 MSS 中各类对象的空间呈现层：检测结果、已知设施、禁打目标、友军打击资产都在同一张图上显示，使目标分析员能直观判断目标与资产之间的距离和关系。

### Target Workbench：看板式目标工作流

MSS 中最具辨识度的模块是 Target Workbench（目标工作台）。Palantir 的产品资料称，其界面以类似 **看板（Kanban）** 的形式组织：各列对应目标定位流程的各个阶段，阶段名称可以按单位自身的流程术语定制；系统支持 **禁打清单（No-Strike List，NSL）** 集成[@mv_target_workbench]。在这种界面中，每个目标是一张"卡片"，随着分析、核查、审批、交战和评估的推进，在列与列之间流转；指挥员和参谋可以一眼看到每个阶段积压了多少目标、哪些目标卡在哪一步。

!fig d_maven_workflow|d_maven_workflow.png|Target Workbench 看板式目标工作流（按 F2T2EA 阶段对照）|本报告依据 Palantir Target Workbench 产品说明、CSIS、CSET 资料整理绘制|160

有分析描述了看板的实际运作：检测结果被"提名"上看板，再从看板为目标分派最合适的资产，优化因素包括到达目标时间、燃油、弹药和距离；整个传感器到射手链路可以概括为"检测 → 行动方案（COA）→ 资产选择 → 打击 → BDA"（弱源，待核）[@mv_cybershafarat,mv_battlepolicy]。看板也不限于 MSS 本身：在陆军下一代指挥控制（NGC2）的"常春藤之刺 1"实弹演习（2025 年 9 月）中，第 4 步兵师在 Anduril 的 Lattice 网格上运行 Palantir Target Workbench，用它管理、跟踪每个目标并为其分配资源[@mv_bd_ivysting]。

【分析】看板式设计的作战含义值得重视。传统联合目标定位流程（JP 3-60）中，目标从提名到批准要经过多级会议和文书；看板把这一流程"可视化、并行化"，使一个小团队能同时处理大量处于不同阶段的目标。这正是"20 人顶 2,000 人""每小时 30 个到 80 个"等效率数字背后的机制。但并行化也意味着单个目标获得的人工注意力减少，这是后文讨论自动化偏见风险的出发点。

### 资产比较与武器—目标配对

CSIS 根据国防部演示描述了一个典型操作流程：操作员选中 AI 检测到的目标，按到达时间、距离、燃油等约束比较附近的打击资产，下令打击，再通过情报、监视与侦察（ISR）跟踪打击效果[@mv_csis]。这就是 MSS 的"资产比较"或"武器—目标配对"功能。2026 年伊朗战事中，据美国官员称五角大楼依靠 Maven 识别最高优先级目标并帮助选择武器[@mv_aca_iran]。

【分析】从现有描述看，MSS 中的"武器—目标配对"更像基于约束（时间、距离、燃油、弹药）的资产推荐与比较，而不是传统意义上的武器—目标分配优化算法。{red:配对算法的具体实现、是否考虑毁伤概率和附带损伤估计，均没有权威公开说明}。

### 火力交接：与 AFATDS 等火控系统的衔接

目标排序和资产选择完成后，打击任务需要交给实际的火力系统执行。有二手分析称，Target Workbench 对目标排序后，把数据传给先进野战炮兵战术数据系统（AFATDS）等火力支援系统（弱源，待核）[@mv_battlepolicy]。分析人士本·范鲁（Ben Van Roo）认为，在"分配并射击"环节，射击诸元由 AFATDS 和弹道计算完成，大模型在这部分几乎不起作用[@mv_vanroo]。这意味着 MSS 不直接控制武器，而是把"打什么、用什么打"的决策结果交给存量火控系统。{red:MSS 与 AFATDS、TAK 的官方接口说明均未找到}。

### 毁伤评估（BDA）

在 CSIS 描述的流程中，打击之后通过 ISR 跟踪效果，即毁伤评估（BDA）[@mv_csis]。在看板上，BDA 对应最后一列：目标卡片在获得评估结果后，或者关闭，或者退回前列重新打击。但{red:没有找到 BDA 模块的具体实现描述}，例如是否由计算机视觉自动比对打击前后图像、评估结论如何回写目标对象等。

### AIP 大模型代理与 Claude 争议

2023 年起，Palantir 把其人工智能平台（AIP）的大模型代理能力引入防务产品。CSIS 特别提醒，Palantir 2023 年的"AIP for Defense"演示展示的是计划中的未来能力和示意场景，不能等同于已部署的功能[@mv_csis]。在已证实的层面，北约演示中 AIP 代理可以用自然语言检索检测对象集[@mv_palantir_blog_nato]；北约也明确称 MSS NATO 包含大语言模型和生成式 AI[@mv_shape_release]。

关于大模型在美军 MSS 中的具体作用，报道分歧很大。多家媒体报道，Anthropic 的 Claude 通过 Anthropic 与 Palantir 的合作，于 2024 年末接入 Maven，用于目标优先级排序和分析[@mv_rs_iran,mv_aca_iran]。《华盛顿邮报》2026 年 3 月 4 日报道称，在对伊朗作战中，内嵌 Claude 的 MSS 给目标排序、生成坐标并建议武器[@mv_wapo_2026]；二手转述还称其生成法律依据草稿[@mv_wapo_2026]，以及"Claude 提出了数百个目标，进行优先排序并给出精确坐标，再由人类指挥官批准"（转述华邮和《自然》）[@mv_strat_intl]。但"和平愿景"（Vision of Humanity）的说法要克制得多：Claude 主要用于把情报报告转成通俗语言[@mv_voh]。

Claude 的现状同样存在冲突。据报道，国防部于 2026 年 3 月 4 日把 Anthropic 列为"供应链风险"，要求 6 个月内淘汰，起因是 Anthropic 拒绝把模型用于大规模国内监控和完全自主武器；OpenAI 等公司据报接替其角色；但 Palantir 首席执行官卡普在 CNBC 上称 Claude 仍在目标系统中运行[@mv_aca_iran,mv_ie_claude]。另有说法提及 2026 年 2 月 28 日的行政令要求六个月内完成过渡[@mv_ie_claude]。倡导团体 Capture Cascade 在 MSS 转正式项目的条目标题中直接写出"Claude 依赖"（弱源，待核）[@mv_capture]。{red:Claude 在 MSS 中的具体角色、是否已被替换、由谁接替，均无法从五角大楼或 Anthropic 的一手文件中证实}。

【分析】无论 Claude 的具体角色如何，可以确认两点：其一，MSS 的大模型层是可替换的，这与"平台加可插拔模型"的架构一致；其二，大模型在 MSS 中的主要价值在"信息整理与排序"这一侧（检索、摘要、排序、生成草案），而在射击诸元解算这一侧几乎不起作用。战事期间按 token 计的使用量激增（日峰值增长 4,425%，最高约 200 亿 token/天，见第四节）说明大模型已深度嵌入日常参谋工作[@mv_bd_insatiable]。

### NGA 机器生成情报标注与"推理"能力

NGA Maven 一侧的功能重点是 AI 情报产品的生产与治理。NGA 局长惠特沃斯 2025 年 6 月称，NGA 在所有 AI 生成的产品上加注"machine-generated GEOINT"（机器生成的地理空间情报）模板标签，在这类模板化产品的分发过程中"没有人工经手"（no human hands）；标签注明 AI 参与的类型和程度，NGA 可能是 18 个情报界成员中第一个常规化使用此类标签的机构[@mv_bd_nohands]。惠特沃斯还表示，Maven 的下一阶段要加入"推理"能力，从识别物体发展到预测和发现威胁；但在向作战司令或总统汇报前，仍需要人工佐证[@mv_meritalk_nga,mv_execgov_predict]。

【分析】"机器生成"标签是目前公开可见的、少有的针对 AI 情报产品的制度化治理措施。它把"AI 参与了多少"作为产品元数据随情报流转，使下游用户可以据此调整信任程度。但它主要适用于 NGA 的 GEOINT 产品；MSS 中目标卡片上的 AI 贡献是否有类似标注，没有公开信息。

### 非作战扩展：五角大楼的"万能应用"

2026 年，MSS 的应用范围明显超出目标定位。CDAO 斯坦利称 MSS 正扩展到后勤、供应链、战备和预算数据[@mv_ds_mazol]。《国防一号》称 Maven 正在成为五角大楼的"万能应用"，据 CDAO 称已取代"6、8、10 个"旧系统[@mv_d1_everything]。陆军联合兵种司令部把"Maven C2 智能系统"纳入训练和院校教育[@mv_army_cac]；国民警卫局也在推广范围之内[@mv_ds_mazol]。

!photo mss_contracting|萨姆休斯顿堡的合同人员在作战演习中使用 AI 与 Maven 智能系统进行仿真。MSS 的使用者已从目标分析员扩展到后勤、合同等保障领域|美国陆军，公有领域

【分析】从"目标工厂"到"万能应用"的扩展，与 Palantir 平台的通用性直接相关：本体既可以描述目标和打击资产，也可以描述零备件、预算科目和战备状态。对国防部而言，这意味着一个平台同时承载作战与管理数据，降低了跨领域关联分析的门槛；对供应商而言，则意味着锁定从作战领域蔓延到整个部门的业务系统。

### 跨梯队与联盟协同

MSS 的用户覆盖从作战司令部、军种到联盟层级。2025 年 5 月，NGA 称 Maven 通过 35 个以上军种和作战司令部工具、跨三个安全域服务约 2 万名活跃用户[@mv_bd_geoint2025]。联盟层面，MSS NATO 部署在 SHAPE 和布林森联合部队司令部，诺福克联合部队司令部随后接入[@mv_janes_norfolk]。乌克兰是美方目标情报的接收方而非 MSS 的直接用户：据《纽约时报》报道，乌方使用的是不依赖美国敏感情报的版本[@mv_kyivind]。{red:MSS 的联盟"可释放性"（releasability）机制，即按标签控制哪些数据可以共享给哪些盟友，没有找到公开细节}。

### 功能模块拆解

!table t_mv_modules|MSS / NGA Maven 功能模块拆解|本报告据北约、CSIS、Palantir 资料及媒体报道整理|26,74,30,30
模块|功能描述|证据等级|主要来源
多源情报融合|CENTCOM 2024 年部署接入 179 个数据源（另有 150 个以上说法），含国家侦察卫星、ICEYE/Capella 商业 SAR、信号情报|智库；二手|[@mv_csis,mv_globalsec]
CV 检测与对象化|外部模型检测结果作为对象写入平台；北约演示中 12,000 个 Safran.AI 检测对象组成对象集|厂商|[@mv_palantir_blog_nato]
共用作战图（COP）|地图式 COP，据称为三维地球视图，叠加卫星、无人机、SIGINT 与地图数据|二手|[@mv_spatial]
Target Workbench|看板式界面，列对应目标定位阶段，阶段名可定制；集成禁打清单|厂商|[@mv_target_workbench]
资产比较与配对|按到达时间、距离、燃油等约束比较附近打击资产并下令打击|智库（据国防部演示）|[@mv_csis]
火力交接|排序后目标交 AFATDS 等火力系统；射击诸元由 AFATDS 解算|二手；分析人士|[@mv_battlepolicy,mv_vanroo]
毁伤评估（BDA）|通过 ISR 跟踪打击效果；无模块级细节|智库|[@mv_csis]
AIP 大模型代理|自然语言检索、排序、COA 草案；Claude 角色有争议|厂商；多源有争议|[@mv_palantir_blog_nato,mv_wapo_2026,mv_voh]
机器生成情报标注|NGA 产品加注 machine-generated GEOINT 标签，注明 AI 参与程度|官方|[@mv_bd_nohands]
推理与威胁预测|从识别物体走向预测威胁；汇报前需人工佐证|官方（规划）|[@mv_meritalk_nga]
非作战扩展|后勤、供应链、战备、预算；取代 6—10 个旧系统|官员|[@mv_d1_everything,mv_ds_mazol]
联盟协同|MSS NATO 在北约机密网络运行；乌克兰为情报接收方|官方；媒体|[@mv_shape_foc,mv_kyivind]
!end

### 与 F2T2EA 杀伤链对照

美军通用的动态目标定位流程可以概括为"发现—定位—跟踪—瞄准—交战—评估"（F2T2EA）六步。把 MSS 已知功能逐一对照这六步，可以看出它在杀伤链中覆盖了从发现到评估的全部环节，但各环节的自动化程度和证据充分程度差别很大（见{tab:t_mv_f2t2ea}）。

!table t_mv_f2t2ea|MSS 功能与 F2T2EA 杀伤链对照|本报告分析整理，各环节证据见所列来源|20,52,40,48
F2T2EA 环节|MSS 对应功能|自动化程度（分析）|证据情况
发现（Find）|179 个以上数据源融合；CV 模型自动检测并对象化|高：检测由机器完成|智库与厂商资料较充分[@mv_csis,mv_palantir_blog_nato]
定位（Fix）|地理定位、生成坐标；据报 Claude 生成精确坐标|中高：机器给出坐标，人工核对|坐标生成见于媒体报道，有争议[@mv_wapo_2026,mv_strat_intl]
跟踪（Track）|COP 持续显示目标与活动；无人机位置与视频回传|中：依赖传感器持续覆盖|仅二手描述[@mv_spatial]
瞄准（Target）|看板上的目标核查、禁打清单比对、优先级排序；人工逐一批准|中：机器排序，人工审批|厂商资料与一线访谈[@mv_target_workbench,mv_bloomberg_2024]
交战（Engage）|按时间、距离、燃油比较打击资产；交 AFATDS 等火控|低到中：资产推荐，射击诸元由火控系统解算|智库与二手[@mv_csis,mv_vanroo]
评估（Assess）|ISR 跟踪打击效果，目标卡片关闭或回流|未知|无模块级细节[@mv_csis]
!end

【分析】对照表显示，MSS 的自动化重心在杀伤链前段（发现、定位）和中段的"组织与排序"，交战环节仍依靠存量火控系统，评估环节公开信息最少。换言之，MSS 压缩的主要是"人找目标、人排目标、人比资产"的时间，而不是"武器飞行和毁伤"的时间。这也解释了为什么其效率指标多以"每小时批准多少目标""多少人完成多少工作"来表述。

### 功能层面的公开空白

以下功能没有找到权威公开描述：全动态视频的接入方式；友军跟踪的接入方式；BDA 模块实现；COA 生成算法；武器—目标配对算法；联盟可释放性与标签化数据访问控制机制；MSS 与 TAK、AFATDS 的官方接口[@mv_csis]。CSET 在其报告中明确表示不公开 MSS 的具体作战细节[@mv_cset_coalition]。因此，本节对上述模块的描述，均应视为"已知存在、细节不明"。

## （三）架构设计：本体驱动的平台、NGA 模型流水线与三个安全域

:::lead
MSS 的架构可以理解为"Palantir 平台加可插拔的模型与数据"：Palantir 控制数据集成、本体与工作流应用，NGA 控制模型的标注、训练与认证，第三方的计算机视觉、商业 SAR 和大模型供应商可以替换，国防部通过 CDAO 项目办公室和陆军企业协议实施治理。本节按七层逐层拆解，并简要对比 Palantir 本体与 Anduril Lattice 实体模型的差异。需要强调：公开资料足以勾勒层次，但 MSS 具体采用 Foundry 还是 Gotham 的组合、托管在哪家云、是否存在绝密网络实例等关键细节，均未得到证实。
:::

!fig d_maven_arch|d_maven_arch.png|Maven / MSS 七层架构|本报告依据 Palantir 官方文档、NGA 合同公告、CSIS、DefenseScoop、SHAPE 等资料整理绘制|160

如图 {fig:d_maven_arch} 所示，本报告把 Maven/MSS 拆为七层：数据源层、NGA Maven 模型流水线、Palantir 平台层、工作流应用层、AIP/大模型代理层、部署与安全域层、治理与合同层。前五层是"技术栈"，后两层是"运行环境与制度框架"。这一分层是本报告依据公开资料所做的归纳，并非官方架构文件。

### 第一层：数据源

数据源层是 MSS 的输入端。已知来源包括国家侦察卫星和 ICEYE、Capella Space 等商业 SAR 卫星，信号情报（截获通信、电子辐射），无人机及其全动态视频，以及既有数据库和地图数据；CENTCOM 2024 年部署时共接入 179 个数据源[@mv_csis]。北约版本同样强调接入涉密和公开、结构化和非结构化的多源数据[@mv_shape_release]。

数据源层也是 MSS 最大的风险来源之一。2026 年 Minab 学校遇袭事件表明，平台本身不会自动发现底层数据库中的过期记录：该地点在旧数据库中仍被标为伊斯兰革命卫队设施，输入 Maven 后被列为推荐目标（详见第五节）[@mv_bloomberg_minab]。Palantir 事后表示自己"不对底层数据负责"[@mv_gizmodo_minab]。【分析】这说明在 MSS 的架构中，数据质量责任仍分散在各情报来源单位，平台只负责汇聚和呈现，二者之间缺少系统性的"数据保鲜"机制。

### 第二层：NGA Maven 模型流水线

2022 年拆分后，整个 Maven"AI 开发流水线"交给 NGA[@mv_ds_2024_03]。这条流水线由三个环节构成：数据标注、系统集成与模型互操作、模型评估认证。

**数据标注**是计算机视觉模型的基础。2024 年 7 月 29 日，NGA 授予 Scale AI 约 2,400 万美元、为期一年的固定价格合同"NGA Maven 数据标注服务过渡"（合同号 HM047624C0047）；NGA 另一条公告写的是"修改 2,400 万美元后总值 1.3 亿美元"，两者关系不明[@mv_nga_contracts]。2024 年 9 月，NGA 宣布约 7 亿美元的数据标注竞标，同时推动标准化建模[@mv_bd_2024_09_label,mv_d1_2024_09]。2025 年 11 月，初创公司 Enabled Intelligence 赢得名为 SEQUOIA 的"AI/ML 数据标注即服务"合同，单一授标 IDIQ，上限 7.08 亿美元，订货期最长 7 年，用于 GEOINT 计算机视觉的目标检测、跟踪和分类标注，合作方包括 BAE、Vantor 和 Whiteboard Federal；这是美国政府迄今最大的 AI 数据标注项目，也是 Maven 的基础能力[@mv_bd_sequoia,mv_ei_release]。落败的 Scale AI 先向 GAO 抗议被驳回（2026 年 1 月下旬），再起诉至联邦索赔法院，法院未推翻授标[@mv_orangeslices]。

**系统集成与模型互操作**由 ECS 承担。ECS 自 2017 年起担任 NGA Maven 项目的"AI 互操作集成商"（AI3）[@mv_execbiz_ecs]。

**模型评估认证**由 NGA 的 AGAIM 试点（GEOINT AI 模型认证/评估）承担，它提供一套标准的评估和风险管理流程。NGA 官方明确表示，不希望 AGAIM 变成"运行授权（ATO）式"的排队审批[@mv_fnn_agaim]。


【分析】把模型流水线放在 NGA 而把作战平台交给 CDAO 和 Palantir，形成了"模型由政府掌握、平台由商业公司提供"的分工。这种分工的好处是政府对训练数据和模型评估保有控制权，不至于完全依赖单一平台厂商；代价是两条线之间需要稳定的接口（检测对象写入本体），以及两个机构之间的协调成本。2026 年 MSS 管理权从 NGA 移交 CDAO 后，NGA 仍保留模型流水线，这一分工没有改变。

### 第三层：Palantir 平台（Apollo、Ontology、Foundry、Gotham、AIP）

平台层是 MSS 的核心，由 Palantir 的几个产品构成。

**Apollo** 是持续交付平台，负责管理承载 Foundry 和 AIP 服务的底层基础设施[@mv_palantir_platforms,mv_apollo_wp]。二手资料称 Apollo 可以运行在本地数据中心、边缘硬件和涉密网络上[@mv_mlq]。对军事用户而言，Apollo 的价值在于让同一套软件在非密云、秘密网、北约网络等多个隔离环境中保持版本一致、持续更新，而不必为每个环境单独开发和认证。

**Ontology（本体）** 把数据源映射为对象、属性和链接，并对"动作"（action）建模，支持把决策实时写回运营系统和边缘系统；边缘端可以用轻量的"嵌入式本体"（Embedded Ontology）记录决策，平台也能接入物联网和边缘数据流[@mv_palantir_ontology,mv_palantir_ontology_system]。在 MSS 中，检测结果、设施、目标、打击资产、禁打对象都可以是本体中的对象；"提名为目标""批准打击""分配资产"则是作用于对象的动作。

**Foundry、Gotham 与 AIP** 分别是 Palantir 的数据集成与分析平台、情报与防务平台、人工智能平台。{red:MSS 具体采用 Foundry 还是 Gotham 的组合，公开资料未证实}，本报告的分层推断是：数据和本体层在 Foundry/Gotham 中把传感器数据和检测结果对象化，AIP 提供大模型代理[@mv_csis]。值得一提的是，Palantir 在 Maven 之外长期为陆军提供情报数据平台：DCGS-A 第二能力包（2021 年下选 Palantir 建设基于 Gotham 的跨密级情报数据织网）和 2024 年的 TITAN 地面站原型（1.784 亿美元）都处在"情报到目标"链条上，与 MSS 形成衔接[@mv_bd_dcgsa,mv_ds_titan]。

### 第四层：工作流应用

工作流应用层是用户直接接触的界面，包括 COP 地图、Target Workbench 看板、资产比较与配对、BDA 跟踪等（见第二节）。这一层是开放的：2024 年 CDAO 启动的 Open DAGIR 计划，旨在把其他厂商的应用接入 MSS 的数据层，使 CJADC2 不必全部依赖 Palantir 自有应用[@mv_bd_opendagir]。Breaking Defense 也指出，2024 年公布的 CJADC2 最小可行能力是"最低限度"的[@mv_bd_opendagir]。

【分析】Open DAGIR 是国防部对"平台锁定"的一种制度回应：数据层由 Palantir 提供，但应用层向第三方开放。然而，第三方应用要读写的仍是 Palantir 的本体，平台层的锁定并未消除。

### 第五层：AIP / 大模型代理

AIP 层提供自然语言检索与问答、目标排序、行动方案草案和报告生成等能力[@mv_palantir_blog_nato,mv_csis]。这一层的模型供应商是可替换的：据报道 Claude 自 2024 年末接入，2026 年起因供应链风险认定而被要求淘汰，OpenAI 等公司据报接替[@mv_aca_iran]。【分析】从架构看，大模型不直接操作武器，而是作用于本体中的对象与动作：它可以查询对象集、生成排序和草案，但"批准打击"等动作仍需人在界面上执行。大模型层的风险主要在于生成内容的可追溯性——排序依据、坐标来源、法律依据草稿是否可审计，公开资料没有说明。

### 第六层：部署与安全域

NGA 称 Maven 跨"三个安全域"运行[@mv_bd_geoint2025]。原文没有说明具体是哪三个网络，推测为非密、秘密和绝密/敏感隔离信息（TS/SCI）三级，但{red:没有公开来源证实 MSS 在联合全球情报通信系统（JWICS）上有实例}。可以确认的部署形态有两个：一是海军陆战队通过企业许可，在 SIPRNet 影响等级 6（IL6）云上"无限量访问"MSS[@mv_ds_maradmin,mv_usmc_release]；二是 MSS NATO 在北约机密网络上运行，数据存放在北约自有的数据中心[@mv_shape_foc]。伊朗战事期间，五角大楼发言人称非密网使用量环比增长 38%、涉密网增长 89%，也印证了 MSS 同时运行在不同密级的网络上[@mv_bd_insatiable]。

{red:MSS 托管在哪家商业云（AWS、微软、甲骨文、谷歌）、是否经由联合作战云能力（JWCC）合同，均没有公开信息}。Feinberg 备忘录提到 USD(R&E) 将接任 MSS"商业云基础设施"的授权官，说明 MSS 至少部分运行在商业云上[@mv_ds_feinberg2]。MSS 在前沿战术节点、断连条件下的边缘部署，也没有找到权威公开描述。

### 第七层：治理与合同

治理层决定了"谁拥有、谁付钱、谁授权运行"。截至 2026 年 10 月，MSS 的治理框架是：CDAO 新设的 MSS 项目办公室负责系统管理与监督，项目主任为索尔斯伯里上校，CDAO 隶属 USD(R&E)[@mv_ds_solsbury,mv_aimil_solsbury]；所有合同经由陆军企业协议执行[@mv_ds_feinberg1]；USD(R&E) 担任商业云的授权官[@mv_ds_feinberg2]；首席技术官评估是否把 MSS 纳入拟设的 CJADC2 项目办公室[@mv_ds_feinberg1]。北约一侧由 NCIA 采办、SHAPE 运行 MSS NATO[@mv_ncia_2025]。NGA 保留 NGA Maven 模型流水线和 GEOINT 产品治理（机器生成标签、AGAIM）[@mv_bd_nohands,mv_fnn_agaim]。

!table t_mv_layers|Maven / MSS 七层架构要点|本报告据各层所列来源整理|28,82,50
层级|组成与机制|主要证据
① 数据源|国家与商业卫星（含 ICEYE、Capella SAR）、无人机 FMV、SIGINT、既有数据库；CENTCOM 2024 年 179 个数据源|[@mv_csis]
② NGA Maven 模型流水线|标注：Scale AI 过渡合同 → Enabled Intelligence SEQUOIA（上限 7.08 亿美元）；集成：ECS（AI3）；认证：AGAIM|[@mv_nga_contracts,mv_bd_sequoia,mv_execbiz_ecs,mv_fnn_agaim]
③ Palantir 平台|Apollo 持续交付；Ontology 对象—属性—链接—动作，可回写；Foundry/Gotham/AIP（具体组合未证实）|[@mv_palantir_platforms,mv_palantir_ontology]
④ 工作流应用|COP、Target Workbench、资产比较、BDA 跟踪；Open DAGIR 第三方应用|[@mv_target_workbench,mv_bd_opendagir]
⑤ AIP/大模型代理|自然语言检索、排序、COA 草案；Claude（有争议）→ OpenAI 等（据报）|[@mv_palantir_blog_nato,mv_aca_iran]
⑥ 部署与安全域|3 个安全域（NGA 口径）；陆战队 SIPRNet IL6 云；北约机密网与自有数据中心；云厂商未公开|[@mv_bd_geoint2025,mv_ds_maradmin,mv_shape_foc]
⑦ 治理与合同|CDAO MSS 项目办公室；陆军 EA；USD(R&E) 任授权官；北约 NCIA/SHAPE|[@mv_ds_feinberg1,mv_ds_feinberg2,mv_ncia_2025]
!end

### MSS 在 CJADC2 体系中的位置

从体系层面看，MSS 是美军"联合全域指挥控制"（CJADC2）的事实骨干。时任国防部常务副部长希克斯曾要求 CDAO 在 2023 年底前通过"全球信息主导实验"（GIDE）交付 CJADC2 的最小可行能力；该能力于 2023 年 12 月获认证、2024 年 2 月公布，重点是 11 个作战司令部之间的信息共享，应用包括联合火力网和一个"全球集成"工具[@mv_ds_mvp_2023,mv_ds_cjadc2_mvc,mv_nextgov_mvc]。此后 CDAO 推动 GIDE 吸纳更多工业界参与者，构建全球作战网络[@mv_bd_gide]。Breaking Defense 在 2024 年末的盘点中，把 CJADC2 与军事 AI 的进展概括为"安静的进步"[@mv_bd_killerapps]。

2026 年的 Feinberg 备忘录把"AI 赋能决策"定为 CJADC2 的基石，并要求评估把 MSS 纳入拟设的 CJADC2 项目办公室[@mv_ds_feinberg1]；FY2027 预算则把"Maven 智能系统与联合火力网"作为交付 CJADC2 的一个预算项列出[@mv_fy27_book]。【分析】这意味着在联合层级，MSS 承担"数据与决策平台"角色，联合火力网承担"火力协调"角色，二者组合构成 CJADC2 的作战核心。值得注意的是，{red:没有任何来源把 MSS 与"金穹"导弹防御直接挂钩}；有关"金穹"的报道只提到 Anduril 与 Palantir 两家公司共同开发其指挥控制软件层[@mv_reuters_goldendome]。

### Palantir 本体与 Lattice 实体模型的差异

由于 Palantir 与 Anduril 在陆军 NGC2 等项目中深度合作，两家的数据模型常被对照讨论。Palantir 本体以"对象—属性—链接—动作"为核心，面向企业级、长周期的数据整合和决策回写[@mv_palantir_ontology]。Lattice 则以"实体"为核心：每个航迹、资产、地理区域和信号都是一个实体，其全部数据由可选的类型化组件承载，如位置、运动学、军事视图（敌我属性）、本体模板、来源（provenance）、密级标记等；在实体之上，再用"任务"对可受领任务的资产下达指令[@mv_lattice_entity]。

!table t_mv_onto_vs_entity|Palantir 本体与 Lattice 实体模型对比|本报告依据 Palantir Ontology 文档与 Lattice SDK 公开 schema 分析整理|30,65,65
维度|Palantir 本体（MSS）|Lattice 实体（Anduril）
基本单元|对象（object），带属性与链接|实体（entity），由类型化组件构成
行为建模|动作（action），可写回运营系统与边缘系统|任务（task），下达给可受领任务的资产
设计重心|企业级数据整合、长周期分析与决策流程|实时航迹、传感器与效应器控制
典型层级|作战司令部、军种、联盟|战术边缘、师级以下网格节点
在 NGC2 中的角色|Foundry 数据平台与 Target Workbench 目标应用|Lattice Mesh 边缘数据网格与实体层
互相映射|无公开文档|无公开文档
!end

在 NGC2 中，Lattice 作为战术边缘网格、数据传输和实体层，Palantir 作为企业数据平台（Foundry）和目标与决策应用（Target Workbench）[@mv_bd_ivysting,mv_ds_anduril_palantir]。2024 年 12 月两家宣布合作时，设想由 Lattice 和 Menace 采集、传输边缘数据，再导入 Palantir AIP 准备 AI 训练，并与 MSS 结合，形成"从边缘到企业"的链路[@mv_ds_anduril_palantir,mv_pltr_ir_anduril]。有分析把两者概括为：MSS 处理历史和近实时情报、形成目标包，Lattice 以机器速度实时执行目标包、协调传感器和效应器[@mv_faf]。{red:但实体与对象之间如何转换、两套模型如何保持一致，没有任何公开文档}，这是两系统集成中最值得关注的技术空白（两系统的比较详见第三章）。

## （四）能力评估：已证实的是"省人、提速"，不是"更准"

:::lead
关于 MSS 能力的公开数字不少，但它们分属吞吐、人力、准确率、时延、战役总量、用户规模等不同口径，彼此不能直接比较。综合来看，被多源证实的是 MSS 能以很少的人力支撑很高的目标处理吞吐，并已扩展到全军和北约；目标识别的准确率不但没有证据显示优于人类，测试数据反而明显偏低；"每小时 1,000 个决策""从数天压缩到数秒"等属于愿景或官方声称。主要风险不在模型本身识别错误，而在数据过期、自动化偏见和人工审查密度下降。
:::

### 速度与吞吐：从每小时 30 个到 80 个

彭博社 2024 年的长篇报道援引 XVIII 空降军资深目标官 Temple 的估计：借助 Maven，他每小时可签批多达 **80 个目标**，不用 Maven 时约 **30 个**；他同时表示，完全信任机器会更快，但会引入错误[@mv_bloomberg_2024,mv_techmeme]。这是目前最常被引用的人机协同吞吐数字。需要注意，它是一名目标官的个人估计，衡量的是"审批"环节的速度，而不是从发现到打击的全流程。

时延方面，二手报道称在"猩红之龙"演习中，"数据传输加打击"的时间从 **12 小时以上缩短到 1 分钟以内**（二手）[@mv_armyrec]。NGA 局长惠特沃斯 2025 年也提到，某目标单元在一次演习中把时间线从数小时缩短到数分钟[@mv_bd_geoint2025]。2026 年 5 月，CDAO 斯坦利在国会书面证词中称，MSS 把目标周期"从数天压缩到数秒"[@mv_stanley_testimony]。【分析】"数秒"是官方在预算申请和转正式项目背景下的表述，没有公开方法说明，应视为官方声称。

### 人力：约 20 人顶 2,000 人

CSET 与 CSIS 都引用了一个对比：XVIII 空降军借助 MSS，以约 **20 人**的目标单元达到了 2003 年伊拉克战争（OIF）时一个 **2,000 多人**时敏目标单元的效能，后者被视为美军史上效率最高的目标单元[@mv_cset_coalition,mv_csis]。这是 MSS"省人"价值最有力的公开证据，也是 MSS 支持者最常引用的数字。【分析】这一对比来自演习而非实战，且两者面对的目标数量、情报环境、通信条件都不同，应理解为数量级上的示意，而非严格的效能比。

### 愿景：每小时 1,000 个高质量决策

陆军为 MSS 设定的远期目标是让一个单位"每小时做出 **1,000 个高质量决策**"，即选择或剔除目标[@mv_bd_geoint2025]。CSET 也把它表述为最终目标：系统与士兵帮助指挥官每小时处理 1,000 个战术决策[@mv_cset_coalition]。Army Recognition 以"每小时 1,000 个目标"为题报道了这一设想[@mv_armyrec]。{red:这是愿景指标，不是实测结果}。

### 战役总量：伊朗 38 天 13,000 个目标

2026 年对伊朗的"史诗怒火"行动提供了 MSS 首个大规模实战总量数据。按时间顺序，已知口径包括：《华盛顿邮报》称头 24 小时打击约 1,000 个目标[@mv_wapo_2026,mv_rs_iran]；中央司令部 3 月 3 日称已打击近 2,000 个目标[@mv_defind_13000]；维基百科条目称 10 天约 5,000 个目标（二手）[@mv_wiki_aiwarfare]；白宫 4 月 8 日的统计称其中指挥控制目标超过 2,000 个、防空目标 1,500 个[@mv_defind_13000]；CDAO 斯坦利称 38 天打击 13,000 个目标[@mv_ds_mazol,mv_stanley_testimony]。

【口径提醒】13,000 个是"打击的目标"总数，不是"Maven 独立识别的目标"，更不是命中率或准确率。MSS 在其中的贡献比例没有公开。只见于低可信站点的"每天 3,000 个目标""11,000 次以上打击""25,000 个以上账户"等说法，本报告不予采信（弱源，待核）[@mv_arturmarkus]；"86 秒完成决策"等说法同样未经证实[@mv_aca_iran]。

### 准确率：60% 对 84%，恶劣条件下低于 30%

与效率数字相比，准确率数据少而且不利。彭博社援引 XVIII 空降军军官的说法：测试中 Maven 识别物体的正确率约 **60%**，与 XVIII 空降军合作的人类分析员约 **84%**；遇到某些物体或雪天图像时，Maven 的正确率"可能低于 30%"[@mv_bloomberg_2024,mv_batch]。Airwars 的报道称，在西伊拉克这类天气多变的沙漠地形中，准确率可降到 30% 以下[@mv_airwars_first]。二手转述常把这组数字写成"雪天 30%"或"识别坦克 60%"。

另有两组数字流传较广但无法溯源：一是 Maven 在乌克兰"每平方公里约 10 个错误检测"，二是准确率"从 70% 降到 30%，有时 10%"（据称出自曼森）；{red:两者均未找到原始出处，不建议引用}（弱源，待核）[@mv_douwe,mv_escudo_failing]。

【分析】60%/84% 是 2023—2024 年单项物体识别测试的结果，早于加入大模型的 2026 版本，不能直接套用到"史诗怒火"行动；2026 年的版本没有公开任何准确率或误报率数据，也没有找到 AGAIM 评估结果的公开数据。同时，"30 → 80 个/小时"衡量的是人机协同的审批吞吐，"60% 对 84%"衡量的是机器单独识别的正确率，二者并不矛盾：MSS 的价值主要来自流程组织和人力节省，而非检测精度。

### 规模：用户从 2 万到 10 万以上

用户规模的增长轨迹是：2024 年 5 月合同扩展至 5 个作战司令部的"数千用户"[@mv_ds_2024_05]；2025 年 5 月活跃用户超过 2 万，覆盖 35 个以上工具、3 个安全域[@mv_bd_geoint2025]；2026 年 1 月约 5 万；2026 年 9 月超过 10 万[@mv_ds_mazol]。【分析】约 16 个月内增长约 5 倍，主要推动力是伊朗战事和向所有作战司令部、国民警卫局的推广。

伊朗战事期间的使用强度数据同样惊人：五角大楼发言人称，非密网使用量环比增长 38%，涉密网增长 89%；按 token 计的日峰值增长 4,425%，最高约 200 亿 token/天[@mv_bd_insatiable]。Breaking Defense 引用 CDAO 的说法，称军方对 AI 的需求"贪得无厌"[@mv_bd_insatiable]。

### 可靠性与风险

**数据投毒。** Maven 的数据投毒风险早已受到关注[@mv_techmeme]。MSS 汇聚上百个数据源，任何一个来源被篡改或污染，都可能通过本体关联传播到目标列表。CSET 明确表示不公开 MSS 的具体作战细节[@mv_cset_coalition]。2023 年 NGA 就 Maven 的 AI/ML 供应链风险发布征询，理由是对下级供应商缺乏可见度[@mv_bd_supplychain_2023]。

**自动化偏差。** 高吞吐的人机协同天然存在"人类背书"的风险。目标官 Temple 自己就指出，完全信任机器会引入错误[@mv_bloomberg_2024]。批评者认为，MSS 已从决策支持变成"附带人类副署以满足法律合规的决策系统"[@mv_strat_intl]；也有文章讨论"橡皮图章问题"，即 AI 的速度超过了它所承诺的监督能力[@mv_medium_rubber]。中央司令部司令则表示，最终打击决定由人作出[@mv_letsdata]。

**Minab 学校事件。** 2026 年 2 月 28 日"史诗怒火"行动首日，伊朗 Minab 一所学校遭打击。据彭博社引述五角大楼内部调查，该地点在旧数据库中仍标为伊斯兰革命卫队设施，输入 Maven 后被列为"第一天推荐目标"；部分用户以为 Maven 会发现过期记录；中央司令部平民伤害评估团队已从约 10 人缩减到 1 人[@mv_bloomberg_minab,mv_gizmodo_minab]。【分析】这是 AI 辅助目标定位中"数据过期加自动化偏差"最具体的公开案例，其失败模式不是模型识别错误，而是平台忠实地呈现了一条过期记录、人没有核查。案例详情与各方说法见第五节。

**透明度与问责。** 国防部指令 DoDD 3000.09（2012 年发布，2023 年 1 月更新）要求自主和半自主武器系统的设计让指挥官和操作员能对武力使用施加"适当程度的人类判断"，正式开发前须经高级官员审查[@mv_gao_22,mv_dodd3000]。【分析】MSS 本身不发射武器，更接近"目标选择支持系统"，3000.09 的高级审查不一定直接适用；问责主要依赖交战规则、联合目标定位流程（JP 3-60）中的人工签批和法律审查。{red:没有找到针对 MSS 的正式"负责任 AI"评估、3000.09 审查记录，也没有找到 GAO 或国防部监察长针对 MSS 的独立评估}。Maven 预算属于机密、不适用 FOIA[@mv_lawfare_book]。

### 商业侧指标：Palantir 美国政府收入

MSS 的规模化也体现在 Palantir 的财务数据上。按公司披露，Palantir 美国政府收入 2022 年为 8.263 亿美元，2023 年为 9.212 亿美元，2024 年约 12 亿美元，2025 年为 18.55 亿美元（同比增长 55%），2026 年上半年约 14.96 亿美元（一季度 6.87 亿、二季度 8.09 亿，同比分别增长 84% 和 90%）[@mv_pltr_10k_2023,mv_pltr_10k_2024,mv_pltr_q4_2025,mv_pltr_q2_8k]。2026 年二季度公司总营收约 19.4 亿美元，同比增长 93%[@mv_cnbc_q2]。

!table t_mv_revenue|Palantir 美国政府收入（2022—2026H1）|Palantir 10-K、季度新闻稿；与 MSS 的对应关系为相关性分析|26,40,94
年份|美国政府收入|同期与 Maven 相关的事件
2022|8.263 亿美元|Maven 拆分，MSS 原型面向有限操作员[@mv_pltr_10k_2023]
2023|9.212 亿美元|NGA Maven 转正式项目；CJADC2 最小可行能力认证[@mv_pltr_10k_2023]
2024|约 12 亿美元|4.8 亿美元 MSS 原型合同；ARL 军种扩展合同[@mv_pltr_10k_2024]
2025|18.55 亿美元（+55%）|MSS 上限增至约 13 亿美元；陆军 EA；陆战队许可；北约采购[@mv_pltr_q4_2025]
2026 上半年|约 14.96 亿美元（+84%/+90%）|"史诗怒火"行动；Feinberg 备忘录；用户破 10 万[@mv_pltr_q2_8k]
!end

【分析】时间上的吻合不等于因果，Palantir 并未单独披露 MSS 收入。有分析师认为 MSS 正"冲刺"10 亿美元年化经常性收入，另有报道称 Maven 年化经常性收入接近 10 亿美元，但都只有单一来源，可信度低（弱源，待核）[@mv_bitget,mv_simplywall]。

### 能力评估总表

!table t_mv_capability|MSS 能力评估：已证实、官方声称与存疑|本报告综合 Bloomberg、CSET、CSIS、DefenseScoop、Breaking Defense 等整理|24,46,46,44
维度|已证实（多源/官方）|官方声称或愿景|存疑或反证
目标处理吞吐|一名目标官估计每小时 30 → 80 个目标[@mv_bloomberg_2024]|每小时 1,000 个高质量决策（愿景）[@mv_bd_geoint2025]|"完全信任机器会引入错误"
人力节省|约 20 人达到 OIF 时 2,000 多人目标单元效能[@mv_cset_coalition]|—|演习对比，非实战；条件不同
时延|演习中从数小时缩短到数分钟[@mv_bd_geoint2025]|"从数天到数秒"[@mv_stanley_testimony]；12 小时以上 → 1 分钟以内（二手）[@mv_armyrec]|无方法说明
战役规模|38 天打击 13,000 个目标（官方总量）[@mv_ds_mazol]|头 24 小时约 1,000 个（媒体）[@mv_wapo_2026]|统计的是打击目标，非 Maven 识别量；"每天 3,000 个"等不予采信
识别准确率|测试中约 60%，人类约 84%[@mv_bloomberg_2024]|2026 版无公开数据|恶劣天气、雪天低于 30%[@mv_airwars_first]；"每平方公里 10 个误检"无出处
用户规模|2 万以上（2025-05）→ 约 5 万（2026-01）→ 10 万以上（2026-09）[@mv_bd_geoint2025,mv_ds_mazol]|推广至全部作战司令部和国民警卫局|注册与活跃口径不一[@mv_govly]
使用强度|涉密网使用量增长 89%；日峰值约 200 亿 token[@mv_bd_insatiable]|—|无独立审计
联盟能力|北约 MSS NATO 达到 FOC[@mv_shape_foc]|—|乌克兰效果"好坏参半"[@mv_kyivind]
人在回路|CENTCOM 称每一步以人工验证结束[@mv_register_2024]|定位为决策支持|Minab 事件；"橡皮图章"批评[@mv_bloomberg_minab,mv_strat_intl]
!end

【综合判断】MSS 被多源证实的核心能力，是多源情报融合和目标工作流管理，以及由此带来的"以少量人力支撑大规模目标吞吐"。仍属声称或未经验证的，是目标识别的准确性、"每小时 1,000 个决策"、"数秒完成目标周期"以及 AI 对每个具体目标的实际贡献。官方数字（13,000 个目标、10 万用户、token 增长）都来自官员，没有独立审计；官方在申请 23 亿美元预算和推动转正式项目时，也有强调成效的动机。

### 口径冲突一览

!table t_mv_conflicts|Maven 相关数据口径冲突与待核清单|本报告整理，引用前应逐项回到原文核对|30,82,48
条目|冲突或存疑内容|来源
谷歌抗议规模|签名约 4,000、4,600 还是近 5,000；辞职约 12 人、13 人还是"数十人"|[@mv_gizmodo_au_resign,mv_fortune_2018]
谷歌合同额|约 900 万美元（对外口径）、1,500 万美元（18 个月内部预期）、2.5 亿美元/年（项目预算展望，非谷歌合同额）|[@mv_intercept_emails]
2024-02 打击|"85 次以上打击"还是"85 个目标"|[@mv_register_2024]
MSS 数据源数|179 个（CSIS）还是 150 个以上（GlobalSecurity）|[@mv_csis,mv_globalsec]
陆军 EA 日期|2025-07-31 还是 2025 年 8 月|[@mv_wt_ea,mv_ds_ea]
MSS 合同上限|约 12.75 亿、"近 12.8 亿"还是"约 13 亿"美元；另有"10 亿美元上限"的低可信说法|[@mv_globalsec_contract,mv_ds_2025_05]
Feinberg 备忘录日期|3 月 9 日（签署）还是 3 月 20—23 日（报道）|[@mv_govconwire_por,mv_capture]
转正式项目|截止 2026-09-30；有媒体称"已成为"，无官方确认|[@mv_motley_por]
FY2027 预算|23 亿美元为单年还是五年合计；超过 15 亿美元为 MSS 访问扩展|[@mv_ds_fy27,mv_isstracker]
用户数|2025 年 2 万以上（NGA）与"130 个站点、约 2.5 万人"（二手）；2026-03"2 万多活跃用户"与 2026-01"约 5 万"|[@mv_bd_geoint2025,mv_hvylya,mv_govly]
伊朗打击数|24 小时约 1,000 个、至 3-3 近 2,000 个、10 天约 5,000 个、38 天 13,000 个；"每天 3,000 个"等不予采信|[@mv_wapo_2026,mv_wiki_aiwarfare,mv_ds_mazol]
Minab 死亡人数|约 123 名儿童、175—180 人、150—170 余人、至少 186 名学生和教师|[@mv_gizmodo_minab,mv_aca_iran,mv_wiki_minab]
Claude 状态|3-4 被列为供应链风险、6 个月内淘汰，或 2-28 行政令；卡普称仍在运行|[@mv_aca_iran,mv_ie_claude]
Scale AI 标注合同|2,400 万美元与"修改后总值 1.3 亿美元"的关系不明|[@mv_nga_contracts]
!end

## （五）案例：从反 ISIS 视频识别到伊朗战役

:::lead
有公开数据支撑的 Maven 实战案例并不多：2017—2018 年反 ISIS 的 FMV 识别、2024 年 2 月伊拉克和叙利亚空袭、2024 年也门和红海作战，以及 2026 年对伊朗的"史诗怒火"行动。前三者只有官员的定性说法，"史诗怒火"有官方总量数字，同时也产生了与 Maven 相关的最严重平民伤亡事件。演习、盟国和军种推广类案例则以采购和部署信息为主。本节逐案记录时间、单位、战区、Maven 的作用、结果和来源，并单列一张"未找到关联证据"的行动清单，避免把 Maven 与所有近年美军行动想当然地挂钩。
:::

### 案例一：反 ISIS 首次部署（2017—2018）

【时间】2017 年 12 月起，持续至 2018 年。【单位】特种作战司令部情报分析员；非洲司令部及中东多个地点。【战区】中东（反 ISIS）、非洲。

【Maven 作用】在 ScanEagle 小型无人机的全动态视频中自动识别物体，辅助分析员完成 PED[@mv_nextgov_2017,mv_trajectory]。沙纳汉称之为"原型战"[@mv_nextgov_2017]。到 2018 年 5 月，官员称非洲司令部自 2017 年 12 月起也在使用，部署扩展到中东多个地点[@mv_bd_2018_africa]。早期还曾用海豹突击队在索马里拍摄的无人机视频测试多家供应商的识别工具[@mv_bloomberg_2024]。

【结果】属于初始部署，没有公开性能数据。其意义主要在于证明国防部能在约 8 个月内把商业计算机视觉送上战场[@mv_bulletin_2017]。GlobalSecurity 提到的其他早期作战使用未获佐证（弱源，待核）[@mv_globalsec]。

### 案例二：XVIII 空降军"猩红之龙"系列演习（2020 年起）

【时间】2020 年起，年度系列。【单位】陆军第 XVIII 空降军（布拉格堡）。【战区】美国本土演习。

【Maven 作用】通过"猩红之龙"系列演习，在 DevSecOps 环境中与多达 70 家公司合作，把 Maven 从视频识别工具发展为整合传感器、目标识别和火力分配的 MSS[@mv_d1_2024_08,mv_cset_coalition]。GAO 把"猩红之龙"描述为使用 Project Maven 数据的陆军目标识别 AI 能力[@mv_gao_22]。

【结果】CSET 记录：约 20 人的目标小组达到 2003 年伊拉克战争时间敏感目标单元（约 2,000 人）的产出；一名目标军官估计用 Maven 每小时可处理 80 个目标，不用时为 30 个[@mv_cset_coalition,mv_bloomberg_2024]。二手报道称"数据传输加打击"时间从 12 小时以上缩短到 1 分钟以内[@mv_armyrec]。"每小时 1,000 个高质量决策"只是目标，未经验证[@mv_interesting_eng_army]。

!photo scarlet_dragon_26_1|XVIII 空降军"猩红之龙"演习（编号 26-1）：参演人员通过 Maven 智能系统共享目标数据。"猩红之龙"是 MSS 从视频识别工具发展为目标工作流平台的主要试验场|美国陆军，公有领域

!photo scarlet_dragon_c_uas|XVIII 空降军在"猩红之龙"系列活动中开展反无人机训练，应对"下一场战争"的无人机威胁|美国陆军，公有领域

### 案例三：支援乌克兰（2022 年起）

【时间】2022 年起。【单位】前沿部署欧洲的 XVIII 空降军。【战区】乌克兰。

【Maven 作用】XVIII 空降军用 MSS 生成目标情报并分享给乌军；乌方使用的是不依赖美国敏感情报的版本[@mv_lawfare_book,mv_kyivind]。

【结果】曼森的专著称美方向乌克兰发送了"数以万计"的目标[@mv_willis_book,mv_lawfare_book]。《纽约时报》2024 年 4 月的报道称效果"好坏参半"：它帮助乌军更有效地打击俄军炮兵，但没能把战场图像送到前线士兵手里，难以把"21 世纪的数据送进 19 世纪的战壕"[@mv_kyivind,mv_defender_nyt]。

【说明】乌克兰是美方目标情报的接收方，而不是 MSS 的直接用户。曼森书中关于威斯巴登方面的细节，因无法打开原文书摘而未能核实。

### 案例四：中央司令部 2024 年 2 月空袭伊拉克、叙利亚

【时间】2024 年 2 月 2 日。【单位】中央司令部。【战区】伊拉克、叙利亚。

【背景】约旦"22 号塔"（Tower 22）前哨遇袭，造成 3 名美军死亡，美军随即对伊拉克和叙利亚境内的目标实施报复性打击[@mv_register_2024,mv_national_2024]。

【Maven 作用】中央司令部首席技术官舒伊勒·摩尔（Schuyler Moore）对彭博社表示，机器学习目标识别帮助"缩小目标范围"；她强调每一步都以人工验证结束[@mv_register_2024,mv_bnn_2024]。

【结果】Maven 参与了 85 次以上打击，涉及 7 处设施[@mv_register_2024]。{red:口径冲突}：彭博社原文说的是 85 次以上"打击"，部分媒体写成 85 个"目标"[@mv_register_2024]。这是官方首次公开确认 Maven 被用于实际打击的目标筛选。

!photo b1b_feb2024_ellsworth|2024 年 2 月 1 日，戴斯空军基地停机坪上的 B-1B"枪骑兵"轰炸机（含埃尔斯沃思基地机组），次日即从此出击，对伊拉克、叙利亚境内 85 处目标实施打击；据中央司令部首席技术官向彭博社透露，Maven 在这轮打击中被用于缩小目标范围|美国空军 Senior Airman Leon Redfern 摄，公有领域（240201-F-MI946-1067）

### 案例五：也门与红海（2024）

【时间】2024 年。【单位】中央司令部。【战区】也门、红海。

【Maven 作用】据摩尔介绍，Maven 被用于定位也门境内的火箭发射器和红海上的水面船只[@mv_bloomberg_2024,mv_batch]。

【结果】没有公开具体数量。【说明】2024 年 1 月起美英对胡塞武装的系列打击是这一时期的主要作战背景，但{red:没有公开来源把某一次具体打击与 Maven 直接对应}。

!photo centcom_jan2024_1|2024 年 1 月 12 日美英对也门胡塞武装目标实施打击（中央司令部发布）。2024 年 Maven 被用于定位也门境内的火箭发射器和红海水面船只，但公开资料未将本次打击与 Maven 直接对应|美国中央司令部，公有领域

!photo gravely_tomahawk|美国海军"格雷夫利"号驱逐舰发射"战斧"巡航导弹打击胡塞目标（2024 年 1 月 12 日）。红海方向的海上打击是 Maven 2024 年实战使用的背景之一|美国海军，公有领域

### 案例六："史诗怒火"行动：对伊朗作战（2026）

【时间】2026 年 2 月 28 日起，官方统计口径为 38 天。【单位】中央司令部。【战区】伊朗。

【Maven 作用】美国官员称五角大楼依靠 Maven 识别最高优先级目标并帮助选择武器[@mv_aca_iran]。《华盛顿邮报》报道称，内嵌 Claude 的 MSS 给目标排序、生成坐标并建议武器；二手转述还称其生成法律依据草稿[@mv_wapo_2026]。中央司令部司令表示，最终打击决定由人作出[@mv_letsdata]。

【结果】多种口径并存（见第四节）：头 24 小时约 1,000 个目标（华邮）；至 3 月 3 日近 2,000 个（中央司令部）；38 天 13,000 个（CDAO 斯坦利），斯坦利称把目标周期"从数天压缩到数秒"；白宫 4 月 8 日统计其中指挥控制目标超过 2,000 个、防空目标 1,500 个[@mv_wapo_2026,mv_defind_13000,mv_stanley_testimony,mv_bd_insatiable]。战事期间 MSS 涉密网使用量增长 89%，token 日峰值增长 4,425%[@mv_bd_insatiable]；用户数从约 5 万增至 10 万以上[@mv_ds_mazol]。

【说明】这些数字统计的是"打击的目标"，不是"Maven 独立识别的目标"；Claude 的具体角色仍存在争议（见第二节）。

!photo b1b_centcom_9762139|B-1B"枪骑兵"轰炸机起飞，支援中央司令部责任区安全任务（2026 年 5 月）。2026 年对伊朗作战期间及之后，MSS 是中央司令部目标定位的核心平台；本照片仅作背景，不表明该架次与 Maven 直接相关|美国空军，公有领域

### 案例七：Minab 学校遇袭事件（2026-02-28）

【时间】2026 年 2 月 28 日前后，即"史诗怒火"行动第一天。【单位】中央司令部。【地点】伊朗 Minab。

【经过】一所学校遭美军打击。据彭博社引述五角大楼内部调查，该地点在旧数据库中仍被标为伊斯兰革命卫队设施，输入 Maven 后被列为"第一天推荐目标"；卫星图像显示该地点近十年前已改建，2018 年的图像上能看到足球场；中央司令部平民伤害评估团队已从约 10 人缩减到 1 人；部分用户以为 Maven 会发现过期记录；调查称这是"一连串可预防的失败"[@mv_bloomberg_minab,mv_gizmodo_minab,mv_theprint_minab]。《纽约时报》援引美国官员称美方对此负责，调查仍在进行[@mv_aca_iran,mv_airwars_guardian]。

【伤亡】{red:死亡人数说法不一}：彭博社/Gizmodo 称约 123 名儿童死亡[@mv_gizmodo_minab]；军控协会称约 175—180 人[@mv_aca_iran]；另有 150—170 余人的说法[@mv_rs_palantir]；伊方称至少 186 名学生和教师死亡[@mv_wiki_minab]。彭博社调查报道的日期也有 9 月 18 日和 9 月 20 日两种说法。

【各方说法】Palantir 称自己"不对底层数据负责"，此后增加了对底层情报中"取消资格因素"的复核[@mv_gizmodo_minab,mv_rs_palantir]。前军官对 Semafor 等媒体表示责任在人而不在 AI[@mv_mt_minab]。也有分析指出，目前没有公开的一手材料能把某个具体的 AI 输出和这次打击直接对应[@mv_beebe_minab]。Maven 或 Claude 是否在其中起作用，仍有争议[@mv_aca_iran]。

【后续】2026 年 3 月 12 日，120 多名众议院民主党议员致信国防部长赫格塞斯，46 名参议员另有类似要求；五角大楼以调查尚在进行为由回应；联合国事实调查团认为"有合理理由"相信构成战争罪[@mv_gizmodo_minab,mv_wiki_minab]。{red:完整调查报告截至 2026 年 10 月仍未公开}。

【分析】Minab 事件的失败链条是"数据过期 → 平台忠实呈现 → 人工核查缺位"，而非"模型识别错误"。它直接揭示了 MSS 规模化的代价：当目标处理吞吐成倍提高、平民伤害评估人员却从 10 人减到 1 人时，人在回路在形式上仍然存在，但实质审查能力已被稀释。

### 案例八：北约 MSS NATO（2025—2026）

【时间】2025 年 3 月 25 日签约，4 月 14 日公布；2026 年 6 月 22 日达到全面作战能力。【单位】北约通信与信息局（采办）、盟军作战司令部（使用）。【战区】欧洲。

【Maven 作用】情报融合与目标定位、战场态势感知与规划、加速决策；包含大语言模型、生成式 AI 和机器学习[@mv_shape_release,mv_ncia_2025]。

【结果】从提出需求到签约约 6 个月，北约称为史上最快采购之一；金额未公开[@mv_shape_2025,mv_ds_nato]。先后部署于 SHAPE、布林森联合部队司令部，诺福克联合部队司令部预计 2026 年 4—5 月接入[@mv_janes_norfolk]。2025 年全年测试，经"坚定威慑 2026"演习检验后达到 FOC，获准在北约机密网络运行，数据存放于北约自有数据中心[@mv_shape_foc,mv_janes_foc]。北约强调该系统不同于"NGA Maven 作战人员支援系统"[@mv_shape_2025]。

!photo shape_hq|位于比利时蒙斯的北约欧洲盟军最高司令部（SHAPE）主入口。2025 年 3 月北约为盟军作战司令部采购 MSS NATO，SHAPE 为首批部署地点|维基共享资源

!photo jfc_brunssum|北约布林森联合部队司令部（荷兰）。该司令部是继 SHAPE 之后部署 MSS NATO 的单位之一|维基共享资源，CC BY-SA 2.0

!photo nato_mss_release|SHAPE 新闻稿页面：《北约采购 AI 赋能作战系统》，宣布通过 NCIA 采购 Palantir MSS NATO（2025 年 4 月）|北约版权，新闻用途

### 案例九：海军陆战队企业许可（2025）

【时间】2025 年 8 月 15 日敲定，9 月 10 日公布，9 月 11 日发布 MARADMIN 424/25。【单位】美国海军陆战队，与 DIU、CDAO、ARL 合作。【战区】全军。

【Maven 作用】陆战队把 MSS 定为跨多个作战司令部的标准"火力与效果集成平台"[@mv_ds_maradmin]。

【结果】通过企业许可，从舰队陆战队到支援机构均可在 SIPRNet（IL6 云）上无限量访问 MSS；金额未披露[@mv_usmc_release,mv_maradmin,mv_ds_usmc]。

### 其他推广与使用

【五个作战司令部推广，2024 年 5 月起】4.8 亿美元合同把 MSS 原型推广到中央、欧洲、印太、北方、运输五个作战司令部和联合参谋部的"数千用户"[@mv_ds_2024_05]。

【五个军种推广，2024 年 9 月起】ARL 约 9,980 万美元合同把 MSS 扩展到陆、空、天、海和陆战队[@mv_govconwire_arl]。

【陆军联合兵种司令部，2026】把"Maven C2 智能系统"纳入训练与院校教育[@mv_army_cac]。

【国民警卫局，2026】马佐尔称 MSS 正推广到国民警卫局[@mv_ds_mazol]。

【陆军 NGC2"常春藤之刺 1"，2025 年 9 月】第 4 步兵师在 Lattice 网格上运行 Palantir Target Workbench 完成师级目标定位流程；{red:但这里使用的是 Target Workbench，公开资料未说明是否就是 MSS 本身}[@mv_bd_ivysting]。

【委内瑞拉马杜罗抓捕行动，2026 年 1 月 3 日】《华尔街日报》称 Claude 通过 Palantir 平台参与，但{red:没有来源明确说用的是 Maven}，具体任务属于机密，Anthropic 不予置评[@mv_swj_maduro,mv_cnbc_karp]。

### 案例总表

!table t_mv_cases|Maven / MSS 主要案例|本报告据各条所列来源整理；可信度分官方、媒体、智库、二手|18,22,18,36,40,26
日期|单位|战区|Maven 作用|结果与数据|可信度与来源
2017-12 起|SOCOM、AFRICOM|中东、非洲|ScanEagle FMV 物体识别|初始部署，无性能数据|官方/媒体[@mv_nextgov_2017,mv_bd_2018_africa]
早期|海豹突击队视频|索马里|测试多家供应商识别工具|—|媒体[@mv_bloomberg_2024]
2020 起|XVIII 空降军|美国本土|"猩红之龙"演习孵化 MSS|20 人顶 2,000 人；每小时 30 → 80 个目标|智库/GAO[@mv_cset_coalition,mv_gao_22]
2022 起|XVIII 空降军|乌克兰|生成目标情报分享乌军|"数以万计"目标；效果"好坏参半"|书、NYT[@mv_willis_book,mv_kyivind]
2024-02-02|CENTCOM|伊拉克、叙利亚|ML 目标识别缩小目标范围|85 次以上打击、7 处设施|官方[@mv_register_2024]
2024|CENTCOM|也门、红海|定位火箭发射器与水面船只|无数量|官方[@mv_bloomberg_2024]
2024-05 起|5 个作战司令部与联合参谋部|全球|MSS 原型推广|"数千用户"|官方[@mv_ds_2024_05]
2025-03 至 2026-06|北约 ACO|欧洲|情报融合、目标定位、规划|6 个月采购；2026-06-22 FOC|官方[@mv_ncia_2025,mv_shape_foc]
2025-09|海军陆战队|全军|标准火力与效果集成平台|IL6 企业许可|官方[@mv_ds_maradmin]
2026-02-28 起|CENTCOM|伊朗|目标排序、坐标、武器建议|38 天 13,000 个目标；用户 10 万以上|官方数字＋媒体[@mv_ds_mazol,mv_wapo_2026]
2026-02-28|CENTCOM|伊朗 Minab|过期记录被列为推荐目标|学校遇袭，死亡人数各说不一|媒体，有争议[@mv_bloomberg_minab,mv_gizmodo_minab]
2026|陆军联合兵种司令部、国民警卫局|训练体系、本土|纳入训练；推广使用|—|官方[@mv_army_cac,mv_ds_mazol]
!end

### 未找到关联证据的行动

以下行动或项目常被与 Maven 联系在一起，但本轮调研{red:没有找到将其与 Maven 直接挂钩的公开报道}。列出它们的目的，是避免在缺乏证据的情况下把 Maven 的作用外推。

!table t_mv_noevidence|未找到 Maven 关联证据的行动与项目|本报告调研结论（截至 2026-10-10）|40,60,60
行动或项目|时间与背景|调研结论
"粗骑兵"行动（Operation Rough Rider）|2025 年，对也门胡塞武装打击|未找到 Maven 参与的公开报道
"午夜之锤"行动（Midnight Hammer）|2025 年 6 月，打击伊朗核设施|未找到 Maven 参与的公开报道
"南方之矛"行动（Southern Spear）|2025 年 9 月起，加勒比海、东太平洋打击船只|搜索结果中无 Maven 或 Palantir 相关信息
马杜罗抓捕行动|2026-01-03，委内瑞拉|仅有"Claude 经 Palantir 参与"说法，未确认使用 Maven[@mv_swj_maduro]
"金穹"导弹防御|2025 年起|未找到 MSS 角色；仅有 Anduril 与 Palantir 共同开发 C2 软件的报道[@mv_reuters_goldendome]
印太司令部专门演习|—|仅能确认印太司令部在 2024 年合同覆盖范围内[@mv_ds_2024_05]
"项目融合"（Project Convergence）|陆军年度试验|未找到 Maven 具体使用记录
太空军|—|已列入 2024-09 军种扩展范围，未找到具体使用记录[@mv_govconwire_arl]
英国国防部|2025-09 宣布与 Palantir 战略伙伴关系，最高 7.5 亿英镑|官方未称 MSS；最终合同签署未证实[@mv_computing_uk]
!end

### 案例综合分析

把上述案例按时间排开，可以看出 Maven 实战使用的三个演进特征。

第一，**作用从"看"转向"排"**。2017 年的作用是在视频中识别物体，属于情报处理；2024 年 2 月的作用是"缩小目标范围"，开始进入目标筛选；2026 年的作用是目标排序、生成坐标和建议武器，已深入目标定位的核心决策环节[@mv_nextgov_2017,mv_register_2024,mv_aca_iran]。

第二，**规模从"试点"转向"战役级"**。2017 年只有少数分析员使用，2024 年 2 月参与 85 次以上打击，2026 年则是 38 天 13,000 个目标、用户 10 万以上[@mv_register_2024,mv_ds_mazol]。规模扩大的同时，官方披露的信息却越来越集中于总量数字，单个目标层面的 AI 贡献、误差和审批时长没有任何公开数据。

第三，**风险从"识别不准"转向"流程失守"**。早期的担忧是模型准确率低（60% 对 84%），Minab 事件暴露的却是数据过期、平民伤害评估人员缩减和用户对系统能力的错误预期[@mv_bloomberg_2024,mv_bloomberg_minab]。这说明当 AI 目标定位系统进入战役级运用后，评估其风险的重点应从模型指标转向数据治理和人机协作流程。

盟国方面，北约 ACO 是已确认的 MSS 直接用户；乌克兰是美方目标情报的接收方；英国 2025 年 9 月宣布与 Palantir 的战略伙伴关系涉及 AI 目标定位，但官方未称其为 MSS，其他国家的采用情况没有找到证据[@mv_shape_foc,mv_kyivind,mv_computing_uk]。

:::judge 研判要点
- Maven 的核心价值是把杀伤链"工业化"：已被多源证实的是以少量人力支撑大规模目标吞吐（20 人顶 2,000 人、每小时 30 → 80 个、38 天 13,000 个目标），而不是识别更准；测试中其识别率约 60%，低于人类的 84%，2026 年版本没有任何公开准确率数据。
- MSS 已从"无人机视频识别工具"演变为国防部事实上的 AI 赋能 C2 与目标定位骨干和"万能应用"：用户约 16 个月增长约 5 倍至 10 万以上，覆盖全部作战司令部、各军种、国民警卫局和北约 ACO，FY2027 申请约 23 亿美元（含联合火力网），Feinberg 备忘录将其推向全军正式项目。
- 架构上形成"政府掌握模型流水线（NGA）、商业公司掌握平台与本体（Palantir）、模型与大模型可插拔"的格局；合同全部并入陆军 100 亿美元企业协议后，平台锁定进一步加深，公开追踪难度上升，Open DAGIR 只开放了应用层。
- 主要风险在数据与人而非算法：Minab 事件暴露了"过期数据 + 自动化偏差 + 人工审查密度下降"的失败链条；大模型层（Claude）的角色与替换状态不透明；MSS 不发射武器，游离于 DoDD 3000.09 高级审查之外，目前没有公开的负责任 AI 评估或独立审计。
- 对我方的启示：AI 目标定位系统的效能瓶颈和风险都集中在"数据保鲜—对象化—审批流程"环节，评估同类系统时应重点关注数据源治理、AI 贡献标注（如 NGA 的机器生成标签）和单目标人工审查时长，而不是单纯比较识别率。
:::
