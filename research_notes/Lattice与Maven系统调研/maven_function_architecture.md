# Maven Smart System (MSS) 与 Project Maven / NGA Maven AI 流水线：功能设计与技术架构（截至 2026 年 10 月）

> 研究方法说明：本轮调研环境中，WebFetch 和 curl 访问外部站点均被出口代理拒绝（DNS/CONNECT 403），因此以下所有发现都来自 WebSearch 返回的结果摘要，未能逐页核读原文。来自 CSIS、DefenseScoop、Breaking Defense、NATO/SHAPE、Palantir、NGA、GAO、CSET 的内容可信度较高；博客、Substack 和聚合站点（cleoops、arturmarkus、abhs.in、cybershafarat、battlepolicy 等）已标为低可信。来源标签含义：**[事实]** 为官方或可靠媒体证实的内容；**[厂商宣称]** 为 Palantir/Anduril 等厂商的表述；**[分析/推断]** 为分析人士或本笔记作者的推断。

## Q1. MSS 有哪些功能模块（数据融合、CV 检测、COP、目标工作流/kill chain、COA、武器-目标配对、BDA、LLM/AIP、跨梯队与联盟协同）？

### Takeaway
MSS 是一个基于 Palantir 的"传感器到射手"决策支持平台，主要包括以下几部分：
- 多源情报融合，2024 年 CENTCOM 部署时接入 179 个数据源；
- 外部 CV 模型的检测结果作为对象写入本体；
- 地图式共用作战图（COP）；
- Target Workbench 看板式目标工作流（No-Strike List 集成、按时间/距离/燃油比较打击资产、向 AFATDS 等火力系统流转）；
- AIP 自然语言代理和 LLM（含 Anthropic Claude）用于检索、优先排序和 COA 生成。

武器-目标配对的算法细节、BDA 模块细节和 FMV 接入方式都没有权威公开描述。

### Cited Findings
**整体定位与数据融合**
- [事实] NATO 对 MSS NATO 的描述是"AI-enabled warfighting system"：用 LLM、生成式 AI 和机器学习做情报融合、目标定位（targeting）、战场态势感知、作战计划和加速决策。它把来自多个来源（涉密和公开）的结构化与非结构化数据汇入一个统一、可搜索的平台，开放架构可接入第三方 AI 模型、仿真工具和应用。— [SHAPE/NATO 新闻稿](https://shape.nato.int/news-releases/nato-acquires-aienabled-warfighting-system-)；[Breaking Defense 2025-04](https://breakingdefense.com/2025/04/nato-picks-palantirs-maven-ai-for-military-planning-amid-trans-atlantic-tension/)
- [事实/智库] CSIS 报道，CENTCOM 2024 年的部署使用了 **179 个不同数据源**，业内人士称此后数量还在增加。卫星来源包括国家侦察卫星和商业 SAR（ICEYE、Capella Space），并接入信号情报（截获通信、电子辐射）。— [CSIS: What Is Maven Smart System](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do)（经搜索摘要转述）
- [二手/低可信] GlobalSecurity 称，按 Palantir 公开演示，MSS 接入了 150 多个数据源；截至 2026 年 3 月约有 2 万多活跃用户。— [GlobalSecurity](https://www.globalsecurity.org/intell/systems/maven.htm)
- [二手] 有描述称 COP 是一个三维地球视图，叠加卫星、无人机、SIGINT 和既有地图数据。也有描述说无人机执行任务时，位置数据和实时视频会实时回传到 Maven。— [spatialintelligence.ai "Inside Palantir's Maven Smart System"](https://www.spatialintelligence.ai/p/inside-palantirs-maven-smart-system)

**CV 检测、对象化与 AIP 代理**
- [厂商宣称] 在 Palantir 的 NATO Industry Day 示例中，一个外部 AI 系统（Safran.AI）生成的目标检测被导入 MSS，可以在 COP 中直接调查，也提供给 AIP Agents 使用。用户可以用自然语言提问，例如"Show me detections of Tu-22s"，代理随后查询由 12,000 个 Safran.AI 检测对象组成的 object set。— [Palantir Blog: Maven Smart System: Innovating for the Alliance](https://blog.palantir.com/maven-smart-system-innovating-for-the-alliance-5ebc31709eea)；[CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do)
- [事实/智库提醒] CSIS 指出，Palantir 2023 年的 "AIP for Defense" 演示展示的是计划中的未来能力和示意场景，不能等同于已部署的功能。— [CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do)

**目标工作流（Target Workbench / 看板 / F2T2EA）**
- [厂商宣称] Palantir Target Workbench 产品资料称，界面以类似 **Kanban 看板** 的形式组织，各列对应目标定位的各个阶段，阶段名称可以按单位自身流程术语定制；支持 **No-Strike List (NSL)** 集成。— [Palantir Target Workbench PDF](https://www.palantir.com/assets/xrfr7uokpv1b/1IqzwzpemtBSm98TNCczao/49bbc30cbec4d2d4d189ab27bd07376c/Palantir_Target_Workbench___1_.pdf)
- [事实/智库] CSIS 根据 DoD 演示描述的操作流程：操作员选中 AI 检测到的目标，按到达时间、距离、燃油等约束比较附近的打击资产，下令打击，再通过 ISR 跟踪打击效果（即 BDA）。— [CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do)
- [二手/低可信] 有分析称检测结果被"提名"上看板，再从看板为目标分派最合适的资产，优化因素包括 time-to-target、燃油、弹药和距离。传感器到射手链路被描述为：检测 → COA → 资产选择 → 打击 → BDA。还有说法称 Target Workbench 对目标排序后，把数据传给 AFATDS 等火力支援系统。— [cybershafarat 2026-03](https://cybershafarat.com/2026/03/16/analysis-of-ai-driven-command-and-control-maven-smart-system/)；[battlepolicy](https://www.battlepolicy.com/maven-smart-system/)
- [分析人士观点] Ben Van Roo 认为，在 assign-and-fire 环节，射击解算由 AFATDS 和弹道计算完成，LLM 在这部分几乎不起作用。— [Ben Van Roo, "Measuring the Machines that Kill"](https://benvanroo.substack.com/p/measuring-the-machines-that-kill)
- [事实] 美国海军陆战队把 MSS 定为跨多个作战司令部的标准"火力与效果集成平台"（fires and effects integration platform）。— [DefenseScoop 2025-09-12 (MARADMIN)](https://defensescoop.com/2025/09/12/marine-corps-maradmin-maven-smart-system-mss-palantir-rollout/)

**LLM / AIP / Claude**
- [多源报道，细节有争议] 多家媒体报道，Anthropic Claude 通过 Anthropic 与 Palantir 的合作（2024 年末）接入 Maven，用于目标优先级排序和分析。2026 年 2 月 28 日起的对伊朗作战中，美军借助 Maven（仍含 Claude）在 **头 24 小时打击了 1,000 多个目标**。— [Responsible Statecraft](https://responsiblestatecraft.org/ai-war-iran/)；[Arms Control Association 2026-05](https://www.armscontrol.org/act/2026-05/news/ai-plays-major-role-war-iran)；[CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do)
- [二手] Wikipedia 给出"10 天约 5,000 个目标"。— [Wikipedia: AI warfare](https://en.wikipedia.org/wiki/AI_warfare)
- [二手，引述华邮/Nature] Claude 提出了数百个目标，进行优先排序并给出精确坐标，再由人类指挥官批准。— [Strategy International 2026-04](https://strategyinternational.org/2026/04/06/publication258/)
- [事实/有冲突] Arms Control Association 报道，Anthropic 因拒绝支持自主武器和国内监控，被禁止向美军提供服务（被列为供应链风险），OpenAI 等公司接替其角色。但据报道 Palantir CEO Karp 表示 Claude 仍在目标系统中运行。— [ACA](https://www.armscontrol.org/act/2026-05/news/ai-plays-major-role-war-iran)
- [低可信，勿采信] 以下数字只出现在低可信站点："每天 3,000 个目标""11,000+ 次打击""25,000+ 账户"。— [cleoops](https://www.cleoops.com/blog/anthropic-claude-iran-targeting-maven)；[arturmarkus](https://www.arturmarkus.com/palantirs-maven-smart-system-running-on-anthropics-claude-powers-11000-us-strikes-in-iran-dod-designates-it-official-programme-of-record-with-25000-military-accounts-deployed/)

**NGA Maven 的 AI 情报产品**
- [事实] NGA 局长 Whitworth（2025-06）称，NGA 在所有 AI 生成的产品上加注 **"machine-generated GEOINT"** 模板标签，在这类模板化产品的分发过程中没有人工参与（"no human hands"）。标签会注明 AI 参与的类型和程度，NGA 可能是 18 个 IC 成员中第一个常规化使用此类标签的机构。— [Breaking Defense 2025-06](https://breakingdefense.com/2025/06/no-human-hands-nga-circulates-ai-generated-intel-director-says/)
- [事实] Whitworth 表示 Maven 的下一阶段要加入"推理"能力，从识别物体发展到预测和发现威胁；向作战司令或总统汇报前仍需要人工佐证。— [MeriTalk](https://www.meritalk.com/articles/nga-expands-maven-ai-system-in-year-of-ai-whitworth-says/)；[ExecutiveGov](https://www.executivegov.com/articles/nga-maven-program-potential-threat-prediction-ai)

**联盟与跨梯队**
- [事实] NCIA 于 2025-03-25 完成 MSS NATO 采购，供盟军作战司令部（ACO）使用。从提出需求到签约约 6 个月，是 NATO 史上最快的采购之一，金额未公开，计划签约后约 30 天内部署。— [SHAPE](https://shape.nato.int/news-releases/nato-acquires-aienabled-warfighting-system-)；[Defense-Update](https://defense-update.com/20250418_palantir-mss-nato.html)
- [事实] Janes 报道，MSS NATO 已部署在 SHAPE 和 JFC Brunssum，JFC Norfolk 预计 2026 年 4—5 月接入。— [Janes](https://www.janes.com/osint-insights/defence-news/security/natos-jfc-norfolk-to-receive-palantirs-maven-smart-system-by-end-of-may)
- [低可信，待核实] 有报道称 NATO 于 2026-06-22 宣布 MSS 全面运行并接入其涉密网络。— [informedclearly](https://informedclearly.com/en/ai/57211/nato-palantir-maven-smart-system-2025)
- [事实] NGA（2025-05）称 Maven 通过 35 个以上军种和作战司令部工具、跨三个安全域，服务约 2 万名活跃用户。— [Breaking Defense 2025-05](https://breakingdefense.com/2025/05/ai-unchained-ngas-maven-tool-significantly-decreasing-time-to-targeting-agency-chief-says/)；[MeriTalk](https://www.meritalk.com/articles/nga-expands-maven-ai-system-in-year-of-ai-whitworth-says/)

### Inferences
- [推断] MSS 由三层组成：(1) 数据/本体层，在 Foundry/Gotham 中把传感器数据和检测结果对象化；(2) 工作流应用层，包括 COP 地图、Target Workbench 看板、资产比较（pairing）和 BDA 跟踪；(3) AIP/LLM 代理层，负责自然语言查询、排序和 COA 草案。CV 模型多由第三方提供，通过开放架构以"检测对象"形式写入本体，而不是由 Palantir 自研。
- [推断] "武器-目标配对"在 MSS 中更像是基于约束（时间、距离、燃油、弹药）的资产推荐与比较。最终的射击诸元和火力分配仍走 AFATDS 等存量火控系统。
- [推断] 机器速度地提名目标，加上 LLM 排序，会让人工审批变成瓶颈或"橡皮图章"。伊朗战役的数字（24 小时 1,000+ 目标）是这一讨论的核心论据。

### Gaps
- 没有找到 FMV（全动态视频）接入方式、友军跟踪（BFT/FFT）接入方式、BDA 模块的具体实现、COA 生成算法和武器-目标配对算法的权威说明。
- 没有找到 MSS 官方"releasability"（联盟可释放性/标签化数据访问控制）机制的公开细节。
- 无法从原始来源（Pentagon 或 Anthropic 官方文件）证实 Claude 在 MSS 中的具体角色。各方报道互相矛盾：一方说已被禁用，另一方说仍在运行。

## Q2. 技术架构：Palantir 平台栈、Apollo、本体、模型托管、Maven 分层（标注/模型/NGA 认证）、云与边缘、分类域、与 CJADC2/NGC2/TAK/AFATDS/Lattice 的互操作

### Takeaway
MSS 构建在 Palantir 平台（Foundry/Gotham + AIP，由 Apollo 跨环境持续交付）上，以本体（Ontology）作为数据和动作模型。Maven 的 AI 流水线由 NGA 主导：
- 数据标注：Scale AI 的过渡合同，之后是 Enabled Intelligence 的 7.08 亿美元 SEQUOIA；
- 系统集成与模型互操作：ECS 担任 AI3 集成商；
- 模型评估认证：NGA 的 AGAIM 试点。

2026 年 3 月 Feinberg 备忘录把 MSS 管理权从 NGA 转给 CDAO，合同统一经由 Army Enterprise Agreement，R&E 接任授权官（AO）职责。Lattice 与 MSS 通过 Anduril–Palantir 联合体对接。对于 TAK、JWICS 部署和具体云厂商，没有找到可靠公开信息。

### Cited Findings
**Palantir 平台栈**
- [厂商文档] Apollo 是持续交付平台，负责管理承载 Foundry 和 AIP 服务的底层基础设施。— [Palantir Docs: AIP, Foundry, and Apollo](https://www.palantir.com/docs/foundry/architecture-center/platforms)；[Apollo 技术白皮书](https://www.palantir.com/assets/xrfr7uokpv1b/3B5KbQ9ujsiDCX4Tnfz3Hy/8d3ee9a6911665f036ce3d28c19cfa0d/PalantirApolloTechnicalWhitePaper.pdf)
- [厂商文档] Ontology 把数据源映射为对象、属性和链接，并对"动作"（action）建模，支持把决策实时写回运营系统和边缘系统。边缘端可以用轻量的 Embedded Ontology 记录决策，平台也能接入 IoT/边缘数据流。— [Palantir Ontology Overview](https://www.palantir.com/docs/foundry/ontology/overview)；[Ontology system](https://www.palantir.com/docs/foundry/architecture-center/ontology-system)
- [二手] Apollo 可以运行在本地数据中心、边缘硬件和涉密网络上。— [mlq.ai](https://mlq.ai/research/palantir-technologies/)

**Maven 流水线与 NGA 角色**
- [事实] 2022 年 GEOINT 大会上宣布，NGA 从 OUSD(I&S) 接管 Maven 的 GEOINT AI 服务（约占原项目的 80%），2023 财年生效。DefenseScoop 称整个 Maven"AI development pipeline"交给了 NGA。— [Breaking Defense 2022-04](https://breakingdefense.com/2022/04/pentagons-flagship-ai-effort-project-maven-moves-to-nga/)；[C4ISRNet 2022-04](https://www.c4isrnet.com/intel-geoint/2022/04/27/intelligence-agency-takes-over-project-maven-the-pentagons-signature-ai-scheme/)；[DefenseScoop 2024-03](https://defensescoop.com/2024/03/14/project-maven-fiscal-2025-budget-still-evolving/)
- [二手] NGA Maven 于 2023-11-07 成为 Program of Record。— [GlobalSecurity](https://www.globalsecurity.org/intell/systems/maven.htm)

**数据标注**
- [事实] NGA 授予 Scale AI 约 2,400 万美元、为期一年的固定价合同，名为"NGA Maven Data Labeling Services Bridge"。— [NGA Contract Announcements](https://www.nga.mil/news/Contract_Announcements.html)
- [事实] 2024-09 NGA 宣布约 7 亿美元的数据标注竞标。2025-11，初创公司 **Enabled Intelligence** 赢得最高 **7.08 亿美元**、最长 7 年的合同（SEQUOIA），用于训练 CV 模型，是美国政府迄今最大的 AI 数据标注项目，也是 Maven 的基础能力。— [Breaking Defense 2024-09](https://breakingdefense.com/2024/09/nga-slates-700m-for-ai-data-labeling-launches-standard-model-push/)；[Defense One 2024-09](https://www.defenseone.com/technology/2024/09/nga-deepens-push-ai-countrys-largest-data-labeling-effort/399255/)；[Breaking Defense 2025-11](https://breakingdefense.com/2025/11/startup-enabled-intelligence-nabs-ngas-708-million-ai-training-contract/)

**模型认证**
- [事实] NGA 的 **AGAIM** 试点（GEOINT AI 模型认证/评估）提供一套标准的评估和风险管理流程。官方明确表示不希望它变成"ATO 式"的排队审批。— [Federal News Network 2025-09](https://federalnewsnetwork.com/intelligence-community/2025/09/ngas-ai-standards-work-aims-to-avoid-ato-like-process/)

**集成商与早期供应商**
- [事实] **ECS** 自 2017 年起担任 NGA Maven 项目的 AI Interoperability Integrator（AI3）。— [ExecutiveBiz](https://www.executivebiz.com/articles/ecs-john-heneghan-nga-maven-program)
- [二手，待证实] GlobalSecurity 称：DIUx 帮助寻找商业供应商；Google 通过与 Northrop Grumman 的安排提供基于 TensorFlow 的 CV 模型；Palantir 提供数据集成层，后来发展为 MSS；L3Harris、Microsoft、Sierra Nevada 等 20 多家公司参与。— [GlobalSecurity](https://www.globalsecurity.org/intell/systems/maven.htm)
- [事实] Bloomberg 报道，Maven 早期用美国海军 SEAL 在索马里拍摄的无人机视频测试多家供应商的识别工具。— [Bloomberg 2024 feature](https://www.bloomberg.com/features/2024-ai-warfare-project-maven/)
- [事实] 18th Airborne Corps 通过 Scarlet Dragon 系列演习，在 DevSecOps 环境中与多达 70 家公司合作打造 MSS。— [Defense One 2024-08](https://www.defenseone.com/technology/2024/08/dod-getting-better-buying-tech-reports-say/398821/)；[CSET Building the Tech Coalition](https://cset.georgetown.edu/wp-content/uploads/CSET-Building-the-Tech-Coalition-1.pdf)
- [事实] GAO 把 Scarlet Dragon 描述为使用 Project Maven 数据的陆军目标识别 AI 能力。— [GAO-22-104765](https://www.gao.gov/assets/gao-22-104765.pdf)

**治理与合同（2026）**
- [事实] Feinberg 备忘录（2026-03-09 信函，DefenseScoop 2026-04-15 报道）的主要内容：
  - 2026 财年结束（2026-09）前，MSS 成为正式 program of record；
  - 30 天内把系统管理权从 NGA 移交给 CDAO 新设的 MSS Program Office；
  - 所有 MSS 合同统一经由现有的 **Army Enterprise Agreement**，由陆军负责今后的 Palantir 合同；
  - **R&E** 从 NGA 接任 MSS 及其商业云基础设施的授权官（AO）职责。
  — [DefenseScoop 2026-04-15](https://defensescoop.com/2026/04/15/palantir-maven-smart-system-pentagon-program-transition-feinberg/)；[CSET 转载](https://cset.georgetown.edu/article/dod-components-face-aggressive-timeline-for-maven-smart-system-transition/)
- [事实] 陆军于 2025-07 与 Palantir 签订最高 100 亿美元的企业协议（EA）。— [GlobalSecurity](https://www.globalsecurity.org/intell/systems/maven.htm)（二手）
- [事实] 海军陆战队通过 enterprise license，在 **SIPRNet Impact Level 6 云** 上"无限制访问"MSS。— [DefenseScoop 2025-09-12](https://defensescoop.com/2025/09/12/marine-corps-maradmin-maven-smart-system-mss-palantir-rollout/)；[USMC 新闻稿](https://www.marines.mil/News/Press-Releases/Press-Release-Display/Article/4305728/marine-corps-partners-with-chief-digital-and-artificial-intelligence-office-and/)
- [事实] NGA 称 Maven 跨"三个安全域"运行（推测为非密/秘密/绝密，但原文没有说明具体网络）。— [Breaking Defense 2025-05](https://breakingdefense.com/2025/05/ai-unchained-ngas-maven-tool-significantly-decreasing-time-to-targeting-agency-chief-says/)
- [事实] 陆军 Combined Arms Command 把 MSS 纳入训练和教育体系。— [army.mil](https://www.army.mil/article/290958/armys_combined_arms_command_to_integrate_maven_c2_smart_system_into_training_and_education)

**互操作（Lattice、NGC2、Joint Fires Network）**
- [厂商宣称] Anduril 与 Palantir 于 2024-12 宣布组建联合体，把 **Lattice Mesh** 与 MSS 和 AIP 互联。— [Palantir IR 2024-12](https://investors.palantir.com/news-details/2024/Anduril-and-Palantir-to-Accelerate-AI-Capabilities-for-National-Security/)
- [分析] 一种分层说法：MSS 处理历史和近实时情报，形成目标包；Lattice 实时执行目标包，以机器速度协调传感器和效应器。— [Foreign Affairs Forum 2026-04](https://www.faf.ae/home/2026/4/21/andurils-lattice-platform-architecture-accountability-and-the-future-of-autonomous-warfare-in-american-defense-strategy)
- [厂商宣称] 在陆军 4ID 的 NGC2 中，Anduril 把 NGC2 数据网格规模扩大到三倍，每个车辆、指挥所和士兵都是 Lattice Mesh 节点。在通信降级条件下，完成了端到端的电子战目标定位与火力流程。— [Anduril: Scaling NGC2](https://www.anduril.com/news/scaling-next-generation-command-and-control-from-prototype-to-fight)
- [事实/二手] FY2027 预算申请中有约 23 亿美元（5 年）用于 MSS 和互补的作战管理平台 Joint Fires Network。— [Venture Atlas](https://www.ventureatlas.org/company/palantir)（低可信，需核对预算文件）

### Inferences
- [推断] 2026 年起，"Maven"在组织上形成两条线：
  - **NGA Maven**：GEOINT CV 模型流水线，负责标注、训练、评估认证（AGAIM）和机器生成情报产品；
  - **MSS**：Palantir 平台上的作战应用，由 CDAO 管理，合同经陆军 EA。
  两者通过"检测对象 → 本体"接口衔接。
- [推断] 涉密部署大概率由 Apollo 在 IL6/SIPR（已证实）以及更高等级环境中持续交付。NGA 的"三个安全域"可能对应非密、秘密和 TS/SCI，但没有公开来源证实 JWICS 上的 MSS 实例。

### Gaps
- 没有找到 MSS 托管在哪家云（AWS/Microsoft/Oracle/Google）、是否经由 JWCC 的公开信息。只知道海军陆战队通过 SIPR IL6 云访问。
- 没有找到 MSS 与 **TAK**、**AFATDS** 的官方接口说明，AFATDS 的说法仅来自二手博客。
- 没有找到 CrowdAI、Clarifai 等早期 CV 供应商在 Maven 中当前角色的来源。
- 没有找到 MSS 边缘部署（如前沿战术节点、断连运行）的权威公开描述。

## Q3. 公开报道的性能指标

### Takeaway
公开指标主要有以下几类：
- 吞吐：目标审批从每小时 30 个提升到 80 个（2024，Bloomberg）；陆军的目标是每小时 1,000 个"高质量决策"，这是愿景，不是实测；
- 人力：18th Airborne 约 20 人的目标单元达到了 OIF（2003 年伊拉克战争）时 2,000 多人时敏目标单元的效能（CSET/CSIS）；
- 识别准确率：Maven 约 60%，人类分析员 84%，沙漠或天气变化场景下可低于 30%（Bloomberg 2024）；
- 时延：Scarlet Dragon 中，数据传输到打击的时间从 12 小时以上降到 1 分钟以内（二手）；
- 实战：对伊朗作战头 24 小时打击 1,000 多个目标。

### Cited Findings
- [事实，Bloomberg] 资深目标官 Temple 估计，借助 Maven 每小时可签批多达 **80 个目标**，不用 Maven 时约 **30 个**；完全信任机器会更快，但会引入错误。— [Bloomberg 2024 feature (Katrina Manson)](https://www.bloomberg.com/features/2024-ai-warfare-project-maven/)；[Techmeme 摘要](https://www.techmeme.com/240302/p4)
- [事实，Bloomberg 经二手转述] 测试中 Maven 识别物体的正确率约 **60%**，与 18th Airborne 合作的人类分析员为 **84%**。— [DeepLearning.ai The Batch](https://www.deeplearning.ai/the-batch/maven-a-system-that-analyzes-satellite-data-to-identify-targets-in-real-world-conflicts)；[GIGAZINE](https://gigazine.net/gsc_news/en/20240305-maven-smart-system/)
- [事实，二手] 在西伊拉克这类天气多变的沙漠地形中，准确率可降到 **30% 以下**。— [Airwars](https://airwars.org/the-first-civilian-confirmed-killed-in-an-ai-assisted-strike/)
- [事实/愿景] Whitworth（GEOINT 2025）称，陆军希望借助 Maven 实现单位"一小时做出 **1,000 个高质量决策**"（选择或剔除目标），还提到某个目标单元在一次演习中把时间线从数小时缩短到数分钟。— [Breaking Defense 2025-05](https://breakingdefense.com/2025/05/ai-unchained-ngas-maven-tool-significantly-decreasing-time-to-targeting-agency-chief-says/)
- [智库] CSET 把它表述为最终目标：系统与士兵帮助指挥官每小时处理 1,000 个战术决策。— [CSET Building the Tech Coalition (2024-08, Emelia Probasco)](https://cset.georgetown.edu/wp-content/uploads/CSET-Building-the-Tech-Coalition-1.pdf)
- [智库] 18th Airborne Corps 用 MSS 达到了 OIF 时敏目标单元（被视为美军史上效率最高的目标单元）的效能，但只用了约 **20 人**，而后者有 **2,000 多人**。— [CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do)；[CSET](https://cset.georgetown.edu/wp-content/uploads/CSET-Building-the-Tech-Coalition-1.pdf)
- [二手] Scarlet Dragon 中，"数据传输+打击"的时间从 **12 小时以上** 缩短到 **1 分钟以内**。— [Army Recognition](https://armyrecognition.com/news/army-news/army-news-2024/us-army-explores-an-ai-system-capable-of-targeting-1-000-objectives-per-hour-2)
- [多源] 对伊朗作战头 24 小时打击 1,000 多个目标，另有"10 天约 5,000 个"的说法。— [CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do)；[Responsible Statecraft](https://responsiblestatecraft.org/ai-war-iran/)；[Wikipedia: AI warfare](https://en.wikipedia.org/wiki/AI_warfare)

**规模与商业指标**
- [事实] MSS 合同的变化：2024-05 签订 4.8 亿美元、5 年期 IDIQ；2025-05 上限提高 7.95 亿美元，达到约 **13 亿美元**（至 2029-05），理由是用户需求激增。— [DefenseScoop 2025-05-23](https://defensescoop.com/2025/05/23/dod-palantir-maven-smart-system-contract-increase/)；[SpaceNews](https://spacenews.com/pentagon-boosts-budget-for-palantirs-ai-software-in-major-expansion-of-project-maven/)
- [事实] NGA 另授予 Palantir 2,800 万美元合同，扩大 NGA 分析员对 MSS 的访问。— [MeriTalk](https://www.meritalk.com/articles/nga-expands-maven-ai-system-in-year-of-ai-whitworth-says/)
- [事实] Palantir 2026 年二季度营收约 19.4 亿美元，同比增长 93%。管理层称"首个 program of record 本季度在平台上启动"。有报道称 Maven 的年化经常性收入接近 10 亿美元，但只有单一来源，可信度低。— [CNBC 2026-08-03](https://www.cnbc.com/2026/08/03/palantir-pltr-earnings-q2-2026.html)；[Motley Fool 电话会实录](https://www.fool.com/earnings/call-transcripts/2026/08/10/palantir-pltr-q2-2026-earnings-call-transcript/)；[Simply Wall St](https://simplywall.st/stocks/us/software/nasdaq-pltr/palantir-technologies/news/palantir-technologies-pltr-is-up-79-after-maven-ai-defense-r)

### Inferences
- [推断] "60% 对 84%"是 2023—2024 年的单项物体识别测试结果；"30→80 目标/小时"是人机协同下的审批吞吐。两者衡量的东西不同，不能混为一谈。1,000 个/小时是陆军提出的愿景指标，伊朗战役 24 小时 1,000+ 目标属于战役级总量，同样不能直接比较。

### Gaps
- 没有找到 2025—2026 年 CV 模型准确率、误报率或 AGAIM 评估结果的公开数据。
- 没有找到对伊朗作战中 AI 辅助目标误差或平民伤亡的官方统计。

## Q4. 人在回路与政策（DoDD 3000.09、负责任 AI、NGA 认证、目标审批）

### Takeaway
官方和主流报道一致把 MSS 定位为决策支持工具：目标由人类指挥官批准，适用 DoDD 3000.09 的"适当程度的人类判断"原则。NGA 通过机器生成产品标签和 AGAIM 模型评估来治理 AI 产出。但没有找到针对 MSS 的正式"负责任 AI 审查"公开文件。批评者认为，高吞吐下人工审批正在变成"人类背书"。

### Cited Findings
- [事实] DoDD 3000.09（2012 年发布，2023 年 1 月更新）要求自主和半自主武器系统的设计，必须让指挥官和操作员能对武力使用施加"适当程度的人类判断"，正式开发前需要高级官员审查。— [GAO-22-104765](https://www.gao.gov/assets/gao-22-104765.pdf)；[DoDD 3000.09 (2012 原文)](https://ogc.osd.mil/Portals/99/autonomy_in_weapon_systems_dodd_3000_09.pdf)；[Wikipedia: DoDD 3000.09](https://en.wikipedia.org/wiki/Department_of_Defense_Directive_3000.09)
- [二手] MSS 被描述为决策支持工具，人类操作员保留最终目标授权。— [X @ReviewingNews](https://x.com/ReviewingNews/status/2065122861304492351)（低可信）；[CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do)
- [事实] 一线流程中，目标官 Temple 逐一签批目标，并表示完全信任机器会引入错误。— [Bloomberg 2024](https://www.bloomberg.com/features/2024-ai-warfare-project-maven/)
- [事实] NGA 的人在回路做法：
  - 机器生成的 GEOINT 加注 AI 参与程度标签；
  - 向作战司令或总统汇报前仍需人工佐证；
  - AGAIM 提供模型评估和风险管理。
  — [Breaking Defense 2025-06](https://breakingdefense.com/2025/06/no-human-hands-nga-circulates-ai-generated-intel-director-says/)；[MeriTalk](https://www.meritalk.com/articles/nga-expands-maven-ai-system-in-year-of-ai-whitworth-says/)；[Federal News Network](https://federalnewsnetwork.com/intelligence-community/2025/09/ngas-ai-standards-work-aims-to-avoid-ato-like-process/)
- [分析/批评] Strategy International 认为，系统已从决策支持变成"附带人类副署以满足法律合规的决策系统"。— [Strategy International](https://strategyinternational.org/2026/04/06/publication258/)
- [分析/批评] 有文章讨论"Rubber Stamp Problem"：AI 的速度超过了它所承诺的监督能力。— [Medium: The Rubber Stamp Problem](https://rbulsing.medium.com/the-rubber-stamp-problem-how-ai-outpaces-the-oversight-it-promises-ff8372752673)
- [事实] Anthropic 因拒绝支持自主武器和国内监控，与五角大楼发生冲突。— [ACA](https://www.armscontrol.org/act/2026-05/news/ai-plays-major-role-war-iran)
- [分析] Airwars 调查了可能"首例经证实死于 AI 辅助打击的平民"案例。— [Airwars](https://airwars.org/the-first-civilian-confirmed-killed-in-an-ai-assisted-strike/)
- [事实，CSET] Maven 的数据投毒风险受到关注；CSET 明确表示不公开 MSS 的具体作战细节。— [Techmeme/Bloomberg](https://www.techmeme.com/240302/p4)；[CSET](https://cset.georgetown.edu/wp-content/uploads/CSET-Building-the-Tech-Coalition-1.pdf)

### Inferences
- [推断] MSS 本身不发射武器，在 3000.09 的框架下更接近"目标选择支持系统"，而不是自主武器系统。因此 3000.09 的高级审查不一定直接适用于它，问责主要依赖交战规则（ROE）、联合目标定位流程（JP 3-60）中的人工签批和法律审查。

### Gaps
- 没有找到针对 MSS 的官方 RAI 评估、3000.09 审查记录，或 CDAO RAI Toolkit 的应用报告。
- 没有找到伊朗战役中目标审批层级和每个目标审核时长的官方数据。

## Q5. Maven 生态中的已知供应商与组件

### Takeaway
核心供应商是 Palantir（MSS/AIP/Apollo）。周边已知供应商包括：
- 标注：Scale AI（过渡合同）、Enabled Intelligence（SEQUOIA，7.08 亿美元）；
- 集成：ECS（AI3）；
- 检测模型：Safran.AI（NATO 演示）；
- 商业 SAR：ICEYE、Capella；
- LLM：Anthropic Claude（存在争议）；
- 执行层：Anduril Lattice（联合体）；
- 早期：Google（TensorFlow）、Northrop、L3Harris、Microsoft、Sierra Nevada 等。

### Cited Findings
- Palantir：MSS 主承包商，合同上限约 13 亿美元，另有 NATO 合同和陆军 EA。— [DefenseScoop 2025-05](https://defensescoop.com/2025/05/23/dod-palantir-maven-smart-system-contract-increase/)；[SHAPE](https://shape.nato.int/news-releases/nato-acquires-aienabled-warfighting-system-)
- Scale AI：NGA Maven 数据标注过渡合同，约 2,400 万美元。— [NGA](https://www.nga.mil/news/Contract_Announcements.html)
- Enabled Intelligence：NGA 数据标注合同，最高 7.08 亿美元、最长 7 年。— [Breaking Defense 2025-11](https://breakingdefense.com/2025/11/startup-enabled-intelligence-nabs-ngas-708-million-ai-training-contract/)
- ECS：自 2017 年起担任 Maven AI3 集成商。— [ExecutiveBiz](https://www.executivebiz.com/articles/ecs-john-heneghan-nga-maven-program)
- Safran.AI：在 MSS NATO 演示中提供检测对象（12,000 个）。— [Palantir Blog](https://blog.palantir.com/maven-smart-system-innovating-for-the-alliance-5ebc31709eea)
- ICEYE、Capella Space：商业 SAR 数据来源。— [CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do)
- Anthropic（Claude）：通过 Palantir 接入，2026 年起存在争议。— [Responsible Statecraft](https://responsiblestatecraft.org/ai-war-iran/)；[ACA](https://www.armscontrol.org/act/2026-05/news/ai-plays-major-role-war-iran)
- Anduril（Lattice）：与 Palantir 组建联合体，也是 NGC2 数据网格。— [Palantir IR](https://investors.palantir.com/news-details/2024/Anduril-and-Palantir-to-Accelerate-AI-Capabilities-for-National-Security/)；[Anduril](https://www.anduril.com/news/scaling-next-generation-command-and-control-from-prototype-to-fight)
- 早期参与方：Google（经 Northrop）、L3Harris、Microsoft、Sierra Nevada 和 20 多家其他公司。— [GlobalSecurity](https://www.globalsecurity.org/intell/systems/maven.htm)（二手）
- 18th Airborne / Scarlet Dragon 生态：多达 70 家公司。— [Defense One](https://www.defenseone.com/technology/2024/08/dod-getting-better-buying-tech-reports-say/398821/)

### Inferences
- [推断] 生态呈"平台 + 可插拔模型/数据"结构：Palantir 控制集成层和工作流层，NGA 控制模型训练、标注和认证，第三方 CV、SAR、LLM 供应商可以替换。2026 年 Anthropic 被 OpenAI 等替代的报道印证了 LLM 层可以替换。

### Gaps
- 没有找到 CrowdAI、Clarifai、Microsoft、AWS 当前在 Maven 中的合同角色的公开来源；OpenAI 替代 Anthropic 的具体合同细节也没有找到。
