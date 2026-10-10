# Anduril Lattice：已展示的能力与实际应用案例（2018 – 2026年10月）

> 方法说明（调研日期 2026-10-10）：共进行约 15 次网络检索。WebFetch 对 anduril.com、techcrunch.com、aol.com 均返回 DNS 解析失败（ENOTFOUND），因此**下文大部分条目依据检索结果摘要，而非全文阅读**。每条均注明来源 URL；可信度标注：**[官方/政府]**、**[独立媒体]**、**[公司声明]**、**[二手聚合/低可信]**。凡由 Anduril 新闻稿或高管发言单独支撑的性能数据，均视为未经验证的说法。

---

## Q1. 边境监视：CBP 自主监视塔（AST / Sentry）

### Takeaway
自主监视塔是 Lattice 部署时间最长、规模最大的实战（非战斗）应用：2020 年成为 CBP 记录在案项目（Program of Record），已部署数百座，2026 年 6 月又追加订购 200 余座增程型（XR）塔。但目前没有公开、独立的检测效能数据。公开的独立评估（GAO 隐私审查、MIT Technology Review 2026 年 9 月调查）对隐私保护和实际效果提出质疑。

### Cited Findings
- **2020年（日期取自来源描述）—CBP（美国西南边境）**：自主监视塔被宣布为美国边境巡逻队的记录在案项目（Program of Record）[官方/政府] — [CBP](https://www.cbp.gov/newsroom/national-media-release/cbp-s-autonomous-surveillance-towers-declared-program-record-along)
- **约 2024 年（具体日期未核实）—Anduril 宣布部署第 300 座 AST**；公司估计这些塔约覆盖美国南部陆地边境的 30% [公司声明] — [Anduril](https://www.anduril.com/news/anduril-deploys-300th-autonomous-surveillance-tower-ast-advancing-capability-for-border-security)
- **2026年6月—CBP 以 3.63 亿美元合同采购 200 余座增程型 Sentry 塔** [公司声明 + 行业媒体] — [Anduril](https://www.anduril.com/news/anduril-and-u-s-customs-and-border-protection-expand-partnership-with-200-additional-extended-range-sentry-towers)；[ExecutiveBiz](https://www.executivebiz.com/articles/cbp-anduril-extended-range-sentry-towers-363m)；[HSToday](https://www.hstoday.us/industry/industry-news/u-s-customs-and-border-protection-set-to-purchase-200-extended-range-sentry-towers-from-anduril/)；[FedScoop](https://fedscoop.com/anduril-sentry-towers-cbp/)
- **全部监视塔（涵盖所有供应商，不只 Anduril）**：二手报道称 GAO 统计在“综合监视塔”（Integrated Surveillance Towers）项目下已部署 803 座塔；另一来源称约 830 座，并计划到 2034 年增至 2,300 座。**两数相互冲突，且未与 GAO 原文核对** [二手] — [MIT Technology Review, 2026-09-21](https://www.technologyreview.com/2026/09/21/1144166/border-towers-surveillance-investigation/)；[State of Surveillance](https://stateofsurveillance.org/news/anduril-border-surveillance-monopoly-big-beautiful-bill-2026/)
- **GAO 2024 年隐私审查**：一个倡导类网站称，GAO 按六项隐私保护措施评估 CBP 的监视塔项目，CBP 全部不达标。**未与 GAO 原文核对** [倡导类/二手] — [State of Surveillance](https://stateofsurveillance.org/news/anduril-border-surveillance-monopoly-big-beautiful-bill-2026/)
- **效果批评**：MIT Technology Review（2026-09-21）的调查估计，自 2021 年以来，有超过 110 人死在 Anduril 现代自主监视塔的覆盖范围内。该文质疑数十亿美元的监视投入为何未能及早发现处于危险中的人员 [独立媒体，数字为该刊自行估算] — [MIT Technology Review](https://www.technologyreview.com/2026/09/21/1144166/border-towers-surveillance-investigation/)
- **政策背景**：2025 年 7 月的《大而美法案》（Big Beautiful Bill）为边境技术拨款，被认为将使 Anduril 的监视塔业务大幅获益 [独立/倡导类] — [The Intercept, 2025-07-09](https://theintercept.com/2025/07/09/trump-big-beautiful-bill-anduril/)

### Inferences
- Lattice 在此场景中的作用是：在监视塔端自动检测、分类、跟踪人员和车辆，并将警报推送给特工。这是 Lattice 最成熟的大规模持续部署，但其效能指标（检测概率、虚警率、可用率）从未公开。
- “覆盖边境 30%”是公司口径，指地理覆盖，而不是实际抓获或检测效果。

### Gaps
- 未找到 GAO 或 DHS 监察长办公室（OIG）发布的 AST 检测率或运行可用率数据；GAO 报告编号未能定位。
- 截至 2026 年 10 月，Anduril 自有塔的确切数量不明（“第 300 座”的说法较旧；803 和 830 这两个数字涵盖所有供应商）。

---

## Q2. 反无人机（C-UAS）：SOCOM、陆战队、陆军、CENTCOM / 中东

### Takeaway
以合同计，反无人机是 Lattice 规模最大的作战应用领域：SOCOM 系统集成商合同（2022 年，9.676 亿美元）、陆战队 I-CsUAS 合同（2025 年，6.42 亿美元）、陆军 IBCS-M 反无人机火控选型（2025 年 11 月）、陆军 JIATF-401 企业级合同（2026 年 3 月，上限 200 亿美元，首个任务订单 8,700 万美元），以及拟议对科威特的 19.8 亿美元军售（2026 年 6 月）。此外，Anduril 声称其系统在“史诗怒火行动”（Operation Epic Fury，对伊朗冲突）中被“大量”用于对抗“沙希德”无人机。但**未找到任何可独立核实的、由 Lattice 引导的击落记录**。

### Cited Findings
- **2022-01-19—SOCOM**：Anduril 被选为反无人系统的系统集成合作伙伴（SIP），合同上限 9.676 亿美元，期限至 2032-01-19，在 11 家竞标者中胜出。工作地点包括美国本土内外。系统组合为 Sentry 塔 + Anvil 拦截器 + Lattice，其中 Lattice 负责“自主检测、分类、跟踪目标，向操作员告警并提供处置/交战选项” [国防部合同公告/独立媒体] — [Defense News](https://www.defensenews.com/unmanned/2022/01/24/us-special-operations-command-picks-anduril-to-lead-counter-drone-integration-work-in-1b-deal/)；[AFCEA Signal](https://www.afcea.org/signal-media/contracting/socom-selects-anduril-integration-partner-967-million-counter-unmanned)；[FedScoop](https://fedscoop.com/anduril-nabs-1b-contract-for-anti-drone-work-with-socom/)
- **SOCOM 后续合同**：另有一笔 8,600 万美元合同，用于帮助 SOCOM 控制其无人机（日期未核实）[行业媒体] — [Tectonic Defense](https://www.tectonicdefense.com/anduril-secures-86m-to-help-socom-control-its-drones/)
- **2024年11月—陆战队 MADIS**：约 2 亿美元的 MADIS（陆战队防空一体化系统）反无人机交战系统合同 [行业媒体] — [Overt Defense](https://www.overtdefense.com/2025/03/21/anduril-secures-642m-deal-to-deliver-ai-driven-counter-drone-defense-for-us-marine-corps/)
- **2025年3月—陆战队 I-CsUAS（设施反小型无人机）**：10 年期 IDIQ 合同，上限 6.42 亿美元，期限至 2035 年 3 月；首笔 950 万美元来自 FY2024 采购预算；内容为 Lattice C2 + Anvil + Pulsar 电子战，在 9 家竞标者中胜出；未公布具体型号和数量 [独立媒体] — [DefenseScoop, 2025-03-13](https://defensescoop.com/2025/03/13/marine-corps-anduril-contract-defend-installations-small-uas-drones/)；[EDR](https://www.edrmagazine.eu/anduril-wins-640-million-i-csuas-contract)
- **2025年11月—陆军 IBCS-M（机动型一体化作战指挥系统）**：陆军选定 Lattice 作为 IBCS-M 的反无人机下一代火控平台。The Defense Post 标题称 Lattice 在测试中实现“完美击杀记录”（perfect killstreak），**该数据来源于公司，细节未核实** — [DefenseScoop, 2025-11-11](https://defensescoop.com/2025/11/11/army-ibcs-maneuver-anduril-lattice-counter-uas/)；[The Defense Post, 2025-11-13](https://thedefensepost.com/2025/11/13/anduril-lattice-us-army/)；[Army Recognition](https://www.armyrecognition.com/news/army-news/2025/us-army-picks-anduril-lattice-for-integrated-battle-command-system-maneuver-counter-drone-role)
- **2026年3月—陆军 / JIATF-401**：企业级合同上限 200 亿美元（陆军强调这是最高潜在价值，而非已拨付金额）。首个任务订单 8,700 万美元，用于“通用反无人 C2”，由 Lattice 将多种反无人机系统连接起来 [独立媒体] — [Breaking Defense](https://breakingdefense.com/2026/03/army-awards-anduril-counter-drone-task-order-as-first-in-new-20b-contract-vehicle/)；[DefenseScoop, 2026-03-14](https://defensescoop.com/2026/03/14/anduril-20-billion-dollar-army-contract/)；[Defense One](https://www.defenseone.com/business/2026/03/anduril-secures-87m-contract-common-counter-unmanned-c2-program/412156/)
- **NORTHCOM 演习**：Lattice 在一次美国北方司令部演习中担任通用 C2（日期未核实）— 见 [Army Recognition（IBCS-M）](https://www.armyrecognition.com/news/army-news/2025/us-army-picks-anduril-lattice-for-integrated-battle-command-system-maneuver-counter-drone-role) 相关检索结果摘要
- **2026-06-05—科威特（拟议对外军售）**：美国国务院批准一项可能的 19.8 亿美元军售，包括 Roadrunner-M、Anvil-Kinetic 和 Lattice。**这是批准，不等于交付或实战使用** [行业媒体，依据国防安全合作局 DSCA 通知] — [Army Recognition](https://www.armyrecognition.com/news/army-news/2026/u-s-approves-1-98b-anduril-counter-drone-system-for-kuwait-to-defend-against-drone-swarm-attacks)
- **2026年（史诗怒火行动 / 伊朗冲突）—中东**：Anduril 总裁称公司是对抗伊朗“沙希德”无人机的“主要”（principal）系统、是“大量”（heavy）参与者，但拒绝透露具体部署了哪些系统；报道同时指出，尚不清楚相关系统近期是否在中东部署 [公司声明，无独立证实] — [AOL / 转载](https://www.aol.com/articles/andurils-president-says-firm-heavy-040829085.html)
- **2026-10-01—第三方拦截器集成**：ORIGIN 公司的 BLAZE 拦截器被集成到 Lattice，说明其开放架构在吸纳第三方效应器 [行业媒体] — [Overt Defense](https://www.overtdefense.com/2026/10/01/anduril-and-origin-integrated-origins-blaze-interceptor-with-andurils-lattice-software-for-drone-defense/)
- **2024-12—Lattice 演示**：MIT Technology Review 记者观看了 Lattice 在反无人机/基地防御场景下的演示 [独立媒体，观摩公司演示] — [MIT Technology Review, 2024-12-10](https://www.technologyreview.com/2024/12/10/1108354/we-saw-a-demo-of-the-new-ai-system-powering-andurils-vision-for-war/)
- **事故**：一次 Anvil 反无人机测试在俄勒冈州引发 22 英亩的野火（据 WSJ 报道）— [Sherwood News](https://sherwood.news/tech/wsj-andurils-weapons-systems-have-failed-during-several-tests/)

### Inferences
- 在反无人机领域，Lattice 的核心价值在于“传感器/效应器无关的集成与火控层”：多家国防客户（SOCOM、陆战队、陆军 IBCS-M、JIATF-401）通过竞标选中了它，这是较强的间接验证。
- 但实战效能（拦截数、交战成功率）**没有任何公开的独立数据**。中东实战说法仅有公司高管笼统表述。

### Gaps
- CENTCOM 基地防御的具体部署（时间、地点、拦截战果）：未找到可靠来源。
- Roadrunner/Anvil 实战拦截记录、红海/胡塞相关使用：未找到。
- 陆军 FAAD C2 与 Lattice 的具体关系（IBCS-M 之外）未查明。
- IBCS-M 合同金额与“完美击杀”测试的具体条件未查明。

---

## Q3. 乌克兰：Altius、Ghost 与电子战韧性

### Takeaway
乌克兰是 Anduril 系统唯一可公开核实的实战使用场景，但结果总体**负面**：据 WSJ（2025 年 11 月）报道，SBU（乌克兰安全局）使用的 Altius 坠毁、未命中目标，因此在 2024 年停用；2022 年交付的约 40 架 Ghost 受俄方干扰严重。这是“公司宣传”与“实战表现”之间最明显的反差。

### Cited Findings
- **2022年—乌克兰**：Anduril 向乌军提供约 40 架 Ghost 小型直升机式侦察无人机，士兵很快因俄方干扰系统影响其运行而感到沮丧 [独立媒体转述 WSJ] — [TechCrunch, 2025-11-27](https://techcrunch.com/2025/11/27/andurils-autonomous-weapons-stumble-in-tests-and-combat-wsj-reports)；[Sherwood News](https://sherwood.news/tech/wsj-andurils-weapons-systems-have-failed-during-several-tests/)
- **2024年—乌克兰 SBU**：Altius 巡飞弹坠毁、未能命中目标，问题严重到乌方在 2024 年停用，此后未再部署；另有报道称其易受俄方干扰，已撤出战场 [独立媒体转述 WSJ] — [TechCrunch](https://techcrunch.com/2025/11/27/andurils-autonomous-weapons-stumble-in-tests-and-combat-wsj-reports)；[TechBuzz](https://www.techbuzz.ai/articles/anduril-s-autonomous-weapons-fail-in-tests-ukraine-combat)
- **Anduril 回应**：公司称这些挑战是武器研发中的正常现象（“We do fail… a lot”），否认存在根本性技术缺陷 — [Edward Conard 摘要](https://www.edwardconard.com/macro-roundup/tests-in-the-us-and-on-the-battlefield-in-ukraine-suggest-that-anduril-a-leading-new-entrant-into-the-defense-industry-is-facing-challenges-in-developing-and-fielding-attritable-mass-weapons-systems/)
- 有二手页面将 Altius 的“电子战失败”与对台交付并列讨论 [二手聚合/低可信] — [drone-warfare.com](https://drone-warfare.com/research/altius/)

### Inferences
- 报道中的失败主要出在飞行平台和导航/数据链在强电子战下的生存能力，并非专门针对 Lattice 软件本身；但 Lattice 宣传的“边缘自主、抗干扰”在乌克兰并未得到实战佐证。

### Gaps
- 未找到 Lattice 本身在乌克兰作为 C2 层使用的公开证据。
- WSJ 原文无法访问；乌方或美方官方没有回应。

---

## Q4. 陆军下一代指挥控制（NGC2）、Ivy Sting、项目融合（Project Convergence）

### Takeaway
NGC2 是 Lattice 作为“战场数据层/C2 骨干”最实质的案例：2025 年 7 月获得 9,960 万美元原型合同 → Ivy Sting 1–5 系列演习 → 2026 年 5 月 Ivy Mass 实现整个第 4 步兵师上线 → 获得 I 军上限 18 亿美元的部署合同。其中性能数据（如“火力时间缩短 90%”）主要来自 Anduril。第 25 步兵师的 NGC2 原型由洛克希德·马丁主导，与 Anduril 无关。

### Cited Findings
- **2025年7月—陆军 / 第 4 步兵师（卡森堡）**：Anduril 牵头的团队（含 Palantir 等）获得 9,960 万美元、为期 11 个月的 NGC2 原型协议，目标是为第 4 步兵师构建原型并扩展到师级 [独立媒体] — [DefenseScoop, 2025-07-21](https://defensescoop.com/2025/07/21/anduril-army-next-generation-command-and-control-award/)；[The Defense Post](https://thedefensepost.com/2025/07/21/anduril-us-army-ngc2-prototype/)
- **2025年9月—Ivy Sting 1（实弹）**：第 4 步兵师使用运行在 Lattice 上的炮兵火控软件，发射 M777 榴弹炮；师级目标处理流程完全在 Lattice Mesh 和 Palantir Target Workbench 上运行；据称使用 AXS 时炮组在 30 秒内完成数字化准备 [公司/行业媒体] — [Defence Industry Europe](https://defence-industry.eu/anduril-and-u-s-army-showcase-next-gen-command-and-control-with-ngc2-in-live-fire-ivy-sting-1/)
- **Ivy Sting 4–5（2025 年末至 2026 年初）**：用例超过 50 个；Ivy Sting 5 将数据网格扩大到原来的三倍，连接 65 个以上战术边缘节点；在通信降级阶段，于本地网格上完成端到端的电子战定位—火力打击流程 [公司声明] — [Anduril](https://www.anduril.com/news/scaling-next-generation-command-and-control-from-prototype-to-fight)；[ASDNews, 2026-04-10](https://www.asdnews.com/news/defense/2026/04/10/scaling-nextgen-command-control-prototype-fight)
- **2026年5月—Ivy Mass**：整个第 4 步兵师在 NGC2 上运行，接入超过 2,500 台终端；Anduril 称炮兵火力时间比传统系统缩短 90%。**该数据仅为公司声明**。Ivy Mass 是项目融合顶点演习 6（PC-C6）之前的最后一次活动 — [MilitaryLeak, 2026-05-26](https://militaryleak.com/2026/05/26/how-team-anduril-and-us-army-took-lattice-across-the-4th-infantry-division/)；[Anduril](https://www.anduril.com/news/anduril-continues-to-scale-next-generation-command-and-control-across-the-army)
- **2026年—部署合同**：陆军授予 Anduril 为期 5 年、上限 18 亿美元的合同，从 I 军开始部署 NGC2，基础期金额 1.628 亿美元 [行业媒体] — [GovConWire](https://www.govconwire.com/articles/anduril-army-ngc2-contract-i-corps)；[Defence Blog](https://defence-blog.com/u-s-army-moves-anduril-battle-network-from-test-to-field/)
- **第 25 步兵师（夏威夷）**：第二个 NGC2 原型由洛克希德·马丁主导，通过 Lightning Surge 系列演习和 2026 年菲律宾“肩并肩”（Balikatan）演习测试，**不是 Anduril/Lattice** — 依据检索结果摘要，见 [GovConWire](https://www.govconwire.com/articles/anduril-army-ngc2-contract-i-corps) 相关报道（需进一步核实）

### Inferences
- 陆军从原型直接转入大额部署合同，说明陆军用户对 Lattice 作为数据层是认可的，这是比公司宣传更硬的信号。但定量性能数据（30 秒、90%、2,500 台设备）仍需陆军官方确认。

### Gaps
- PC-C6 的结果未找到。
- 没有陆军或 GAO 对 NGC2 网络安全、可靠性的独立评估。

---

## Q5. 空军：CCA（YFQ-44A“狂怒”Fury）、ABMS / 美国空军作战网络（DAF Battle Network）

### Takeaway
YFQ-44A 于 2025-10-31 首飞，2026 年 6 月获得生产合同，并完成了一次端到端、超视距、使用惰性 AIM-120 的模拟打击。但**公开资料未明确说明 Lattice 在 CCA 自主软件中的角色**。空军 CCA 采用政府参考自主架构，并另行选定自主软件供应商；本轮检索未核实 Lattice 是否为 YFQ-44A 的任务自主软件。

### Cited Findings
- **2025-10-31—YFQ-44A 首飞**；**2026-06-17—空军授予 FQ-44A 和 FQ-42A 生产合同**，比原计划提前约 4 个月 — [TWZ](https://www.twz.com/air/usaf-orders-both-general-atomics-fq-42-and-andurils-fq-44-into-production)；[Wikipedia](https://en.wikipedia.org/wiki/Anduril_YFQ-44)
- **2026-03-24 / 2026-07-28—投产时间说法冲突**：The Aviationist 称 3 月已在俄亥俄州 Arsenal-1 工厂进入批量生产；Military Times 称首架俄亥俄制造的飞机 7 月 28 日才下线 — [The Aviationist](https://theaviationist.com/2026/03/24/yfq-44a-fury-cca-is-now-in-production/)；[Military Times](https://www.militarytimes.com/industry/techwatch/2026/07/28/first-anduril-yfq-44a-rolls-off-production-line-for-us-cca-program/)
- YFQ-44A 完成了针对模拟目标、使用惰性 AIM-120 的端到端超视距打击 — [Military Times](https://www.militarytimes.com/industry/techwatch/2026/07/28/first-anduril-yfq-44a-rolls-off-production-line-for-us-cca-program/)
- **2026-09-14**：空军部长 Meink 将目标提高到 2032 年至少 500 架 CCA — [migflug（二手）](https://migflug.com/afterburner/fq-42-vengeance-fq-44-fury-usaf-500-cca-2032/)
- **事故**：据 WSJ 报道，一台 Fury 发动机在地面测试中受损 — [Sherwood News](https://sherwood.news/tech/wsj-andurils-weapons-systems-have-failed-during-several-tests/)

### Gaps
- Lattice 与 CCA 任务自主软件的关系、ABMS/DAF 作战网络中 Lattice 的合同情况：本轮检索均未找到可靠来源。

---

## Q6. 海军 / 海上：无人艇、Ghost Shark、Dive-LD、Replicator

### Takeaway
澳大利亚 Ghost Shark 是最成功的海上案例：按期按预算交付 3 艘原型，2025 年 9 月签订 17 亿澳元生产合同，2026 年 4 月交付首批生产艇并成立 MASU 部队，自主功能由 Lattice 管理。相反，据 WSJ 报道，在美国海军一次加州近海演习中，十余艘由 Lattice 控制的无人艇失灵或停机，水兵警告存在安全风险。

### Cited Findings
- **2022–2024 年—澳大利亚皇家海军**：联合开发协议，生产 3 艘原型；首艘原型于 2024 年交付，原型阶段按期按预算完成（开发经费有约 1.4 亿澳元和约 9,250 万美元两种说法，相互冲突）— [Breaking Defense, 2025-11](https://breakingdefense.com/2025/11/first-ghost-shark-extra-large-auv-delivered-to-australian-navy/)；[Wikipedia](https://en.wikipedia.org/wiki/Ghost_Shark_(submarine))
- **2025-09-10—澳大利亚**：签订为期 5 年的 Ghost Shark 交付、维护和持续开发合同，金额 17 亿澳元（约 11 亿美元），首批数十艘 [官方/政府] — [澳大利亚国防部长新闻稿](https://www.minister.defence.gov.au/media-releases/2025-09-10/equipping-royal-australian-navy-next-generation-autonomous-undersea-vehicles)；[GovConExec](https://www.govconexec.com/2025/09/australia-anduril-ghost-shark-auv-contract/)
- **2026-04-14/15**：皇家海军海上自主系统部队（MASU，SEA 1200 项目）成立，接收首批生产型 Ghost Shark；交付时间由原定的 2026 年 1 月推迟到 4 月左右 — [The Defense News](https://www.thedefensenews.com/news-details/Royal-Australian-Navy-Activates-Maritime-Autonomous-Systems-Unit-Integrating-Ghost-Shark-Bluebottle-and-Speartooth-Uncrewed-Systems/)
- 艇载自主功能由 Lattice 管理 [二手] — [speedoscience](https://www.speedoscience.com/2026/03/anduril-ghost-shark-autonomous-xl-auv.html)
- **美国海军无人艇失败（据 WSJ）**：在加州近海演习中，十余艘由 Lattice C2 控制的无人艇停机，对其他船只构成危险；水兵警告“安全违规和潜在人员伤亡”。时间有冲突：多数来源称 2025 年 5 月或夏季，TechBuzz 称 2024 年。Anduril 回应称这是迭代开发的一部分 — [Sherwood News](https://sherwood.news/tech/wsj-andurils-weapons-systems-have-failed-during-several-tests/)；[TechBuzz](https://www.techbuzz.ai/articles/anduril-s-autonomous-weapons-fail-in-tests-ukraine-combat)；[Edward Conard](https://www.edwardconard.com/macro-roundup/tests-in-the-us-and-on-the-battlefield-in-ukraine-suggest-that-anduril-a-leading-new-entrant-into-the-defense-industry-is-facing-challenges-in-developing-and-fielding-attritable-mass-weapons-systems/)
- 另有一起海军无人艇试验事故：2025 年 7 月，一艘无人艇在加州海峡群岛附近掀翻支援船，试验中止。**该报道未点名 Anduril** — [DefenseScoop, 2025-07-01](https://defensescoop.com/2025/07/01/navy-unmanned-vessel-accident-boat-ventura-channel-islands-california/)
- Anduril 创始人称 WSJ 关于无人艇工厂的报道失实（属于另一则 WSJ 报道）— [Defence Blog](https://defence-blog.com/anduril-founder-calls-wsj-drone-boat-factory-story-false/)

### Gaps
- Dive-LD 的具体海军合同和测试数据、Replicator 中 Lattice 的角色（如“Replicator 无人艇编队协同软件”）：本轮检索均未能核实。

---

## Q7. 盟国客户：台湾、英国、澳大利亚、日本、中东、韩国

### Cited Findings
- **台湾—Altius-600M**：2024 年 6 月批准对外军售 291 套；2025 年 8 月开始交付，约 7 个月后完成。合同金额说法冲突（3 亿美元 vs 11 亿美元；台湾“国防部”未公布）。另有二手来源称 2026 年 8 月追加 2,032 套（新台币 269 亿元），**仅单一来源，未证实** — [The Defense Post, 2026-03-20](https://thedefensepost.com/2026/03/20/anduril-altius-600m-taiwan/)；[Janes](https://www.janes.com/defence-intelligence-insights/defence-news/defence/taiwan-acquires-first-batch-of-altius-600m-loitering-munitions)；[Venture Atlas（二手）](https://www.ventureatlas.org/company/anduril)
- **台湾 / 韩国合作**：2025 年 8 月，Anduril 扩大在印太地区的合作伙伴关系 — [Breaking Defense](https://breakingdefense.com/2025/08/anduril-increases-indo-pacific-footprint-with-taiwan-south-korea-partnerships/)
- **英国**：Anduril 自 2019 年起在英国开展业务，服务过皇家海军陆战队和战略司令部；2021 年获得 520 万美元合同，演示部队防护技术（Ghost 4 + Lattice）；之后获得 1,700 万英镑、31 个月的合同，研究海外常设联合作战基地（PJOBs）的固定站点防护与反无人机需求，Lattice 作为核心指挥层（日期约 2023 年，未核实）— [Anduril](https://www.anduril.com/news/anduril-industries-awarded-gbp17-million-ministry-of-defence-force-protection-technology)；[TBIJ, 2025-07-23](https://www.thebureauinvestigates.com/stories/2025-07-23/selling-weapons-to-westminster-how-defence-giant-anduril-trained-its-sights-on-the-uk)
- **科威特**：见 Q2（2026 年 6 月拟议军售 19.8 亿美元）。

### Gaps
- 日本、阿联酋等中东客户的 Lattice 合同：本轮未检索到。
- 未找到英国皇家海军陆战队专门的 Lattice 反无人机合同。

---

## Q8. 演习与其他展示（Valiant Shield、金穹 Golden Dome、太空等）

### Cited Findings
- **2026年（约 8 月）—“勇敢之盾”（Valiant Shield）2026，关岛**：Anduril 演示基于 Lattice 的关岛防御系统作战管理器，融合陆军、空军、海军和导弹防御局（MDA）的资产；截至 2026-09-15，未见后续部署合同 [二手聚合，需核实] — [Venture Atlas](https://www.ventureatlas.org/company/anduril)
- **金穹（Golden Dome）**：路透社报道 Anduril 与 Palantir 共同开发金穹软件；Anduril 是太空军 12 个天基拦截器团队之一（奖励总额上限 32 亿美元，目标 2028 年完成演示）— [AOL/Reuters](https://www.aol.com/articles/anduril-palantir-developing-golden-dome-233842760.html)；[Airforce Technology](https://www.airforce-technology.com/news/anduril-us-golden-dome/)
- **太空态势感知**：Varda、LeoLabs、Anduril 联合跟踪 Varda 返回舱的轨道机动，数据实时输入 Lattice — [ExecutiveBiz](https://www.executivebiz.com/articles/varda-leolabs-anduril-hypersonic-reentry-demo)
- **Altius 测试事故（WSJ）**：在埃格林空军基地，一架 Altius 从飞机投放后垂直坠地约 8,000 英尺 — [Mid Bay News](https://midbaynews.com/post/eglin-drone-failures-put-anduril-under-the-microscope)

### Gaps
- 北方利刃（Northern Edge）、Balikatan（Anduril 部分）、REPMUS、沙漠守护者（Desert Guardian）、超级碗/体育场反无人机：本轮检索均无可靠结果。

---

## 总结：Lattice 实际能做什么 vs. 宣传

| 维度 | 有较强证据（政府合同/官方/独立媒体） | 主要依赖公司声明 | 有反证或负面证据 |
|---|---|---|---|
| 传感器融合与自动检测/跟踪（固定站点） | CBP 记录在案项目，数百座塔持续运行；SOCOM、陆战队反无人机合同 | “覆盖边境 30%” | 无公开检测效能数据；MIT TR 调查质疑实际效果；GAO 隐私审查不达标（二手） |
| 多传感器/多效应器的反无人机 C2 | IBCS-M 选型、JIATF-401、I-CsUAS、科威特拟议军售 | IBCS-M 测试“完美击杀”；中东“主要系统” | 无公开实战拦截战果；Anvil 测试引发野火 |
| 师级战场数据网格 / 火力链 | 9,960 万美元原型 → 18 亿美元部署合同；第 4 步兵师整师上线 | 30 秒、90%、65+ 节点、2,500 台设备 | 无独立评估 |
| 无人平台自主/集群控制 | Ghost Shark 按期交付并投入使用（澳大利亚） | CCA 中 Lattice 的角色 | 美国海军演习中十余艘无人艇失灵；乌克兰 Altius/Ghost 受干扰失败 |

结论：Lattice 作为**集成/数据层/C2 软件**，已经得到多军种采购决策的认可（这是最硬的证据）。但**定量效能数据几乎全部来自 Anduril**；**唯一可公开核实的实战使用（乌克兰）结果是负面的**；对抗性电子战环境下的表现是最主要的未证实领域。
