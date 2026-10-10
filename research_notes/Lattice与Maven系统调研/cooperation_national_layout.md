# Anduril–Palantir 合作与布局：Lattice / Maven Smart System 在美国国家级无人/自主/AI作战战略中的位置（2023 – 2026年10月）

> 调研说明（2026-10-10）：本笔记基于 WebSearch 结果摘要整理。尝试用 WebFetch 抓取 DefenseScoop 原文时失败（DNS 解析错误 `getaddrinfo ENOTFOUND defensescoop.com`），所以多数事实来自搜索结果摘要，没有逐字核对原文。标记规则：
> - 【确认】= 官方或一手来源（政府网站、公司新闻稿），或多家主流媒体口径一致
> - 【报道】= 依据匿名消息源或单一媒体
> - 【弱源】= 博客、聚合站或投资分析类站点，仅作线索

---

## 问题1：Anduril–Palantir 伙伴关系本身——2024年12月公告、财团传闻、后续正式协议、联合投标与分工、摩擦与竞争

### Takeaway
双方从 2024-12-06 的"数据+软件"合作公告起步，逐步把合作落到三个国家级项目上：陆军 NGC2、Golden Dome 指挥控制"胶水层"、陆军 NGC2 通用数据层基线。分工基本稳定：Anduril/Lattice 负责战术边缘的传感器-效应器网格、自主和武器控制；Palantir 负责企业级数据（Foundry/AIP）、AI 与决策/目标工作流（Maven Smart System, MSS）。但在 NATO 增强型空中指挥控制（eAirC2）项目上，两家是正面竞争对手；陆军 CTO 的安全备忘录也给联合方案带来过公开的负面压力。

### Cited Findings
**A. 2024-12-06 合作公告【确认，一手新闻稿】**
- 2024-12-06，Anduril 与 Palantir 联合宣布合作，目标是解决国防 AI 的两大瓶颈："数据就绪"（data readiness）和规模化处理。具体做法是用 Anduril 的 Lattice 和 Menace（可部署的边缘计算/通信系统）"instrument the tactical edge"，为政府提供安全、大规模的数据留存和分发；Palantir AIP 负责数据侧，双方计划建立一个云端数据管理能力，在各密级上提供 AI 训练用数据（AI-ready data）。— [Anduril 新闻稿](https://www.anduril.com/news/anduril-and-palantir-to-accelerate-ai-capabilities-for-national-security)；[BusinessWire 原稿](https://www.businesswire.com/news/home/20241206684306/en/Anduril-and-Palantir-to-Accelerate-AI-Capabilities-for-National-Security)
- 软件侧：把 Palantir 的 Maven Smart System 与 Lattice 结合，提供"从边缘到企业"（edge to enterprise）的无缝作战能力。公告称该平台已在两家公司内部和政府合同中使用，并预计以后引入更多行业伙伴。— [Anduril 新闻稿](https://www.anduril.com/news/anduril-and-palantir-to-accelerate-ai-capabilities-for-national-security)；[Defense News 2024-12-06](https://www.defensenews.com/pentagon/2024/12/06/defense-tech-firms-establish-ai-focused-consortium/)
- 后续报道把它表述为"打通 Lattice Mesh 与 MSS 和 AIP 的财团"，并给出角色定义：MSS 是"企业级任务指挥平台"（enterprise mission command platform），Lattice 是"直接集成机器人系统的边缘任务自主平台"（edge-based mission autonomy platform）。— [Inside Defense](https://insidedefense.com/share/222750)；[MIT Technology Review 2024-12-10](https://www.technologyreview.com/2024/12/10/1108354/we-saw-a-demo-of-the-new-ai-system-powering-andurils-vision-for-war/)
- 注意：部分二手稿件称"AIP 负责标注数据供 AI 训练""无人机视频识别目标"，这些细节不在原始新闻稿中。— [ExecutiveBiz](https://www.executivebiz.com/articles/anduril-palantir-artificial-intelligence-consortium)（据搜索摘要对比）

**B. 2024年12月财团传闻【报道，FT 匿名消息源】**
- 2024-12-22，FT 报道（Reuters 转述）：Palantir 与 Anduril 正与约十几家科技公司商谈组建联合投标财团，候选成员包括 SpaceX、OpenAI、Saronic、Scale AI，最早可能在 2025 年 1 月宣布协议；目标是挑战 Lockheed Martin、Raytheon、Boeing 等传统主承包商。公司当时未置评。— [TechCrunch 2024-12-22](https://techcrunch.com/2024/12/22/palantir-and-anduril-reportedly-building-a-tech-consortium-to-bid-on-defense-contracts/)；[MarketScreener/Reuters](https://www.marketscreener.com/quote/stock/PALANTIR-TECHNOLOGIES-INC-113108869/news/Palantir-Anduril-join-forces-with-tech-groups-to-bid-for-Pentagon-contracts-FT-reports-48641749/)；[Fortune 2024-12-23](https://dc.fortune.com/2024/12/23/palantir-anduril-spacex-openai-could-partner-to-bid-for-u-s-defense-contracts)
- 同期背景：Anduril 与 OpenAI 已于 2024 年 12 月宣布反无人机合作。— [Maginative](https://www.maginative.com/article/palantir-and-anduril-lead-silicon-valley-consortium-to-bid-for-pentagon-contracts/)

**C. 陆军 Next Generation Command & Control（NGC2）——最主要的联合落地项目【确认】**
- 2025年7月：陆军代表 PEO C3N 授予 Anduril 9,960 万美元 OTA，为第4步兵师建造师级 NGC2 原型，周期 11 个月。"Team Anduril" 成员有 Palantir、Striveworks、Govini、Instant Connect Enterprise、Research Innovations Inc.、Microsoft；NGC2 是"传输、基础设施、数据、应用"四层技术栈。— [Anduril 新闻稿](https://www.anduril.com/news/anduril-awarded-usd99-6m-for-u-s-army-next-generation-command-and-control-prototype)；[Breaking Defense 2025-07](https://breakingdefense.com/2025/07/army-awards-team-anduril-nearly-100m-to-lead-ngc2-prototype-for-4th-infantry-division/)
- 2026-02：Rune Technologies 加入 Team Anduril。— [BusinessWire 2026-02-11](https://www.businesswire.com/news/home/20260211819036/en)
- 2026年6月（约 06-22）：陆军选定 Anduril 牵头 NGC2"通用数据层基线"（common data layer baseline）。分工明确：Anduril 与 Palantir 一起，用 Anduril Lattice + Palantir Foundry 提供"边缘到云"的数据网格（edge-to-cloud data mesh）和配套软件部署工具；Raft 负责数据/服务注册、数据转换和联邦。合同在 Anduril 的 200 亿美元企业协议下授予，未公布金额。Lockheed Martin 此前为第25步兵师（夏威夷）的 NGC2 牵头方（"C2 Fix"网络基线），仍负责 25th ID 的全栈实施。— [DefenseScoop 2026-06-22](https://defensescoop.com/2026/06/22/army-taps-anduril-lead-ngc2-common-data-layer-baseline/)；[Breaking Defense 2026-06](https://breakingdefense.com/2026/06/army-picks-anduril-to-lead-next-gen-c2-common-data-layer-baseline/)；[ExecutiveGov](https://www.executivegov.com/articles/data-baseline-us-army-ngc2-palantir-anduril)
- 2026-10（DefenseScoop 2026-10-06）：陆军授予 Anduril 最高 18 亿美元、5 年期合同，把 NGC2 从师级原型推向第1军（I Corps）作战部署；基期 1.628 亿美元。— [DefenseScoop 2026-10-06](https://defensescoop.com/2026/10/06/army-awards-anduril-1-8b-contract-expand-ngc2/)；[GovConWire](https://www.govconwire.com/articles/anduril-army-ngc2-contract-i-corps)；[Anduril 新闻稿](https://www.anduril.com/news/anduril-continues-to-scale-next-generation-command-and-control-across-the-army)
- 公司声称：到 2026 年 5 月，第4步兵师全师运行在 NGC2 上，终端设备超过 2,500 台；炮兵火力时间线比旧系统缩短 90%（公司自述，未独立核实）。— [Defence Blog](https://defence-blog.com/u-s-army-moves-anduril-battle-network-from-test-to-field/)

**D. 摩擦与风险：陆军 CTO 安全备忘录【确认，Reuters 获得的文件】**
- 2025-09-05，陆军 CTO Gabriele Chiulli 签发备忘录，称 NGC2 原型应视为"very high risk"，理由是"对手获得持久且不可察觉访问的可能性"；问题包括任何授权用户可不受限制地访问全部应用和数据、第三方应用未经审查（其中一个有 25 个高危漏洞）。Reuters（Mike Stone）于 2025-10-03 前后报道，此事最先由 Breaking Defense 披露。— [Reuters via WHBL](https://whbl.com/2025/10/03/anduril-and-palantir-battlefield-communication-system-has-deep-flaws-army-memo-says/)；[Sherwood](https://sherwood.news/markets/an-internal-army-memo-reportedly-says-anduril-and-palantirs-battlefield/)
- 各方回应：Anduril 称报告是"过时快照"，问题已在正常开发流程中解决；Palantir 称其平台未发现漏洞；陆军 CIO Leonel Garciga 称这是"分诊网络安全漏洞"流程的一部分。Palantir 股价当日下跌约 5%–7%（不同来源数字不同）。— [AOL/Reuters](https://www.aol.com/articles/anduril-palantir-battlefield-communication-system-192105341.html)；[TradingView/GuruFocus](https://pl.tradingview.com/news/gurufocus:cbd24d9be094b:0-palantir-falls-on-army-memo-flagging-security-risks-in-battlefield-system)

**E. Golden Dome 指挥控制软件【报道，Reuters/WSJ 匿名消息源】**
- 2026-03-24，Reuters 援引知情人士：Anduril 与 Palantir 正合作开发 Golden Dome 导弹防御软件，把雷达、卫星、传感器和拦截弹连接起来；Aalyria、Scale AI、Swoop Technologies 也参与。Lockheed Martin、RTX、Northrop Grumman 此前已作为主承包商加入。公司未回应置评请求。— [AOL/Reuters 2026-03-24](https://www.aol.com/articles/anduril-palantir-developing-golden-dome-233842760.html)；[GovConWire](https://www.govconwire.com/articles/anduril-palantir-golden-dome-software-wash100)
- Golden Dome 主任、太空军上将 Michael Guetlein 把这一软件称为"glue layer"（据 WSJ 系报道），并说"command-and-control was going to be our secret sauce"。报道称财团目标是 2026 年夏季让平台进入测试。成本从 1,750 亿美元上调到 1,850 亿美元，用于"额外的太空能力"。— [CXO Digitalpulse](https://www.cxodigitalpulse.com/anduril-and-palantir-working-on-software-backbone-for-golden-dome-missile-defense-system/)；[Motley Fool 2026-03-25](https://www.fool.com/investing/2026/03/25/palantir-named-as-part-of-trump-administrations-18/)
- 两家在 Golden Dome 内部的具体分工没有公开确认。

**F. NATO 增强型空中指挥控制（eAirC2）——两家是竞争者【确认，NCIA 官方】**
- 2026-07-07，NATO NCIA 在 eAirC2 项目下授予三份竞争性评估合同，对象是 Anduril（Lattice）、Palantir 和法国 Athea SAS。三家在 NATO 环境中跑软件、做任务场景测试，约 9 个月后 NATO 选出一家长期使用。预征集公告显示每份首阶段开发合同 300 万欧元。这是 Anduril 的首个 NATO 合同。— [NCIA 新闻](https://www.ncia.nato.int/newsroom/news/nato-accelerates-transformation-of-air-command-and-control-with-key-contract-awards)；[Defence Blog](https://defence-blog.com/nato-picks-three-tech-firms-to-modernize-its-air-defense-data/)；[Defence Finance Monitor](https://www.defencefinancemonitor.com/p/the-air-command-data-layer)；[Battle Policy](https://www.battlepolicy.com/nato-picks-andurils-lattice-for-air-command-trial-against-palantir-and-athea/)

**G. 分头签下的"企业协议"（同一合同模板）【确认】**
- 2025年8月：陆军与 Palantir 签订企业协议，上限 100 亿美元，把 75 份合同（15 份主合同 + 60 份相关合同）合并为一份。— [HSToday](https://www.hstoday.us/industry/industry-news/u-s-army-awards-palantir-potential-10-billion-contract/)
- 2026年3月（03-13/14 前后）：陆军与 Anduril 签订企业协议，上限 200 亿美元、最长 10 年，把 120 份合同合并，以 Lattice 为核心。两份协议结构相同：5 年基期 + 5 年选项期。首份任务订单是 JIATF-401 的 8,700 万美元订单，以 Lattice 作为反无人机通用 C2 平台。— [DefenseScoop 2026-03-14](https://defensescoop.com/2026/03/14/anduril-20-billion-dollar-army-contract/)；[Washington Technology](https://www.washingtontechnology.com/contracts/2026/03/army-anduril-enter-new-20b-enterprise-agreement/412143/)；[Unmanned Airspace](https://www.unmannedairspace.info/counter-uas-systems-and-policies/jiatf-401-usd87m-contract-is-andurils-first-task-order-under-new-enterprise-agreement/)

### Inferences
- 分工公式可以概括为："Lattice = 边缘（传感器 / 无人平台 / 效应器的网格与自主），Palantir（Foundry/AIP/MSS）= 企业云（数据治理、AI 模型、指挥决策与目标工作流）"。这一分工在 NGC2 数据层基线中写成了正式结构（Lattice + Foundry = edge-to-cloud mesh）。
- 2024 年 12 月的财团设想没有以独立法人或公开协议的形式出现。合作的实际形式是"项目制团队"（Team Anduril 等）加上各自的企业协议。两家各拿一份陆军企业协议、结构相同，说明陆军把它们当作两类不同的"平台型供应商"分别锁定，而不是一个打包的供应商。
- NATO eAirC2 的正面竞争表明，当某个任务层（空中 C2 数据层）两家都能覆盖时，合作并不排他。"latent tension"（Lattice 向上做分析、MSS 向下做作战 C2）在弱源分析中被提到过（[droneintelligence.ai](https://droneintelligence.ai/compare/anduril-vs-palantir)，弱源）。

### Gaps
- 2024-12 财团（SpaceX、OpenAI、Scale AI、Saronic）是否正式成立、有无公开协议：没有找到确认来源。
- Golden Dome 中 Anduril 与 Palantir 的具体模块分工，以及是否已获正式合同：只有匿名消息源，未见官方授予公告。
- Space Force 层面的联合投标：没有找到可靠来源。
- NATO eAirC2 最终选择结果：评估期约 9 个月，截至 2026-10 尚无结果。
- 陆军 CTO 备忘录所指问题后来的整改结论：未见公开文件。

---

## 问题2：创始人/高管表态、"新主承包商"叙事、共同投资人与人员流动

### Takeaway
两家公司共享"Palantir 系"人脉和 Thiel 网络（Anduril 联合创始人 Schimpf、Stephens、Grimm 均出自 Palantir），并共同推动"挑战传统 primes"的叙事，Sankar 的"Defense Reformation"18 条论纲是代表。人员流入政府方面有两个突出节点：Palantir CTO Sankar 等人于 2025-06-13 被任命为陆军预备役中校（Detachment 201）；Anduril 高管 Michael Obadal 出任陆军副部长（2025-09 宣誓就职）。没有找到两家 CEO 公开、系统地阐述双方分工的原话。

### Cited Findings
- **人脉同源【确认】**：Palantir 于 2003 年由 Peter Thiel 等人创立；Anduril 联合创始人 Trae Stephens、Brian Schimpf、Matt Grimm 均为前 Palantir 员工；Palantir 联合创始人 Joe Lonsdale 通过 8VC 投资国防初创企业。— [TechCrunch 2024-09-01（Sankar 专访）](https://techcrunch.com/2024/09/01/palantirs-cto-and-13th-employee-has-become-a-secret-weapon-for-valley-defense-tech-startups)；Schimpf 早年是 Palantir 工程负责人，参与构建 Foundry — [a16z 播客 2025-01](https://a16z.com/how-ai-is-changing-warfare-anduril-ceo-brian-schimpf/)
- **Sankar 的"Defense Reformation"【确认，本人言论】**：Sankar 仿照马丁·路德提出 18 条论纲，主张国家处于"未宣布的紧急状态"；他称冷战时期主要武器系统开支只有 6% 流向专业国防承包商（primes），如今已升到 86%。他还长期公开推广 Palantir、Tesla、SpaceX 校友创办的国防初创企业。— [Tectonic Defense 专访](https://www.tectonicdefense.com/interview-with-shyam-sankar-cto-of-palantir-technologies/)；[School of War Ep.165](https://schoolofwar.substack.com/p/ep-165-shyam-sankar-on-a-defense)；[TechCrunch 2024-09-01](https://techcrunch.com/2024/09/01/palantirs-cto-and-13th-employee-has-become-a-secret-weapon-for-valley-defense-tech-startups)
- **"新国防科技阵营"批判 primes 的叙事**：NYRB 2025-10-04 文章描述该阵营抨击传统 primes"僵化、低效、垄断"。— [NYRB](https://www.nybooks.com/online/2025/10/04/the-war-over-defense-tech/)
- **Luckey 表态**：Luckey 在 CNBC 上称，美国只花现在五角大楼预算的一半左右，也能建成更有效的防务，前提是不再买错误的东西。— [FPIF 转述](https://fpif.org/planet-palantir/)
- **政治资金**：Punchbowl News 报道过 Karp 与 Luckey 的政治献金（标题为"Inside Karp, Luckey's political warchests"），细节未获取。— [Punchbowl](https://punchbowl.news/article/defense/karp-luckey-political-warchest/)
- **Schimpf 访谈**：2025-01-09 Stratechery 专访涉及 Lattice SDK、CCA 竞争以及"与 Palantir 一起构建 AI"，但搜索摘要中没有关于 Palantir 部分的原话。— [Stratechery](https://stratechery.com/2025/an-interview-with-anduril-co-founder-and-ceo-brian-schimpf-about-paradigm-shifts/)
- **Detachment 201【确认】**：2025-06-13，陆军成立 Executive Innovation Corps / Detachment 201，四名科技高管宣誓成为陆军预备役中校：Shyam Sankar（Palantir CTO）、Andrew Bosworth（Meta CTO）、Kevin Weil（OpenAI CPO）、Bob McGrew（前 OpenAI 首席研究官）。四人以兼职技术专家身份参与"定向项目"，陆军称此举是为"Army Transformation Initiative"提速。— [Defense News 2025-06-13](https://www.defensenews.com/land/2025/06/13/tech-execs-enlist-in-army-reserve-for-new-innovation-detachment/)；[Task & Purpose](https://taskandpurpose.com/military-life/army-reserve-lt-col-tech-execs/)
- **Michael Obadal【确认】**：2025-03-11，特朗普提名 Anduril 高级总监、前特种作战军官 Obadal 为陆军副部长；参议院以 51–47 确认，2025-09-22 宣誓就职。他曾计划保留 Anduril 股票（据 The Intercept 2025-05-01 引述伦理披露文件），后修改伦理协议，承诺不再持有。— [DefenseScoop 2025-03-11](https://defensescoop.com/2025/03/11/trump-nominates-michael-obadal-army-undersecretary-anduril/)；[The Intercept](https://theintercept.com/2025/05/01/trump-army-anduril-mike-obadal-ethics/)；[Inside Defense](https://insidedefense.com/daily-news/obadal-steps-army-under-secretary-role-sheds-anduril-stocks)；[Responsible Statecraft](https://responsiblestatecraft.org/michael-obadal-trump/)

### Inferences
- 陆军是两家合作最集中的军种：NGC2 和两份企业协议都在陆军；Sankar 在陆军预备役任职、Obadal 任陆军副部长，再加上 Army Transformation Initiative 这一背景，形成"人员—改革议程—合同"的同向叠加。这是推断，没有直接证据表明存在利益输送。
- "neoprime/新主承包商"更像是两家及其投资网络共同塑造的叙事框架。它在 Hegseth 2025-11 的采办改革讲话中得到官方层面的呼应（见问题3）。

### Gaps
- Founders Fund 投资 Anduril 并领投多轮属于公开常识，但本轮搜索没有取得可引用来源，需要补充。
- Luckey、Karp、Schimpf、Sankar 直接、系统地谈两家分工（如"我们做边缘、他们做企业"）的原话：未找到。
- 两家联合游说（共同提交游说议题、共同出资的行业组织）：未找到可靠来源。
- 其他从两家进入国防部的官员（除 Obadal 之外）：本轮未检索到。

---

## 问题3：国家级无人/自主/AI 作战布局，以及 Lattice 与 MSS 各自的位置

### Takeaway
2023–2026 年美国的布局大致沿三条线推进：(1) 规模化无人系统，从 Replicator 到 DAWG 再到 Drone Dominance，FY2027 自主系统申请约 540 亿美元；(2) AI 驱动的指挥控制，即 CJADC2，以 MSS 为基石，2026-03 Feinberg 备忘录推动 MSS 成为"program of record"；(3) 采办体制改革，包括 2025-04 行政令、2025-07 无人机备忘录、2025-11"Warfighting Acquisition System"与 PAE。Lattice 主要嵌在第一条线的"群体协同自主软件"（Replicator ACT、CCA 自主、反无人机 C2）和陆军 NGC2 中；MSS 主要嵌在第二条线的联合/企业级决策与火力层。

### Cited Findings
**Replicator（2023–2025）**
- 原副部长 Kathleen Hicks 设定的目标是在 2025 年 8 月前部署"数千个"全域、可消耗的自主系统（ADA2）。— [Army Times 2024-11-13](https://www.armytimes.com/unmanned/2024/11/13/pentagon-announces-new-batch-of-drones-for-replicator-program/)；[INDOPACOM](https://www.pacom.mil/Media/News/News-Articles/Article/3965715/deputy-secretary-of-defense-kathleen-hicks-announces-additional-replicator-all/)
- 第一批（1.1）中公开的是 AeroVironment Switchblade 600；DIU 官员 2025-09 称已交付"数百"套。第二批（1.2，2024-11）包括 Anduril Ghost-X（陆军连级小型无人机）和 Anduril Altius-600（陆战队 Organic Precision Fires）。不同来源对承担这些系统的军种项目有分歧，Axios 称 Altius-600 与 Ghost-X 经由空军 Enterprise Test Vehicle 项目。— [Inside Unmanned Systems](https://insideunmannedsystems.com/dod-announces-second-tranche-of-replicator-platforms/)；[Avionics/Aviation Today 2025-09-04](https://www.aviationtoday.com/2025/09/04/hundreds-of-switchblades-delivered-so-far-in-first-replicator-tranche-diu-official-says)；[Axios 2024-11-20](https://www.axios.com/2024/11/20/replicator-hicks-anduril-pdw-drones)
- **Lattice 的位置【确认】**：2024-11-20，DIU 公布 Replicator 软件授标。Anduril（Lattice）与 L3Harris、Swarm Aero 赢得"Autonomous Collaborative Teaming（ACT）"，内容是在通信和 GNSS 拒止环境下协调"数百到数千个"跨域无人资产；另一条线 ORIENT（韧性 C2）由 Viasat、Aalyria、Higher Ground、IoT/AI 获得。— [DIU](https://www.diu.mil/latest/defense-innovation-unit-announces-software-vendors-to-support-replicator)；[Defense One 2024-11](https://www.defenseone.com/defense-systems/2024/11/diu-announces-software-awards-ai-enabled-drone-swarms/401197/)
- Replicator 2 指向反无人机。JIATF-401 于 2026-01-11 宣布首笔 Replicator 2 采购（Fortem DroneHunter F700），2026-02 采购 Perennial Autonomy Bumblebee V2（520 万美元）。— [Soldier Systems 2026-01-16](https://soldiersystems.net/2026/01/16/joint-interagency-task-force-announces-first-replicator-2-purchase-to-counter-homeland-drone-threats/)；[Defense Post 2026-02-09](https://thedefensepost.com/2026/02/09/jiatf-401-bumblebee-v2/amp/)。Lattice 随后通过 8,700 万美元任务订单成为 JIATF-401 的反无人机通用 C2（见问题1-G）。

**DAWG（Defense Autonomous Warfare Group）**
- 2025 年秋 Replicator 未能按 2025-08 期限完成大规模部署，整个组合从 DIU 移交 SOCOM 下新设的 DAWG。五角大楼于 2025-11-18 向 Washington Times 确认。— [Washington Times 2025-11-18](https://www.washingtontimes.com/news/2025/nov/18/pentagon-says-biden-era-replicator-drone-program-new-special-unit/)；[SOF News 2025-09-30](https://sof.news/drones/20250930/)
- 负责人为陆战队中将 Francis L. Donovan（Hegseth 任命）。FY2027 申请把 DAWG 经费从 FY2026 的约 2.259 亿美元提高到约 546 亿美元，主要放在 reconciliation（强制性）部分，不在 1.15 万亿美元基础预算内。【报道】有分析称三个国会委员会只写入约 10 亿美元。【报道/待核】Hegseth 承诺建立自主作战次级联合司令部，截至 2026-05 未建立；参院版 FY2027 NDAA 允许但不强制设立"Robotic and Autonomous Systems Combatant Command"，众院版没有该条款。— [GlobalSecurity DAWG budget](https://www.globalsecurity.org/military/agency/dod/dawg-budget.htm)；[Inside Government Contracts 2026-05](https://www.insidegovernmentcontracts.com/2026/05/the-pentagons-new-sub-unified-command-for-autonomous-warfare-what-it-means-and-where-it-might-land/)；[Defense-Aerospace](https://www.defense-aerospace.com/dawg-54b-requested-1b-written-down/)；[Forecast International 2026-05-21](https://dsm.forecastinternational.com/2026/05/21/a-new-dawg-in-the-fight-the-pentagons-54-billion-bet-on-autonomous-warfare/)
- 另有报道称 2026-04-21 成立了 SOUTHCOM Autonomous Warfare Command，由 Donovan 指挥（【弱源/待核】，来自搜索摘要）。

**行政令与部长备忘录**
- EO 14265"Modernizing Defense Acquisitions and Spurring Innovation in the Defense Industrial Base"（2025-04-09）要求改革国防采办。— 引自 [DoW 2026-07-01 备忘录（设立无人系统直接报告组合经理）](https://media.defense.gov/2026/Jul/01/2003956955/-1/-1/1/ESTABLISHMENT-OF-THE-DIRECT-REPORTING-PORTFOLIO-MANAGER-FOR-UNMANNED-SYSTEMS.PDF)
- EO 14307"Unleashing American Drone Dominance"（2025-06-06）：推动 BVLOS 常态化、eVTOL 试点、优先采用美制无人机并促进出口；同日签署 EO 14305"Restoring American Airspace Sovereignty"（反无人机）。— [White House Fact Sheet](https://www.whitehouse.gov/fact-sheets/2025/06/fact-sheet-president-donald-j-trump-unleashes-american-drone-dominance/)；[UCSB Presidency Project](https://www.presidency.ucsb.edu/documents/executive-order-14307-unleashing-american-drone-dominance)
- 2026-07-01 DoW 备忘录设立"Direct Reporting Portfolio Manager for Unmanned Systems"，引用了 EO 14265、14307、14305、14275。— [defense.gov PDF](https://media.defense.gov/2026/Jul/01/2003956955/-1/-1/1/ESTABLISHMENT-OF-THE-DIRECT-REPORTING-PORTFOLIO-MANAGER-FOR-UNMANNED-SYSTEMS.PDF)
- Hegseth"Unleashing U.S. Military Drone Dominance"备忘录（2025-07-10 公开）：把小型无人机重新归类为消耗性弹药，采购权下放到上校级指挥官，目标是 2026 年底前每个班配备。— [Inside Defense 文件](https://insidedefense.com/document/hegseth-memo-drone-dominance)；[DroneLife 2025-07-15](https://dronelife.com/2025/07/15/department-defense-accelerates-drone-procurement-military-operations/)
- **Drone Dominance Program**：由 2025 年 reconciliation 法案资助约 10 亿美元（另有 11 亿美元的说法），两年采购约 34 万架小型攻击无人机（另有"30 万+"的说法），单价从约 5,000 美元降到 2,300 美元；分四个"Gauntlet"阶段，第一阶段 2026-02-03 选出 25 家供应商竞争 1.5 亿美元订单，最大阶段可能只授予 3 家。— [army.mil](https://www.army.mil/article/289322/war_department_asks_industry_to_make_more_than_300k_drones_quickly_cheaply)；[DefenseScoop 2026-02-03](https://defensescoop.com/2026/02/03/drone-dominance-program-hegseth-military-uas-vendors/)；[DefenseScoop 2026-02-13](https://defensescoop.com/2026/02/13/military-drone-dominance-program-competition/)
- **采办转型（2025-11-07）**：Hegseth 在国防大学讲话并签发备忘录，把 Defense Acquisition System 更名为"Warfighting Acquisition System"；PEO 改组为 Portfolio Acquisition Executives（PAE），PAE 可在组合内依据绩效调剂资金，任期 4 年，薪酬与结果挂钩，2 年内完成过渡。他警告不配合的大公司"可能会消失"。海军设 5 个 PAE；空军 2026-01 任命首批 5 名 PAE。— [DefenseScoop 2025-11-07](https://defensescoop.com/2025/11/07/hegseth-acquisition-transformation-speech-memo-guidance/)；[ClearanceJobs 2025-11-17](https://news.clearancejobs.com/2025/11/17/inside-the-pentagons-new-acquisition-revolution-portfolio-executives-replace-layers-of-bureaucracy/)；[Navy.mil](https://www.navy.mil/Press-Office/Press-Releases/display-pressreleases/Article/4435370/navy-reshapes-warfighting-acquisition-system/)；[Military Times 2026-01-09](https://www.militarytimes.com/air/2026/01/09/air-force-outlines-acquisition-changes-supporting-hegseth-mandate/)

**预算**
- **OBBBA（2025 reconciliation）**：防务部分约 1,500 亿美元（另有 1,433 亿美元、10 个优先方向、至 FY2034 的说法）。众院军委会版本中，无人机、单向攻击自主系统、水面/水下无人系统和 AI 合计超过 100 亿美元；无人水面艇约 21 亿美元（报道口径）。最终法律的自主类明细没有取得。— [Reason 2025-05-27](https://reason.com/2025/05/27/the-pentagon-is-getting-150-billion-from-the-big-beautiful-bill/)；[DSEI](https://www.dsei.co.uk/news/bill-allocates-usd150-billion-defence-spending)
- **FY2026**：自主系统申请 134 亿美元，反无人机 31 亿美元。分项为空中 94 亿、地面 2.1 亿、海上 17 亿、水下 7.34 亿、软件与跨域集成 12 亿美元（分项来自弱源 labla.org，总数来自 DefenseScoop）。— [DefenseScoop 2026-04-21](https://defensescoop.com/2026/04/21/dod-plans-largest-ever-investment-drones-anti-drone-weapons/)；[labla.org（弱源）](https://www.labla.org/ai-war/the-pentagon-is-spending-13-4-billion-on-ai-heres-where-every-dollar-is-going/)
- **FY2027【确认，主计长概览书】**：自主/遥控系统 540 亿美元，其中 392 亿美元与 Drone Dominance 强制性申请相关；AI 投资 585 亿美元，其中 MSS 与 Joint Fires Network（JFN）合计 23 亿美元，另有 460 亿美元多年期强制性"sovereign AI arsenal"。— [FY2027 Budget Overview Book](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2027/FY2027_Budget_Request_Overview_Book.pdf)；[Greenberg Traurig 解读](https://www.gtlaw.com/en/insights/2026/5/understanding-the-presidents-fy-2027-budget-request-for-the-department-of-war)；[The Hill](https://thehill.com/opinion/national-security/5833242-dawg-pentagon-2027-budget/)

**MSS 在 CJADC2 中的位置（CDAO）**
- 2026-03-09，副部长 Steve Feinberg 签发备忘录，要求在 FY2026 结束（2026-09-30）前把 MSS 转为正式 program of record，列出近二十项任务；系统管理权从 NGA 转到 CDAO 下的 MSS 项目办公室；备忘录把"AI 赋能决策"定为 CJADC2 的"cornerstone"。— [DefenseScoop 2026-04-03](https://defensescoop.com/2026/04/03/palantir-maven-feinberg-directive/)；[DefenseScoop 2026-04-15](https://defensescoop.com/2026/04/15/palantir-maven-smart-system-pentagon-program-transition-feinberg/)
- 2026-08 任命新的 MSS 项目主任，同时推进 C2 集成；预算材料提到与"Joint Force AI-Enabled Headquarters initiative"相关的 15 亿美元以上申请。— [DefenseScoop 2026-08-05](https://defensescoop.com/2026/08/05/pentagon-appoints-new-maven-smart-system-program-director/)
- 2026-09-22：五角大楼官员称 MSS 用户超过 10 万人。— [DefenseScoop 2026-09-22](https://defensescoop.com/2026/09/22/maven-smart-system-ai-james-mazol-cameron-stanley-defensetalks/)
- **状态冲突**：Crypto Briefing（2026-08-25）称 MSS"已正式指定"为 program of record，FY2027 五年 23 亿美元；DefenseScoop（2026-09-22）仍把它描述为年底前的过渡指令。截至 2026-10-10，未找到正式完成的官方公告。— [Crypto Briefing（弱源）](https://cryptobriefing.com/palantir-maven-pentagon-program-of-record/)

**Golden Dome 与 CCA**
- Golden Dome：行政令（2025-01；本轮没有检索 EO 原文，日期依据任务说明）初始估算 1,750 亿美元，2026-03 上调到 1,850 亿；Guetlein 把 C2 视为"secret sauce"，软件由 Anduril/Palantir 等财团开发（报道，见问题1-E）。— [Motley Fool](https://www.fool.com/investing/2026/03/25/palantir-named-as-part-of-trump-administrations-18/)
- CCA：Anduril YFQ-44A 于 2025-10-31 首飞。【报道】2026-06-18 空军选定 Anduril（FQ-44 Fury）与 General Atomics（FQ-42）进入 Increment 1 生产；Lattice 被选入 CCA 任务自主下一阶段的软件池，同池还有 GA、Lockheed、Northrop、RTX Collins、Shield AI，自主软件竞争持续到 2027 年。未与空军官方发布核对。— [DefenseScoop 2025-10-31](https://defensescoop.com/2025/10/31/anduril-cca-air-force-first-flight/)；[Amphenol 转载](https://www.amphenol-aerospace.com/markets/u-s-air-force-selects-anduril-and-general-atomics-for-first-production-collaborative-combat-aircraft)；[Circleville Herald](https://www.circlevilleherald.com/news/usaf-selects-anduril-for-production-phase-of-cca-program-next-phase-of-cca-mission-autonomy/article_1895a663-5acc-4002-803d-562350724e8c.html)

**Hellscape（INDOPACOM）**
- 2024-06，Adm. Samuel Paparo 提出在中国入侵部队渡海时投放无人机、无人潜航器和无人水面艇群，制造"unmanned hellscape"，为美盟争取约一个月的时间；2025 年美方称该战略"on track"。有媒体把它与 Replicator 联系起来。— [Washington Times 2024-06-14](https://www.washingtontimes.com/news/2024/jun/14/indo-pacific-commander-plans-hellscape-chinas-mili/)；[SCMP](https://www.scmp.com/news/china/military/article/3296808/us-navy-confirms-drone-hellscape-use-against-pla-taiwan-strait-track)；[USNI Proceedings 2025-04](https://www.usni.org/magazines/proceedings/2025/april/envisioning-hellscape-ukrainian-lessons-taiwan-drone-strategy)
- 2026-08 Valiant Shield 演习中演示了基于 Lattice 的"Guam Defense System Battle Manager"，融合陆军、空军、海军和 MDA 资产（【弱源/待核】，来自聚合站摘要）。— [Venture Atlas（弱源）](https://www.ventureatlas.org/company/anduril)

### Inferences
- 国家级布局可以分为三层：
  1. **战略/企业决策层**：CJADC2、MSS（CDAO 管理，已立项或即将立项，FY2027 与 JFN 合计 23 亿美元）
  2. **战役/军种 C2 数据层**：陆军 NGC2（Lattice + Foundry）、Golden Dome C2 胶水层（两家合作）、JFN
  3. **战术边缘自主与效应器层**：Replicator→DAWG、Drone Dominance、CCA、反无人机（JIATF-401），Lattice 作为群体协同、自主和 C2 软件
- 两家合作的空间正好卡在第2层（中间层），这也是 Feinberg 备忘录和 FY2027 预算加码最集中的位置。
- 采办改革（企业协议、PAE 资金调剂、商业优先、OTA）在制度上有利于"平台型软件 + 快速硬件"的供应商。两份陆军企业协议的结构就是例证。

### Gaps
- JFN（Joint Fires Network）与 MSS、Lattice 的具体技术关系：未找到可靠来源。
- Army Transformation Initiative（2025-05）原文中有关无人/C2 的条目：本轮未直接检索，只在 Det.201 报道中被提及。
- CDAO 对 Lattice 是否有正式角色：未找到。
- OBBBA 最终法律的自主类明细：未取得。

---

## 问题4：MSS 到 Lattice 的"战略/战役 AI 目标识别 → 战术边缘自主与效应器"管线

### Takeaway
官方和公司文件确认了"edge to enterprise"的整合意图（2024-12 公告），也确认了 NGC2 中 Lattice + Foundry 的 edge-to-cloud 数据网格。"MSS 生成目标包、Lattice 在边缘执行"这一管线说法主要来自二手分析。本轮没有检索到 CSIS、CNAS、RAND、War on the Rocks、Hudson 对两者组合的专门分析。

### Cited Findings
- 一手：两家称 MSS 与 Lattice 结合提供"从边缘到企业"的无缝作战能力。— [Anduril 新闻稿 2024-12-06](https://www.anduril.com/news/anduril-and-palantir-to-accelerate-ai-capabilities-for-national-security)
- 一手/主流媒体：NGC2 基线中 Lattice（边缘）与 Foundry（云）组成 edge-to-cloud data mesh。— [DefenseScoop 2026-06-22](https://defensescoop.com/2026/06/22/army-taps-anduril-lead-ngc2-common-data-layer-baseline/)
- 角色定义："MSS = enterprise mission command platform（情报与火力决策）；Lattice = edge-based mission autonomy platform（直接集成机器人系统）"。— [Inside Defense](https://insidedefense.com/share/222750)
- 二手分析：MSS 处理历史和近实时情报以形成目标包，Lattice 以机器速度实时执行目标包、协调传感器与效应器，两者是互补层而非竞争者。— [Foreign Affairs Forum 2026-04-21（弱源，非知名智库）](https://www.faf.ae/home/2026/4/21/andurils-lattice-platform-architecture-accountability-and-the-future-of-autonomous-warfare-in-american-defense-strategy)
- 杀伤链分段：某军级单位（摘要只说"the corps"，未点名；通常认为指第18空降军，但未核实）把杀伤链分为六步（识别、定位、筛选合法有效目标、排序、分配火力单元、交战），MSS 可以自动化或加速其中四步。— [GlobalSecurity Maven 页](https://www.globalsecurity.org/intell/systems/maven.htm)
- 速度指标【弱源/待核】：训练中 MSS 从卫星探测到火力单元的目标数据传递不到 1 分钟，2020 年需要 743 分钟。有文章称"Operation Epic Fury"中 24 小时打击 1,000 次，平均每个目标决策约 86 秒（作者自己的推算，相关事件的报道自称初步）。— [abhs.in（弱源）](https://abhs.in/blog/palantir-maven-smart-system-ai-kill-chain-dod-deployment-2026)；[Medium（弱源）](https://medium.com/@Gbgrow/the-ai-kill-chain-0d825639ce75)
- MSS 的数据模型：把原始传感器数据转为 Ontology 对象（如"Detection""Satellite Image"），形成可在云和边缘共享的通用作战图。— [Spatial Intelligence](https://www.spatialintelligence.ai/p/inside-palantirs-maven-smart-system)
- 张力：有分析认为 Lattice 正向上进入情报与分析，MSS 正向下进入作战 C2，双方存在"潜在竞争"。— [droneintelligence.ai（弱源）](https://droneintelligence.ai/compare/anduril-vs-palantir)
- 战场可靠性的反证：Reuters 报道 Anduril Ghost 无人机在乌克兰难以对抗俄方电子战，Altius 在 2025-11 空军测试中坠毁两架；台湾陆军称 2025 年收到 131 架 Anduril 无人机，对性能不予置评。— [BNN Bloomberg/Reuters 2025-11-27](https://www.bnnbloomberg.ca/business/2025/11/27/us-defense-firm-anduril-faces-setbacks-from-drone-crashes/)

### Inferences
- 可以合理地把这条管线写成：传感器/情报汇聚 → MSS（目标发现、排序、交战分配，人在回路，企业级）→ NGC2/Golden Dome 等 C2 数据层（Lattice + Foundry）→ Lattice 边缘（群体协同、武器/效应器控制、自主平台）。正文中应把这一表述标为"分析性构建"，因为官方文件只确认了两端的整合意图和 NGC2 数据层的结构，没有确认一条端到端、制度化的管线。
- 管线的薄弱环节在于：网络安全（陆军 CTO 备忘录）、硬件战场可靠性（Reuters 关于乌克兰的报道）、决策时间压缩带来的人类监督问题（弱源推算）。

### Gaps
- CSIS、CNAS、RAND、War on the Rocks、Hudson 对 MSS 与 Lattice 组合的专门分析：本轮没有检索到，需另行定向搜索。
- MSS 与 Lattice 之间的接口标准（API、数据模型互认）：未找到公开技术文件。

---

## 问题5：盟友布局——NATO、英国、澳大利亚、日本、台湾、乌克兰

### Takeaway
Palantir 以 MSS NATO（2025-03）、英国 MoD 战略伙伴关系（2025-09）占据盟军企业/目标层；Anduril 以 Ghost Shark（澳大利亚，2025-09 成为 program of record）、台湾 Altius/Barracuda 合作、日本 Lattice 演示占据边缘平台层。日本可能同时引入两家系统，这是两家分工在盟友层面的一个镜像。NATO 空中 C2 上两家正面竞争。

### Cited Findings
- **NATO–MSS【确认】**：NCIA 于 2025-03-25 完成采购 Maven Smart System NATO，供盟军作战司令部（ACO）使用，用途是情报融合与目标、战场感知与规划、加速决策；从提出需求到采购只用了 6 个月，金额未披露；ACO 预计 30 天内启用。— [DefenseScoop 2025-04-14](https://defensescoop.com/2025/04/14/nato-palantir-maven-smart-system-contract/)
- 法国开发 Artemis 作为"国内替代"，2026 年法国以 Arcadia 参与 NATO AI 竞争。— [AIN.ua](https://en.ain.ua/2025/04/15/nato-acquires-palantir-military-ai-system)；[Defence Matters](https://defencematters.eu/france-arcadia-nato-military-ai-classified-networks/)
- **NATO eAirC2**：2026-07-07 Anduril、Palantir、Athea 三方竞争（见问题1-F）。
- **英国【确认】**：2025-09-18 MoD 与 Palantir 建立战略伙伴关系。Palantir 承诺最多投资 15 亿英镑，伦敦成为其欧洲防务总部；合同潜在价值最高 7.5 亿英镑/5 年，取代此前 7,500 万英镑/3 年的安排；范围包括决策支持、军事规划与目标，对接 SDR 的"Digital Targeting Web"；部分工具已在乌克兰测试。— [GOV.UK](https://www.gov.uk/government/news/new-strategic-partnership-to-unlock-billions-and-boost-military-ai-and-innovation)；[Computing](https://www.computing.co.uk/news/2025/ai/uk-signs-defence-ai-partnership-palantir)；[SCMP/Bloomberg](https://www.scmp.com/tech/tech-trends/article/3325947/palantir-pledges-us2-billion-uk-investment-after-ministry-defence-deal)
- **澳大利亚【确认】**：2025-09-10 国防部与 Anduril Australia 签约，Ghost Shark 超大型自主水下航行器合同 17 亿澳元（约 11 亿美元），5 年期，含交付、维护与持续开发；2022 年以来已投入约 1.4 亿澳元开发经费；悉尼 7,400 平方米工厂 2026 年全面量产；官方定位为 AUKUS 核潜艇的补充，经批准后可出口美国等国。— [澳国防部长新闻稿](https://www.minister.defence.gov.au/media-releases/2025-09-10/equipping-royal-australian-navy-next-generation-autonomous-undersea-vehicles)；[Naval News 2025-09](https://www.navalnews.com/naval-news/2025/09/anduril-ghost-shark-now-australian-1-7-bn-program-of-record/)；[SLDinfo 2026-05](https://sldinfo.com/2026/05/ghost-shark-and-the-strategic-opportunity-a-conversation-with-david-goodrich-of-anduril-australia/)
- **日本【报道】**：Defense Post 2026-08-11 引述 Nikkei Asia，日本考虑把 Palantir MSS 和 Anduril Lattice 结合用于 C2，并在其上放一个国产 AI 平台进行监督；范围包括导弹防御、反击和无人机作战，可能写入年内国家安全战略修订；执政联盟内部有人担忧过度依赖外国供应商。此前 Anduril 与 Sumisho Aero-Systems 签约，为海上自卫队演示 Lattice。— [The Defense Post 2026-08-11](https://thedefensepost.com/2026/08/11/japan-military-ai-palantir-anduril/amp/)；[Asia Pacific Defence Reporter](https://asiapacificdefencereporter.com/anduril-industries-sumisho-aero-systems-sign-deal-for-japan-cc/)
- **台湾**：2024 年 FMS 合同，Altius 首批于 2025-08 交付；台湾陆军称 2025 年收到 131 架（Reuters）；采购 Altius-600M 与 Switchblade-300 共 1,000 架以上，被视为 Hellscape 的组成部分（USNI）。【弱源/待核】NCSIST 与 Anduril 于 2025-09 同意合作生产 Barracuda-500 和水下无人机。— [USNI Proceedings](https://www.usni.org/magazines/proceedings/2025/april/envisioning-hellscape-ukrainian-lessons-taiwan-drone-strategy)；[Eurasian Times](https://www.eurasiantimes.com/taiwan-accelerates-hellscape-strategy-to-deter-china-signs-key-underwater-drone-deal-with-u-s-firm/)；[BNN Bloomberg/Reuters](https://www.bnnbloomberg.ca/business/2025/11/27/us-defense-firm-anduril-faces-setbacks-from-drone-crashes/)
- **乌克兰**：Anduril 称自 2022 年起向乌克兰交付数百架 Altius；Reuters 称 Ghost 早期型号难以对抗俄方电子战。MSS 曾在乌克兰测试，结果"mixed"。— [BNN Bloomberg/Reuters](https://www.bnnbloomberg.ca/business/2025/11/27/us-defense-firm-anduril-faces-setbacks-from-drone-crashes/)；[AIN.ua](https://en.ain.ua/2025/04/15/nato-acquires-palantir-military-ai-system)

### Inferences
- 盟友层面复制了美国国内的分工：Palantir 进入盟军和盟国的企业/目标层（NATO ACO、英国 Digital Targeting Web），Anduril 进入盟国的边缘平台和本地化生产（澳、台、日）。日本"MSS + Lattice + 国产监督层"的方案若落地，就是这一分工模式的直接出口版本。
- 盟友对"主权/依赖"的顾虑（法国 Artemis/Arcadia、日本国产 AI 主张）是这一布局在外部最主要的制约因素。

### Gaps
- AUKUS Pillar II 框架下 Lattice 或 Ghost Shark 的正式定位：未找到官方文件。
- Anduril 英国业务（工厂、MoD 合同）：本轮未检索到。
- 日本最终决定（国家安全战略修订文本）：截至 2026-10 未见官方公告。
- Palantir 在乌克兰的具体合同与部署范围：本轮未检索到可靠来源。
