# Anduril Lattice (Lattice OS)：起源与演进史（2017 – 2026年10月）

> 调研日期：2026-10-10。来源以行业媒体、官方公告和开发者文档为主。下文的 Wikipedia 引文来自搜索摘要，因为该页面无法直接抓取。第三方聚合/追踪站点（andurilnews.com、Tracxn、Sacra 等）只作为次要来源，并已在相应位置注明。

---

## Q1. Lattice 何时、为何被创建？最初解决什么问题？

### Takeaway
Lattice 与 Anduril 同在 2017 年诞生。它最初是一套 AI 传感器融合与自主监视软件，跑在太阳能 Sentry 塔上，用来给 CBP 做美墨边境的"虚拟墙"：自动识别目标，再向边境人员告警。经过 2018 年试点、2019 年圣迭戈测试，它在 2020 年成为 CBP 的正式采购项目（Program of Record）。

### Cited Findings
**公司创立**
- 2017 年：Anduril 由 Palmer Luckey（Oculus 创始人）与 Trae Stephens、Brian Schimpf、Matt Grimm、Joe Chen 共同创立，其中三人出自 Palantir。具体日期说法不一：一说 2017-04-20 注册成立，TechCrunch 则称公司于 2017 年 6 月"悄然成立"。较合理的解释是前者为注册日、后者为公开日，但没有找到证实。— [Wikipedia](https://en.wikipedia.org/wiki/Anduril_Industries)；[TechCrunch](https://techcrunch.com/?p=1654777)；[Built In](https://builtin.com/articles/who-is-palmer-luckey)
- 2017 年 8 月：18M 美元种子轮。据 andurilnews 追踪，Multiples.vc 把 Series A 记在 2018 年 6 月，估值 2.62 亿美元。— [andurilnews funding tracker](https://www.andurilnews.com/funding/)；[Multiples.vc](https://multiples.vc/private-comps/anduril)
- 与 Founders Fund / Thiel 的关系：Trae Stephens 是 Founders Fund 合伙人。Founders Fund 领投了 Series F（2024）和 Series G（2025），并在 Series G 中出资 10 亿美元。— [andurilnews](https://www.andurilnews.com/funding/)；[Sacra](https://sacra.com/c/anduril/)（Stephens 在 FF 的身份属常识，本轮搜索没有找到专门的一手来源）

**边境起源（Lattice 的第一个用例）**
- 2017 年 6 月：Anduril 高管联系 DHS 加州办公室，推销低成本的边境安全方案。CBP 圣迭戈办公室后来付费让 Anduril 测试新系统。— [Wikipedia](https://en.wikipedia.org/wiki/Anduril_Industries)
- 2018 年 6 月：Lattice 监视塔在一位德州牧场主的私人土地上做非正式测试，由 Anduril 技术员远程操作。— [Wikipedia](https://en.wikipedia.org/wiki/Anduril_Industries)
- 2018 年 6 月：首个 DHS 合同，金额 480 万美元，在圣迭戈和尤马部署 10 座塔。— [FedScoop](https://fedscoop.com/anduril-sentry-towers-cbp/)；[Shadowproof](https://shadowproof.com/2021/04/08/the-virtual-wall-documents-show-cbp-plans-for-surveillance-towers-at-us-mexico-border/)
- 2019 年：CBP 创新团队在圣迭戈区测试 5 座塔，结果成功。— [FedScoop](https://fedscoop.com/anduril-sentry-towers-cbp/)
- 2020 年：自主监视塔（AST）成为 CBP 正式采购项目，据报道还获得 8500 万美元，扩展到 El Paso 和 Rio Grande Valley。注意：采购项目针对的是塔的项目，不是单独的 Lattice 软件，各来源对 Lattice 本身是否被点名说法不一。— [AI Business](https://aibusiness.com/verticals/anduril-raises-200m-wins-contract-for-autonomous-surveillance-towers-along-us-mexico-border)；[GovConWire](https://www.govconwire.com/articles/anduril-uav-uuv-lattice-homeland-security)
- Lattice 在塔上的作用：用 AI 处理传感器数据，识别潜在威胁，再自动告警 CBP 人员。— [GovConWire](https://www.govconwire.com/articles/anduril-uav-uuv-lattice-homeland-security)
- 2024 年 9 月：部署第 300 座 AST。Anduril 自称覆盖约 30% 的南部陆地边境（公司说法）。— [ASDNews](https://www.asdnews.com/news/defense/2024/09/27/anduril-deploys-300th-autonomous-surveillance-tower-ast-advancing-capability-border-security)
- 2026 年 6 月：据报道获得 3.63 亿美元的 CBP 合同，部署 200 多座增程哨兵塔（XRST）。合同性质说法不一：一说是一年期 SBIR Phase III，一说是多年扩展。— [TheDefenseNews](https://www.thedefensenews.com/Anduril-Wins-363-Million-CBP-Contract-to-Deploy-Over-200-Extended-Range-AI-Surveillance-Towers/)；[State of Surveillance](https://stateofsurveillance.org/news/anduril-border-surveillance-monopoly-big-beautiful-bill-2026/)（倡导类媒体）

### Inferences
- Lattice 以"感知→融合→识别→告警"的边境监视场景起家。它从一开始就是硬件无关的融合层（塔只是载体），这正是它后来能横向扩展到反无人机、指挥控制（C2）和集群自主的基础。
- 先拿到 CBP 的采购项目地位，再进入 DoD，这是 Anduril "用低成本、自筹研发产品打开采购大门"策略的第一次验证。

### Gaps
- 没有找到 Lattice 命名时间、首个内部版本号或 2017 年原始设计文档等一手来源。
- 本轮没有检索到 2018 年 Wired 报道的原文。
- 本轮没有核实 GAO 关于 CBP 塔隐私问题的报告。

---

## Q2. Lattice 的主要版本与产品里程碑

### Takeaway
Lattice 先后经历了四个阶段：边境监视软件（2017–2020）、反无人机 C2 核心（2020–2022）、集群自主产品 Lattice for Mission Autonomy（2023-05），以及开放平台 Lattice SDK 与合作伙伴计划（2024-12）。2025–2026 年它又演进为 Lattice Mesh 数据层，成为陆军 NGC2、陆军 200 亿美元企业合同、空军 CCA 和 NATO 项目的核心。

### Cited Findings
**反无人机阶段**
- 2022-01-24：SOCOM 选定 Anduril 作为反无人机系统集成商。合同为 10 年期 IDIQ，金额"约 10 亿美元"（Monch 记为 9.68 亿美元），Anduril 击败了另外 11 家投标方。方案以 Lattice 为中心，配合 Sentry 塔和 Anvil 拦截无人机，并要求集成第三方传感器与效应器。— [Defense News](https://www.defensenews.com/unmanned/2022/01/24/us-special-operations-command-picks-anduril-to-lead-counter-drone-integration-work-in-1b-deal/)；[Monch](https://monch.com/anduril-industries-lands-socom-cuxs-contract/)；[The Defense Post](https://thedefensepost.com/2022/01/26/us-special-ops-counter-drone-contract/amp/)

**产品化：Lattice for Mission Autonomy**
- 2023-05-03：发布 Lattice for Mission Autonomy。它是硬件无关的端到端平台，支持在人类监督下管理"数百架"异构无人系统，理念是"一人操控多机"，取代"多人操控一机"。功能包括自主驾驶、威胁识别、多平台机动编排，以及电子特征与通信管理。— [Defense News](https://www.defensenews.com/industry/2023/05/03/anduril-unveils-software-to-manage-hordes-of-drones/)；[Anduril blog](https://blog.anduril.com/anduril-unveils-lattice-for-mission-autonomy-8e0c5fa0e94b)
- 2023 年：在陆军 EDGE23 演习中，一名士兵用该软件协调多家厂商的无人机，定位并摧毁了地空导弹阵地。— [Anduril blog](https://blog.anduril.com/anduril-demonstrates-lattice-for-mission-autonomy-controlling-teams-of-autonomous-assets-at-us-f617c489441)
- 2025 年 3 月：新加坡 DSTA 与 RSAF 同 Anduril 合作，这是 Lattice for Mission Autonomy 的首个国际合作。— [Asian Military Review](https://asianmilitaryreview.com/?p=18585)

**开放平台：Lattice SDK 与合作伙伴计划**
- 2024-12-10：Lattice SDK 公开发布，同时推出 Lattice Partner Program（首批合作伙伴超过 10 家）。SDK 用于在没有中心云的边缘、通信降级环境中构建去中心化应用，内容包括数据模型定义、API 绑定、示例和参考实现。— [Defense Daily](https://www.defensedaily.com/anduril-offers-software-development-kit-for-lattice-networking-platform-to-boost-interoperability/advanced-transformational-technology/)；[Anduril on X](https://x.com/anduriltech/status/1866525275644633517)；[OCBJ](https://www.ocbj.com/defense-2/anduril-industries-enabling-partners-to-operate-on-lattice/)（OCBJ 页面的日期戳与此不一致）
- 架构：SDK 用来构建"创建、使用和改进 Lattice Mesh 数据"的应用、数据服务和硬件集成，核心是 gRPC 的 Entity Manager / Task Manager API，以及 HTTP 的 Entities / Tasks API。Lattice Developer Program 提供运行 Lattice Mesh、带模拟数据的环境。— [docs.anduril.com](https://docs.anduril.com/guide/overview)
- 许可：有限、可撤销、免版税，只能用于为"兼容的 Lattice 实现"开发应用，禁止用来构建其他 SDK 或不兼容的实现。— [developer.anduril.com/license](https://developer.anduril.com/license)；[buf.build](https://buf.build/anduril/lattice-sdk/raw/main/-/LICENSE)
- SDK 覆盖多种语言：Python、JS、Java、Go、C++、Rust。2025-07-24，C++ 仓库归档，protobuf 改由 Buf Schema Registry 托管。— [GitHub anduril](https://github.com/anduril)；[lattice-sdk-cpp](https://github.com/anduril/lattice-sdk-cpp)
- 2026 年开发者更新（据开发者 changelog 的搜索摘要）：
  - 6-09：Developer Console
  - 7-23：Lattice Schema Registry
  - 8-03：面向编程智能体的官方 "Lattice SDK skills"
  - 9-09：Lattice Video API 进入 Preview
  - 9-17：Schema 自动同步到 Sandbox
  - 10-05：Rust（REST）SDK
  - 来源：[developer.anduril.com/changelog](https://developer.anduril.com/changelog)
  - 这些日期来自搜索摘要，未逐条打开核实。

**Lattice Mesh / Lattice for C2**
- Lattice Mesh 的定位是去中心化的网状数据分发能力，面向战术边缘、低带宽环境。据报道 DoD CDAO 采购了它，让前线单位不必经总部中转就能共享数据。Lattice for Command & Control 则被描述为 AI 战斗管理平台。— [Breaking Defense tag page](https://breakingdefense.com/tag/lattice/)；[Unmanned Airspace](https://www.unmannedairspace.info/counter-uas-systems-and-policies/us-army-awards-anduril-the-worlds-largest-ever-c-uas-contact-at-usd20-billion/)
- 2024 年 11 月：太空军太空监视网络（SSN）现代化合同使用基于 Lattice 的网状网络，预计 2026 年底全面部署。— [ExecutiveBiz](https://executivebiz.com/2024/11/anduril-contract-award-modernize-space-surveillance-network-ssc)
- 2024 年 12 月初：Palantir AIP 与 Anduril Lattice 宣布集成。— [TechCrunch](https://techcrunch.com/2024/12/22/palantir-and-anduril-reportedly-building-a-tech-consortium-to-bid-on-defense-contracts/)

**2025–2026 重大项目里程碑**
- 2025 年 4 月：NGC2 转为采购项目。2025 年 7 月，陆军授予 Anduril 一份 9960 万美元、为期 11 个月的 OTA，牵头为第 4 步兵师交付 NGC2 原型。"Team Anduril" 成员包括 Palantir、Striveworks、Govini、Instant Connect、Research Innovations 和 Microsoft。— [Army.mil](https://www.army.mil/article/287180/army_announces_next_generation_command_and_control_ngc2_prototype_award)；[The Defense Post](https://thedefensepost.com/2025/07/21/anduril-us-army-ngc2-prototype/)
- Ivy Sting 1 实弹演习：师级目标处理流程完全运行在 Lattice Mesh 和 Palantir Target Workbench 上。— [Defence Industry Europe](https://defence-industry.eu/anduril-and-u-s-army-showcase-next-gen-command-and-control-with-ngc2-in-live-fire-ivy-sting-1/)
- 2026-02-24：Lattice for Mission Autonomy 首次在 YFQ-44A（Fury）上飞行。2026 年 6 月，空军选择它用于 CCA 项目的下一阶段。— [Defence Industry Europe](https://defence-industry.eu/u-s-air-force-selects-anduril-lattice-mission-autonomy-software-for-next-collaborative-combat-aircraft-program-phase/)
- 2026-03-13/14：陆军授予 Anduril 一份 10 年期企业合同（5 年基础期 + 5 年选择期，预计 2036-03-12 完成），上限 200 亿美元，固定价格，把 120 多项采购行动并入一个以 Lattice 为中心的框架。首个任务单为 8770 万美元（另一来源记为 8700 万美元），用于 JIATF 401 反无人机任务部队的 Lattice 软件、集成与培训。200 亿美元是上限，不是承诺支出。— [DefenseScoop](https://defensescoop.com/2026/03/14/anduril-20-billion-dollar-army-contract/)；[Breaking Defense](https://breakingdefense.com/2026/03/army-awards-anduril-counter-drone-task-order-as-first-in-new-20b-contract-vehicle/)；[Inside Unmanned Systems](https://insideunmannedsystems.com/u-s-army-enterprise-contract-with-anduril-positions-lattice-as-core-platform-for-c-uas-operations/)
- 2026 年 5 月：Anduril 获得陆军原型 C2 导弹防御系统合同。— [Breaking Defense](https://breakingdefense.com/2026/05/anduril-wins-army-contract-for-prototype-c2-missile-defense-system/)
- 2026-06-22：陆军指定 Anduril 牵头 NGC2 通用数据层基线（common data layer baseline）。— [DefenseScoop](https://defensescoop.com/2026/06/22/army-taps-anduril-lead-ngc2-common-data-layer-baseline/)
- 2026-07-07：NATO NCIA 选择 Lattice 用于 eAirC2 数据平台计划，这是 Anduril 的首个 NATO 合同，从 9 个月评估期起步。据报道竞争对手包括 Palantir 等。— [Anduril](https://www.anduril.com/news/anduril-secures-first-nato-contract-lattice-for-eairc2-data-platform-initiative)；[BattlePolicy](https://www.battlepolicy.com/nato-picks-andurils-lattice-for-air-command-trial-against-palantir-and-athea/)
- 2026-10-05/06：陆军授予 Anduril NGC2 指挥网络推广合同，5 年上限 18 亿美元，基础期 1.628 亿美元，从 I Corps 开始。Lattice 作为分布式数据层，连接应用、数据、AI 模型、传感器和载具，并继续与 Palantir Foundry 组成"边缘到云"的数据网格。— [Anduril](https://www.anduril.com/news/anduril-continues-to-scale-next-generation-command-and-control-across-the-army)；[GovConWire](https://www.govconwire.com/articles/anduril-army-ngc2-contract-i-corps)；[ASDNews](https://www.asdnews.com/news/defense/2026/10/05/anduril-continues-scale-nextgen-command-control-across-army)
- 2026 年 6 月：Defense One 报道，陆军目标是在年底前用 NGC2 同步两个师。— [Defense One](https://www.defenseone.com/defense-systems/2026/06/army-aims-sync-two-divisions-using-next-gen-c2-years-end/414367/)
- 2025 年 10 月（AUSA）：Anduril 发布 EagleEye 混合现实设备，归在 Breaking Defense 的 Lattice 标签下。— [Breaking Defense](https://breakingdefense.com/tag/lattice/)

### Inferences
- 产品线可以概括为四个阶段：
  1. 单场景软件（边境监视）
  2. 系统集成内核（反无人机）
  3. 命名产品族（Mission Autonomy、C2、Mesh）
  4. 平台/生态（SDK、Schema Registry、合作伙伴计划、面向 AI 编程智能体的 skills）
- 2026 年后，Lattice 的身份从"Anduril 自家硬件的操作系统"转向"军种级通用数据层"（NGC2、200 亿美元企业合同、NATO），开始与 Palantir 既合作又竞争。

### Gaps
- 没有找到 Lattice Mesh 和 Lattice for Command & Control 的正式发布日期，也没有官方版本号体系。
- 没有找到 "Lattice OS" 是否发生过正式更名或重新品牌化的一手证据。
- 本轮没有核实 2024 年 4 月 CCA Increment 1 选定 Anduril 与 GA 的确切日期（只有 Janes/Wikipedia 摘要提到 Fury 是两家胜出方之一）。

---

## Q3. 哪些收购与合作扩展了 Lattice？

### Takeaway
Anduril 通过收购补齐了 Lattice 可以编排的"末端节点"：空射效应器（Area-I）、水下（Dive）、大型自主飞机/CCA（Blue Force）、雷达与 C2 软件（Numerica）、边缘计算与战术通信（Klas）。合作方面，它与 Palantir 组成软件联盟（AIP×Lattice 集成，2024-12），并联合牵头 NGC2。

### Cited Findings
- Area-I：多数来源记为 2021 年 4 月宣布收购（空射效应器 ALE，保留品牌，作为全资子公司）；Anduril newsroom 的一处列表记为 2022 年 10 月，存在冲突。— [Contrary Research](https://research.contrary.com/company/anduril)；[andurilnews acquisitions](https://www.andurilnews.com/topics/acquisitions/)
- Dive Technologies：2022 年 2 月（另有列表记为 2023 年 3 月，存在冲突），后改组为 Anduril Maritime。它是 Ghost Shark / Dive-LD 等 AUV 的基础。— [Contrary Research](https://research.contrary.com/company/anduril)；[Not Boring](https://www.notboring.co/p/anduril-acquiring-prime)
- Adranos：2023 年 6 月，固体火箭发动机。— [Built In](https://builtin.com/articles/what-is-anduril)
- Blue Force Technologies：2023-09-07，Fury Group-5 自主飞机，后来发展为 YFQ-44A，成为 CCA Increment 1 两家胜出方之一（另一家是 GA 的 YFQ-42）。— [Janes](https://www.janes.com/defence-intelligence-insights/defence-news/air/anduril-acquires-blue-force-technologies-entering-large-uav-market)；[Wikipedia YFQ-44](https://en.wikipedia.org/wiki/Anduril_YFQ-44)
- Numerica 的雷达与 C2 业务：2025 年 1 月宣布，包括 Spyglass、Spark 雷达和 Mimir C2 软件。— [Built In](https://builtin.com/articles/what-is-anduril)；[Contrary Research](https://research.contrary.com/company/anduril)
- Klas：2025-05-05 签署最终协议，把 Voyager 坚固边缘计算与战术通信硬件集成进 Anduril 自主系统和 Lattice。— [PrivSource](https://www.privsource.com/acquisitions/deal/anduril-industries-acquires-klas-7YSEr6)；[Builtin](https://builtin.com/articles/what-is-anduril)
- Palantir 联盟：2024 年 12 月初宣布 AIP 与 Lattice 集成，并"启动新联盟"。2024-12-22，FT/Reuters 报道两家正与约十几家公司商谈联合投标，可能的成员包括 SpaceX、OpenAI、Saronic、Scale AI（成员名单来自匿名消息源）。— [TechCrunch](https://techcrunch.com/2024/12/22/palantir-and-anduril-reportedly-building-a-tech-consortium-to-bid-on-defense-contracts/)；[MarketScreener/FT](https://www.marketscreener.com/quote/stock/PALANTIR-TECHNOLOGIES-INC-113108869/news/Palantir-Anduril-join-forces-with-tech-groups-to-bid-for-Pentagon-contracts-FT-reports-48641749/)
- Team Anduril（NGC2，2025-07）：成员见 Q2。— [Army.mil](https://www.army.mil/article/287180/army_announces_next_generation_command_and_control_ngc2_prototype_award)
- Golden Dome：据一些概况类来源，Anduril 是 Golden Dome C2 软件联盟九家成员之一，另一来源称 Anduril 与 Palantir 于 2025 年 1 月加入该 C2 联盟；Anduril 还牵头一个天基拦截器原型团队，该团队 8 月通过首次设计评审。这些说法都来自次要来源。— [Venture Atlas](https://www.ventureatlas.org/company/anduril)；[FedSavvy](https://www.fedsavvystrategies.com/the-neo-prime-ascendancy-analyzing-andurils-continued-expansion/)；[Flying Mag](https://www.flyingmag.com/space-force-awards-golden-dome-contracts/)
- 国际：
  - 澳大利亚，2025-09-10：与 Anduril Australia 签订 5 年合同，金额 17 亿澳元（约 11 亿美元），用于 Ghost Shark 超大型 AUV 的生产、维护和持续开发（2022 年起已有约 1.4 亿澳元开发投入）。— [Australian Defence Minister](https://www.minister.defence.gov.au/media-releases/2025-09-10/equipping-royal-australian-navy-next-generation-autonomous-undersea-vehicles)；[Breaking Defense](https://breakingdefense.com/2025/09/australia-signs-contract-with-anduril-for-ghost-shark-autonomous-underwater-vehicle/)
  - Ghost Shark 运行 Lattice for Mission Autonomy：这一说法来自次要来源。— [Engineer's Perspective](https://engineersperspective.substack.com/p/ghost-shark)
  - 英国：有说法称 MoD 的 TALOS 基地防护项目集成了 Sentry、Ghost 和 Lattice，但只有次要来源，未经核实。— [Medium deep dive](https://medium.com/buvcg-research/anduril-industries-deep-dive-6949c7dd41c7)
  - 台湾：有说法称双方共同生产 Dive-LD / Dive-XL，只有 Substack 来源，未经核实。另据 UDN 报道，创始人曾于 2025 年 8 月赴台交付无人机。— [Substack](https://iwantmydemocracysausage.substack.com/p/australia-and-anduril-autonomous-e31)；[UDN](https://udn.com/news/story/6809/9168353)

### Inferences
- 收购逻辑是"Lattice 为中枢，硬件为末梢"：每一次收购都为 Lattice 增加一类可感知或可打击的节点，从而强化它的平台锁定效应。

### Gaps
- Numerica 与 Klas 交易的完成日期没有核实。
- 日本相关合同本轮没有找到。
- 英国和台湾的合同细节缺乏官方来源。
- Golden Dome 中 Lattice 的具体角色和金额没有一手来源。

---

## Q4. Anduril 增长轨迹（估值、营收、人员）

### Takeaway
估值从 2019 年的约 10 亿美元，涨到 2026 年 5 月的 610 亿美元，2026 年 7 月据报道正以约 1000 亿美元估值洽谈融资。营收从 2024 年的约 10 亿美元翻倍到 2025 年的 22 亿美元，2026 年目标约 43 亿美元（均为公司口径）。

### Cited Findings

| 日期 | 轮次 | 金额 | 估值 | 领投 / 来源 |
|---|---|---|---|---|
| 2017-08 | 种子轮 | 18M | — | [andurilnews](https://www.andurilnews.com/funding/) |
| 2018-06 | Series A | — | 2.62 亿美元 | [Multiples.vc](https://multiples.vc/private-comps/anduril)（日期与种子轮存在 2017/2018 混淆） |
| 2019-09 | Series B | 未披露 | 10 亿美元 | a16z |
| 2020-07 | Series C | 2 亿美元 | 19 亿美元 | a16z。同期获得 CBP 塔合同。[AI Business](https://aibusiness.com/verticals/anduril-raises-200m-wins-contract-for-autonomous-surveillance-towers-along-us-mexico-border) |
| 2021-06 | Series D | 4.5 亿美元 | 46 亿美元（Sacra 记为约 47 亿） | Elad Gil |
| 2022-12 | Series E | 14.8 亿美元 | 84.8 亿美元（投后） | Valor |
| 2024-08 | Series F | 15 亿美元 | 140 亿美元 | Founders Fund、Sands Capital |
| 2025-06 | Series G | 25 亿美元 | 305 亿美元 | Founders Fund（出资 10 亿美元） |
| 2026-05-13 | Series H | 50 亿美元 | 610 亿美元 | Thrive Capital、a16z。[TechCrunch](https://techcrunch.com/2026/05/13/anduril-raises-5b-doubles-valuation-to-61b/)；[CNBC](https://www.cnbc.com/2026/05/13/anduril-valuation-defense-tech-funding-boom.html) |
| 2026-07-24 | 洽谈中 | — | 约 1000 亿美元 | Reuters 报道，未见交割确认。[Defense News](https://www.defensenews.com/industry/techwatch/2026/07/24/anduril-in-talks-to-raise-funding-at-about-100-billion-valuation/)；[TechCrunch](https://techcrunch.com/2026/07/24/anduril-reportedly-in-talks-to-raise-funding-at-100b-valuation-more-than-3x-last-years-mark/) |

- Series B 至 Series G 各行数据来自 [andurilnews](https://www.andurilnews.com/funding/) 和 [Sacra](https://sacra.com/c/anduril/)。
- 估值冲突：Tracxn 列出 2026 年 9 月估值 1110 亿美元，与其他来源不符，视为离群值。— [Tracxn](https://tracxn.com/d/companies/anduril/__qqOI0HKR47lFXorj9FAQlDfmJOqfOpDNWiW3JcO--ss/funding-and-investors)
- 累计融资额说法不一：62.6 亿、69 亿、111.3 亿、113 亿美元都有。— [Acquinox](https://acquinox.capital/insights/space-and-defense-tech/anduril-industries-investor-insights-rewriting-the-defence-industrial-base-at-a-30-5-billion-valuation)；[FNEX](https://fnex.com/anduril-stock/)；[Tracxn](https://tracxn.com/d/companies/anduril/__qqOI0HKR47lFXorj9FAQlDfmJOqfOpDNWiW3JcO--ss/funding-and-investors)
- 营收：2024 年约 10 亿美元，2025 年 22 亿美元（+120%），2026 年目标约 43 亿美元。均为公司口径，未经审计。— [Sacra](https://sacra.com/c/anduril/)；[CNBC](https://www.cnbc.com/2026/05/13/anduril-valuation-defense-tech-funding-boom.html)
- Arsenal-1：
  - 2025-01-16 宣布在俄亥俄州 Pickaway County 建设，占地 500 英亩，建筑面积 500 万平方英尺，承诺到 2035 年创造约 4000 个岗位，获 JobsOhio 3.1 亿美元和州税收抵免 4.522 亿美元。— [Defense News](https://www.defensenews.com/industry/2025/01/16/anduril-to-build-arsenal-1-autonomous-weapons-plant-in-central-ohio/)；[Ohio Governor](https://governor.ohio.gov/media/news-and-media/ohio-partners-with-anduril-to-rebuild-the-arsenal-for-essential-national-security-needs)
  - 2026 年 3 月：Fury 开始生产。计划到 2026 年底生产 Fury、Roadrunner、Barracuda 及一种保密平台。— [Breaking Defense](https://breakingdefense.com/2026/03/as-fury-production-starts-anduril-pledging-a-different-production-approach-at-arsenal-1/)
  - 有追踪站点称 2026-07-30 首架 YFQ-44A 在此下线，未经核实。— [andurilnews manufacturing](https://www.andurilnews.com/manufacturing/)
  - 另有报道提到 37 亿美元的 Arsenal-2 船厂，来源质量较低。— [STL.News](https://www.stl.news/inside-andurils-3-7b-arsenal-2-shipyard/)
- IPO：截至 2026 年 10 月，尚未宣布 IPO 日期。— [Yahoo/Reuters](https://finance.yahoo.com/news/anduril-set-double-valuation-4-192755828.html)；[TechCrunch](https://techcrunch.com/2026/05/13/anduril-raises-5b-doubles-valuation-to-61b/)

### Inferences
- 估值跃升与 Lattice 地位的上升节奏一致：2022 年 SOCOM 合同后进入 E 轮；2025–2026 年 NGC2、200 亿美元企业合同和 CCA 相继落地，估值随之翻倍。这说明市场把 Anduril 当作"软件平台型 Prime"来定价，而不只是硬件公司。

### Gaps
- 员工人数（headcount）在本轮没有找到可靠的、按年份分列的数据。
- 1000 亿美元那一轮是否已经交割，没有找到确认。

---

## Q5. 截至 2026 年 10 月的最新状态

### Takeaway
截至 2026 年 10 月，Lattice 已成为美陆军反无人机（200 亿美元企业合同和 JIATF 401）和 NGC2（I Corps 推广，上限 18 亿美元）的核心数据层，进入了空军 CCA 下一阶段（Mission Autonomy），并赢得首个 NATO 合同（eAirC2）。开发者平台仍在快速迭代（Schema Registry、Video API、Rust SDK、AI 智能体 skills）。公司估值 610 亿美元，据报道正以约 1000 亿美元估值洽谈新一轮，尚未 IPO。

### Cited Findings
- 2026-10-05/06：NGC2 I Corps 合同（上限 18 亿美元，基础期 1.628 亿美元），继续与 Palantir Foundry 合作。— [GovConWire](https://www.govconwire.com/articles/anduril-army-ngc2-contract-i-corps)；[Anduril](https://www.anduril.com/news/anduril-continues-to-scale-next-generation-command-and-control-across-the-army)
- 2026-10-05：Lattice SDK for Rust（REST）发布。— [developer changelog](https://developer.anduril.com/changelog)
- 2026-07-07：NATO eAirC2 合同。— [Anduril](https://www.anduril.com/news/anduril-secures-first-nato-contract-lattice-for-eairc2-data-platform-initiative)
- 2026 年 6 月：XRST 边境塔合同（3.63 亿美元），说明边境监视这条起源业务线仍在扩张。— [TheDefenseNews](https://www.thedefensenews.com/Anduril-Wins-363-Million-CBP-Contract-to-Deploy-Over-200-Extended-Range-AI-Surveillance-Towers/)
- 2026 年 6 月：空军在 CCA 下一阶段选定 Lattice for Mission Autonomy。— [Defence Industry Europe](https://defence-industry.eu/u-s-air-force-selects-anduril-lattice-mission-autonomy-software-for-next-collaborative-combat-aircraft-program-phase/)

### Inferences
- Lattice 的竞争格局正从"对抗传统 Prime"转为"与 Palantir 分层合作、在部分招标中直接竞争"。NATO eAirC2 招标就有报道称它与 Palantir 同场竞争。

### Gaps
- 2026 年是否发生 "Lattice OS" 更名，或推出新的命名产品，没有找到证据。
- Golden Dome 中 Lattice 的正式授标，没有找到一手来源。
- 日本合同没有找到。
