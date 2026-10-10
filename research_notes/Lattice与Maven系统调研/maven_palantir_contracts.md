# 合同与任务：Project Maven / Maven Smart System 与 Palantir 美国及盟国防务合同目录（2017–2026.10）

> 方法说明：本笔记基于 WebSearch 结果摘要（检索日期 2026-10-10）。WebFetch 抓取原文失败（如 defensescoop.com 返回 `getaddrinfo ENOTFOUND`），因此所有数字来自搜索摘要及其引用的原始来源，未逐页核对原文。ceiling（上限）≠ obligation（实际拨付），下表严格区分；冲突之处均已标注。"Maven专属"列：Y = Maven/MSS 直接相关；P = 部分相关或间接相关；N = 非 Maven。

## Q1. Project Maven 早期（2017–2023）的供应商与集成商合同有哪些？

### Takeaway
2017–2021 年间，Maven 的合同大多通过集成商 ECS Federal 下达（采购渠道为 ARL 的 BAA 合同），Google、Microsoft、AWS、Clarifai 都是 ECS 体系下的分包商。最大的单笔合同"Pavement"金额为 1.42 亿美元，但其采购记录已被五角大楼依据 FAR 4.606 从公开数据库中删除，所以官方数据缺失严重，现有数字主要来自 Jack Poulson（Tech Inquiry）的调查。

### Cited Findings

| 日期 | 客户 | 项目 | 合同载体/类型 | 金额（base/ceiling） | 期限 | 范围 | 状态 | Maven专属 | 来源 |
|---|---|---|---|---|---|---|---|---|---|
| 2017–2018（具体日期未公开） | OSD / AWCFT（经 ECS Federal） | Project Maven，Google 分包 | 分包，经 ECS Federal | Google 高管对内称"只有约 900 万美元"（Diane Greene，据 NYT）；泄露邮件写的是"总交易 2500–3000 万美元，其中 1500 万美元在 18 个月内归 Google"，并称"项目扩大后预算为每年 2.5 亿美元" | 约 18 个月；Google 于 2018-06 宣布 2019 年合同到期后不再续约 | 无人机全动态视频（FMV）目标检测 AI | 已终止（2019 年到期不续） | Y | [The Intercept 2018-05-31](https://theintercept.com/2018/05/31/google-leaked-emails-drone-ai-pentagon-lucrative/); [The Intercept 2018-06-01](https://theintercept.com/2018/06/01/google-drone-ai-project-maven-contract-renew/); [VentureBeat](https://venturebeat.com/business/google-expected-to-rake-in-250-million-from-ai-drone-research); [Gizmodo](https://gizmodo.com/the-pentagons-controversial-drone-ai-imaging-project-ex-1826046321) |
| 约 2018–2019 起 | DoD（经 ECS Federal） | "Pavement"（Maven 代号） | ECS Federal 主合同（ARL BAA 渠道） | 1.42 亿美元；另有关联的 ECS 合同 5,225 万美元（SUNet 开源数据聚合） | 不详 | 无人机与卫星监视 AI | 记录已从联邦采购数据库删除；OSD 发言人援引 FAR 4.606(c)(d) | Y | [Poulson：1.42 亿合同被抹除](https://jackpoulson.substack.com/p/142-million-ai-drone-warfare-contract); [Poulson：五角大楼确认删除](https://jackpoulson.substack.com/p/pentagon-confirms-erasure-of-project) |
| 2019 起（Microsoft）/ 2020 起（AWS） | DoD（经 ECS Federal） | Maven 相关分包（分包合同未明确写 Maven） | 分包，隶属 ECS 的 3 份总合同 | Microsoft 3,000 万美元；AWS 2,000 万美元（合计约 5,000 万美元） | 不详 | 云计算与 AI 支持 | 已完成或不详 | P | [Forbes 2021-09-08](https://www.forbes.com/sites/thomasbrewster/2021/09/08/project-maven-amazon-and-microsoft-get-50-million-in-pentagon-drone-surveillance-contracts-after-google/); [ITPro](https://www.itpro.com/business-strategy/public-sector/360824/amazon-microsoft-google-project-maven-dod-contracts) |
| 2017–2021 | DoD（经 ECS Federal） | Clarifai Maven 分包 | 分包 | 合计超过 2,500 万美元，其中一项人脸识别任务 560 万美元 | 不详 | 计算机视觉、人脸识别 | 不详 | Y/P | [Forbes 2021-09-08（Maven 初创公司）](https://www.forbes.com/sites/thomasbrewster/2021/09/08/project-maven-startups-backed-by-google-peter-thiel-eric-schmidt-and-james-murdoch-are-building-ai-and-facial-recognition-surveillance-tools-for-the-defense-department/); [Fast Company](https://www.fastcompany.com/90277470/despite-a-surge-of-tech-activism-clarifai-plans-to-push-further-into-government-work) |
| FY2020 | Army（ACC-APG），授予 ECS Federal | 合同 W911QX20C0023（USASpending 可查，是否属于 Maven 未经证实） | 合同 | 金额未检索到 | — | — | — | 待核 | [USASpending](https://www.usaspending.gov/award/CONT_AWD_W911QX20C0023_9700_-NONE-_-NONE-) |
| 2024-07-29 | NGA | Scale AI "Data Labeling Services Bridge"（Maven 数据标注过渡合同），合同号 HM047624C0047 | 固定价格（FFP），1 年 | 2,400 万美元；NGA 另一条公告写的是"修改 2,400 万美元后总值 1.3 亿美元"，两者关系不明，存在冲突 | 1 年 | Maven 计算机视觉训练数据标注 | 已到期；Scale 竞标后续 SEQUOIA 落败 | Y | [NGA 合同公告](https://www.nga.mil/news/Contract_Announcements.html); [Defense Briefing](https://defensebriefing.co/intel/companies/scale-ai) |
| 2025-09 选定；2025-11-24 公布 | NGA | SEQUOIA，AI/ML 数据标注即服务，授予 Enabled Intelligence | 单一授标 IDIQ，订货期 7 年 | 上限 7.08 亿美元（Payload 写作 7.083 亿） | 7 年 | Maven 及 DoD/IC 的 GEOINT 计算机视觉标注（目标检测、跟踪、分类）；合作方为 BAE、Vantor、Whiteboard Federal | 执行中。Scale AI 先向 GAO 抗议被驳回（2026 年 1 月下旬），再起诉至联邦索赔法院，法院未推翻授标 | Y | [Breaking Defense](https://breakingdefense.com/2025/11/startup-enabled-intelligence-nabs-ngas-708-million-ai-training-contract/); [Enabled Intelligence 新闻稿](https://enabledintelligence.net/press/enabled-intelligence-awarded-ngas-708-million-sequoia-contract-for-ai-ml-data-labeling-as-a-service/); [GovConWire](https://www.govconwire.com/articles/enabled-intelligence-nga-sequoia-data-labeling); [Payload](https://payloadspace.com/enabled-intelligence-bags-708m-nga-contract/); [OrangeSlices：Scale 抗议失败](https://orangeslices.ai/protest-filed-ii-ml-data-labeling/); [NGA RFP 新闻稿 24-12](https://www.nga.mil/assets/files/24-12_Release_Sequoia.pdf) |

- 背景：Maven 合同渠道之一是"ARL 基础与应用科学研究合同"（BAA）——[FedSavvy](https://www.fedsavvystrategies.com/competitor-highlights-ecs-federal/)。ASGN 于 2018 年 4 月以 7.75 亿美元收购 ECS Federal——[FedSavvy](https://www.fedsavvystrategies.com/competitor-highlights-ecs-federal/)。
- 竞争者：泄露邮件显示，Google 当年与 Amazon、IBM、Microsoft 竞争 Maven 工作——[The Intercept](https://theintercept.com/2018/05/31/google-leaked-emails-drone-ai-pentagon-lucrative/)。
- Wikipedia 列出的 Maven 承包商包括 Palantir、Anduril、AWS、Anthropic，并注明 Anthropic 于 2026 年退出——[Wikipedia](https://en.wikipedia.org/wiki/Project_Maven)（二手来源，仅作背景）。
- 2023 年 NGA 发布征询，评估 Maven 的 AI/ML 供应链风险，理由是对主承包商及下级供应商的可见度不足——[Breaking Defense 2023-04](https://breakingdefense.com/2023/04/nga-wants-to-asses-ai-ml-supply-chain-risks-for-project-maven/)。

### Inferences
- Google 的数字分三层：约 900 万美元是对外口径的初始合同额；1,500 万美元是 18 个月的内部预期；2.5 亿美元是整个 Maven 项目的年度预算展望，不是 Google 的合同额。章节中把"Google 最高 2.5 亿美元"写成合同上限是错误的，应写作"项目年度预算预期"。
- 由于 Pavement 等记录被删除，2017–2021 年 Maven 实际支出的公开可核查部分很可能明显低于真实规模。

### Gaps
- ECS Federal 各份 Maven 合同的原始授予日期和上限均未找到官方授标公告（USASpending/SAM 记录已被删除）。
- CrowdAI 的 Maven 合同：搜索没有找到任何可靠来源。
- Anduril 在 Maven 下的具体合同金额，以及 Microsoft/AWS 分包的具体起止日期：未找到。
- Scale AI "2,400 万美元 vs 总值 1.3 亿美元"的关系没有解决（可能是此前 Maven 标注合同的累计值，属推测）。

## Q2. Project Maven / NGA Maven 各财年经费是多少？

### Takeaway
Maven 早期经费由国会大幅加码：FY2018 拨款 1.31 亿美元（请求仅约 3,100 万），FY2020 为 2.21 亿，FY2021 为 2.5 亿。2023 年 Maven 的 GEOINT 部分移交 NGA，并于 2023-11-07 成为 program of record。从 FY2025 起经费并入 CDAO 预算项目编码，公开预算中再无 Maven 单列数字。FY2027 申请约 23 亿美元用于"Maven + Joint Fires Network"（交付 CJADC2）。

### Cited Findings

| 财年 | 金额 | 性质 | 来源 |
|---|---|---|---|
| FY2018 | 1.31 亿美元拨款（DoD 请求约 3,100 万） | 国会拨款（AWCFT/Project Maven） | [Inside Defense](https://insidedefense.com/node/194699) |
| FY2020 | 2.21 亿美元 | 国会拨款 | [DefenseScoop 2024-03-14](https://defensescoop.com/2024/03/14/project-maven-fiscal-2025-budget-still-evolving/)；[Defense Daily：NDAA 授权 2.5 亿](https://defensedaily.com/ndaa-conference-bill-authorizes-250-million-project-maven/advanced-transformational-technology) |
| FY2021 | 2.5 亿美元（按请求拨付，项目改名为 "Algorithmic Warfare Cross Functional Teams Software Pilot Program"） | 国会拨款/授权 | 同上 |
| FY2022–FY2025（早期 FYDP 规划） | FY22 2.52 亿；FY23 1.20 亿；FY24 1.21 亿；FY25 1.22 亿 | 规划值，非实际拨款 | [DefenseScoop 2024-03-14](https://defensescoop.com/2024/03/14/project-maven-fiscal-2025-budget-still-evolving/) |
| FY2025 | 原 CDAO 项目编码在 FY2024 后不再延续；相关 PE 0604122D8Z（JADC2 开发与试验）为 2.23 亿美元，这是 CDAO 汇总线，不等于 Maven 预算 | 预算重组 | 同上 |
| 2023-11-07 | Maven（GEOINT 部分）在 NGA 成为 program of record | 项目地位变化 | [Wikipedia](https://en.wikipedia.org/wiki/Project_Maven)；[Military.com 2026-03-22](https://365.military.com/feature/2026/03/22/pentagon-expands-palantirs-role-ai-contract.html) |
| FY2027 申请 | 约 23 亿美元，用于 "Maven 和 Joint Fires Network"，交付 CJADC2。DefenseScoop 的拆分：其中超过 15 亿美元用于 "Joint Force AI-Enabled Headquarters initiative"，扩大 MSS 用户访问；6,000 万美元用于 Virtual Joint Operations Center | 总统预算请求 | [FY2027 Budget Overview Book（comptroller.war.gov）](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2027/FY2027_Budget_Request_Overview_Book.pdf)；[DefenseScoop 2026-05-28](https://defensescoop.com/2026/05/28/dod-fy27-budget-cjadc2-maven-smart-system-palantir/)；[SpaceNews](https://spacenews.com/pentagon-seeks-2-3-billion-for-maven-ai-battlefield-system/) |

- 冲突：ISS Tracker 与 Venture Atlas 把 23 亿美元描述为"未来五年"的总额；DefenseScoop 和预算概览则描述为 FY2027 单年申请（超过 20 亿美元）——[ISS Tracker](https://isstracker.pl/en/news/pentagon-poszukuje-23-miliarda-dolarow-na-system-pola-bitwy-maven-ai,x4x5P)；[DefenseScoop](https://defensescoop.com/2026/05/28/dod-fy27-budget-cjadc2-maven-smart-system-palantir/)。以官方预算概览为准，口径为 FY2027 单年。

### Inferences
- 写图表时应把 FY2018–FY2021 的实际拨款与 FY2022–FY2025 的 FYDP 规划值区分开。FY2027 的 23 亿美元包含 Joint Fires Network，不能全部计为 Palantir MSS 收入。

### Gaps
- FY2019 Maven 拨款数字未检索到。
- FY2022–FY2026 的 Maven/NGA Maven 实际拨款没有单列（NGA 属情报预算，涉密）。
- FY2026 MSS 的具体请求额未找到。

## Q3. Palantir Maven Smart System（MSS）合同链条（2024–2026）

### Takeaway
MSS 的主合同是 Army ACC-APG 的 W911QX-24-D-0012。2024-05 授予时上限 4.8 亿美元，2025-05 的第 P00005 号修改追加 7.95 亿美元，上限升至约 12.75–13 亿美元（期限至 2029-05-28）。此外还有 2024-09 ARL 的 9,980 万美元扩展合同、2025-05 NGA 的 2,800 万美元合同、2025-08 海军陆战队的企业许可。2026-03-09 Feinberg 备忘录指示：MSS 在 FY2026 结束前转为全 DoD 的 program of record，监管从 NGA 移交 CDAO，所有 MSS 合同改由 Army 企业协议（EA）载体执行。

### Cited Findings

| 日期 | 客户 | 项目 | 合同载体/类型 | 金额（base/ceiling） | 期限 | 范围 | 状态 | Maven专属 | 来源 |
|---|---|---|---|---|---|---|---|---|---|
| 2024-05-29 | Army ACC-APG（为 DoD/COCOM 采购） | MSS 原型（Maven Smart System prototype） | IDIQ（W911QX-24-D-0012），固定价格（FFP），单一投标人 | 上限 4.8 亿美元；工作地点和资金"随每笔订单确定" | 至 2029-05-28（约 5 年） | 扩展至 5 个作战司令部（CENTCOM、EUCOM、INDOPACOM、NORTHCOM、TRANSCOM）的数千名用户 | 执行中（后被修改） | Y | [DefenseScoop 2024-05-29](https://defensescoop.com/2024/05/29/palantir-480-million-army-contract-maven-smart-system-artificial-intelligence); [Defense News](https://www.defensenews.com/artificial-intelligence/2024/05/30/palantir-wins-contract-to-expand-access-to-project-maven-ai-tools/); [MeriTalk](https://www.meritalk.com/articles/army-awards-480m-contract-for-maven-prototype/) |
| 2024-09（Bloomberg 2024-09-19 报道） | Army DEVCOM ARL | MSS 扩展至全部军种（Army、Air Force、Space Force、Navy、USMC） | FFP 合同，5 年 | 9,980 万美元（约 1 亿美元） | 5 年 | 新增数万名军种用户 | 执行中 | Y | [GovConWire](https://www.govconwire.com/2024/09/palantir-receives-100m-army-contract-for-maven-smart-system-expansion/); [Bloomberg](https://www.bloomberg.com/news/articles/2024-09-19/palantir-wins-100-million-us-contract-for-ai-targeting-tech); [Palantir/BusinessWire](https://www.businesswire.com/news/home/20240920746094/en/Palantir-Expands-Maven-Smart-System-AIML-Capabilities-to-Military-Services); [Inside Defense](https://insidedefense.com/daily-news/army-awards-palantir-998m-deliver-maven-smart-system-prototype-across-services) |
| 2025-05-20（2025-05-21 公布） | Army ACC-APG | MSS 软件许可 | 修改 P00005，针对 W911QX-24-D-0012 | +7.95 亿美元，上限升至约 12.75 亿美元（各方表述为"近 12.8 亿"或"约 13 亿"） | 至 2029-05-28 | 新增软件许可，非新增范围；依据是 COCOM 需求激增 | 执行中 | Y | [GlobalSecurity 转载 DoD 合同公告](https://www.globalsecurity.org/military/library/news/2025/05/dod-contracts_4194643.htm); [ClearanceJobs](https://news.clearancejobs.com/2025/05/21/army-awards-palantir-nearly-800m-for-maven-smart-system-software/); [ExecutiveBiz](https://www.executivebiz.com/articles/palantir-usg-795-million-army-contract-maven-smart-system-software-license); [Inside Defense](https://insidedefense.com/node/224187) |
| 2025-05（NGA 局长 Whitworth 于 2025-05-21 GEOINT 大会披露） | NGA | 扩大 NGA 分析员的 MSS 访问 | 合同 | 2,800 万美元 | 不详 | NGA 分析员 MSS 许可 | 执行中 | Y | [MeriTalk](https://www.meritalk.com/articles/nga-expands-maven-ai-system-in-year-of-ai-whitworth-says/) |
| 2025-08-15 敲定（2025-09-10 公告；MARADMIN 424/25 于 2025-09-11 发布） | USMC（与 DIU、CDAO、ARL 合作） | MSS 海军陆战队企业许可 | 企业许可（经 CDAO/DIU/ARL 渠道） | 未披露 | 不详 | 在 SIPRNet（IL-6 云）上对 FMF 至支援机构无限量访问 | 执行中 | Y | [Marines.mil 新闻稿](https://www.marines.mil/News/Press-Releases/Press-Release-Display/Article/4305728/marine-corps-partners-with-chief-digital-and-artificial-intelligence-office-and/); [MARADMIN](https://www.marines.mil/News/Messages/Messages-Display/Article/4299351/announcement-of-maven-smart-system-licensing-for-marine-corps/); [DefenseScoop 2025-09-10](https://defensescoop.com/2025/09/10/palantir-maven-smart-system-mss-marine-corps/); [DefenseScoop 2025-09-12](https://defensescoop.com/2025/09/12/marine-corps-maradmin-maven-smart-system-mss-palantir-rollout/) |
| 2026-03-09 | DepSecDef Feinberg 备忘录 | MSS 转为 DoD program of record | 政策指令，非合同 | —（带来专门预算线并纳入 FYDP） | 期限：FY2026 结束前（2026-09-30） | 监管由 NGA 移交 CDAO 新设的项目办公室；所有 MSS 合同转入现有 Army EA 载体；未来对 Palantir 的合同行动由 Army 负责 | 已发布；截至 2026-10 未检索到"正式完成转制"的公告 | Y | [DefenseScoop 2026-04-03](https://defensescoop.com/2026/04/03/palantir-maven-feinberg-directive/); [DefenseScoop 2026-04-15](https://defensescoop.com/2026/04/15/palantir-maven-smart-system-pentagon-program-transition-feinberg/); [GovConWire](https://www.govconwire.com/articles/pentagon-palantir-maven-ai-program-of-record) |
| 2026-08（任命） | DoD/CDAO | 任命新的 MSS 项目主任 | 人事 | — | — | 推动 C2 集成 | — | Y | [DefenseScoop 2026-08-05](https://defensescoop.com/2026/08/05/pentagon-appoints-new-maven-smart-system-program-director/) |
| 2026-08-25/26（未证实） | Army PEO IEW&S（据报道） | MSS 扩展 | 不详 | "最高 6.18 亿美元、5 年"（仅见单一聚合站及 Eastern Herald） | 5 年 | MSS 扩展 | 未证实；可能与 2024-12 Army Vantage 的 6.189 亿美元混淆 | Y? | [Govly](https://app.govly.com/public/signals/177815); [Eastern Herald](https://easternherald.com/2026/08/27/palantir-pltr-stock-today-august-26-2026/) |

- 用户规模：截至 2026-09，MSS 用户超过 10 万（DefenseScoop 2026-09-22，正值伊朗冲突期间）——[DefenseScoop](https://defensescoop.com/2026/09/22/maven-smart-system-ai-james-mazol-cameron-stanley-defensetalks/)；另有来源称 2026-03 有超过 2 万名活跃军方用户——[Govly 汇总](https://app.govly.com/public/signals/177815)。两者口径不同（注册用户 vs 活跃用户），存在冲突。
- 另一来源称上限"提高到 10 亿美元并扩展到超过 10 万名用户"——[Industrial Base Alpha](https://industrialbasealpha.com/article/palantir-maven-smart-system-expands-to-100k-defense-users-with-1b-ceiling)，与 12.75/13 亿美元冲突，可靠性低。
- 2024-05 合同的阶段定性也有冲突：合同名称为 "prototype"，MeriTalk 称其开启原型阶段，Palantir（Shannon Clark）则称"从原型走向生产"——[MeriTalk](https://www.meritalk.com/articles/army-awards-480m-contract-for-maven-prototype/)；[Defense News](https://www.defensenews.com/artificial-intelligence/2024/05/30/palantir-wins-contract-to-expand-access-to-project-maven-ai-tools/)。
- 有报道称 2025-04 时美方 Maven 版本"5 年合同价值近 1 亿美元"——[DefenseScoop 2025-04-14](https://defensescoop.com/2025/04/14/nato-palantir-maven-smart-system-contract/)（可能指 ARL 的 9,980 万合同），属于引用口径差异。

### Inferences
- MSS 可汇总的已知上限：W911QX-24-D-0012 约 12.75 亿 + ARL 9,980 万 + NGA 2,800 万 ≈ 14 亿美元（不含 USMC 未披露金额，也不含未证实的 6.18 亿）。这是上限累加，不代表实际拨付。
- Feinberg 备忘录之后，MSS 的新采购将记在 Army EA（上限 100 亿美元）之下。2026 年 9 月之后的新 MSS 授标可能不再以独立合同公告出现，追踪难度会上升。

### Gaps
- W911QX-24-D-0012 下各订单的实际拨付额未找到（可查 USASpending/FPDS，但本次无法抓取页面）。
- 2026 年 8 月 6.18 亿美元扩展没有官方 DoD 合同公告佐证。
- MSS 是否已在 2026-09-30 前正式完成 program of record 转制：未见公告。

## Q4. MSS 及 Palantir 在盟国（NATO、英国等）的合同

### Takeaway
NATO NCIA 于 2025-03-25 签约采购 "MSS NATO"，供盟军作战司令部（ACO/SHAPE）使用，金额未披露，从需求到授标仅 6 个月。英国 MoD 于 2025-09-18 宣布与 Palantir 建立战略伙伴关系：五年内"最高 7.5 亿英镑"的机会或合同额（取代原 3 年 7,500 万英镑的协议），另有 Palantir 承诺的 15 亿英镑对英投资（这是公司投资，不是政府采购）。未找到 2025 年 12 月正式签署 7.5 亿英镑合同的证据。

### Cited Findings

| 日期 | 客户 | 项目 | 类型 | 金额 | 期限 | 范围 | 状态 | Maven专属 | 来源 |
|---|---|---|---|---|---|---|---|---|---|
| 2025-03-25 签约（2025-04-14 公布） | NATO NCIA，用于 ACO | Maven Smart System NATO（MSS NATO） | 采购合同 | 未披露 | 不详 | 情报融合与目标定位、战场态势感知与规划、加速决策 | 执行中 | Y | [DefenseScoop 2025-04-14](https://defensescoop.com/2025/04/14/nato-palantir-maven-smart-system-contract/); [DSEI](https://www.dsei.co.uk/sponsored-news/nato-acquires-ai-enabled-warfighting-system-palantir) |
| 2025-09-18 | 英国 MoD | UK–Palantir 战略伙伴关系 | 伙伴关系框架；彭博称将于年底前敲定 5 年合同 | 最高 7.5 亿英镑机会额（MoD 表述）/ 5 年合同（彭博表述）；取代原 7,500 万英镑、3 年协议；Palantir 另承诺 2030 年前对英投资 15 亿英镑，并设伦敦欧洲防务总部（约 350 个岗位） | 5 年 | AI 驱动的目标定位、决策支持、军事规划；扶持英国国防中小企业 | 宣布；最终合同签署未证实 | P（目标定位能力与 MSS 同源，但官方未称 MSS） | [Bloomberg 2025-09-17](https://www.bloomberg.com/news/articles/2025-09-17/palantir-expands-uk-defense-deal-investments-amid-trump-visit); [Computing](https://www.computing.co.uk/news/2025/ai/uk-signs-defence-ai-partnership-palantir); [UKAuthority](https://www.ukauthority.com/articles/mod-partnership-with-palantir-targets-ai-innovation); [DSEI 新闻](https://www.dsei.co.uk/news/uk-announces-gbp15bn-partnership-palantir) |

- 欧洲渗透背景：Palantir 嵌入多国欧洲军队，德国有所保留——[Escudo Digital](https://www.escudodigital.com/en/defense/europe/palantir-embeds-across-european-militaries-nato-germany-holds-back.html)。
- 国际政府收入：2026 年 Q2 为 1.81 亿美元，同比增长 42%——[Palantir Q2 2026 8-K](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)。

### Inferences
- 7.5 亿英镑在 MoD 口径下是"机会或上限"，在 Karp 口径下是"投资"。章节写作时应写"最高 7.5 亿英镑（五年）"，并注明最终合同签署未证实。

### Gaps
- NATO MSS 合同金额及后续扩展（如 2026 年）未找到。
- 英国最终合同的签署日期和金额，以及是否明确使用 MSS：未找到。
- 其他盟国（如乌克兰、日本、澳大利亚）的 MSS 合同：本次未检索到可靠来源。

## Q5. Palantir 其他美国防务合同（非 MSS）

### Takeaway
Palantir 在 Maven 之外的防务合同主要包括：Army Vantage（2019 年 4.58 亿美元，2024 年后续 4.007 亿 / 上限 6.189 亿）、DCGS-A CD1（与 Raytheon 共享 8.76 亿）和 CD2（2020 年与 BAE 共享 8.23 亿 IDIQ，2021 年 Palantir 胜出数据织网）、TITAN（2024 年 1.784 亿美元 OTA）、ARL AI/ML（2020 年 9,120 万美元）、SOCOM（2016 年 2.22 亿、2021 年 1.11 亿、2023 年 4.63 亿）、太空军（2.178 亿交付令、1.103 亿延期）、海军 ShipOS（2025-12，最高 4.48 亿），最终在 2025-07-31 汇总为 Army EA（10 年、上限 100 亿美元，整合 75 份合同）。

### Cited Findings

| 日期 | 客户 | 项目 | 载体/类型 | 金额（base/ceiling） | 期限 | 范围 | 状态 | Maven专属 | 来源 |
|---|---|---|---|---|---|---|---|---|---|
| 2016-05 | SOCOM | All Source Information Fusion 软件许可 | 单一来源 | 上限 2.22 亿美元（授予时拨付 500 万维护费） | 不详 | 情报融合软件 | 已完成 | N | [Washington Technology](https://washingtontechnology.com/articles/2016/05/26/palantir-socom.aspx) |
| 2018-03-09（C4ISRNet 所载 Army 声明；Bloomberg Government 称 2019-03，存在冲突） | Army | DCGS-A Capability Drop 1（与 Raytheon 共享） | 多授标合同 | 上限 8.76 亿美元 | 10 年 | 商业情报分析软件 | 已完成或演进 | P（情报/目标链） | [C4ISRNet 2018-03-09](https://c4isrnet.com/land/2018/03/09/army-awards-contract-to-buy-commercial-solutions-to-fix-troubled-intel-analysis-framework); [Defense News 2019-03-29](https://www.defensenews.com/land/2019/03/29/palantir-who-successfully-sued-the-army-just-won-a-major-army-contract/) |
| 2019-12 | Army PEO EIS | Army Vantage 生产合同 | 1 个基础年 + 3 个选项年 | 上限 4.58 亿美元；基础年约 1.10 亿，2020-12 选项年 1.138 亿，第二选项年 1.163 亿，2023-12 延期 1.15 亿 | 4 年及延期 | 陆军企业数据平台 | 已被后续合同接替 | N | [TipRanks](https://www.tipranks.com/news/palantir-u-s-army-partnership-continues-for-third-consecutive-year); [Daily Palantir：1.15 亿延期](https://dailypalantir.substack.com/p/palantir-wins-a-115m-contract-extension) |
| 2020-02 | Army | DCGS-A Capability Drop 2（与 BAE 共享） | 多授标 IDIQ（FFP），任务订单竞争 | 上限 8.23 亿美元 | 7 年 | 情报数据平台 | 2021 年下选 Palantir | P | [Washington Technology 2020-02-26](https://washingtontechnology.com/articles/2020/02/26/palantir-bae-army-dcgs.aspx); [BGOV](https://about.bgov.com/?p=25184) |
| 2020-10-01/02 | Army Research Lab | AI/ML 研发（Foundry/Gotham） | 2 年合同 | 9,120 万美元 | 至 2022-09-28 | AI 数据整合与模型训练，面向 COCOM | 已完成；后续有 9,990 万美元 2 年延续（日期未查到） | P（Maven 前身性质） | [Datanami](https://www.datanami.com/this-just-in/u-s-army-research-lab-selects-palantir-technologies-inc-for-91m-artificial-intelligence-and-machine-learning-development/); [BusinessWire 2020-10-01](https://www.businesswire.com/news/home/20201001005334/en); [ICN](https://intelligencecommunitynews.com/palantir-wins-arl-ai-ml-contract/) |
| 2021-05 | SOCOM | Mission Command Platform | 2 年合同（含选项） | 1.11 亿美元（HigherGov 记为 1.12 亿），授予时执行 5,250 万 | 2 年 | 任务指挥 | 已完成 | N | [ICN](https://intelligencecommunitynews.com/palantir-wins-111m-ussocom-contract/); [HigherGov](https://highergov.com/news/palantir-awarded-463m-ussocom-ai-contract-1627533) |
| 2021-10-05/06 | Army | DCGS-A CD2 情报数据织网与分析（Gotham，跨密级） | CD2 IDIQ 下选（Breaking Defense 标题称"8.23 亿美元合同"） | 8.23 亿美元（与 2020 年 CD2 上限相同，疑为同一载体，存在重复计算风险） | 不详 | 情报数据织网 | 执行中或已演进 | P | [Breaking Defense](https://breakingdefense.com/2021/10/army-awards-palantir-823m-contract-for-enterprise-data-fabric/); [C4ISRNet](https://www.c4isrnet.com/battlefield-tech/2021/10/06/palantir-scores-us-army-contract-to-build-out-intelligence-data-fabric/) |
| 2023（日期待核） | SOCOM PEO SOF Digital Applications | 企业能力（含 AI） | 5 年 | 上限 4.63 亿美元（约 9,000 万/年，此前年均 5,000–6,000 万） | 5 年 | 企业数据与 AI | 执行中 | N | [HigherGov](https://highergov.com/news/palantir-awarded-463m-ussocom-ai-contract-1627533); [Potomac Officers Club](https://potomacofficersclub.com/news/palantir-secures-463m-ussocom-contract-to-improve-decision-making-process) |
| 2023 | Space Force / SSC | Space C2 与 Mission Partner 数据即服务平台 | 单一来源 FFP | 约 3,280 万美元；2025 年修改追加 20,051,882 美元 | 不详 | 太空 C2 数据 | 执行中 | N | [Defense Daily](https://defensedaily.com/contract-awards/contract-award-palantir-usg-inc-palo-alto-california-20051882) |
| 日期待核（约 2024） | Space Force SSC | Space C2 数据平台交付令 | Data Software Services IDIQ（2023 年多授标，5 年约 9 亿美元）下的交付令 | 2.178 亿美元 | 不详 | 太空与空中多域作战数据同步 | 执行中 | N | [FedScoop](https://www.fedscoop.com/palantir-space-force-contract/); [AFCEA Signal](https://www.afcea.org/signal-media/air-force-awards-contract-space-command-and-control) |
| 2025-06 | Space Force | 云数据服务延期 | 合同延期 | 1.103 亿美元 | 不详 | 云数据服务 | 执行中 | N | 同上（FedScoop 检索摘要；具体 URL 为 [spacenews.com/?p=164108](https://spacenews.com/?p=164108)，待核） |
| 2024-03-06 | Army ACC-APG（PEO IEW&S） | TITAN 地面站 Phase 3 | OTA 原型协议 | 1.784 亿美元，10 套原型（5 Advanced + 5 Basic） | 24 个月 | 下一代 ISR 地面站，缩短传感器到射手时间；击败 RTX；合作方为 Northrop、L3Harris、Anduril | 交付中 | P（目标链，与 Maven 衔接） | [Army.mil](https://www.army.mil/article/274301/army_tactical_intelligence_targeting_access_node_titan_ground_station_prototype_award); [DefenseScoop](https://defensescoop.com/2024/03/06/palantir-army-titan-ground-station-award-178-million/); [Defense News](https://www.defensenews.com/artificial-intelligence/2024/03/06/army-chooses-palantir-to-build-next-generation-targeting-system) |
| 2024-12-18 | Army | Army Vantage 后续（单一来源再竞标） | 合同（含选项） | 4.007 亿美元（基础），上限约 6.189 亿美元 | 最长 4 年 | 陆军主数据平台 | 已被纳入 EA（推测） | N | [Defense News](https://www.defensenews.com/land/2024/12/18/us-army-extends-palantirs-contract-for-its-data-harnessing-platform/); [BGOV](https://news.bgov.com/bloomberg-government-news/palantir-extends-army-vantage-deal-with-618-9-million-contract); [GovConWire](https://www.govconwire.com/?p=331655) |
| 2025-07-18 | Army PEO C3N | NGC2 原型（4ID），Anduril 为主承包商 | OTA | 9,960 万美元（Palantir 份额未披露） | 11 个月 | Team Anduril：Palantir、Striveworks、Govini、Instant Connect、RII、Microsoft | 执行中 | P | [Breaking Defense](https://breakingdefense.com/2025/07/army-awards-team-anduril-nearly-100m-to-lead-ngc2-prototype-for-4th-infantry-division/); [Inside Defense](https://insidedefense.com/node/224724) |
| 2025-07-31（2025-08-01 公告） | Army | Palantir Enterprise Agreement（EA） | 企业协议 | 上限 100 亿美元（不承诺支出）；整合 75 份合同（15 份主合同 + 60 份分包），消除转售商加价，享受批量折扣；每 18–24 个月复评 | 10 年 | 商业软件与数据；2026 年起成为 MSS 采购载体 | 执行中 | P（2026 年起承载 MSS） | [Washington Technology](https://www.washingtontechnology.com/contracts/2025/08/palantir-signs-10b-enterprise-agreement-army/407153/); [CNBC](https://www.cnbc.com/2025/08/01/palantir-lands-10-billion-army-software-and-data-contract.html); [Defense One](https://www.defenseone.com/defense-systems/2025/08/armys-giant-data-deal-palantir-harbinger-service-cio/407174/); [Inside Defense](https://insidedefense.com/insider/army-merges-software-contracts-under-10-billion-deal-palantir) |
| 2025-12-10 | Navy（Maritime Industrial Base Program + NAVSEA） | ShipOS | 合同或伙伴关系（资金来自 Reconciliation Act） | 最高 4.48 亿美元 | 初始 2 年 | 在潜艇工业基地（2 家主要船厂、3 个造船厂、100 家供应商）部署 Foundry/AIP | 执行中 | N | [Breaking Defense](https://breakingdefense.com/2025/12/navy-palantir-unveil-shipos-in-a-bid-to-boost-nuclear-sub-production/); [BusinessWire](https://www.businesswire.com/news/home/20251210738739/en/U.S.-Navy-Partners-with-Palantir-to-Modernize-Shipbuilding-Supply-Chain-and-Accelerate-Shipbuilding); [The Register](https://www.theregister.com/2025/12/10/palantir_navy_448_million_contract/) |
| 2025-04（Reuters 报道）→ 2026-03 | MDA/Space Force（Golden Dome） | Golden Dome 软件或 C2 层 | 行业联盟；无确认的 Palantir 主合同 | 未披露（项目总估算 1,850 亿美元） | — | 指挥控制软件层（与 Anduril、SpaceX 合作） | 报道阶段 | N | [Defense One D Brief](https://www.defenseone.com/threats/2025/04/the-d-brief-april-17-2025/404643/); [GovConWire](https://www.govconwire.com/articles/anduril-palantir-golden-dome-software-wash100); [Yahoo/Reuters](https://finance.yahoo.com/sectors/technology/articles/anduril-palantir-developing-golden-dome-233807794.html) |

- 冲突：Marine Insight 把 ShipOS 金额写成 "£448m"，其余来源均为 4.48 亿美元——[Marine Insight](https://www.marineinsight.com/us-navy-palantir-begin-448m-ship-os-ai-programme-to-modernise-shipbuilding/)。
- DCGS-A 金额冲突：8.23 亿美元对应的是 CD2（2020 年，与 BAE 共享），不是 CD1；CD1 是 8.76 亿美元（与 Raytheon 共享）——[Washington Technology](https://washingtontechnology.com/articles/2020/02/26/palantir-bae-army-dcgs.aspx)。

### Inferences
- Army EA 整合了 Vantage、ARL、MSS 等众多存量合同。2025-08 之后，Palantir 陆军业务的增量主要以 EA 下的订单形式出现，很难再与旧合同逐项对应。图表中不应把 EA 的 100 亿美元与被整合合同的上限相加。
- 2.178 亿美元太空军交付令的日期未检索到确切值（可能为 2024 年），需要回查原始公告。

### Gaps
- Air Force（非 SSC）、Coast Guard、CDAO 直接合同（如 Open DAGIR、AI 加速类载体）：本次没有找到可靠的具体金额。
- "Army Data Platform"作为独立合同名称没有检索到（可能即 Vantage 或 DCGS-A CD2 数据织网）。
- ICE/DHS、NHS 等非防务背景合同未检索（任务要求仅作简要背景）。
- 2023 年 SOCOM 4.63 亿美元合同的具体月份未确认。

## Q6. Palantir 美国政府收入年度汇总（用于作图）

### Takeaway
美国政府收入：2022 年 8.263 亿 → 2023 年 9.212 亿（+11.5%）→ 2024 年约 12 亿 → 2025 年 18.55 亿（+55%）→ 2026 年 H1 约 14.96 亿（Q1 6.87 亿 + Q2 8.09 亿，同比 +84%/+90%）。2019–2021 年 10-K 只披露政府收入总额（含国际），没有直接给出美国单列数字。

### Cited Findings

| 年份 | 美国政府收入 | 政府总收入（含国际） | 说明 | 来源 |
|---|---|---|---|---|
| 2019 | 未单列 | 约 3.44 亿美元（推算：2020 年增量 2.647 亿 ÷ 77%）；S-1 称政府占 2019 年收入 47%（约 7.426 亿 × 47% ≈ 3.49 亿） | 推算值 | [FY2020 10-K](https://www.sec.gov/Archives/edgar/data/1321655/000119312521060650/d65934d10k.htm); [GovTech](https://www.govtech.com/biz/Palantir-Reveals-Business-Details-Before-Going-Public.html) |
| 2020 | 未单列 | 约 6.09 亿美元（推算：同比 +2.647 亿、+77%） | 推算值 | [FY2020 10-K](https://www.sec.gov/Archives/edgar/data/1321655/000119312521060650/d65934d10k.htm) |
| 2021 | 约 6.77 亿美元（推算：2022 年 8.263 亿 ÷ 1.22） | 8.974 亿美元（+47%） | 美国数据为推算 | [FY2021 10-K](https://www.sec.gov/Archives/edgar/data/1321655/000119312522050913/d273589d10k.htm); [FY2022 Q4 新闻稿](https://www.sec.gov/Archives/edgar/data/1321655/000132165523000005/a2022q4ex991pressrelease.htm) |
| 2022 | 8.263 亿美元（+22%） | 10.718 亿美元 | 公司披露 | [FY2023 10-K](https://www.sec.gov/Archives/edgar/data/1321655/000132165524000022/pltr-20231231.htm); [FY2022 Q4 新闻稿](https://www.sec.gov/Archives/edgar/data/1321655/000132165523000005/a2022q4ex991pressrelease.htm) |
| 2023 | 9.212 亿美元 | 12.222 亿美元 | 公司披露 | [FY2023 10-K](https://www.sec.gov/Archives/edgar/data/1321655/000132165524000022/pltr-20231231.htm) |
| 2024 | 约 12 亿美元（10-K 原文 "$1.2 billion"；按 2025 年 +55% 反推约 11.97 亿） | 15.696 亿美元 | 公司披露 | [FY2024 10-K](https://www.sec.gov/Archives/edgar/data/1321655/000132165525000022/pltr-20241231.htm) |
| 2025 | 18.55 亿美元（+55%）；分季度：Q1 3.73 亿，Q2 4.26 亿，Q3 约 4.86 亿（推算），Q4 5.70 亿（同比 +66%） | 未检索 | 公司披露；Q3 为推算 | [Q4 2025 投资者演示](https://investors.palantir.com/files/Palantir%20-%20Q4%202025%20Investor%20Presentation.pdf); [Q4 2025 新闻稿](https://www.businesswire.com/news/home/20260201154946/en/Palantir-Reports-Q4-2025-U.S.-Comm-Revenue-Growth-of-137-YY-and-Revenue-Growth-of-70-YY-Issues-FY-2026-Revenue-Guidance-of-61-YY-and-U.S.-Comm-Revenue-Guidance-of-115-YY-Crushing-Consensus-Expectati) |
| 2026 H1 | Q1 6.87 亿（+84%）；Q2 8.09 亿（+90%，环比 +18%）；H1 合计约 14.96 亿（10-Q 写作 "$1.5 billion"） | Q2 政府总收入 9.90 亿（+79%）；Q2 国际政府 1.81 亿（+42%） | 公司披露 | [Q1 2026 8-K](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000026/a2026q1ex991pressrelease.htm); [Q2 2026 8-K](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm); [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000041/pltr-20260630.htm) |

- 公司指引：2026 年全年总收入指引上调至 81.5–81.58 亿美元（约 +80–82%），未单列美国政府收入指引——[Q2 2026 新闻稿](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)。
- 威廉布莱尔认为 MSS 正"冲刺" 10 亿美元 ARR（二手转述）——[Bitget 转载](https://www.bitget.com/news/detail/12560605738051)。仅作分析师观点。

### Inferences
- 2025 年美国政府收入增长（+55%）正好与 MSS 上限扩大（2025-05）、Army EA（2025-07）和 USMC 许可（2025-08）同期；2026 年 H1 增速加快到 84–90%，与 Feinberg 备忘录及伊朗冲突期间用户激增在时间上吻合（相关性，不是已证实的因果）。
- 作图建议：2022–2026H1 用公司披露的美国政府收入；2019–2021 用政府总收入（虚线标注含国际）或推算值，并注明口径。

### Gaps
- 2019–2021 年美国政府收入的官方单列数字（需查 10-K 地理分部附注，本次无法抓取）。
- 2025 年 Q3 的官方数字（目前为推算值）。
- 2026 年 Q3 财报（预计 2026 年 11 月初发布）尚未发布，超出本次时间窗口。
