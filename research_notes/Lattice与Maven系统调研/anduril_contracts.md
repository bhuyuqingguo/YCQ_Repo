# Anduril Industries 政府合同与任务目录（2017 – 2026年10月），侧重 Lattice

> 方法说明：本笔记基于 WebSearch 检索结果摘要编制（约 25 次检索），**未逐页抓取原文**（WebFetch 未使用/可能被拦截），因此金额、日期以检索摘要中引用的媒体/官方表述为准；凡单一来源或来源冲突处均已标注。"Lattice?" 一栏：**Y** = 来源明确提到 Lattice；**(Y)** = 系统架构上基于 Lattice（如 Sentry/C-UAS 体系）但该条来源未明确写出；**N/?** = 未提及。
> 金额区分：**上限（ceiling）** ≠ **已拨付（obligated）** ≠ **FMS 批准估值**（DSCA 通知仅为可能销售的估算上限，非合同）。

## 问题一：主合同表（按时间排序）

### Takeaway
Anduril 从 2018 年 CBP 边境塔试点起步，2022 年 SOCOM 9.676 亿美元 C-UAS 集成商合同是首个近十亿级合同；2024–2026 年合同规模急剧放大，2026 年出现 200 亿美元 Army 企业协议（上限）、29 亿美元海军潜艇部件合同、18 亿美元 NGC2 扩展合同。大部分 C2/C-UAS 合同以 Lattice 为核心软件。

### Cited Findings

#### 主表

| # | 日期 | 客户 | 项目 | 合同形式 | 金额（上限/已拨付，币种） | 期限 | 范围（Lattice/硬件作用） | 状态 | Lattice? | 来源 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2018 | 美国 CBP | Autonomous Surveillance Tower (AST) 试点 | 试点/测试 | 未查到可靠金额（任务书中 "$4.8M" 未能核实） | — | Sentry 塔首次部署于 CBP AST 试点 | 已完成，转为项目 | (Y) | [Privacy International](https://privacyinternational.org/report/5704/dual-use-tech-anduril-example) |
| 2 | 2019 | 美国 CBP | AST 测试（5 座测试塔） | 测试 | 未披露 | — | 5 座测试塔，后扩至数百座 | 已完成 | (Y) | [ExecutiveBiz](https://www.executivebiz.com/articles/cbp-anduril-extended-range-sentry-towers-363m) |
| 3 | 2020-07 | 美国 CBP | AST 列为 Program of Record | 5年合同 | **未披露**；高管称"数亿美元"；Privacy International 称 $250M/5年 | 5年 | 计划部署 200 座塔（FY21–22 再采购 140 座，加既有 60 座） | 执行；2024-09 第 300 座塔部署，覆盖约 30% 南部陆地边境（公司说法） | (Y) | [FedScoop](https://www.fedscoop.com/anduril-sentry-towers-cbp/); [Nextgov](https://nextgov.com/acquisition/2020/07/cbp-taps-anduril-for-virtual-border-sentinel-system/257835); [Defense Daily](https://defensedaily.com/cbp-makes-autonomous-surveillance-tower-program-record/homeland-security); [Privacy International](https://privacyinternational.org/report/5704/dual-use-tech-anduril-example) |
| 4 | 2021-09 | 英国 MoD（Strategic Command jHub） | TALOS 基地防御试验 | 试验合同 | £3.8M（≈US$5.2M） | 最长2年 | 基于 Lattice，Sentry 塔+地面传感器+无人机检测分类跟踪入侵（地面与空中） | 已完成 | **Y** | [EDR Magazine](https://www.edrmagazine.eu/uk-mod-awards-3-8-million-contract-for-advanced-base-protection-system); [Anduril blog](https://blog.anduril.com/anduril-industries-to-provide-advanced-force-protection-technology-to-uk-ministry-of-defences-f34f32d71cc7) |
| 5 | 约2021–2022（日期未核实） | 英国 Home Office | 边境/海峡监视 | 服务合同 | 初始 £16M/3年，延至 2026 累计 £21M | 至2026 | 监视（细节未详） | 执行 | ? | [Privacy International](https://privacyinternational.org/report/5704/dual-use-tech-anduril-example) |
| 6 | 2022-01 | 美国 SOCOM | C-UxS 系统集成伙伴 | IDIQ（H92402-22-D-0001），源自原型项目竞争（12 份提案） | **上限 $967,599,957**；授予时拨付 $1,096,092（FY22 O&M） | 10年，至 2032-01-19（GovConWire 误作 2023） | 集成传感器/效应器构建分层 C-UAS，交付 Lattice，配 Sentry、Anvil、Pulsar、FoxHound | 执行 | **Y** | [Anduril blog](https://blog.anduril.com/special-operations-command-selects-anduril-industries-as-systems-integration-partner-e40da542f18d); [Washington Technology](https://washingtontechnology.com/companies/2022/01/andurils-market-inroads-clear-1b-counter-unmanned-system-tech-win/361017/); [GovConWire](https://govconwire.com/2022/01/anduril-wins-968m-socom-counter-uas-tech-integration-contract/) |
| 7 | 2022 | 澳大利亚 国防部/RAN | Ghost Shark XL-AUV 协作开发 | 协作合同（共同投资） | 澳政府累计投入约 A$140M（2022 起） | ~3年 | XL-AUV 原型研制 | 已转生产（见 #27） | ? | [Naval News](https://www.navalnews.com/naval-news/2025/09/anduril-ghost-shark-now-australian-1-7-bn-program-of-record/) |
| 8 | 2022–2024 | 美国太空军 | 太空监视网（SSN）升级系列合同 | 系列合同 | 累计 $33.5M | — | SSN 传感器/网络升级 | 已完成 | (Y) | [DefenseScoop](https://defensescoop.com/2024/11/21/anduril-space-surveillance-network-upgrade-contract-sdanet/) |
| 9 | 2023-05-31 | 日本 | 与 Sumitomo Aero-Systems、Itochu 等签 MOU | **MOU，非合同** | — | — | 拓展日本防卫省市场 | — | N | [Defence Connect](https://defenceconnect.com.au/industry/12069-anduril-partners-japanese-firms-to-enhance-defence-capability) |
| 10 | 2023-11-02 | 英国 MoD | TALOS 第三阶段 "Entrelazar"：固定设施部队防护/反入侵/C-UAS（常设联合作战基地） | 合同 | 初始 £17M，可增至 £24M（美元换算 $20–20.6M 不一） | 31个月 | Sentry 塔等基地防护 | 执行/可能已完成 | (Y) | [GOV.UK](https://www.gov.uk/government/news/17million-contract-awarded-for-force-protection-technology); [Shephard](https://www.shephardmedia.com/news/air-warfare/anduril-takes-20-million-uk-mod-contract-to-enhance-force-protection-and-counter-intrusion-capabilit/); [Army Technology](https://www.army-technology.com/news/anduril-begins-third-phase-of-uk-mods-integrated-force-protection-facilities/) |
| 11 | 2024-02-07 | 美国海军 PMS 394 + DIU | Dive-LD 大型 UUV 原型（与 Oceaneering、Kongsberg 共三家） | DIU CSO 原型 OT；后续合同允许部队借用/采购 | 未披露 | 未披露 | 竞速测试中用 Lattice 实时跟踪和共享 Dive-LD 位置；2025-04 首台交付 UUVRON-1 | 已交付 | **Y** | [Defense News](https://www.defensenews.com/unmanned/2024/02/08/pentagon-tech-hub-hires-anduril-to-get-large-underwater-drone-to-navy/); [GlobalSecurity](https://www.globalsecurity.org/military/systems/ship/lduuv-dive-ld.htm) |
| 12 | 2024-04-24 | 美国空军 | CCA Increment 1 —— 进入详细设计/制造/测试阶段（与 GA 胜出，淘汰洛马、诺格、波音） | 研发合同 | 未披露（FY25 项目申请 $557M，FY29 前计划约 $9B，为整个项目） | — | YFQ-44A Fury 生产代表性试验件 | 已完成，转生产（#36） | ? | [DefenseScoop](https://defensescoop.com/2024/04/24/anduril-general-atomics-air-force-cca-program/); [TWZ](https://www.twz.com/air/general-atomics-anduril-move-ahead-in-collaborative-combat-aircraft-drone-program) |
| 13 | 2024-06 | 美国海军 | SM-6 二级 21 英寸固体火箭发动机演示 | 研发合同 | $19M | — | 原 Adranos（2023 收购）SRM 能力 | 执行 | N | [WDAM](https://www.wdam.com/2024/06/13/anduril-awarded-19m-build-rocket-motors-us-navy/) |
| 14 | 2024-06-18 | 台湾（TECRO）FMS | ALTIUS 600M-V | **FMS（DSCA 批准，估值）** | 估值 $300M，最多 291 套 | — | 巡飞弹+PILS 发射器+地面控制站 | 2024 签约，2025-08 首批交付 | N | [DSCA](https://www.dsca.mil/press-media/major-arms-sales/taipei-economic-and-cultural-representative-office-united-states-34); [Defense Post](https://thedefensepost.com/2025/08/07/taiwan-altius-drones-anduril/) |
| 15 | 2024（约9–10月） | 美国陆军 | Company-Level sUAS Directed Requirement Tranche 1（Ghost-X，与 PDW C-100 共同入选） | DLA 合同载体 | $14.417M（Tranche 1，两家合计？来源表述为 "the award… value of $14.417M"） | — | Ghost-X 小型无人机 | 执行 | ? | [Inside Unmanned Systems](https://insideunmannedsystems.com/u-s-army-selects-anduril-and-pdw-for-company-level-suas-requirement/) |
| 16 | 2024-10-08 | 美国国防部（未具名客户，多军种） | Roadrunner-M 拦截器 + Pulsar 电子战 | 生产合同 | $249,978,466 | — | 500 发 Roadrunner 全备弹 + Pulsar | 执行 | ? | [Defense News](https://www.defensenews.com/unmanned/2024/10/08/anduril-lands-250-million-pentagon-contract-for-drone-defense-system/) |
| 17 | 2024-10/11 | 美国国防部 Replicator 1.2 | Ghost-X（由陆军 MRR 项目提名）；Altius-600 亦曾被选入 Replicator | 选定（非独立合同） | 未披露 | — | 小型无人机/巡飞弹 | 选定 | N | [DefenseScoop](https://defensescoop.com/2024/10/17/replicator-ghost-x-drones-anduril-army/); [Military Times](https://www.militarytimes.com/unmanned/2024/11/13/pentagon-announces-new-batch-of-drones-for-replicator-program/) |
| 18 | 2024-11 | 美国海军陆战队 | MADIS C-UAS Engagement System | 合同 | ≈$200M | — | MADIS 车载防空系统的 C-UAS 交战系统 | 执行 | (Y) | [Inside Unmanned Systems（引 Anduril 声明）](https://insideunmannedsystems.com/anduril-awarded-10-year-642m-program-of-record-to-deliver-cuas-systems-for-u-s-marine-corps/) |
| 19 | 2024-11-21 | 美国太空军 SSC（服务 USSPACECOM） | SSN 现代化 / SDANet | IDIQ，Program of Record | ≈$99.7M（任务书写 $99.6M） | 5年；要求 2026 年底完成部署 | 交付 Lattice 作为弹性网状网络，现代化太空监视网 | 执行 | **Y** | [DefenseScoop](https://defensescoop.com/2024/11/21/anduril-space-surveillance-network-upgrade-contract-sdanet/); [Breaking Defense](https://breakingdefense.com/2024/11/anduril-could-receive-up-to-100m-for-space-surveillance-network-upgrade/) |
| 20 | 2024-12-03 | 美国 CDAO | Edge Data Integration Services（Lattice Mesh / Edge Data Mesh，CJADC2） | 生产 OTA（源自 GIDE 原型 OT） | $100M；授予时拨付约 $33M（FY24/25 RDT&E） | 3年（至2028-11）；OrangeSlices 称4年 | Lattice 驱动的边缘数据网格，扩展至断连/分布式系统 | 执行 | **Y** | [DefenseScoop](https://defensescoop.com/2024/12/03/anduril-awarded-100m-deal-cdao-scale-edge-data-mesh-capabilities-ota/); [Inside Defense](https://insidedefense.com/node/222723) |
| 21 | 2025-02 / 04 | 美国陆军 | IVAS 生产合同从 Microsoft 转由 Anduril 管理（novation） | 既有生产合同接管 | 原合同"数十亿美元级"；本次检索未取得精确数字 | — | 头显项目监管；后续演变为 SBMC | 已接管 | (Y) | [Breaking Defense](https://breakingdefense.com/2025/10/i-have-got-this-s-figured-out-anduril-unveiling-eagleeye-mixed-reality-device-at-ausa/) |
| 22 | 2025-03（DoD 公告 3-07 或 3-14） | 美国海军陆战队 | Installation C-sUAS（I-CsUAS）Program of Record | 10年 IDIQ（10 家竞标） | **上限 $642.2M**；授予时约 $9.5M | 至 2035-03 | Lattice 驱动，集成多传感器和效应器，覆盖交付、安装、维护 | 执行 | **Y** | [Washington Technology](https://washingtontechnology.com/contracts/2025/03/anduril-wins-642m-marines-counter-drone-tech-contract/403613/); [EDR](https://www.edrmagazine.eu/anduril-wins-640-million-i-csuas-contract) |
| 23 | 2025-03 | 美国陆军 | 4.75 英寸固体火箭发动机（远程精确火箭炮） | 研发 | 未披露 | — | Anduril Rocket Motor Systems | 执行 | N | [Defense News](https://defensenews.com/digital-show-dailies/global-force-symposium/2025/03/21/to-amass-cheap-rockets-us-army-picks-anduril-to-develop-solid-motor) |
| 24 | 日期未核实（2025?） | 美国（DPA Title III） | 固体火箭发动机产能 | DPA 资助 | $43.7M | — | SRM 产能 | ? | N | [Tectonic Defense](https://www.tectonicdefense.com/anduril-scores-43-7m-in-dpa-funding-for-srms/) |
| 25 | 2025-03（年份按检索摘要推断） | 英国 MoD（援乌） | Altius 无人机交付乌克兰 | 合同 | £30M（≈$40M） | — | Altius 巡飞弹 | 执行 | N | [Privacy International（摘要）](https://privacyinternational.org/report/5704/dual-use-tech-anduril-example) |
| 26 | 2025-07-18 | 美国陆军 | NGC2 原型（第4步兵师），Team Anduril 含 Palantir、Microsoft、Striveworks、Govini 等 | OTA 原型 | $99.6M | 11个月 | 师级下一代指挥控制原型（Lattice 为基础） | 已完成并转扩展（#41） | (Y) | [DefenseScoop](https://defensescoop.com/?p=116201); [Defense Post](https://thedefensepost.com/2025/07/21/anduril-us-army-ngc2-prototype/amp/) |
| 27 | 2025-09-10（8-26 签署） | 澳大利亚 RAN | Ghost Shark XL-AUV 生产、维护、后续开发（Program of Record） | 生产合同 | **A$1.7B**（≈US$1.12B） | 5年 | 情报监视侦察与打击 XL-AUV，数量未披露 | 执行；首批 2026-01 服役 | ? | [Naval News](https://www.navalnews.com/naval-news/2025/09/anduril-ghost-shark-now-australian-1-7-bn-program-of-record/); [Defense News](https://defensenews.com/global/asia-pacific/2025/09/10/australia-orders-fleet-of-large-unmanned-submarines-from-anduril/) |
| 28 | 2025-09 | 美国陆军 | SBMC（原 IVAS Next）第一阶段原型硬件 —— EagleEye（与 Meta 合作）；Rivet 另获 $195M | 原型 | $159M | 交付约 7 个月后 | 头显硬件；SBMC-A 数据/AI 架构基于 Lattice | 执行；规模化交付预计 2027 | **Y**（SBMC-A） | [UploadVR](https://www.uploadvr.com/anduril-meta-rivet-sbmc-hundreds-ar-headsets/); [Breaking Defense](https://breakingdefense.com/2025/10/i-have-got-this-s-figured-out-anduril-unveiling-eagleeye-mixed-reality-device-at-ausa/) |
| 29 | 2025-11-10 | 美国陆军 | IBCS-M（机动）C-UAS 火控 | 协议（未披露金额、期限） | 未披露 | 未披露 | Lattice 作为下一代 C-UAS 火控/集成骨干；尤马试验 4/4 击落 | 执行 | **Y** | [Military Embedded Systems](https://militaryembedded.com/unmanned/counter-uas/us-armys-integrated-battle-command-system-to-use-andurils-lattice-software-for-counter-uas); [Janes](https://www.janes.com/defence-intelligence-insights/defence-news/c4isr/us-army-anduril-reach-deal-on-ibcs-maneuver-programme) |
| 30 | 2025-12（低可信博客称）/ 2026-06-12 公开 | 美国 CBP（Border Patrol 资金） | Extended Range Sentry Towers（XRST，200+ 座） | SBIR Phase III AST IDIQ 下任务 | $362,974,500 | 1年 | 80 英尺塔，>5 英里自主探测（有人辅助 7.5 英里），集成 Lattice 与既有 350+ 标准塔网络 | 执行 | **Y** | [Anduril](https://www.anduril.com/news/anduril-and-u-s-customs-and-border-protection-expand-partnership-with-200-additional-extended-range-sentry-towers); [ExecutiveBiz](https://www.executivebiz.com/articles/cbp-anduril-extended-range-sentry-towers-363m); [OrangeSlices](https://orangeslices.ai/anduril-scores-1-year-363m-sbir-phase-iii-autonomous-surveillance-towers-idiq-task-with-dhs-border-patrol/) |
| 31 | 2026-03-13/14 | 美国陆军 | 企业协议（Enterprise contract）——整合 120+ 既有采购行动 | 企业级 IDIQ 类合同载体 | **上限 $20B**（"无资金附带，只是合同载体"） | 10年（5年基期+5年订购期），至 2036-03 | Lattice 软件、集成硬件、数据、算力、支持服务；联邦机构可共用 | 执行 | **Y** | [Army.mil](https://www.army.mil/article/291074); [DefenseScoop](https://defensescoop.com/2026/03/14/anduril-20-billion-dollar-army-contract/); [Bloomberg](https://www.bloomberg.com/news/articles/2026-03-14/us-army-awards-anduril-contract-worth-as-much-as-20-billion) |
| 32 | 2026-03 | 美国陆军 JIATF-401 | 首个任务订单：通用 C-UAS C2 | 任务订单（企业协议下） | ≈$87M（任务书写 $87.7M，未核实小数） | — | Lattice 作为 C-UAS 指挥控制骨干 | 执行 | **Y** | [Defense One](https://www.defenseone.com/business/2026/03/anduril-secures-87m-contract-common-counter-unmanned-c2-program/412156); [DroneXL](https://dronexl.co/2026/03/22/army-anduril-20b-ai-counter-drone/) |
| 33 | 2026-04-24（协议签于 2025 末–2026 初） | 美国太空军 SSC（Golden Dome） | 天基拦截器（SBI）原型，12 家共 20 份 OTA；Anduril 牵头 Impulse、Inversion、K2、Sandia、Voyager | OTA 原型 | 总上限 $3.2B（12家合计）；Anduril 份额未披露 | 2028 前演示 | 助推段拦截卫星 | 原型 | ? | [Bloomberg](https://www.bloomberg.com/news/articles/2026-04-24/spacex-anduril-among-companies-to-win-space-interceptor-deals); [Fortune](https://www.fortune.com/2026/04/25/spacex-anduril-lockheed-raytheon-northrop-golden-dome-interceptor-contracts/); [Airforce Technology](https://www.airforce-technology.com/news/anduril-us-golden-dome/) |
| 34 | 2026-06-05（批准公告）；联邦公报 2026-07-22 | 科威特 FMS | C-UAS 一揽子（Roadrunner-M、Anvil-Kinetic、Sentry 塔多型、EW、战术作战中心、C2） | **FMS（DSCA 批准，估值）** | 估值 $1.98B | — | Anduril 为主承包商；含 C2 系统与软件开发 | 已批准；未见合同签署报道 | (Y) | [Breaking Defense](https://breakingdefense.com/2026/06/us-approves-2b-sale-of-anduril-counter-drone-systems-to-kuwait/); [Defense News](https://www.defensenews.com/industry/techwatch/2026/06/08/us-approves-kuwait-request-to-buy-nearly-2-billion-of-counter-drone-platforms/) |
| 35 | 2026-06（报道） | 日本 | 洽购日产 Oppama 工厂生产无人机 | **谈判，非合同** | — | — | — | 未决 | N | [Reuters via Internazionale](https://www.internazionale.it/ultime-notizie-reuters/2026/06/25/exclusive-u-s-defence-firm-anduril-in-talks-for-nissan-plant-to-build-drones-in-japan-sources-say) |
| 36 | 2026-06-17 | 美国空军 | CCA Increment 1 生产（FQ-44A "Fury"；GA FQ-42A 同时获选） | EMD + 生产（前三批次） | **未披露**；有二手文章称 Inc 1 共 150 架（两型合计，未核实） | — | 生产型 CCA，Arsenal-1（俄亥俄）制造 | 执行 | ? | [DefenseScoop](https://defensescoop.com/2026/06/17/air-force-picks-anduril-general-atomics-to-build-first-operational-cca-drones/) |
| 37 | 2026-07-07 | NATO NCIA | 增强型空中指挥控制（eAirC2）数据平台评估（与 Palantir、Athea 并列） | 竞争性采购的评估阶段合同（通过 Anduril UK） | 未披露 | 约9个月，之后择一长期实施 | 在 NATO 环境部署 Lattice | 评估中 | **Y** | [NCIA](https://www.ncia.nato.int/newsroom/news/nato-accelerates-transformation-of-air-command-and-control-with-key-contract-awards); [Defence Industry EU](https://defence-industry.eu/anduril-secures-first-nato-contract-as-ncia-selects-lattice-for-allied-air-command-and-control-data-platform-evaluation/) |
| 38 | 2026-08（报道 8-28） | 台湾 | Altius-700M ×1,554 + Altius-600ISR ×478 及发射设备 | 合同（是否 FMS 未确认） | ≈NT$26.9B（≈US$847M） | — | 巡飞弹/ISR 无人机 | 签约 | N | [Defense Post](https://thedefensepost.com/2026/08/28/taiwan-acquires-anduril-altius/) |
| 39 | 日期未核实（约2026） | 美国陆军 | Barracuda-500M 地面发射集装箱式巡航导弹 3,000 枚（2027 起每年 1,000 枚） | 生产 | **未披露**（单价 $150–300K 为分析师推测） | 3年 | 低成本远程打击 | 执行 | N | [Sandboxx](https://www.sandboxx.us/news/army-will-buy-3000-barracuda-500m-missiles-from-anduril-to-massively-boost-its-long-range-strike-capabilities/) |
| 40 | 2026-09 | 美国陆军 | TITAN 地面站生产（Palantir 主承 $127M） | 生产 | Anduril $65M（合计 $192M） | — | 情报地面站（Anduril 部分） | 执行 | ? | [Breaking Defense](https://breakingdefense.com/2026/09/army-awards-192m-to-palantir-and-anduril-to-produce-titan-system/) |
| 41 | 2026-10-06 | 美国陆军 | NGC2 扩展（首个为 I Corps） | 5年合同 | **上限 $1.8B**；基期 $162.8M | 5年 | 将 NGC2（Lattice 为基础）扩展到更多部队 | 执行 | (Y) | [DefenseScoop](https://defensescoop.com/2026/10/06/army-awards-anduril-1-8b-contract-expand-ngc2/) |
| 42 | 2026-10-06 | 美国海军 | 弗吉尼亚级潜艇部件/大型组件（Arsenal-2，巴尔的摩 Sparrows Point），交付 GD Electric Boat、HII NNS | 按产出付款合同 | **上限 $2.9B**；Anduril 自投 $3.7B（合计宣称 $6.6B） | 2029 招聘、2030 投产 | 鱼雷管等部件，后扩展至超级模块 | 新授予 | N | [CNBC](https://www.cnbc.com/2026/10/06/anduril-navy-submarine-shipyard-contract.html); [Janes](https://www.janes.com/defence-intelligence-insights/defence-news/industry/anduril-industries-awarded-usd29-billion-us-navy-contract-for-submarine-work) |

### Inferences
- 合同结构演进：2018–2021 以试点/小额试验为主 → 2022 起出现 IDIQ/OTA 大额上限合同 → 2026 年进入"企业协议 + 任务订单"模式（Army $20B），意味着后续陆军订单（如 JIATF-401）多以任务订单形式出现，单独公告可能减少。
- Lattice 是 Anduril 与政府签约的"粘合剂"：几乎所有 C2/C-UAS/传感器网络合同（SOCOM、USMC、CDAO、SSN、IBCS-M、JIATF-401、NATO、CBP XRST、Army 企业协议）明确以 Lattice 为核心；而硬件/弹药类（SRM、Altius、Barracuda、CCA、潜艇部件）来源中通常不提 Lattice。
- 2026 年 NGC2 $1.8B 扩展紧随 2025 年 $99.6M 原型之后，说明原型 OTA → 生产/扩展的快速转化路径。

### Gaps
- **CBP 2018 "$4.8M"** 与 **2020 "~$250M"**：未在官方记录中找到；2020 金额只有高管"数亿美元"说法与 Privacy International 的 $250M/5年，应查 USASpending（CBP PIID）。
- **"Copperhead"**（自主鱼雷/水下弹药）相关海军合同：本次未检索到任何合同记录。
- **空军/SOCOM Roadrunner**、**空军 Barracuda**（如 AFRL/Enterprise Test Vehicle 相关）专项合同：未找到具体金额来源。
- **SOCOM Bolt**、**海军 CCA / 陆战队 CCA（MUX TACAIR）**、**高超音速/海军**相关合同：未检索（工具调用预算所限）。
- **2025-02 IVAS 接管**的原合同上限（Microsoft 2021 年约 $21.9B 上限的说法）本次未经来源核实。
- **日本**：未发现防卫省正式合同，仅 MOU（2023）与工厂收购谈判（2026-06）。
- **Barracuda-500M 3,000 枚**合同日期、**Taiwan 2026 合同**是否 FMS、**Kuwait** 是否已签约，均未确认。
- DIU 其他 CSO 原型（Ghost、Anvil 等）及 USASpending 中大量小额合同未系统梳理。

## 问题二：Lattice 明确参与的合同子集

### Takeaway
明确提到 Lattice 的合同至少 12 项，覆盖 C-UAS（SOCOM、USMC、IBCS-M、JIATF-401、Kuwait 系统中的 C2）、联合数据网格（CDAO）、太空监视（SSN）、边境监视（CBP）、单兵（SBMC-A）、联盟 C2（NATO）以及陆军企业级（$20B）。

### Cited Findings
- SOCOM 2022：交付 Lattice 软件平台并集成 Sentry/Anvil/Pulsar/FoxHound — [Washington Technology](https://washingtontechnology.com/companies/2022/01/andurils-market-inroads-clear-1b-counter-unmanned-system-tech-win/361017/)
- UK TALOS 2021：系统运行在 Lattice 上 — [Anduril blog](https://blog.anduril.com/anduril-industries-to-provide-advanced-force-protection-technology-to-uk-ministry-of-defences-f34f32d71cc7)
- Dive-LD 2024：竞速测试中用 Lattice 实时共享位置 — [GlobalSecurity](https://www.globalsecurity.org/military/systems/ship/lduuv-dive-ld.htm)
- SSN 2024：交付 Lattice 作为弹性网状网络 — [DefenseScoop](https://defensescoop.com/2024/11/21/anduril-space-surveillance-network-upgrade-contract-sdanet/)
- CDAO 2024：Lattice 驱动 Edge Data Mesh — [DefenseScoop](https://defensescoop.com/2024/12/03/anduril-awarded-100m-deal-cdao-scale-edge-data-mesh-capabilities-ota/)
- USMC I-CsUAS 2025：核心软件为 Lattice — [Inside Unmanned Systems](https://insideunmannedsystems.com/anduril-awarded-10-year-642m-program-of-record-to-deliver-cuas-systems-for-u-s-marine-corps/)
- SBMC-A 构建于 Lattice C2 之上 — [Breaking Defense](https://breakingdefense.com/2025/10/i-have-got-this-s-figured-out-anduril-unveiling-eagleeye-mixed-reality-device-at-ausa/)
- IBCS-M 2025：Lattice 作为 C-UAS 火控平台 — [Military Embedded Systems](https://militaryembedded.com/unmanned/counter-uas/us-armys-integrated-battle-command-system-to-use-andurils-lattice-software-for-counter-uas)
- CBP XRST：与 Lattice 及既有 Sentry 网络集成 — [ExecutiveBiz](https://www.executivebiz.com/articles/cbp-anduril-extended-range-sentry-towers-363m)
- Army 企业协议 2026：涵盖 Lattice 软件、硬件、数据、算力 — [Army.mil](https://www.army.mil/article/291074)
- JIATF-401 首单：Lattice 作为 C-UAS C2 骨干 — [Defense One](https://www.defenseone.com/business/2026/03/anduril-secures-87m-contract-common-counter-unmanned-c2-program/412156)
- NATO eAirC2 2026：在 NATO 环境部署 Lattice — [Defence Industry EU](https://defence-industry.eu/anduril-secures-first-nato-contract-as-ncia-selects-lattice-for-allied-air-command-and-control-data-platform-evaluation/)

### Inferences
- Lattice 合同的明确金额上限合计（不含 $20B 企业协议）约 $2.2B（SOCOM 0.968 + USMC 0.642 + CDAO 0.1 + SSN 0.1 + CBP XRST 0.363 + JIATF 0.087 + UK ~0.03），若计入 Army 企业协议则达 ~$22B；若将 NGC2（$99.6M + $1.8B）视作 Lattice 系，则再加约 $1.9B。

### Gaps
- NGC2 两份合同的来源摘要未直接写 "Lattice"（虽普遍认为基于 Lattice），按标准标为 (Y)。

## 问题三：数字冲突与需注意事项

### Takeaway
主要冲突集中在：SSN 金额（$99.6M vs $99.7M）、JIATF-401（$87M vs $87.7M）、CBP XRST 授予日期、USMC $642M 公告日期、CDAO 期限、CCA 产量。

### Cited Findings
- SSN：检索称 ≈$99.7M，而任务书写 $99.6M — [Space Insider](https://spaceinsider.tech/2024/11/21/anduril-secures-99-7m-contract-to-modernize-u-s-space-surveillance-network)
- SOCOM 完成日期 2032 vs GovConWire 2023（后者应为错误） — [GovConWire](https://govconwire.com/2022/01/anduril-wins-968m-socom-counter-uas-tech-integration-contract/)
- USMC I-CsUAS 公告日期 3-07 vs 3-14；$642M vs $642.2M — [EDR](https://www.edrmagazine.eu/anduril-wins-640-million-i-csuas-contract); [Military Embedded Systems](https://militaryembedded.com/unmanned/counter-uas/counter-uas-systems-to-be-provided-to-us-marine-corps-by-anduril)
- CDAO 期限 3 年 vs 4 年 — [OrangeSlices](https://orangeslices.ai/?p=115927)
- CBP XRST：一说 2025-12 授予、2026-06-12 才公开（低可信来源） — [ZeroG Talent](https://zerogtalent.com/blog/anduril-s-363m-border-wall-tech-deal-is-fueling-a-hidden-hiring-surge-in-autonomous-sensing-and-rhode-island-is-ground-zero)
- IVAS 接管时间 2 月 vs 4 月 — [Breaking Defense](https://breakingdefense.com/2025/10/i-have-got-this-s-figured-out-anduril-unveiling-eagleeye-mixed-reality-device-at-ausa/)
- UK 2023 合同美元换算 $20M vs $20.6M；以英镑 £17M（可增至 £24M）为准 — [GOV.UK](https://www.gov.uk/government/news/17million-contract-awarded-for-force-protection-technology)
- Ghost Shark 签署 8-26，公告 9-10，Anduril 称 9-9 授予 — [Naval News](https://www.navalnews.com/naval-news/2025/09/anduril-ghost-shark-now-australian-1-7-bn-program-of-record/)
- CDAO "$100M Lattice Mesh"：一次检索未能匹配，另一次以 "Edge Data Integration Services/Edge Data Mesh" 名称确认 — [Inside Defense](https://insidedefense.com/node/222723)

### Inferences
- FMS 批准估值（台湾 $300M、科威特 $1.98B）不应与合同额直接相加；Army $20B 为载体上限，JIATF-401 $87M 属其中，不能重复计算。

### Gaps
- 未能访问 defense.gov 每日合同公告原文、USASpending 记录逐条核对 PIID 与拨付额。

## 问题四：年度汇总（供绘图，USD，近似）

### Takeaway
按公开上限/估值粗算：2017–2021 年各年 < $0.3B；2022 约 $1.0B；2024 约 $1.0B；2025 约 $2.0B；2026（至10月）约 $28B（其中 $20B 为 Army 企业协议上限）。

### Cited Findings
（各项金额来源见问题一主表对应行；以下为汇总计算）

| 年份 | 条目数（主表，含非合同选定/批准） | 已披露金额合计（近似，USD） | 构成 / 说明 |
|---|---|---|---|
| 2017 | 0 | — | 2017 向 DHS 推介，未见合同 |
| 2018 | 1 | 未知 | CBP AST 试点 |
| 2019 | 1 | 未知 | CBP 5 座测试塔 |
| 2020 | 1 | 未披露（~$250M 存疑） | CBP AST 列项 |
| 2021 | 2 | ≈$0.03B | UK TALOS £3.8M；Home Office £16M（日期存疑） |
| 2022 | 3 | ≈$1.07B | SOCOM $967.6M；Ghost Shark 协作 ~A$140M（≈US$0.09B）；SSN 系列（$33.5M，跨 2022–24） |
| 2023 | 2 | ≈$0.02–0.03B | UK TALOS 3 £17M（上限 £24M）；日本 MOU（非合同） |
| 2024 | 10 | ≈$0.98B（含台湾 FMS 估值 $0.3B） | Dive-LD（未披露）、CCA 选定（未披露）、SRM $19M、台湾 Altius $300M、Ghost-X $14.4M、Roadrunner $250M、Replicator（未披露）、MADIS ~$200M、SSN $99.7M、CDAO $100M |
| 2025 | 9 | ≈$2.1B | USMC $642M、陆军 SRM（未披露）、DPA $43.7M（日期存疑）、UK 援乌 £30M、IVAS 接管（未计）、NGC2 $99.6M、Ghost Shark ≈$1.12B、SBMC $159M、IBCS-M（未披露） |
| 2026（至10-10） | 12 | ≈$28.0B（不含 Golden Dome 份额与 CCA 生产额；JIATF $87M 计入 $20B 内不重复） | Army 企业 $20B、CBP XRST $363M、Golden Dome SBI（份额未披露）、科威特 FMS $1.98B、CCA 生产（未披露）、NATO（未披露）、台湾 $847M、Barracuda（未披露）、TITAN $65M、NGC2 $1.8B、海军潜艇 $2.9B |

### Inferences
- 若剔除 Army $20B 企业协议上限，2026 年仍约 $8B，为 2025 年的约 4 倍。
- "条目数"含 FMS 批准、Replicator 选定、MOU 等非合同事件；绘图时可只统计带"合同"标签的行。

### Gaps
- 未披露金额的项目（CCA 生产、Golden Dome SBI、Barracuda、IBCS-M、Dive-LD、NATO）可能数额巨大（CCA、Barracuda 尤甚），年度合计显著低估真实规模。
- 2018–2020 年度数据缺乏官方金额。
