# 九、关键人物与机构：谁在推动算法战

:::lead
Lattice 与 Maven 智能系统（MSS）能在九年间从边境监视塔和无人机视频识别发展为军种级数据层和全军目标平台，背后是三股力量的叠加：以 Palantir 校友和 Founders Fund 为核心的硅谷防务创业网络，以沃克、沙纳汉、库科为代表、在国防部内部推动“算法战”的改革派官员，以及 2025 年后以赫格塞斯、范伯格为代表、用行政指令和采办改革为两家企业铺路的新一届决策层。本章分人物与机构两条线梳理：先写两家公司的创始团队、高管与资本，再写国防部和军方的推动者，然后列出与两系统相关的关键机构及其职责，最后客观梳理有据可查的人员流动与利益关联。我部研判，两系统的扩张主要由少数关键人物在关键节点上的决定推动，人员与资本网络的同源性降低了两家的合作成本，也带来了透明度和利益冲突方面的持续质疑；截至本报告，没有证据表明存在利益输送。
:::

本章人物信息全部来自研究笔记所载的公开报道、官方文件和公司材料。研究笔记明确列出了几处空白：没有找到勒基、卡普、申普夫、桑卡尔系统阐述两家分工的原话；没有检索到桑卡尔关于 Maven 的具体表态；2022—2025 年 CDAO 历任负责人名单未经一手来源核实；除奥巴达尔外，没有检索到从两家进入国防部的其他官员。下文凡涉及这些空白处均如实注明。

## （一）Anduril 创始团队与资本

### 帕尔默·勒基：公众形象与政治表态

帕尔默·勒基（Palmer Luckey）是 Anduril 最具公众知名度的联合创始人。他此前创办了 Oculus 虚拟现实头显公司，2017 年与特雷·斯蒂芬斯、布赖恩·申普夫、马特·格林、陈乔（Joe Chen）共同创立 Anduril[@la_builtin_luckey,la_wiki_anduril]。公司成立日期有两种说法：一说 2017 年 4 月 20 日注册，TechCrunch 称其 2017 年 6 月“悄然成立”[@la_wiki_anduril,la_tc_founding]。2017 年 6 月，Anduril 高管即向国土安全部加州办公室推销低成本边境安全方案，这是 Lattice 的起点[@la_wiki_anduril]。

!photo luckey_oculus_2015|帕尔默·勒基在 Oculus 时期展示 Touch 控制器原型（2015 年 6 月 11 日）。勒基以消费级虚拟现实硬件起家，两年后转入防务领域创立 Anduril|Wikimedia Commons，CC0

勒基在公司中的角色偏重对外发声和政策倡导。他在 CNBC 上称，美国只花现在五角大楼预算的一半左右也能建成更有效的防务，前提是不再买错误的东西[@co_fpif]。这一表态是“新主承包商”叙事的典型版本。Punchbowl News 报道过勒基与 Palantir 首席执行官卡普的政治献金，报道细节未获取[@co_punchbowl]。在应对负面报道方面，Anduril 创始人曾公开称《华尔街日报》关于无人艇工厂的报道失实[@la_defblog_wsjfalse]。

!photo luckey_ces_2026|帕尔默·勒基出席 2026 年国际消费电子展（CES 2026，2026 年 1 月）。勒基长期保持消费科技圈与防务圈的双重曝光|Wikimedia Commons，CC BY-SA 4.0

勒基也直接参与客户拓展。据台湾《联合报》报道，他曾于 2025 年 8 月赴台交付无人机，同月台湾开始接收首批 ALTIUS-600M[@gp_udn_luckey,la_tdp_taiwan_2025]。2026 年 8 月 6 日，勒基访问洛杉矶空军基地的太空系统司令部并向该司令部人员讲话；此前该司令部已授予 Anduril 太空监视网现代化合同，同年 4 月又把 Anduril 列入天基拦截器原型团队[@gp_dvids_luckey_ssc,la_ds_ssn,la_bloomberg_sbi]。

!photo luckey_ssc_2|勒基向太空系统司令部人员讲话（2026 年 8 月 6 日，洛杉矶空军基地）。太空系统司令部是 Anduril 太空监视网现代化和天基拦截器原型合同的授予方|Christopher Kim（U.S. Space Force，经 DVIDS），美国政府作品

### 布赖恩·申普夫：首席执行官与 Palantir 工程背景

布赖恩·申普夫（Brian Schimpf）是 Anduril 联合创始人兼首席执行官，早年是 Palantir 的工程负责人，参与构建了 Foundry[@co_a16z_schimpf]。这一背景是两家工程层面互通的人事基础：Lattice 的实体模型与 Palantir 本体之间没有公开的映射规范，但两家核心工程团队熟悉对方的设计思想[@co_tc_sankar,co_a16z_schimpf]。2025 年 1 月 9 日，Stratechery 专访申普夫，话题涉及 Lattice SDK、CCA 竞争以及“与 Palantir 一起构建 AI”，但检索摘要中没有关于 Palantir 部分的原话[@gp_stratechery_schimpf]。

申普夫任内，Anduril 完成了从边境监视到军种级数据层的转型：2022 年 SOCOM 反无人系统集成伙伴合同（上限 9.676 亿美元），2024 年 12 月 Lattice SDK 公开发布并与 Palantir 宣布合作，2026 年 3 月获得陆军上限 200 亿美元企业合同[@la_wt_socom,la_dd_sdk,la_bw_palantir,la_ds_20b]。研究笔记没有找到申普夫本人对这些决策的系统阐述。

### 特雷·斯蒂芬斯、马特·格林与陈乔

特雷·斯蒂芬斯（Trae Stephens）出自 Palantir，同时是 Founders Fund 合伙人[@co_tc_sankar,la_wiki_anduril]。据其公开活动照片的说明，他任 Anduril 董事长。研究笔记指出，斯蒂芬斯在 Founders Fund 的身份属公开常识，但本轮检索没有找到专门的一手来源[@la_sacra]。斯蒂芬斯是连接 Anduril 与 Founders Fund 的关键人物：Founders Fund 领投了 Anduril 2024 年的 F 轮和 2025 年的 G 轮，并在 G 轮中出资 10 亿美元[@la_andurilnews_funding,la_sacra]。

马特·格林（Matt Grimm）同样出自 Palantir；陈乔是第五位联合创始人[@la_wiki_anduril,co_tc_sankar]。研究笔记中没有两人在公司内部职责的公开记录。五位创始人中三人出自 Palantir，这是理解两家后来“分层合作、局部竞争”关系的背景线索[@la_wiki_anduril]。

### 资本：Founders Fund、蒂尔与估值曲线

Anduril 的融资史与 Lattice 地位的上升同步。2017 年 8 月种子轮 1,800 万美元；2019 年 B 轮估值约 10 亿美元，2020 年 C 轮融资 2 亿美元、估值 19 亿美元，两轮均由 a16z 领投；2022 年 E 轮 14.8 亿美元由 Valor 领投；2024 年 F 轮 15 亿美元、估值 140 亿美元，由 Founders Fund 和 Sands Capital 领投；2025 年 G 轮 25 亿美元、估值 305 亿美元；2026 年 5 月 13 日 H 轮 50 亿美元、估值 610 亿美元，由 Thrive Capital 和 a16z 领投[@la_andurilnews_funding,la_sacra,la_tc_seriesh,la_cnbc_seriesh]。2026 年 7 月 24 日，路透社报道其正以约 1,000 亿美元估值洽谈新一轮，未见交割确认[@la_dn_100b]。营收方面，公司口径为 2024 年约 10 亿美元、2025 年 22 亿美元、2026 年目标约 43 亿美元，均未经审计[@la_sacra,la_cnbc_seriesh]。

彼得·蒂尔（Peter Thiel）是这一资本网络的源头。Palantir 于 2003 年由蒂尔等人创立，蒂尔又创办了 Founders Fund[@co_tc_sankar]。Palantir 另一位联合创始人乔·朗斯代尔（Joe Lonsdale）通过 8VC 投资国防初创企业[@co_tc_sankar]。蒂尔网络的覆盖面早在 Maven 初期就已显现：《福布斯》2021 年的一篇报道以“由谷歌、彼得·蒂尔、埃里克·施密特支持的 Project Maven 初创企业”为题，梳理了 Maven 供应链中的风投背景[@mv_forbes_startups]。

!photo thiel_2022|彼得·蒂尔（2022 年 2 月）。蒂尔是 Palantir 联合创始人和 Founders Fund 创始人，Founders Fund 领投 Anduril 2024 年 F 轮和 2025 年 G 轮|Gage Skidmore，CC BY-SA 3.0

我部研判，资本对两系统的作用体现在两点。第一，Anduril 用风险资本自筹研发产品，再以成品争取合同，这一模式使其能在没有政府研发经费的情况下推出 Sentry、Anvil 等系列硬件，并自建“武库-1”工厂（获 JobsOhio 3.1 亿美元资助）和投资 37 亿美元的“武库-2”船厂[@la_dn_arsenal1,la_cnbc_sub]。第二，估值跃升与合同节点高度同步，2022 年 SOCOM 合同后进入 E 轮，2025—2026 年 NGC2、200 亿美元企业合同和 CCA 落地后估值翻倍，资本市场把 Anduril 当作“软件平台型主承包商”定价[@la_andurilnews_funding,la_ds_20b]。

## （二）Palantir 与 Maven 推动者

### 亚历克斯·卡普：Palantir 的对外代言人

亚历克斯·卡普（Alex Karp）是 Palantir 首席执行官。研究笔记中，卡普与 Maven 直接相关的公开表态集中在 2026 年：对伊朗作战期间，他在 CNBC 上称 Palantir 技术给了西方在中东的关键优势[@mv_cnbc_karp]；国防部据报于 2026 年 3 月 4 日把 Anthropic 列为“供应链风险”、要求 6 个月内淘汰其工具后，卡普在 CNBC 上表示 Claude 仍在目标系统中运行[@mv_aca_iran,mv_ie_claude]。这两处表态说明，卡普在 MSS 的大模型供应商问题上掌握着公开信息的主动权，五角大楼和 Anthropic 都没有发布一手文件澄清 Claude 的去留。

!photo karp_2015|Palantir 首席执行官亚历克斯·卡普工作照（2015 年 12 月）|Benamischarfstein（Wikimedia Commons），CC BY-SA 4.0

卡普任内，Palantir 走出了一条“诉讼—数据平台—唯一来源—企业协议”的路径。2016 年 5 月，SOCOM 以单一来源方式授予 Palantir 上限 2.22 亿美元的全源信息融合软件许可[@mv_wt_socom]；Defense News 2019 年的报道标题称其为“曾成功起诉陆军的 Palantir”，此后 Palantir 进入陆军分布式通用地面系统（DCGS-A）[@co_dn_2019_dcgs,mv_c4isr_dcgsa]；2024 年 Tech Inquiry 报道五角大楼认证 Palantir 为 MSS 唯一供应商[@mv_poulson_solesource]；2025 年 7 月 31 日，陆军与 Palantir 签订 10 年、上限 100 亿美元的企业协议，整合 75 份合同[@mv_wt_ea,mv_ds_ea]。在英国，2025 年 9 月英国国防部与 Palantir 建立战略伙伴关系，五年内最高 7.5 亿英镑的机会额，Palantir 另承诺到 2030 年对英投资最多 15 亿英镑[@co_govuk_palantir,co_bbg_uk_2509]。Palantir 美国政府收入 2025 年为 18.55 亿美元，同比增长 55%[@mv_pltr_q4_2025]。

### 沙姆·桑卡尔：“国防宗教改革”与 201 支队

沙姆·桑卡尔（Shyam Sankar）是 Palantir 首席技术官，TechCrunch 2024 年的专访称他是 Palantir 第 13 号员工，并把他描述为硅谷防务初创企业的“秘密武器”[@co_tc_sankar]。桑卡尔长期公开扶持由 Palantir、Tesla、SpaceX 校友创办的国防初创企业[@co_tc_sankar]。他仿照马丁·路德提出“国防宗教改革”18 条论纲，主张美国处于“未宣布的紧急状态”，并称冷战时期主要武器系统开支只有 6% 流向专业国防承包商，如今已升到 86%[@co_tectonic_sankar,co_schoolofwar]。这套论述为“新主承包商”叙事提供了最系统的理论版本。

2025 年 6 月 13 日，陆军成立“行政创新军团”即 201 支队，桑卡尔与 Meta 首席技术官安德鲁·博斯沃思、OpenAI 首席产品官凯文·威尔和前 OpenAI 首席研究官鲍勃·麦格鲁宣誓成为陆军预备役中校，以兼职技术专家身份参与“定向项目”，陆军称此举是为“陆军转型倡议”提速[@co_dn_det201,co_taskpurpose]。据陆军发布的照片说明，授衔仪式由陆军参谋长乔治上将讲话。

!photo det201_george|陆军“201 支队：行政创新军团”授衔仪式，陆军参谋长乔治上将讲话（2025 年 6 月 13 日）。Palantir 首席技术官桑卡尔在此次仪式上受衔陆军预备役中校|U.S. Army photo by Leroy Council，美国政府作品

研究笔记没有检索到桑卡尔关于 Maven 的具体表态，也没有找到他在 201 支队中所参与项目的公开清单。他的预备役身份与 Palantir 在陆军的合同集中同时存在，这一点在本章第五节讨论。

### 合同链上的其他企业角色

Maven 早期的主要集成商是 ECS Federal。ECS 自 2017 年起担任 Maven 的“AI 互操作集成商”，此后陆续持有 3 份与 Maven 相关、总额约 3.64 亿美元的合同，其中代号“Pavement”的主合同 1.42 亿美元；ECS 本身于 2018 年 4 月被 ASGN 以 7.75 亿美元收购[@mv_execbiz_ecs,mv_itpro,mv_poulson_pavement,mv_fedsavvy]。ECS 高管约翰·赫尼根（John Heneghan）曾就 NGA Maven 项目接受专访[@mv_execbiz_ecs]。

谷歌是 Maven 早期最受关注、也最早退出的企业。2018 年春谷歌员工联名请愿反对参与 Maven，签名人数有近 4,000 人和 4,600 人以上等说法，约十余人辞职；2018 年 6 月 1 日前后，谷歌云首席执行官黛安·格林告知员工，合同 2019 年 3 月到期后不再续约[@mv_gizmodo_au_resign,mv_fortune_2018,mv_nbc_google]。谷歌的位置随后由 ECS 的其他分包商和 Palantir 填补。2026 年 Anthropic 因拒绝把模型用于大规模国内监控和完全自主武器而被国防部据报列为“供应链风险”，这是继谷歌之后第二起供应商因用途限制与五角大楼公开冲突的事件[@mv_aca_iran]。

标注环节的企业同样关键。Scale AI 2024 年 7 月获得约 2,400 万美元的 NGA Maven 数据标注过渡合同，2025 年 11 月 Enabled Intelligence 赢得上限 7.08 亿美元的 SEQUOIA 合同，Scale AI 先向 GAO 抗议被驳回，再起诉至联邦索赔法院，法院未推翻授标[@mv_nga_contracts,mv_bd_sequoia,mv_orangeslices]。Scale AI 同时是 Lattice SDK 首批合作伙伴，并牵头 DIU 的 Thunderforge 项目，该项目以 Lattice 为数据共享层[@la_ocbj_partners,la_ds_thunderforge]。我部研判，同一批企业在 Maven 的模型侧、Lattice 的开发者生态和联合层级项目中交替以竞争者与合作者身份出现，是这一领域的常态。

## （三）国防部与军方推动者

### 立项者：罗伯特·沃克

罗伯特·沃克（Robert O. Work）时任国防部常务副部长，2017 年 4 月 26 日签署《成立算法战跨职能小组（Project Maven）》备忘录，以“加速国防部整合大数据和机器学习”，首个任务是战术和中空无人机全动态视频的处理、利用和分发[@mv_work_memo,mv_globalsec]。Maven 成立约两个月内即从国会获得约 7,000 万美元[@mv_wiki_maven]。沃克备忘录的制度意义在于采用了“跨职能小组”的组织形式，使一个小团队可以绕开传统的需求论证—研制—试验—列装流程，直接对接作战用户、商业供应商和经费渠道[@mv_wiki_maven,mv_trajectory]。

!photo work_portrait_crop|罗伯特·沃克官方肖像（裁切，2014 年）。沃克任国防部常务副部长期间签署成立算法战跨职能小组的备忘录，是 Project Maven 的立项人|美国国防部，美国政府作品

### 执行者：杰克·沙纳汉与德鲁·库科

杰克·沙纳汉（Jack Shanahan）空军中将自 2017 年 4 月至 2018 年 12 月负责 Maven 的总体指导，随后出任新成立的联合人工智能中心（JAIC）首任主任；陆战队上校德鲁·库科（Drew Cukor）是算法战跨职能小组负责人，承担大量日常领导工作[@mv_wiki_maven,mv_globalsec]。2017 年 7 月，项目方公开表示要在“年底前”把算法部署到战区，12 月首个识别 ScanEagle 视频物体的算法即部署中东；沙纳汉把这种做法称为“原型战”[@mv_techsparx,mv_nextgov_2017]。

!photo shanahan_2015|杰克·沙纳汉中将官方肖像（2015 年 8 月）。沙纳汉 2017—2018 年指导 Project Maven，随后任联合人工智能中心首任主任|U.S. Air Force，美国政府作品

沙纳汉的调任没有改变 Maven 的隶属关系。JAIC 成立后，Maven 仍留在负责情报的副部长办公室之下，JAIC 从来不是 Maven 的主管单位，二者后来在 2022 年一同并入首席数字与人工智能办公室（CDAO）[@mv_wiki_maven]。2019 年 9 月 4 日，沙纳汉以 JAIC 主任身份在第 10 届 Billington 网络安全峰会发言，此时他已从 Maven 的执行者转为国防部 AI 整体推进的牵头人。

!photo shanahan_billington|沙纳汉在第 10 届 Billington 网络安全峰会发言（2019 年 9 月 4 日）。此时沙纳汉已任联合人工智能中心主任|美国国防部，美国政府作品

库科的公开资料较少。2026 年 3 月，彭博社记者凯特琳娜·曼森（Katrina Manson）出版专著《Project Maven：一位陆战队上校、他的团队与 AI 战争的黎明》，书名中的“陆战队上校”推测指库科，检索结果未直接确认[@mv_npr_book]。该书称美方向乌克兰发送了“数以万计”的目标，是迄今关于 Maven 内部运作最详细的公开叙事[@mv_lawfare_book,mv_willis_book]。

### 制度化推动者：希克斯与 CDAO 负责人

凯瑟琳·希克斯（Kathleen Hicks）时任国防部常务副部长，在两个方向上推动了两系统。一是要求 CDAO 在 2023 年底前通过“全球信息主导实验”（GIDE）交付联合全域指挥控制（CJADC2）的最小可行能力，该能力 2023 年 12 月获认证、2024 年 2 月公布，MSS 为其事实骨干[@mv_ds_mvp_2023,mv_ds_cjadc2_mvc]；二是提出“复制者”计划，目标是在 2025 年 8 月前部署“数千个”全域、可消耗的自主系统，Anduril 的 Ghost-X、ALTIUS-600 和 Lattice 协同组队软件均在其中[@co_armytimes_replicator,co_pacom_hicks,co_diu_replicator_sw]。

CDAO 于 2022 年成立，承接 Maven 的非 GEOINT 部分及 JAIC 等机构[@mv_bd_2022_nga]。据国防部发布的图片说明，马特尔（Craig Martell）博士 2024 年 2 月以 CDAO 身份主讲“AI 现状与 CDAO”专场[@gp_dvids_martell]。研究笔记未能以一手来源核实 2022—2025 年 CDAO 历任负责人名单，因此本报告不对马特尔任内具体决策作归因。可以确认的是，CDAO 在 2024 年 12 月授予 Anduril 1 亿美元生产型协议推广 Lattice 边缘数据网格，同年启动 Open DAGIR 计划把第三方应用接入 MSS 数据层，同时持有两系统的合同[@la_ds_cdao,mv_bd_opendagir]。

!photo martell_session|“AI 现状与 CDAO”——马特尔博士专场活动（2024 年 2 月）。CDAO 同时是 MSS 的主管机构和 Lattice 边缘数据网格合同的授予方|美国国防部（DVIDS），美国政府作品

2026 年的 CDAO 由卡梅伦·斯坦利（Cameron Stanley）领导。斯坦利 2026 年 5 月 14 日向众议院军事委员会提交书面证词，称 MSS 把目标周期“从数天压缩到数秒”；9 月 22 日他又称 Maven 在“史诗怒火”行动 38 天中帮助打击了 13,000 个目标，并正在扩展到后勤、供应链、战备和预算数据[@mv_stanley_testimony,mv_ds_mazol]。同场会议上，负责研究与工程的副次长詹姆斯·马佐尔（James Mazol）称 MSS 用户从 2026 年 1 月的约 5 万人增至 10 万人以上[@mv_ds_mazol]。2026 年 8 月 5 日，陆军上校莫莉·索尔斯伯里（Molly Solsbury，ai.mil 简历写作 Melissa）被任命为 CDAO 内的 MSS 项目主任，此前任职于陆军参谋长办公室[@mv_ds_solsbury,mv_aimil_solsbury]。斯坦利和马佐尔的数字是在申请预算和推动转正式项目的背景下提出的，没有公开方法说明。

### NGA：惠特沃斯与 GEOINT 流水线

2022 年 4 月，国家地理空间情报局（NGA）宣布接管 Maven 的 GEOINT AI 服务，约占原项目的 80%，自 2023 财年起生效；2023 年 11 月，“NGA Maven”成为该局的正式采购项目[@mv_bd_2022_nga,mv_dd_por]。NGA 局长弗兰克·惠特沃斯（Frank Whitworth）海军中将是这一阶段 Maven 最主要的公开发言人。2025 年 5 月 GEOINT 大会上，他称 Maven 已向所有军种和作战司令部开放，活跃用户超过 2 万，覆盖 35 个以上工具、3 个安全域，并披露 NGA 另授予 Palantir 2,800 万美元合同以扩大分析员访问[@mv_bd_geoint2025,mv_meritalk_nga]。2025 年 6 月，他称 NGA 在所有 AI 生成的产品上加注“机器生成的地理空间情报”标签，这类模板化产品的分发过程中“没有人工经手”[@mv_bd_nohands]。他还表示 Maven 下一阶段要加入“推理”能力，从识别物体走向预测威胁，但向作战司令或总统汇报前仍需人工佐证[@mv_meritalk_nga,mv_execgov_predict]。

!photo nga_new_hq|国家地理空间情报局（NGA）新总部大楼（弗吉尼亚州斯普林菲尔德，约 2011 年）。NGA 自 2023 财年起主管 Maven 的 GEOINT 模型流水线，至 2026 年 3 月前承担 MSS 系统管理与运行授权职责|NGA，可能属公有领域（待核）

惠特沃斯任内的“机器生成”标签是目前公开可见的、针对 AI 情报产品的少数制度化治理措施之一。研究笔记没有找到其继任者姓名。2026 年 3 月 Feinberg 备忘录生效后，MSS 的系统管理权移出 NGA，NGA 保留模型流水线和 GEOINT 产品治理[@mv_ds_feinberg2,mv_fnn_agaim]。

### 第二届特朗普政府决策层：赫格塞斯、范伯格与迈克尔

皮特·赫格塞斯（Pete Hegseth）任国防部长（战争部长）后，从三个方向为两家企业的扩张提供了制度条件。第一是无人机政策：2025 年 7 月 10 日公开的“释放美军无人机主导权”备忘录把小型无人机重新归类为消耗性弹药，采购权下放到上校级指挥官，目标是 2026 年底前每个班配备无人机[@co_dronelife_memo,co_insidedef_hegseth_memo]。第二是采办改革：2025 年 11 月 7 日，他在国防大学讲话并签发备忘录，把“国防采办体系”更名为“作战采办体系”，项目执行官改组为可在组合内调剂资金的组合采办执行官，并警告不配合的大公司“可能会消失”[@co_ds_2511_acq]。第三是自主作战机构：“复制者”组合 2025 年秋从 DIU 移交特种作战司令部下新设的自主作战群（DAWG），由他任命的陆战队中将弗朗西斯·多诺万（Francis L. Donovan）负责；他承诺建立的自主作战次级联合司令部截至 2026 年 5 月未建立[@co_wt_dawg,co_gs_dawg,co_igc_subunified]。

!photo hegseth_portrait|国防部长（战争部长）皮特·赫格塞斯官方肖像（2025 年 1 月）。赫格塞斯签发无人机主导权备忘录和采办转型备忘录，并因 Minab 学校遇袭事件收到国会议员联名信|美国国防部，美国政府作品

赫格塞斯同时是 Maven 问责压力的承受者。2026 年 3 月 12 日，120 多名众议院民主党议员就 Minab 学校遇袭事件致信赫格塞斯，46 名参议员另有类似要求，五角大楼以调查尚在进行为由回应[@mv_gizmodo_minab,mv_wiki_minab]。

史蒂夫·范伯格（Steve Feinberg）任国防部常务副部长，2026 年 3 月 9 日签发的备忘录是 MSS 制度化的关键文件：MSS 须在 2026 财年结束前成为正式采购项目，系统管理职责 30 天内从 NGA 移交 CDAO 新设的 MSS 项目办公室，所有 MSS 合同转入陆军企业协议，负责研究与工程的副部长接任授权官[@mv_ds_feinberg1,mv_ds_feinberg2,mv_csis]。备忘录同时要求首席技术官埃米尔·迈克尔（Emil Michael）评估是否把 MSS 纳入拟设的 CJADC2 项目办公室，并把“AI 赋能决策”定为 CJADC2 的“基石”[@mv_ds_feinberg1]。转正式项目是否按期完成，截至 2026 年 10 月未见国防部或 CDAO 的正式确认[@mv_govconwire_por]。

### 陆军：两份企业协议背后的军种

陆军是两家合作最集中的军种，NGC2、TITAN 和两份企业协议都在陆军。研究笔记记录的陆军关键人物分三类。

决策与监督层面，陆军参谋长主持了 201 支队授衔仪式，2024 年 3 月“项目融合—顶点 4”期间还听取了 Anduril Ghost 能力简报[@co_dn_det201,gp_dvids_pcc4_csa]。陆军首席技术官加布里埃尔·奇乌利（Gabriele Chiulli）2025 年 9 月 5 日签发备忘录，称 NGC2 原型应被视为“极高风险”，写道“我们无法控制谁看到什么，无法看到用户在做什么，也无法验证软件本身是安全的”[@la_reuters_memo]。陆军首席信息官莱昂内尔·加西加（Leonel Garciga）称备忘录属于分诊流程的一部分，陆军随后表示关键缺陷已缓解[@la_bd_memo]；陆军首席信息官还把 Palantir 的 100 亿美元企业协议称为“风向标”[@co_d1_2508_ea]。这两位官员分别代表了陆军内部对快速采购的安全质疑和对企业协议模式的认可。

一线用户层面，XVIII 空降军是把 Maven 改造成目标工作流平台的主要推手，自 2020 年起通过“猩红之龙”系列演习与多达 70 家公司合作[@mv_d1_2024_08,mv_cset_coalition]。该军资深目标官 Temple 对彭博社估计，借助 Maven 他每小时可签批多达 80 个目标，不用时约 30 个，同时提醒完全信任机器会引入错误[@mv_bloomberg_2024]。第 4 步兵师则是 Lattice 在 NGC2 中的首个用户，2025 年 9 月起通过“常春藤之刺”系列演习把师级目标处理流程搬上 Lattice Mesh 和 Palantir Target Workbench[@la_bd_ivysting1,la_army_ivysting1]。

陆军副部长迈克尔·奥巴达尔（Michael Obadal）是本章唯一一位从两家企业直接进入国防部高层的官员，其情况在第五节讨论。

### 联合与战区层面的推动者

中央司令部首席技术官舒伊勒·摩尔（Schuyler Moore）是首位公开确认 Maven 用于实战打击的官员：她对彭博社表示，2024 年 2 月对伊拉克、叙利亚的 85 次以上打击中，机器学习目标识别帮助“缩小目标范围”，每一步以人工验证结束；她还介绍 Maven 被用于定位也门境内的火箭发射器和红海水面船只[@mv_register_2024,mv_bloomberg_2024]。

印太司令部司令塞缪尔·帕帕罗（Samuel Paparo）上将 2024 年 6 月提出“无人地狱景观”构想，在入侵部队渡海时投放无人机、无人潜航器和无人水面艇群，为美国及盟友争取约一个月时间[@co_wt_hellscape]。台湾采购的 ALTIUS 系列被纳入这一构想的讨论框架[@co_usni_hellscape]。金穹导弹防御负责人、太空军上将迈克尔·盖特莱因（Michael Guetlein）把 Anduril 与 Palantir 据报共同开发的指挥控制软件称为“胶水层”，并说“指挥控制将是我们的秘方”[@co_cxo_gd]。空军部长米因克 2026 年 9 月把 CCA 目标提高到 2032 年前至少 500 架（二手来源）[@la_migflug]。

北约一侧，北约通信与信息局（NCIA）2025 年 3 月 25 日完成 MSS NATO 采购，从提出需求到签约约 6 个月；2026 年 7 月 7 日又授出增强型空中指挥控制（eAirC2）评估合同，Anduril、Palantir 与法国 Athea 同场竞争[@mv_ncia_2025,mv_shape_2025,la_ncia_nato]。研究笔记没有记录推动这两项采购的北约具体官员姓名。

### 人物一览

{tab:t_gp_people}汇总本章涉及的主要人物。

!table t_gp_people|推动两系统的关键人物一览|本报告依据研究笔记整理；职务为相关事件发生时的职务|28,40,92
人物|身份|与两系统的关系
帕尔默·勒基|Anduril 联合创始人，Oculus 创办人|公司对外代言；2025 年赴台交付无人机，2026 年访问太空系统司令部[@la_builtin_luckey,gp_udn_luckey,gp_dvids_luckey_ssc]
布赖恩·申普夫|Anduril 联合创始人、首席执行官|前 Palantir 工程负责人，参与构建 Foundry；主导 Lattice 平台化[@co_a16z_schimpf]
特雷·斯蒂芬斯|Anduril 联合创始人，Founders Fund 合伙人|连接 Anduril 与 Founders Fund（领投 F、G 轮）[@la_andurilnews_funding]
马特·格林、陈乔|Anduril 联合创始人|格林出自 Palantir；职责无公开记录[@la_wiki_anduril]
彼得·蒂尔|Palantir 联合创始人，Founders Fund 创始人|两家共同的资本与人脉源头[@co_tc_sankar]
亚历克斯·卡普|Palantir 首席执行官|对伊作战期间称 Claude 仍在目标系统中运行[@mv_aca_iran,mv_cnbc_karp]
沙姆·桑卡尔|Palantir 首席技术官，陆军预备役中校|“国防宗教改革”论纲；201 支队成员[@co_tectonic_sankar,co_dn_det201]
罗伯特·沃克|时任国防部常务副部长|2017-04-26 签署 Maven 立项备忘录[@mv_work_memo]
杰克·沙纳汉|空军中将，后任 JAIC 首任主任|2017-04 至 2018-12 指导 Maven[@mv_wiki_maven]
德鲁·库科|陆战队上校|算法战跨职能小组负责人[@mv_globalsec]
凯瑟琳·希克斯|时任国防部常务副部长|推动 CJADC2 最小可行能力与“复制者”[@mv_ds_mvp_2023,co_pacom_hicks]
弗兰克·惠特沃斯|NGA 局长|公开 Maven 用户规模；推行“机器生成”标签[@mv_bd_geoint2025,mv_bd_nohands]
皮特·赫格塞斯|国防部长（战争部长）|无人机主导权与采办转型备忘录；收到 Minab 事件联名信[@co_ds_2511_acq,mv_gizmodo_minab]
史蒂夫·范伯格|国防部常务副部长|2026-03-09 备忘录推动 MSS 转正式项目[@mv_ds_feinberg1]
埃米尔·迈克尔|国防部首席技术官|评估将 MSS 纳入拟设 CJADC2 项目办公室[@mv_ds_feinberg1]
卡梅伦·斯坦利|CDAO|称 38 天打击 13,000 个目标；“数天到数秒”[@mv_ds_mazol,mv_stanley_testimony]
詹姆斯·马佐尔|负责研究与工程的副次长|公布 MSS 用户 10 万以上[@mv_ds_mazol]
莫莉·索尔斯伯里|陆军上校，CDAO MSS 项目主任|2026-08-05 任命[@mv_ds_solsbury]
加布里埃尔·奇乌利|陆军首席技术官|NGC2“极高风险”备忘录[@la_reuters_memo]
迈克尔·奥巴达尔|陆军副部长，前 Anduril 高级总监|2025-09-22 就职，承诺不再持有 Anduril 股票[@co_ds_obadal,co_insidedef_obadal]
舒伊勒·摩尔|中央司令部首席技术官|首次公开确认 Maven 用于实战打击[@mv_register_2024]
弗朗西斯·多诺万|陆战队中将，DAWG 负责人|接管“复制者”组合[@co_gs_dawg]
迈克尔·盖特莱因|太空军上将，金穹负责人|称指挥控制软件为“胶水层”[@co_cxo_gd]
塞缪尔·帕帕罗|印太司令部司令|“无人地狱景观”构想[@co_wt_hellscape]
!end

## （四）关键机构与职责

两系统的推动与管理分散在十余个机构中。Maven 一侧的机构链条随治理改组多次变化，Lattice 一侧则表现为“多个项目办公室分头采购同一软件”。{tab:t_gp_orgs}按机构列出职责和与两系统的关系，下文再作分析。

!table t_gp_orgs|关键机构—职责—与两系统关系|本报告依据第一、二、四、五章与研究笔记整理|34,52,74
机构|职责|与两系统的关系
算法战跨职能小组（AWCFT）|2017 年依沃克备忘录成立，隶属负责情报的副部长办公室|即 Project Maven 本体；2022 年拆分为 NGA Maven 与 CDAO/MSS 两条线[@mv_work_memo,mv_bd_2022_nga]
联合人工智能中心（JAIC）|2018 年成立，国防部 AI 统筹|从未主管 Maven；首任主任为沙纳汉；2022 年并入 CDAO[@mv_wiki_maven]
首席数字与人工智能办公室（CDAO）|2022 年成立，国防部数据与 AI 主管；现隶属研究与工程副部长|MSS 项目办公室所在地；授予 Lattice 边缘数据网格 1 亿美元协议；Open DAGIR[@mv_ds_feinberg2,la_ds_cdao,mv_bd_opendagir]
国家地理空间情报局（NGA）|地理空间情报主管机构|NGA Maven 模型流水线与标注合同；2026 年 3 月前承担 MSS 系统管理与运行授权[@mv_dd_por,mv_bd_sequoia]
国防创新单元（DIU）|商业技术快速引进|“复制者”软件授标（Lattice 入选 ACT）；Dive-LD 原型；Thunderforge[@co_diu_replicator_sw,la_dn_diveld,la_diu_thunderforge]
陆军 PEO C3N|陆军指挥控制通信网络项目执行办公室|NGC2 原型与推广合同授标方（Lattice 数据层）[@co_anduril_ngc2_pr,la_ds_icorps]
陆军 PEO IEW&S|情报电子战与传感器项目执行办公室|TITAN 地面站（Palantir 主承、Anduril 分包）[@mv_ds_titan,co_bd_2609_titan]
陆军合同司令部阿伯丁分部与陆军研究实验室|合同签订与研发|MSS 主合同 W911QX-24-D-0012；MSS 军种扩展合同[@mv_ds_2024_05,mv_govconwire_arl]
自主作战群（DAWG）|2025 年接管“复制者”组合，隶属特种作战司令部|承接 Lattice 赢得的 ACT 群体协同软件角色；FY2027 申请约 546 亿美元[@co_wt_dawg,co_gs_dawg]
JIATF-401|陆军牵头的联合跨机构反无人机特遣部队|Lattice 作为通用反无人机指挥控制，首单约 8,700 万美元[@la_bd_jiatf]
特种作战司令部（SOCOM）|特种作战装备采办|Lattice 反无人系统集成伙伴（上限 9.676 亿美元）；Palantir 全源情报融合、任务指挥[@la_wt_socom,mv_wt_socom]
陆战队（含地基防空项目办公室）|陆战队装备与许可|I-CsUAS、MADIS 采用 Anduril 系统；MSS 企业许可（SIPRNet IL6）[@la_ds_icsuas,mv_usmc_release]
空军与太空系统司令部|空天装备采办|CCA（YFQ-44A、LMA）；SSN 现代化；天基拦截器原型[@la_ds_cca_prod,la_ds_ssn,la_bloomberg_sbi]
海关与边境保护局（CBP）|边境监视|Lattice 首个客户；AST 正式采购项目；XRST 3.63 亿美元[@la_cbp_por,la_execbiz_xrst]
北约 NCIA 与 SHAPE|北约采办与盟军作战司令部|MSS NATO 采购与运行（2026-06 全面作战能力）；eAirC2 评估（Lattice 与 Palantir 竞争）[@mv_ncia_2025,mv_shape_foc,la_ncia_nato]
!end

### 治理链的三次改组

Maven 一侧的治理链经历了三次改组。2017—2022 年，算法战跨职能小组隶属负责情报的副部长办公室，以“探路者”方式运作[@mv_work_memo,mv_wiki_maven]。2022 年起，GEOINT 部分划归 NGA，非 GEOINT 部分划归新成立的 CDAO，MSS 形成“CDAO 主管、NGA 承担系统管理与运行授权、陆军负责签约”的三方结构[@mv_bd_2022_nga,mv_ds_2024_03]。2026 年 3 月 Feinberg 备忘录把系统管理集中到 CDAO 下的 MSS 项目办公室，合同集中到陆军企业协议，授权官改由研究与工程副部长担任[@mv_ds_feinberg1,mv_ds_feinberg2]。三次改组的共同方向是把 Maven 从情报系统的附属项目，转为研究与工程体系下的作战平台。改组的代价是透明度：2022 年移交期间五角大楼对 Maven“保持沉默”，2024 年后 NGA、CDAO 和情报副部长办公室对 Maven“大体守口如瓶”，Maven 预算被列为机密且不适用《信息自由法》[@mv_ds_2022_cr,mv_ds_2024_03,mv_lawfare_book]。

### Lattice 的“多头采购”格局

Lattice 一侧没有统一的主管机构，它以软件内核身份嵌入各项目办公室的合同：SOCOM、陆战队、陆军 PEO C3N、陆军防空项目、CDAO、DIU、太空系统司令部、CBP 和北约 NCIA 都是直接客户[@la_wt_socom,la_ds_icsuas,la_army_ngc2_award,la_ds_ibcsm,la_ds_cdao,la_ds_ssn,la_cbp_por,la_ncia_nato]。2026 年 3 月陆军企业合同是第一次尝试把分散采购收拢：120 多项采购行动并入一个以 Lattice 为中心的框架，其他联邦机构也可以使用[@la_army_20b,la_ds_20b]。我部研判，这一格局使 Lattice 的实际地位难以从预算文件中读出，它没有单列预算线，规模取决于所嵌入项目的预算，FY2027 自主系统预算尤其是 DAWG 的最终拨款将直接影响其增长空间[@co_fy27_book,co_gs_dawg]。

### 机构间的交叉点

CDAO 和陆军是两系统的交叉机构。CDAO 同时持有 MSS 和 Lattice 边缘数据网格合同，在 CJADC2 组合中前者承担企业层、后者承担边缘层[@mv_ds_cjadc2_mvc,la_ds_cdao]。陆军同时与两家签订结构相同的十年期企业协议，Palantir 协议上限 100 亿美元、Anduril 协议上限 200 亿美元，并在 NGC2 通用数据层基线中把“Lattice 加 Foundry”定为标准结构[@mv_wt_ea,la_ds_20b,la_ds_cdl]。陆军自己把“避免厂商锁定”列为通用数据层的关键考虑，但实际走向是向两家基线收敛[@la_bd_cdl]。北约 NCIA 是两家正面竞争的唯一机构，eAirC2 评估结果约在 2027 年春揭晓[@la_ncia_nato]。

## （五）旋转门与利益关联

本节只列有据可查的人员流动、资本关联和利益冲突质疑，并按“事实—争议—证据边界”陈述。

### 奥巴达尔：从 Anduril 到陆军副部长

2025 年 3 月 11 日，特朗普提名 Anduril 高级总监、前特种作战军官迈克尔·奥巴达尔为陆军副部长；参议院以 51 票对 47 票确认，他于 2025 年 9 月 22 日宣誓就职[@co_ds_obadal,co_rs_obadal]。据 The Intercept 引述伦理披露文件，他曾计划保留 Anduril 股票，后修改伦理协议，承诺不再持有[@co_intercept_obadal,co_insidedef_obadal]。奥巴达尔任职期间，陆军先后授予 Anduril 上限 200 亿美元的企业合同、NGC2 通用数据层基线和上限 18 亿美元的 NGC2 推广合同[@la_ds_20b,la_ds_cdl,la_ds_icorps]。研究笔记没有找到奥巴达尔参与或回避这些合同决策的公开记录，也没有找到国会或监察长就此开展审查的记录。

### 201 支队：企业高管进入军队预备役

桑卡尔等四名科技高管以陆军预备役中校身份进入 201 支队，以兼职技术专家参与“定向项目”[@co_dn_det201,co_taskpurpose]。这一安排使 Palantir 首席技术官在陆军内部拥有正式身份，同期 Palantir 在陆军获得 100 亿美元企业协议、TITAN 生产合同和 NGC2 团队成员资格[@mv_wt_ea,co_bd_2609_titan,la_army_ngc2_award]。陆军没有公开 201 支队成员所参与项目的清单及利益冲突回避规则，研究笔记也没有检索到相关审查。

### 同源网络：Palantir 校友与 Founders Fund

两家共享“Palantir 系”人脉和蒂尔资本网络：Anduril 五位创始人中三人出自 Palantir，斯蒂芬斯任 Founders Fund 合伙人，Founders Fund 领投 Anduril 的 F、G 两轮，桑卡尔长期扶持 Palantir 校友创办的国防初创企业[@co_tc_sankar,la_andurilnews_funding,co_a16z_schimpf]。研究笔记没有找到两家联合游说、共同出资行业组织的可靠来源。我部研判，同源网络的直接效果是降低合作成本：2024 年 12 月合作公告到 2025 年 7 月 NGC2“Team Anduril”成立只用了 7 个月，2026 年 6 月“Lattice 加 Foundry”即被定为全陆军基线[@la_bw_palantir,la_army_ngc2_award,la_ds_cdl]。同一网络也意味着陆军的两家“平台型供应商”在人事与资本上并不独立，这一点在评估“避免厂商锁定”时需要考虑。

### 唯一来源、记录删除与预算保密

Palantir 在 MSS 上的地位部分建立在唯一来源认证之上，据 Tech Inquiry 报道，五角大楼认证 Palantir 为 MSS 唯一供应商[@mv_poulson_solesource]。Maven 早期合同的公开记录有缺口：代号“Pavement”的 1.42 亿美元 ECS 主合同和一份 5,225 万美元的关联合同，被五角大楼依据《联邦采购条例》第 4.606 条从公开采购数据库中删除，国防部长办公室发言人确认了删除行为[@mv_poulson_pavement,mv_poulson_erasure]。Maven 预算被列为机密[@mv_lawfare_book]。2026 年起，MSS 新采购经陆军企业协议执行，可能不再有独立的合同公告[@mv_ds_feinberg1]。这些安排各有其制度依据，但叠加之后，外界核查 Maven 经济规模和供应商关系的难度持续上升。

### 政治资金与“新主承包商”叙事

Punchbowl News 报道过卡普与勒基的政治献金，细节未获取[@co_punchbowl]。“新主承包商”叙事由两家及其投资网络共同塑造：桑卡尔的 18 条论纲、勒基关于“半数预算”的表态、行业分析对 Anduril“新主承包商崛起”的定性，以及《纽约书评》描述的“新国防科技阵营”对传统主承包商“僵化、低效、垄断”的抨击[@co_tectonic_sankar,co_fpif,co_fedsavvy_neoprime,co_nyrb]。这一叙事在赫格塞斯 2025 年 11 月的采办改革讲话中得到官方呼应，他警告不配合的大公司“可能会消失”[@co_ds_2511_acq]。我部研判，叙事与制度改革同向，为企业协议、其他交易授权和商业优先等安排提供了舆论正当性，但这属于政策倾向，不构成利益输送证据。

### 反向力量：员工抗议、供应商冲突与国会问询

推动力量之外，研究笔记也记录了几股制约力量。2018 年谷歌员工抗议迫使谷歌退出 Maven[@mv_nbc_google]。2026 年 Anthropic 因拒绝把模型用于大规模国内监控和完全自主武器，据报被列为供应链风险[@mv_aca_iran]。2025 年 9 月陆军首席技术官的“极高风险”备忘录来自军方内部[@la_reuters_memo]。2026 年 3 月，120 多名众议院民主党议员和 46 名参议员就 Minab 事件致信国防部长[@mv_gizmodo_minab]。在盟国层面，欧洲评论认为 MSS NATO 意味着美国软件影响欧洲军事决策，德国对 Palantir 有所保留，日本执政联盟内部有人担忧过度依赖外国供应商[@co_escudo_eu,co_escudo_germany,co_defpost_japan]。这些制约因素至今没有改变两系统的扩张方向，但它们构成了未来政策调整的潜在触发点。

:::judge 研判要点
- 两系统的扩张由少数关键人物在关键节点上的决定推动：沃克 2017 年立项、沙纳汉与库科以“原型战”方式 8 个月上线首个算法、希克斯推动 CJADC2 与“复制者”、范伯格 2026 年备忘录推动 MSS 转正式项目、赫格塞斯以无人机与采办备忘录重塑采购规则。
- 企业一侧形成了以 Palantir 校友和 Founders Fund 为核心的同源网络：Anduril 五位创始人中三人出自 Palantir，申普夫曾参与构建 Foundry，斯蒂芬斯连接 Founders Fund，桑卡尔提供“国防宗教改革”理论叙事。同源性降低了两家合作成本，也削弱了陆军“避免厂商锁定”目标下两家供应商的相互独立性。
- Maven 的治理链经三次改组，从情报副部长办公室转到 NGA 与 CDAO，再集中到研究与工程体系下的 CDAO MSS 项目办公室；Lattice 没有统一主管机构，以软件内核身份嵌入十余个机构的合同。CDAO 和陆军是两系统的交叉机构，北约 NCIA 是两家正面竞争的唯一机构。
- 旋转门与利益关联有据可查的节点是奥巴达尔由 Anduril 出任陆军副部长、桑卡尔进入 201 支队、Palantir 获唯一来源认证和 Maven 早期合同记录被删除；没有证据表明存在利益输送，但陆军未公开相关回避规则和审查记录，这将持续成为国会和舆论的关注点。
- 建议后续重点跟踪三类人事信号：CDAO MSS 项目办公室与拟设 CJADC2 项目办公室的人员安排，NGC2 推广中陆军 PEO C3N 的决策人员，以及北约 eAirC2 选型的评审机构构成。
:::
