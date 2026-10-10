# Project Maven / Maven Smart System (MSS): Demonstrated Capabilities and Real-World Cases, 2017 – Oct 2026

> 方法说明（Method note）：本笔记于 2026-10-10 编写。WebFetch 和 curl 在本会话中都被代理挡住（DNS/403），所以下面的内容都来自搜索引擎对原文的摘要。原文全文没有逐篇核对。每条都附原始 URL，供撰稿人复核。标注说明：**[官方]**＝美国国防部、北约或官员的公开表态，**[媒体]**＝独立报道（多为匿名信源），**[二手]**＝聚合站或博客，可靠性低。

## Q1. Case-by-case catalogue (dated)

### Takeaway
Maven 的发展分四个阶段。2017–18 年是 SOCOM、CENTCOM、AFRICOM 反 ISIS 任务中的无人机视频目标检测。2020–24 年由 XVIII 空降军通过 Scarlet Dragon 演习，把它做成"数据融合 + 目标工作流"平台（MSS）。2022 年起用于支援乌克兰。2024 年起在 CENTCOM 实战中参与打击目标的提名。2026 年在对伊朗的"史诗之怒"（Operation Epic Fury）行动中被大规模使用：官方称 38 天内打击了 13,000 个目标，用户数超过 10 万。同一时期也出现了与 Maven 相关的最严重平民伤亡事件，即 Minab 学校遇袭。

### Cited Findings

**Catalogue table（案例目录）**

| # | 日期 | 用户/单位 | 战区 | Maven 的作用 | 规模/结果数据 | 可信度 | 来源 |
|---|---|---|---|---|---|---|---|
| 1 | 2017-04 | DepSecDef Robert Work 备忘录成立 AWCFT（Project Maven）；Lt Gen Jack Shanahan 主管，Col Drew Cukor 领导 | — | 计划启动 | — | 官方 | [Bulletin of the Atomic Scientists](https://thebulletin.org/2017/12/project-maven-brings-ai-to-the-fight-against-isis/) |
| 2 | 2017-12 | SOCOM 情报分析员 | 中东（反 ISIS） | 在 ScanEagle 小型无人机全动态视频（FMV）中识别物体；Shanahan 称之为 "prototype warfare" | 初始部署，无性能数据 | 官方/媒体 | [Nextgov 2017-12](https://www.nextgov.com/artificial-intelligence/2017/12/pentagons-new-artificial-intelligence-already-hunting-terrorists/144769/) |
| 3 | 2017-12 → 2018-05 | AFRICOM 及多个中东地点 | 非洲、中东 | 同上，扩展部署 | 官员称 AFRICOM 自 2017-12 起使用 | 媒体 | [Breaking Defense 2018-05](https://breakingdefense.com/2018/05/pentagons-big-ai-program-maven-already-hunts-data-in-middle-east-africa/) |
| 4 | 2018-04 → 06 | Google（承包商） | — | 争议：员工抗议 | 超过 4,000 人签名（后称超过 4,600），约 12–13 人辞职；2018-06-01 Diane Greene 宣布合同（约 900 万美元）2019-03 到期后不再续签 | 媒体 | [Fortune 2018-06-02](https://fortune.com/2018/06/02/google-pentagon-drone-deal-protests); [Bloomberg 2018-06-04](https://www.bloomberg.com/news/articles/2018-06-04/google-staff-ai-revolt-puts-pentagon-cloud-deals-in-jeopardy) |
| 5 | 2020 起（年度系列） | XVIII Airborne Corps（Fort Bragg） | 美国本土演习 | Scarlet Dragon 系列演习：把 Maven 发展为整合传感器、目标识别和火力分配的 MSS | CSET：约 20 人的目标小组达到 2003 年伊拉克战争时间敏感目标单元（约 2,000 人）的产出；一名目标军官估计用 Maven 每小时可处理 80 个目标，不用时为 30 个；"每小时 1,000 个高质量决策"只是**目标**，未经验证 | 智库/媒体 | [CSET Policy Brief 2024-08](https://cset.georgetown.edu/wp-content/uploads/CSET-Building-the-Tech-Coalition-1.pdf); [Interesting Engineering](https://interestingengineering.com/military/us-maven-smart-system-army) |
| 6 | 2022 起 | XVIII Airborne Corps（欧洲前沿部署，支援乌克兰） | 乌克兰 | 用 MSS 生成目标情报并分享给乌军；乌方用的是不依赖美国敏感情报的版本 | Manson 书称向乌克兰发送了"数以万计"的目标；NYT（2024-04）称效果"好坏参半"：帮助乌军更有效地打击俄军炮兵，但没能把战场图像送到前线士兵手里 | 媒体（书、NYT） | [Lawfare 书评](https://www.lawfaremedia.org/article/how-the-u.s.-military-learned-to-embrace-ai-warfare); [Willis Strategy 书评](https://willis-strategy.com/insights/review-project-maven.html); [Kyiv Independent 转述 NYT](https://kyivindependent.com/nyt-project-maven-ai-having-mixed-results-on-ukraines-battlefields/); [The Defender 转述 NYT](https://thedefender.media/en/2024/04/nyt-how-us-ai-maven-helps-ukrainian-military/) |
| 7 | 2024-02-02 | CENTCOM | 伊拉克、叙利亚 | 机器学习目标识别帮助"缩小目标范围" | 参与 85 次以上打击（7 处设施），起因是约旦"Tower 22"遇袭致 3 名美军死亡；CENTCOM CTO Schuyler Moore 称每一步都以人工验证结束 | 官方（Moore 对 Bloomberg 的发言） | [The Register 2024-02-27](https://www.theregister.com/2024/02/27/us_military_maven_ai_used/); [The National 2024-02-26](https://www.thenationalnews.com/world/us-news/2024/02/26/us-ai-syria-yemen/); [BNN Bloomberg](https://www.bnnbloomberg.ca/us-used-ai-to-help-find-middle-east-targets-for-airstrikes-1.2039269) |
| 8 | 2024 | CENTCOM | 也门、红海 | 定位也门境内的火箭发射器和红海上的水面船只 | 无具体数量 | 官方（Moore） | [Bloomberg 2024 feature](https://www.bloomberg.com/features/2024-ai-warfare-project-maven/); [deeplearning.ai The Batch](https://www.deeplearning.ai/the-batch/maven-a-system-that-analyzes-satellite-data-to-identify-targets-in-real-world-conflicts) |
| 9 | 2024-05 | DoD 与 Palantir | 5 个 COCOM：CENTCOM、EUCOM、INDOPACOM、NORTHCOM/NORAD、TRANSCOM | MSS 五年期 IDIQ 合同，金额 4.8 亿美元 | 扩展到"数千用户" | 官方 | [DefenseScoop 2025-05-23](https://defensescoop.com/2025/05/23/dod-palantir-maven-smart-system-contract-increase/); [Defense News on X](https://x.com/defense_news/status/1796219793328013505) |
| 10 | 2025-03-25 签约 / 2025-04-14 公布 | NATO NCIA → Allied Command Operations（SHAPE） | 欧洲/北约 | 采购 MSS NATO，用于情报融合、目标、战场感知和规划 | 从提出需求到采购只用 6 个月，北约称是史上最快之一；合同金额未公开；北约强调它不同于"NGA Maven" | 官方 | [SHAPE 2025](https://shape.nato.int/news-archive/2025/nato-acquires-aienabled-warfighting-system.aspx); [NCIA](https://www.ncia.nato.int/newsroom/news/nato-acquires-aienabled-warfighting-system); [DefenseScoop 2025-04-14](https://defensescoop.com/2025/04/14/nato-palantir-maven-smart-system-contract/) |
| 11 | 2025-05 | DoD | 全军 | 合同上限提高到约 13 亿美元（至 2029 年），理由是"需求增长" | NGA 局长 Whitworth：活跃用户超过 20,000，覆盖 35 个以上的军种和 COCOM 工具、3 个安全域，自 2025-01 以来翻了一倍多 | 官方 | [DefenseScoop 2025-05-23](https://defensescoop.com/2025/05/23/dod-palantir-maven-smart-system-contract-increase/) |
| 12 | 2026-01-03 | 美军（Maduro 抓捕行动） | 委内瑞拉 | WSJ 报道称 Anthropic 的 Claude 通过 Palantir 平台参与；**没有来源明确说用的是 Maven** | 具体任务属于机密 | 媒体（WSJ，匿名信源）；Anthropic 不予置评 | [Small Wars Journal 2026-02-17](https://smallwarsjournal.com/2026/02/17/ai-enabled-decapitation-strike-maduro-raid/); [CNBC 2026-03-12](https://www.cnbc.com/2026/03/12/palantir-tech-gives-west-critical-edge-in-middle-east-ceo-alex-karp.html) |
| 13 | 2026-02-28 起（Operation Epic Fury） | CENTCOM | 伊朗 | MSS（内嵌 Claude）给目标排序、生成坐标并建议武器；WaPo 报道称还会生成法律依据草稿（二手转述） | WaPo：头 24 小时打击约 1,000 个目标；CENTCOM 3-3：已打击近 2,000 个目标；CDAO Cameron Stanley：38 天 13,000 个目标，把目标周期"从数天压缩到数秒"；白宫 4-8 统计：其中指挥控制目标超过 2,000 个、防空目标 1,500 个 | 官方（数量）＋ 媒体（Claude 的角色） | [WaPo 2026-03-04](https://www.washingtonpost.com/technology/2026/03/04/anthropic-ai-iran-campaign/); [Stanley 国会书面证词 2026-05-14](https://www.congress.gov/119/meeting/house/119184/witnesses/HHRG-119-AS35-Wstate-StanleyC-20260514.pdf); [Breaking Defense 2026-05](https://breakingdefense.com/2026/05/insatiable-appetite-for-ai-maven-usage-surged-for-strikes-on-iran-pentagon-ai-chief-says/); [defence-industry.eu](https://defence-industry.eu/operation-epic-fury-u-s-forces-strike-over-13000-targets-in-38-days/); [Arms Control Assoc. 2026-05](https://www.armscontrol.org/act/2026-05/news/ai-plays-major-role-war-iran) |
| 14 | 2026-02-28 前后（Epic Fury 第一天） | CENTCOM | 伊朗 Minab | **事故**：一所学校被打击，据报约 123 名儿童死亡（伊方另称至少 186 名学生和教师死亡）。该地点在旧数据库中仍标为 IRGC 设施，输入 Maven 后被列为"第一天推荐目标" | Bloomberg（2026-09-18 前后）引述五角大楼内部调查称是"一连串可预防的失败"：卫星图像显示该地点近十年前就已改建，2018 年图像可见足球场；平民伤害评估团队从约 10 人缩减到 1 人；部分用户以为 Maven 会发现过期记录。Palantir 称自己"不对底层数据负责"。前军官对 Semafor 表示责任在人，不在 AI。2026-03-12 有 120 多名众议院民主党议员致信，46 名参议员另有类似要求；联合国事实调查团认为"有合理理由"相信构成战争罪。完整报告未公开 | 媒体（匿名官员）；存在争议 | [Bloomberg graphics](https://www.bloomberg.com/graphics/2026-iran-school-attack/); [Gizmodo](https://gizmodo.com/pentagon-investigators-say-overreliance-on-palantir-ai-tech-contributed-to-u-s-strike-that-killed-123-iranian-children-2000814477); [ThePrint](https://theprint.in/world/us-strike-on-school-in-irans-minab-was-result-of-over-reliance-on-ai-outdated-sat-images-bloomberg/3047604/); [Military Times 2026-03-24](https://www.militarytimes.com/news/your-military/2026/03/24/deadly-iran-school-strike-casts-shadow-over-pentagons-ai-targeting-push/); [Wikipedia: 2026 Minab school attack](https://en.wikipedia.org/wiki/2026_Minab_school_attack) |
| 15 | 2026-03 | DepSecDef Steve Feinberg 备忘录 | 全军 | 要求在本财年结束（2026-09）前把 MSS 转为正式的 program of record | 被称为"激进"的时间表；有官员称 ATO（运行授权）是瓶颈，全面完成可能要 18 个月 | 官方 | [DefenseScoop 2026-04-15](https://defensescoop.com/2026/04/15/palantir-maven-smart-system-pentagon-program-transition-feinberg/) |
| 16 | 2026-06-22 达到 FOC，2026-06-30 公布 | NATO ACO | 欧洲 | MSS NATO 达到全面作战能力（FOC），获准在机密网络上运行，数据存放在北约自有的数据中心 | 2025 年全年测试，并经 Steadfast Deterrence 2026 演习检验 | 官方 | [SHAPE](https://shape.nato.int/news-releases/Maven-System-achieves-full-capability); [Janes](https://www.janes.com/defence-intelligence-insights/defence-news/security/maven-smart-system-achieves-full-operating-capability-with-nato) |
| 17 | 2026-08 | DoD | — | 任命 Col. Molly Solsbury 为 MSS 项目主任，推动与 C2 的整合 | 外界报道，国防部对如何走出"碎片化部署"披露很少 | 官方 | [DefenseScoop 2026-08-05](https://defensescoop.com/2026/08/05/pentagon-appoints-new-maven-smart-system-program-director/) |
| 18 | 2026 | Army Combined Arms Command | 训练体系 | 把 "Maven C2 smart system" 纳入训练和院校教育 | — | 官方 | [army.mil](https://www.army.mil/article/290958/armys_combined_arms_command_to_integrate_maven_c2_smart_system_into_training_and_education) |
| 19 | 2026-09-22 | 全军（DefenseTalks 会议） | 全球 | 用户规模和用途扩展 | USD(R&E) 副次长 James Mazol：2026-01 约 50,000 用户，Epic Fury 后超过 100,000；扩展到所有 COCOM 和国民警卫队局；Defense One 称它正成为五角大楼的"everything app"（后勤、战备、供应链、预算），取代了"6、8、10 个"旧 IT 系统；国防部向国会申请未来五年 23 亿美元 | 官方 | [DefenseScoop 2026-09-22](https://defensescoop.com/2026/09/22/maven-smart-system-ai-james-mazol-cameron-stanley-defensetalks/); [Defense One 2026-09](https://www.defenseone.com/technology/2026/09/maven-becoming-pentagons-everything-app/415882/); [SpaceNews](https://spacenews.com/pentagon-seeks-2-3-billion-for-maven-ai-battlefield-system/) |

**Usage-growth metrics during Epic Fury（伊朗战事期间的使用增长）**
- 五角大楼发言人称，环比来看，非密网使用量增长 38%，涉密网增长 89%；按 token 计的日峰值增长 4,425%，最高约 200 亿 token/天。见 [Breaking Defense 2026-05](https://breakingdefense.com/2026/05/insatiable-appetite-for-ai-maven-usage-surged-for-strikes-on-iran-pentagon-ai-chief-says/)。
- 用户数时间线：2024-05 为"数千"（5 个 COCOM），见 [Defense News](https://x.com/defense_news/status/1796219793328013505)；2025-05 超过 20,000，见 [DefenseScoop](https://defensescoop.com/2025/05/23/dod-palantir-maven-smart-system-contract-increase/)；2026-01 约 50,000，2026-09 超过 100,000，见 [DefenseScoop](https://defensescoop.com/2026/09/22/maven-smart-system-ai-james-mazol-cameron-stanley-defensetalks/)。

### Inferences
- 有公开数据的实战案例只有三类：2024-02 伊拉克/叙利亚、2024 年也门/红海，以及 2026 年 Epic Fury。前两类只有 CENTCOM CTO 的定性说法，Epic Fury 有官方的总量数字，但这些数字统计的是"打击的目标"，不是"Maven 独立识别的目标"。13,000 这个数不能理解为 Maven 的识别量或命中率。
- Maven 已从"计算机视觉检测器"变成"目标工作流 + 数据集成平台"，2026 年又加入了 LLM（Claude）。它被认可的主要价值是**压缩流程、减少人手**，不是检测更准。

### Gaps
- **Operation Rough Rider（2025 年对胡塞武装）**：没有找到把 Maven 与该行动直接挂钩的公开报道。
- **Midnight Hammer（2025-06 打击伊朗核设施）**：没有找到 Maven 参与的公开报道。
- **Southern Spear（2025-09 起加勒比海、东太平洋打击船只）**：搜索结果里没有 Maven 或 Palantir 的相关信息。
- **Maduro 抓捕**：只有"Claude 经 Palantir 参与"的说法，没有确认用的是 Maven。
- **Golden Dome、INDOPACOM 专门演习、Project Convergence、陆战队、太空军、英国国防部**：本轮搜索没有找到 Maven 的具体使用记录。可以确认的只有 INDOPACOM 在 2024 年合同的五个 COCOM 之列。
- 没能打开 WIRED 刊登的 Manson 书摘原文，所以 Wiesbaden 方面的细节没有核实。

## Q2. Reported performance numbers and limitations

### Takeaway
公开的准确率数据很少，而且都来自测试或演习：识别率约 60%（人工分析员约 84%），雪天等条件下低于 30%。效率数据主要是"省人力"和"省时间"。实战中的主要失败模式是**数据过期加上自动化偏见**（Minab），不是模型本身识别错误。

### Cited Findings
- XVIII 空降军军官 O'Callaghan 告诉 Bloomberg：人工分析员的正确率约 84%，Maven 约 60%；遇到某些物体或雪天图像时"可能低于 30%"。二手转述常写成"雪天 30%"或"识别坦克 60%"。见 [Bloomberg 2024 feature](https://www.bloomberg.com/features/2024-ai-warfare-project-maven/)；[Kyiv Independent](https://kyivindependent.com/nyt-project-maven-ai-having-mixed-results-on-ukraines-battlefields/)。
- 效率：约 20 人相当于 2003 年约 2,000 人的目标单元；单人从每小时 30 个目标提升到 80 个，见 [CSET 2024-08](https://cset.georgetown.edu/wp-content/uploads/CSET-Building-the-Tech-Coalition-1.pdf)。Stanley 称把时间从"数天"压缩到"数秒"，见 [国会证词](https://www.congress.gov/119/meeting/house/119184/witnesses/HHRG-119-AS35-Wstate-StanleyC-20260514.pdf)。
- 乌克兰：NYT 报道称 Maven 难以把"21 世纪的数据送进 19 世纪的战壕"，见 [Kyiv Independent](https://kyivindependent.com/nyt-project-maven-ai-having-mixed-results-on-ukraines-battlefields/)。
- 未核实的二手数字：有材料称 Maven 在乌克兰"每平方公里约 10 个错误检测"，见 [douwe.com wiki](https://douwe.com/projects/the_world_this_wiki/topics/maven_smart_system)；也有材料称准确率"从 70% 降到 30%，有时 10%"，据称出自 Manson，见 [Escudo Digital](https://www.escudodigital.com/en/technology/artificial-intelligence/inside-project-maven-why-ai-is-still-failing-on-the-battlefield.html)。两者都没有找到原始出处，**不建议直接引用**。
- Minab：数据库里的过期标签被 Maven 当作推荐目标输出，部分用户误以为系统会发现过期记录（自动化偏见），见 [Bloomberg 2026](https://www.bloomberg.com/graphics/2026-iran-school-attack/)。不同说法：前军官认为主要是人的问题，见 [Military Times](https://www.militarytimes.com/news/your-military/2026/03/24/deadly-iran-school-strike-casts-shadow-over-pentagons-ai-targeting-push/)；也有分析指出，目前没有公开的一手材料能把某个具体的 AI 输出和这次打击对应起来，见 [Substack 分析](https://brendonbeebe.substack.com/p/the-minab-school-strike-what-we-know)。
- 透明度：Lawfare 书评指出，Maven 的预算是机密的，且不适用 FOIA，见 [Lawfare](https://www.lawfaremedia.org/article/how-the-u.s.-military-learned-to-embrace-ai-warfare)。

### Inferences
- 60%/84% 的对比来自 2023–24 年 XVIII 空降军的测试，比加入 LLM 的 2026 版本早，不能直接套用到 Epic Fury。2026 年的版本没有公开任何准确率数据。
- "13,000 个目标"、"10 万用户"、token 增长这些数字都来自官员，没有独立审计。官方也有动力在申请预算（23 亿美元）和推动转为正式项目时强调成效。

### Gaps
- 没有找到任何公开的作战准确率或误报率数据，也没有找到 GAO 或 DoD IG 针对 MSS 的独立评估。
- Minab 的完整调查报告截至 2026-10 仍未公开。

## Q3. Actual capabilities vs. claims（总结）

### Takeaway
**已证实的能力**：多源情报融合和目标工作流管理，在大规模作战中以很少的人力支撑很高的目标吞吐量；用户覆盖全部 COCOM 和北约 ACO。**仍属声称或未经验证的**：目标识别的准确性、"每小时 1,000 个决策"、"数秒完成目标周期"，以及 AI 对每个具体目标的实际贡献。

### Cited Findings
- 已证实（多来源、官方）：
  - 2017-12 首次部署，见 [Nextgov](https://www.nextgov.com/artificial-intelligence/2017/12/pentagons-new-artificial-intelligence-already-hunting-terrorists/144769/)。
  - 2024-02-02 打击中参与目标筛选，见 [The Register](https://www.theregister.com/2024/02/27/us_military_maven_ai_used/)。
  - Epic Fury 中被大规模使用，见 [Breaking Defense](https://breakingdefense.com/2026/05/insatiable-appetite-for-ai-maven-usage-surged-for-strikes-on-iran-pentagon-ai-chief-says/)。
  - 北约 FOC，见 [SHAPE](https://shape.nato.int/news-releases/Maven-System-achieves-full-capability)。
  - 用户超过 10 万，见 [DefenseScoop](https://defensescoop.com/2026/09/22/maven-smart-system-ai-james-mazol-cameron-stanley-defensetalks/)。
- 声称：
  - "每小时 1,000 个决策"只是目标，见 [CSET](https://cset.georgetown.edu/wp-content/uploads/CSET-Building-the-Tech-Coalition-1.pdf)。
  - "从数天到数秒"，见 [Stanley 证词](https://www.congress.gov/119/meeting/house/119184/witnesses/HHRG-119-AS35-Wstate-StanleyC-20260514.pdf)。
  - Claude 生成坐标、武器建议和法律依据，来自 WaPo 及二手转述，见 [WaPo](https://www.washingtonpost.com/technology/2026/03/04/anthropic-ai-iran-campaign/)。
- 说法冲突：
  - 2024-02 的"85"：Bloomberg 原文说的是 85 次以上**打击**，部分媒体写成 85 个**目标**，见 [The Register](https://www.theregister.com/2024/02/27/us_military_maven_ai_used/)。
  - Google 抗议的签名人数：4,000 以上与 4,600 以上两种说法，见 [Fortune](https://fortune.com/2018/06/02/google-pentagon-drone-deal-protests)。
  - Bloomberg 的 Minab 调查报道：日期有 2026-09-18 和 09-20 两种说法。
  - Minab 死亡人数：123 名儿童与"至少 186 名学生和教师"两种说法。
- 北约强调 MSS NATO 与"NGA Maven Warfighter Support System"是两个不同的系统，见 [DefenseScoop 2025-04-14](https://defensescoop.com/2025/04/14/nato-palantir-maven-smart-system-contract/)。撰稿时需要区分 NGA 的 GEOINT Maven（计算机视觉模型）和 Palantir 的 MSS（平台）。

### Inferences
- Maven 的核心价值是让"杀伤链"实现**工业化和规模化**，代价是人工审查的密度下降。Minab 事件中平民伤害评估人员从约 10 人减到 1 人，就是这一权衡的具体体现。
- 盟国使用方面：北约 ACO 已确认；乌克兰是作为美方目标情报的**接收方**，而不是 MSS 的直接用户（NYT 报道称它使用不依赖美国敏感情报的版本）。英国等其他国家的采用情况没有找到证据。

### Gaps
- Claude 被逐步移出 Maven 的情况：2026-02-28 的行政令要求在六个月内完成过渡，最终是否完成及替代模型是什么，均未查到。
- 2026-09 是否按期完成"正式项目"转换，没有找到确认。
