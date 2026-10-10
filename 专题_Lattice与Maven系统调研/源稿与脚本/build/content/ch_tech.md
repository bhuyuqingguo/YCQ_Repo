# 四、关键技术剖析：两系统的“硬核”在哪里

:::lead
本章面向技术读者，按八个技术专题拆解 Lattice 与 Maven 智能系统（MSS）的核心机制：边缘数据网格与 DDIL 通信、多源融合与航迹关联、AI 目标识别与模型管线、本体与工作流、人机协同与自主等级、大模型代理、跨密级交付与安全、开放接口与生态。Lattice 一侧的主要依据是 Anduril 在 GitHub 公开的官方 Python SDK（由 Lattice OpenAPI 规范自动生成）和 Lattice Mesh 专利，属一手技术证据；MSS 一侧没有可读取的代码，主要依据 Palantir 产品文档、NGA 合同公告、北约新闻稿和 CSIS、CSET 等智库材料。我部研判，两系统的技术重心分处杀伤链两端：Lattice 的硬核在“断续链路下的实时实体同步与任务确认”，MSS 的硬核在“上百个数据源的对象化与看板式目标流程”；两者共同的短板是缺乏独立的效能与安全评估，且彼此之间没有公开的数据映射规范。各节末给出“技术判读”。
:::

## （一）边缘数据网格与 DDIL 通信

### 设计前提：链路不可靠是常态

Lattice Mesh 的设计目标写在 Anduril 的公开表述中：一个“已连接全球数千个防务系统的去中心化网络”，专为在降级环境下实现安全的点对点数据共享而构建，通过对数据路径排定优先级，在平台、作战域和合作伙伴之间分发数据[@la_x_mesh,la_ua_cdao]。这是公司口径。可核查的技术依据来自两处：一是 Lattice Mesh 专利 US 10,506,436（公开号 US 2020/0068404），二是官方 SDK 中与传输、订阅和存储相关的接口约定[@la_patent_436,la_patent_pub,la_sdk_ref]。

DDIL 是美军对“拒止、降级、时断时续、带宽受限”通信环境的统称。对一个前沿传感器—效应器网络而言，这意味着三个工程问题：带宽不足时先传什么，链路中断后如何补齐，节点被缴获后如何止损。Lattice 专利和 SDK 对这三个问题都给出了可识别的答案。

### 专利要点：实时优先、逐跳授权、密钥不落盘

专利文本给出三项设计原则[@la_patent_436]。第一项是实时优先：“实时数据是系统的优先级，回填只使用剩余带宽”。网络在链路性能波动时首先保障当前态势的传输，历史数据和补发数据只占用剩余容量。对反无人机这类以秒计的交战，这一取舍直接决定了航迹能否及时到达火控节点。第二项是点对点授权路由，每条转发路径都需要授权，网络中不存在默认可信的中继。第三项是密钥不落盘，普通节点的密钥只保存在内存中，不写入永久存储，节点断电或被缴获后密钥随之消失[@la_patent_436,co_patent_mesh]。

专利描述的是设计意图。Mesh 的传输层协议、同步模型（例如是否采用 CRDT 一类的无冲突复制数据类型）以及“后写者胜”之外的冲突消解机制，均无公开描述。一篇个人博客称 Mesh 使用 gossip 协议、在每个节点保存资产数据库、网络可以自愈，该说法无法核实[@la_phil_blog]。

### SDK 侧证据：存储转发与带宽节约

SDK 从接口一侧印证了“节点本地存储加跨节点复制”的结构。对象接口默认只列出本节点上的对象，参数 all_objects_in_mesh 为真时列出 Mesh 中所有环境节点上的对象；last_updated_at 字段记录的是对象“到达持有它的节点的时间”[@la_sdk_ref,la_dev_objects]。这一字段语义说明，同一对象在不同节点上有各自的副本和到达时间，节点之间是存储转发式复制。单个对象最大 1 GiB，带 expiry_time 时效；获取接口支持 RFC 9218 优先级头和压缩[@la_sdk_ref]。图像、文档和模型文件因此可以按优先级在网格中分发。

实体订阅接口有三项面向 DDIL 的约定[@la_sdk_ref]。长轮询会话中，如果客户端落后超过“环境中实体总数的 3 倍”，会话会被服务端终止，客户端需要重新同步，避免慢节点拖垮整个网格；SSE 流“自动从临时断连中恢复，从断点继续”；订阅时可以用 components_to_include 只取需要的组件，并用过滤语句（Statement）筛选实体，该过滤器“镜像 gRPC 的 StreamEntityComponents 端点”。消费者模式下，客户端先收到全部 PREEXISTING 事件，再接收增量，默认每 30 秒一次心跳[@la_sdk_ref]。

实体层的强制时效同样服务于 DDIL。发布实体时 expiry_time 为必填，“必须在未来，但距当前时间少于 30 天”[@la_sdk_entity]。链路中断后，过期数据自动退出共用作战图，断线节点重新接入时不会把陈旧航迹当作当前态势回灌。视频接口区分边缘与云：MPEG-TS 接入“只在边缘封闭网络中支持”，Lattice 运行在“经公共互联网访问的云环境”时可能被禁用[@la_sdk_ref]。这一限制说明 Anduril 把边缘封闭网络和云端视为两种部署形态，并按形态裁剪功能。

上述机制汇总于{tab:t_tech_mesh}，Mesh 在 Lattice 六层架构中的位置见{fig:d_lattice_arch}。

!table t_tech_mesh|Lattice Mesh 面向 DDIL 的机制与证据|本报告依据 Lattice Mesh 专利、lattice-sdk-python 接口参考与公开报道整理|30,48,48,34
DDIL 问题|Lattice 对应机制|作战含义|证据性质
带宽不足时先传什么|实时数据优先，回填只用剩余带宽；对象获取支持 RFC 9218 优先级头[@la_patent_436,la_sdk_ref]|航迹与告警先于历史数据和大文件到达|专利与一手 SDK
链路中断后如何补齐|SSE 断点续传；对象按节点存副本，记录到达时间[@la_sdk_ref]|断线节点恢复后补齐增量|一手 SDK
慢节点拖累全网|客户端落后超过实体总数 3 倍即终止会话[@la_sdk_ref]|以重新同步换取整体时效|一手 SDK
陈旧数据回灌|实体 expiry_time 必填且少于 30 天[@la_sdk_entity]|过期航迹自动退出作战图|一手 SDK
订阅流量过大|按组件订阅加过滤语句，镜像 gRPC 端点[@la_sdk_ref]|前沿节点只收本区域、本任务所需字段|一手 SDK
节点被缴获|逐跳授权路由；普通节点密钥只存内存[@la_patent_436]|降低密钥泄露与冒充节点风险|专利，未见实测
传输协议与同步模型|gossip、自愈等说法[@la_phil_blog]|无法评估|弱源，待核
!end

### 硬件承载与部署实证

Mesh 运行在 Anduril 的边缘计算硬件上。2025 年 5 月发布的 Menace-T 是两箱式 C4 套件，一名操作员几分钟即可架设，基于被收购的 Klas 公司 Voyager 坚固计算硬件，运行 Lattice Mesh，可承载第三方边缘 AI 软件栈；Menace-X 面向远征和动中通[@la_tc_menace,la_everythingrf_menace]。Menace 同时被定为 Palantir 边缘软件的首选硬件[@la_dc_menace]。Ivy Sting 1 中，Lattice Mesh 运行在坚固的 Voyager 边缘计算套件上[@la_bd_ivysting1]。

部署实证有四项。2024 年 12 月 CDAO 授予 Anduril 1 亿美元生产型 OTA，目标是把基于 Lattice Mesh 的边缘数据网格扩展到断连和分布式系统，授标时网格已“在多个军种和作战司令部运行”[@la_ds_cdao,co_insidedef_222723]；太空军太空监视网现代化合同以 Lattice 作为弹性网状网络[@la_ds_ssn]；Anduril 英国公司在英国陆军“阿斯加德”项目中演示了从前线到司令部的边缘数据网格[@la_die_asgard]；陆军 NGC2 中 Lattice Mesh 是第 4 步兵师的数据骨干[@la_bd_ivysting1]。据 Anduril 称，Ivy Sting 5 把数据网格扩大到原来的 3 倍，连接 65 个以上战术边缘节点，每辆车、每个指挥所和每名士兵都是 Mesh 节点，在卫星和商用通信失效时继续工作[@la_anduril_scaling,co_anduril_scaling]。后两项数字只有公司来源。

!photo ivysting_9448307|第 4 步兵师在卡森堡开展“常春藤之刺”系列 NGC2 演习（2025 年 12 月）。该系列演习中，Lattice Mesh 运行在车载与指挥所边缘计算节点上，承担师级数据骨干|美国陆军（DVIDS），美国政府作品

### 与战术数据链的关系

Lattice 的数据模型直接吸收了美军战术数据链的概念。tracked 组件中的航迹质量为 0—15 级，number_of_objects 字段注释写明“在某些语境下称为强度（Strength），见 Link 16”[@la_sdk_tracked]；实体带有 transponder_codes（应答机与敌我识别代码）和“遵循既有标准”的 symbology 组件[@la_sdk_entity]；任务生命周期中的 ACK、WILCO 沿用战术通信的确认语义[@la_sdk_task_status_status]。这些设计使 Lattice 实体与 Link 16 航迹报告、军标符号之间的映射成本较低。

Lattice 是否原生收发 Link 16 或 JREAP 消息，没有一手证据。只有一份二手材料称 Menace 通过包括 Link 16 在内的多条通信路径运行 Lattice[@la_phil_blog]。TAK/CoT 方面，仅见 Anduril 招聘“高级 ATAK 工程师”的信息，不能证明存在桥接产品[@la_builtin_atak]；OMS/UCI 无任何可靠来源。indicators 组件中 egressable 标识的注释为“该实体应被外发到外部来源”，并说明“由各集成决定如何外发”[@la_sdk_indicators]。我部研判，Lattice 通过集成适配层把实体翻译为外部格式，Mesh 本身承担节点间同步，与 Link 16 一类战术数据链是并行与互补关系，并不替代后者的抗干扰波形与时隙管理。

MSS 一侧没有对应的边缘网格设计。公开资料没有 MSS 在前沿战术节点、断连条件下运行的权威描述。Palantir 本体文档提到边缘端可以用轻量的“嵌入式本体”记录决策，平台也能接入物联网和边缘数据流[@mv_palantir_ontology,mv_palantir_ontology_system]，但未见其在 DDIL 条件下的部署实例。在 NGC2 中，这一缺口由 Lattice Mesh 填补，Foundry 承担云端一侧[@co_ds_2606_baseline]。

【技术判读】**Lattice Mesh 是两系统中唯一有专利和接口证据支撑的 DDIL 数据层，实时优先、存储转发、强制时效和按需订阅构成了完整的工程闭环。**其抗干扰能力的证据仍停留在设计和公司口径层面：Ivy Sting 5“通信降级下继续运行”只有公司来源，乌克兰战场上 Anduril 平台受俄方电子战干扰严重的报道则指向链路与导航层的真实短板[@la_tc_wsj]。Mesh 与 Link 16 的关系属于互补，Lattice 的价值在于把多源数据链汇入同一实体集合。

## （二）多源融合与航迹关联

### Lattice：以实体组件承载融合结果

Lattice 的融合对象是“实体”。SDK 对 Entity 的定义是“代表 Lattice 作战环境中的一个已知对象”，全部数据放在 30 余个可选组件中[@la_sdk_entity]。与融合直接相关的组件有五个。location 与 kinematics 只能二选一，航迹实体“优先使用 kinematics”，后者携带速度和加速度，是航迹外推和火控解算的输入[@la_sdk_entity]。location_uncertainty 表达定位误差。tracked 组件描述航迹质量，包括 0—15 级质量评分、sensor_hits（传感器命中数）、radar_cross_section（雷达截面积）和 number_of_objects[@la_sdk_tracked]。correlation 组件实现多传感器航迹关联。provenance 组件记录数据来源与更新时间[@la_sdk_ref]。

实体类型由 ontology 组件中的本体模板决定，公开 SDK 中共五类：航迹（TEMPLATE_TRACK）、传感器关注点、资产、地理形状和关注信号，另有 platform_type、specific_type 细化平台类别与型号[@la_sdk_ontology,la_sdk_ontology_tpl]。mil_view 组件承载敌我属性，枚举值为不明、友、敌、可疑、假定友、中立、待定，并含所处环境和国籍字段，与北约和美军通用分类基本一致[@la_sdk_milview_disp,la_sdk_milview]。实体组件模型与任务状态机的关系见{fig:d_lattice_entity_task}。

融合范围不限于空中航迹。signal 组件描述关注信号，orbit 组件承载“空间目标的轨道信息”，transponder_codes 记录应答机与敌我识别代码[@la_sdk_entity]。Varda、LeoLabs 与 Anduril 联合跟踪 Varda 返回舱的轨道机动时，数据实时输入 Lattice[@la_execbiz_varda]，太空态势数据已按同一实体模型进入融合。indicators 组件中的 simulated 和 exercise 标识允许真实数据与模拟、演习数据在同一作战图中混跑[@la_sdk_indicators]；health 组件把连接状态、健康状态和当前告警挂在资产实体上[@la_sdk_health]。融合结果因此同时包含目标信息和己方传感器的可信状态。我部推断，下游应用可依据发布节点的健康状态调整对其航迹的信任程度，SDK 未规定这一权重机制。

### 关联与去关联：自动关联器受人工约束

correlation 组件支持“N 对 1”的关联集合，一个实体为主航迹，其余为从航迹[@la_sdk_correlation]。组件中的 decorrelation（去关联）记录有一段关键注释：当“UI 中的用户判定两条航迹实际上并不相同，尽管自动关联器已将它们关联”时，系统记录这一决定，“防止关联器再次把它们关联起来”[@la_sdk_correlation]。

这段注释确认了两点技术事实。Lattice 内部存在自动关联器；人工去关联的结论对自动化具有持续约束力。多传感器融合中常见的“错误合批”问题，即两个邻近目标被合并为一条系统航迹，在 Lattice 中有明确的人工纠正入口，且纠正结果不会被下一轮自动关联覆盖。Anduril 称“每一件 Anduril 产品都内置 Lattice AI Core，在边缘完成传感器融合、目标分类和多航迹调和”[@la_airrec_socom]。结合 SDK 结构，我部推断 Lattice 采用“节点生成局部航迹、关联器合成系统航迹”的分布式融合架构。关联算法本身（门限、评分、是否使用多假设跟踪）没有公开。

### 所有权、覆写与审计

多源融合的另一个难题是传感器持续刷新与人工判断之间的冲突。SDK 的规则是：通过 API 发布的实体归发布者所有，“UI 等其他来源不得编辑或删除这些实体”；只有当 provenance.sourceUpdateTime 比现有数据更新时，更新才被接受[@la_sdk_ref]。操作员可以覆写被标为可覆写的字段，示例字段路径为 mil_view.disposition，覆写最终一致，采用“后写者胜”[@la_sdk_ref]。实体事件分为创建、更新、删除、订阅时已存在、过期后覆写五类[@la_sdk_event_type]。

这套规则把“传感器事实”和“人的判断”分层存放：位置、速度由数据源独占，敌我属性、目标优先级由人覆写。其直接产物是一条带时间戳和操作者身份的审计链，记录谁在何时把哪个目标定为敌对。这一记录的保存期限、访问权限和能否被独立调阅，公开资料没有说明。可覆写字段的完整清单也未公开。

!photo ghostx_pcc4|“项目融合—顶点 4”期间在加州欧文堡开展的 Ghost-X 无人机试验（2024 年 3 月）。据 Anduril 网站描述，Ghost-X 的指挥控制运行在 Lattice 上，其机载传感器输出可作为航迹实体进入共用作战图|美国陆军（DVIDS），美国政府作品

### MSS：以对象链接组织多源情报

MSS 的融合发生在更高层级、更长时间尺度上。据 CSIS 报道，中央司令部 2024 年的 MSS 部署接入了 179 个不同数据源，包括国家侦察卫星、ICEYE 与 Capella Space 等商业合成孔径雷达卫星，以及截获通信和电子辐射等信号情报[@mv_csis]；GlobalSecurity 依据 Palantir 演示给出“150 个以上”的数字[@mv_globalsec]。

MSS 的融合机制是“对象化”。检测结果、已知设施、打击资产、禁打对象都映射为本体中的对象，带有类型、置信度、时间、来源模型等属性，并通过链接与其他对象关联[@mv_palantir_ontology]。Palantir 在北约工业日的示例中，把外部系统 Safran.AI 生成的 12,000 个检测对象导入 MSS，用户可在共用作战图中直接调查，也可用自然语言让 AIP 代理查询“显示图-22 的检测结果”[@mv_palantir_blog_nato,co_pltr_blog_nato]。同一目标的图像、信号、历史记录和地理信息因此可以在一个对象下关联查询，目标分析员无需在多个终端间人工比对。

MSS 的航迹级关联算法、全动态视频与友军跟踪的接入方式均无公开说明[@mv_csis]。两系统在融合机制上的差异集中在三处。时间尺度上，Lattice 处理秒级刷新的实时航迹，MSS 处理小时到年尺度的情报对象。冲突处理上，Lattice 有显式的去关联和所有权规则，MSS 的对象合并与去重规则未公开。时效控制上，Lattice 强制设定 30 天以内的过期时间，MSS 未见系统性的数据保鲜机制。

Minab 学校遇袭事件暴露了后一项差异的代价。据彭博社引述五角大楼内部调查，该地点在旧数据库中仍被标为伊斯兰革命卫队设施，输入 Maven 后被列为“第一天推荐目标”，部分用户以为 Maven 会发现过期记录[@mv_bloomberg_minab,mv_gizmodo_minab]。Palantir 事后称“不对底层数据负责”，此后增加了对底层情报中“取消资格因素”的复核[@mv_gizmodo_minab,mv_rs_palantir]。

【技术判读】**Lattice 的融合设计在航迹层面完整且可审计，自动关联器、人工去关联、所有权与覆写规则在 SDK 中有明文约定；MSS 的融合优势在于数据源广度和对象链接，但缺少对底层记录时效的系统性校验。**两系统在融合环节的风险类型不同：Lattice 的风险在关联算法未经独立测试，MSS 的风险在过期数据经对象化后获得了与新数据相同的呈现权重。

## （三）AI 目标识别与模型管线

### 管线分工：模型归 NGA，平台归 Palantir

2022 年 Maven 拆分后，整个 AI 开发流水线移交国家地理空间情报局（NGA），作战平台 MSS 由 CDAO 与陆军承担，Palantir 提供平台[@mv_ds_2024_03,co_bd_2204_nga]。2023 年 11 月 NGA Maven 成为正式采购项目[@co_defdaily_nga_por]。2026 年 3 月 Feinberg 备忘录把 MSS 系统管理权从 NGA 移交 CDAO 新设的项目办公室，NGA 保留模型流水线和 GEOINT 产品治理[@co_ds_2604_transition,mv_ds_feinberg1]。管线在 MSS 七层架构中的位置见{fig:d_maven_arch}。

NGA 管线由标注、集成与认证三个环节构成。标注环节，2024 年 7 月 29 日 NGA 授予 Scale AI 约 2,400 万美元、为期一年的“NGA Maven 数据标注服务过渡”固定价格合同（合同号 HM047624C0047），NGA 另一条公告写的是“修改 2,400 万美元后总值 1.3 亿美元”，两者关系不明[@mv_nga_contracts]；2024 年 9 月 NGA 宣布约 7 亿美元的数据标注竞标，同时推动标准化建模[@mv_bd_2024_09_label,mv_d1_2024_09]；2025 年 11 月 Enabled Intelligence 赢得 SEQUOIA“AI/ML 数据标注即服务”合同，单一授标 IDIQ，上限 7.08 亿美元，订货期最长 7 年，用于 GEOINT 计算机视觉的目标检测、跟踪和分类标注，合作方包括 BAE、Vantor 和 Whiteboard Federal[@mv_bd_sequoia,mv_ei_release]。落败的 Scale AI 向 GAO 抗议于 2026 年 1 月下旬被驳回，后起诉至联邦索赔法院，授标未被推翻[@mv_orangeslices,co_orangeslices_protest]。

集成环节由 ECS 承担，ECS 自 2017 年起担任 NGA Maven 项目的“AI 互操作集成商”（AI3）[@mv_execbiz_ecs]。认证环节由 AGAIM 试点（GEOINT AI 模型认证与评估）承担，提供标准化的评估和风险管理流程；NGA 官方明确表示不希望 AGAIM 变成“运行授权（ATO）式”的排队审批[@mv_fnn_agaim]。供应链方面，NGA 于 2023 年就 Maven 的 AI/ML 供应链风险发布征询，理由是对下级供应商缺乏可见度[@mv_bd_supplychain_2023]。

!table t_tech_aipipe|NGA Maven 模型管线各环节|本报告依据 NGA 合同公告、Breaking Defense、Federal News Network 等整理|24,46,50,40
环节|承担方与合同|已知机制|公开空白
数据标注|Scale AI 过渡合同约 2,400 万美元；Enabled Intelligence SEQUOIA 上限 7.08 亿美元[@mv_nga_contracts,mv_bd_sequoia]|GEOINT 目标检测、跟踪、分类标注；推动标准化建模[@mv_bd_2024_09_label]|标注规范、样本规模、对手样本覆盖
集成与互操作|ECS，AI3 角色，2017 年起[@mv_execbiz_ecs]|多供应商模型接入与互操作|模型接口规范未公开
评估与认证|NGA AGAIM 试点[@mv_fnn_agaim]|标准化评估与风险管理，避免 ATO 式排队|评估指标与结果未公开
产品标注|NGA 机器生成 GEOINT 标签[@mv_bd_nohands]|注明 AI 参与类型与程度；模板化产品分发“无人工经手”|MSS 目标卡片是否有同类标注
平台接入|MSS 本体与第三方模型[@mv_palantir_blog_nato]|检测结果作为对象写入平台|对象写入的置信度与来源字段规范
供应链治理|NGA 2023 年征询[@mv_bd_supplychain_2023]|评估下级供应商风险|评估结论未公开
!end

{tab:t_tech_aipipe}显示，管线中公开程度最高的是合同与承包商，最低的是评估指标与结果。Maven 早期采用多供应商并行的模式，经 ECS 渠道接入多家公司的识别工具[@mv_execbiz_ecs,mv_itpro]；2024 年以后标注集中到单一大额合同，模型评估集中到 AGAIM，管线由分散试验转向标准化生产。SEQUOIA 标注合同上限 7.08 亿美元，高于 2024 年 5 月 MSS 原型合同的 4.8 亿美元[@mv_bd_sequoia,mv_ds_2024_05]，政府在模型数据侧的投入规模已与平台侧相当。

### 机器生成 GEOINT 标注

NGA 局长惠特沃斯 2025 年 6 月称，NGA 在所有 AI 生成的产品上加注“machine-generated GEOINT”（机器生成的地理空间情报）模板标签，在这类模板化产品的分发过程中“没有人工经手”；标签注明 AI 参与的类型和程度，NGA 可能是 18 个情报界成员中第一个常规化使用此类标签的机构[@mv_bd_nohands]。惠特沃斯还表示，Maven 下一阶段要加入“推理”能力，从识别物体走向预测和发现威胁，但向作战司令或总统汇报前仍需人工佐证[@mv_meritalk_nga,mv_execgov_predict]。

这一标签制度把“AI 参与了多少”作为产品元数据随情报流转，下游用户可据此调整信任程度。它适用于 NGA 的 GEOINT 产品。MSS 中的目标卡片、排序结果和坐标是否携带类似的 AI 贡献标注，公开资料没有说明。我部研判，标签制度在 NGA 产品线内建立了 AI 产出的可追溯性，但这一可追溯性在进入 MSS 目标工作流后能否延续，是 Maven 体系中可审计性的关键断点。

### 准确率：唯一公开数据不利

彭博社 2024 年援引 XVIII 空降军军官称，测试中 Maven 识别物体的正确率约 60%，与其合作的人类分析员约 84%；遇到某些物体或雪天图像时，Maven 的正确率“可能低于 30%”[@mv_bloomberg_2024,mv_batch]。Airwars 报道称，在西伊拉克天气多变的沙漠地形中，准确率可降到 30% 以下[@mv_airwars_first]。另有“乌克兰每平方公里约 10 个错误检测”“从 70% 降到 30%，有时 10%”等说法流传，均无法溯源[@mv_douwe,mv_escudo_failing]。

60% 对 84% 是 2023—2024 年单项物体识别测试的结果，早于加入大模型的 2026 版本。2025—2026 年的计算机视觉模型准确率、误报率和 AGAIM 评估结果均无公开数据[@mv_csis]。同一彭博社报道给出的效率数字是：一名资深目标官借助 Maven 每小时可签批多达 80 个目标，不用时约 30 个[@mv_bloomberg_2024]。识别正确率与审批吞吐衡量的是不同环节，两组数据并存说明 MSS 的增益主要来自流程组织，检测精度并未领先人工。

Lattice 一侧的识别能力证据更少。公司称 AI“识别威胁比人类操作员更准确”，没有任何独立测试数据[@la_airrec_socom,la_popsci]；计算机视觉模型的架构、训练数据和准确率指标均未公开[@la_sdk_ref]。CBP 自主监视塔是 Lattice 识别能力运行时间最长的场景，检测概率、虚警率等效能指标从未公开[@la_cbp_por,la_mittr_towers]。

【技术判读】**Maven 体系的模型治理在制度上领先于 Lattice：标注、集成、认证分属不同承包商和政府机构，产品带机器生成标签，政府保有训练数据和模型评估的控制权。**治理制度的完备并未转化为可公开验证的精度优势，唯一公开的识别准确率明显低于人工；Lattice 的边缘识别则既无治理制度说明，也无精度数据。两系统在“AI 看得准不准”这一问题上，均缺乏可供第三方复核的证据。

## （四）本体与工作流

### Palantir 本体：对象、链接与动作

Palantir 本体把数据源映射为对象、属性和链接，并对“动作”（action）建模，支持把决策实时写回运营系统和边缘系统[@mv_palantir_ontology,mv_palantir_ontology_system]。在 MSS 中，检测、设施、目标、打击资产、禁打对象都可以是本体对象；“提名为目标”“批准打击”“分配资产”是作用于对象的动作。动作的执行者、时间和前后状态由平台记录，这为目标决策提供了可审计的结构化轨迹。

本体设计使识别模型成为可替换部件。Palantir 控制对象模型和工作流，模型供应商只需按接口输出检测对象。北约演示中第三方 Safran.AI 检测对象直接进入 MSS，即为一例[@mv_palantir_blog_nato]。这一“平台加可插拔模型”的结构，是 MSS 在 2024 年后快速吸纳第三方模型、2026 年据报更换大模型供应商的技术前提[@mv_aca_iran]。

### Target Workbench：看板式目标流程

MSS 中辨识度最高的模块是 Target Workbench。Palantir 产品资料称，其界面以看板（Kanban）形式组织，各列对应目标定位流程的各个阶段，阶段名称可按单位自身流程术语定制，系统支持禁打清单（NSL）集成[@mv_target_workbench]。每个目标是一张卡片，随分析、核查、审批、交战和评估在列间流转。看板与 F2T2EA 各阶段的对应关系见{fig:d_maven_workflow}。

CSIS 依据国防部演示描述的操作流程是：操作员选中 AI 检测到的目标，按到达时间、距离、燃油等约束比较附近的打击资产，下令打击，再通过 ISR 跟踪打击效果[@mv_csis]。二手分析把全链路概括为“检测、行动方案、资产选择、打击、毁伤评估”，并称排序后的目标数据交给先进野战炮兵战术数据系统（AFATDS）等火力支援系统[@mv_cybershafarat,mv_battlepolicy]。分析人士范鲁认为，射击诸元由 AFATDS 和弹道计算完成，大模型在这一环节几乎不起作用[@mv_vanroo]。

从现有描述看，MSS 的“武器—目标配对”是基于时间、距离、燃油、弹药等约束的资产推荐与比较。配对算法的实现、是否计入毁伤概率和附带损伤估计、毁伤评估模块如何回写目标对象，均无权威公开说明[@mv_csis]。MSS 与 AFATDS、TAK 的官方接口说明同样未找到。

看板设计的作战效果在于把联合目标定位流程（JP 3-60）中串行的多级会签变为可视化、可并行的流转。XVIII 空降军以约 20 人的目标单元达到 2003 年伊拉克战争中 2,000 多人时敏目标单元的效能[@mv_cset_coalition,mv_csis]，这一对比来自演习，条件不同，应视为数量级示意。并行化同时意味着单个目标获得的人工注意力下降。

### Lattice 实体与任务：另一种“动作”模型

Lattice 用“任务”表达动作。任务对象包含 specification（以 protobuf Any 封装的具体任务定义）、author（发起人）、relations（父任务与受领者）、initial_entities（任务涉及的初始实体，文档举例为“一个目标实体、一个限入区实体”）、重试策略、投递约束和执行约束[@la_sdk_ref]。资产实体通过 task_catalog 组件声明自己能执行哪些任务[@la_sdk_task_catalog]，调度逻辑因此与具体平台解耦。

两套模型的取向不同。Palantir 本体是语义中心、持久、可审计的，关心对象与情报、规则、计划之间的关系；Lattice 实体是航迹中心、实时、短寿命的，关心目标此刻在哪里、谁在跟踪、能派谁去。两者对比见{tab:t_mv_onto_vs_entity}。在 NGC2 Ivy Sting 1 中，第 4 步兵师的师级目标处理流程从师部到炮位运行在 Lattice Mesh 和 Target Workbench 上，Target Workbench 负责管理、跟踪每个目标并分配资源[@la_bd_ivysting1,mv_bd_ivysting]。这是两种模型在同一流程中协同运行的唯一公开实例。实体与对象如何转换、两套模型如何保持一致，没有任何公开文档[@mv_lattice_entity,co_ds_2606_baseline]。

### 开放应用层：Open DAGIR

CDAO 2024 年启动的 Open DAGIR 计划，旨在把其他厂商的应用接入 MSS 的数据层，使 CJADC2 不必全部依赖 Palantir 自有应用；Breaking Defense 指出 2024 年公布的 CJADC2 最小可行能力是“最低限度”的[@mv_bd_opendagir]。第三方应用读写的仍是 Palantir 本体，平台层锁定并未因应用层开放而消除。

【技术判读】**MSS 的技术核心在本体加看板：本体把多源情报转为可链接、可执行动作的对象，看板把联合目标定位流程并行化，二者共同解释了“20 人顶 2,000 人”的效率来源。**武器—目标配对、毁伤评估和火力交接三个模块的实现细节均未公开，MSS 在杀伤链后段对存量火控系统的依赖程度无法评估。Lattice 任务与 Palantir 动作之间缺乏公开映射，是两系统集成链路上技术风险最集中的接口。

## （五）人机协同与自主等级

### Lattice：任务生命周期中的确认语义

Lattice 任务状态的完整枚举为：已创建、已在管理器排程、已发送、机器已接收、已确认（ACK）、将遵照执行（WILCO）、执行中、等待更新、成功完成、未成功完成、已被替换、请求取消、请求完成、版本被拒[@la_sdk_task_status_status]。从“已发送”到“机器已接收”“已确认”“将遵照执行”再到“执行中”，复制的是战术数据链与语音指挥的确认语义。人机界面可据此显示一条任务在执行链上的确切位置。

并发与取消规则体现了作战约束。状态更新通过 status_version 实现乐观并发控制，“成功完成”和“未成功完成”是不可逆终态[@la_sdk_ref]。取消请求发出后，如果任务已交给执行代理，“由代理决定能否取消”，代理可用 ERROR_CODE_REJECTED 拒绝[@la_sdk_ref]。这一规定承认了物理现实：拦截弹出膛后不一定可以召回。任务状态对象另含进度、结果、预估和“任务已分配的代理”[@la_sdk_task_status]。

手动控制接口 stream_manual_control_frames 把摇杆动作以流的形式发给执行代理，每帧带纪元号和序号，用于处理多个控制会话并发和过期帧问题[@la_sdk_ref]。操作员可以随时接管单个平台。纪元号设计针对的是控制权交接时新旧指令交错的风险。

SDK 中可识别的人机交互挂钩共五类：带溯源的敌我属性覆写、对自动关联器有约束力的人工去关联、记录发起人的任务创建与取消、执行代理的拒绝权、手动摇杆控制[@la_sdk_ref,la_sdk_correlation]。七步交战流程中人与机器的分工见{fig:d_lattice_killchain}。

### 公开案例中的武器释放权

所有公开记录的 Lattice 交战案例中，开火决定由人作出。2020 年空军巡航导弹演示中，操作员先确认 Lattice 跟踪的是预期目标，再向效应器下达交战指令[@la_dn_cruise]。陆战队地基防空项目办公室明确，Anvil 可以利用传感器航迹数据自主跟踪，但“只在人工操作员下令后才拦截”[@la_marines_gbad]。陆军 EDGE23 中，一名士兵控制多架无人机，把地空导弹阵地定为敌对并授权 ALTIUS-600M 打击，系统随后自动把一架 ALTIUS 侦察型改派去做毁伤评估[@la_blog_edge23]。

我部据此把 Lattice 的人机关系归纳为：机动、感知和资源调度处于“人在回路上”（人监督、可干预），武器释放处于“人在回路中”（须经人批准）。这一归纳的边界很清楚。公开资料中没有交战规则的配置方式，没有针对一类、二类小型无人机的自动交战模式说明，也没有 Lattice 如何满足国防部第 3000.09 号指令的公开文件[@la_sdk_ref]。批评者认为 Lattice“为比人类判断更快地行动而设计”，公司材料没有解释自主致命决策的问责机制[@la_freepress]。

Lattice for Mission Autonomy（LMA）的理念是从“多人操控一个系统”转为“一人操控多个”[@la_blog_lma,la_d1_lma]。2026 年 2 月 24 日 LMA 首次在 YFQ-44A 上飞行[@la_die_cca]，YFQ-44A 已完成以惰性 AIM-120 对模拟目标的端到端超视距打击[@la_militarytimes_rolloff]。协同作战飞机的武器使用授权链路未见公开描述。

!photo yfq44_creech_2|YFQ-44A“狂怒”停放在内华达州克里奇空军基地航线上进行武器挂载，由空军实验作战部队操作（2026 年 7 月）。LMA 已在该机型上飞行，协同作战飞机的武器释放授权链路未见公开描述|美国空军，美国政府作品

### MSS：决策支持定位与审批密度

官方和主流报道把 MSS 定位为决策支持工具，目标由人类指挥官批准[@mv_csis]。中央司令部首席技术官摩尔称，2024 年 2 月打击中机器学习帮助缩小目标范围，每一步都以人工验证结束[@mv_register_2024]。中央司令部司令表示，伊朗作战中最终打击决定由人作出[@mv_letsdata]。

MSS 的人机问题集中在审批密度。目标官 Temple 估计每小时签批量从 30 个增至 80 个，并指出完全信任机器会更快，但会引入错误[@mv_bloomberg_2024]。陆军的远期目标是每小时 1,000 个高质量决策[@mv_bd_geoint2025]。Minab 事件中，中央司令部平民伤害评估团队已从约 10 人缩减到 1 人[@mv_bloomberg_minab]。批评者认为 MSS 已从决策支持变为“附带人类副署以满足法律合规的决策系统”[@mv_strat_intl]，另有文章讨论“橡皮图章问题”[@mv_medium_rubber]。

### DoDD 3000.09 的适用

国防部指令 3000.09（2012 年发布，2023 年 1 月更新）要求自主和半自主武器系统的设计让指挥官和操作员能对武力使用施加“适当程度的人类判断”，正式开发前须经高级官员审查[@mv_gao_22,mv_dodd3000]。MSS 本身不发射武器，更接近目标选择支持系统，3000.09 的高级审查不一定直接适用，问责主要依靠交战规则、JP 3-60 中的人工签批和法律审查[@co_gao_3000]。Lattice 直接向效应器下发任务，处于 3000.09 适用范围的边缘，但公开资料中没有任何针对 Lattice 或 MSS 的 3000.09 审查记录，也没有 GAO 或国防部监察长的独立评估[@mv_lawfare_book]。

!table t_tech_hmi|两系统在杀伤链各环节的人机分工|本报告依据 SDK、产品资料与公开报道分析整理；“推断”指依据接口与案例归纳|22,50,50,38
环节|Lattice|MSS|证据与空白
发现|边缘 AI Core 检测分类，机器为主[@la_airrec_socom]|CV 模型检测并对象化，机器为主[@mv_palantir_blog_nato]|两系统精度均无独立数据
定位与跟踪|自动关联器合成航迹；人可去关联[@la_sdk_correlation]|地理定位与坐标生成；据报大模型参与[@mv_wapo_2026]|MSS 坐标生成方式有争议
识别定性|人覆写敌我属性，带溯源[@la_sdk_ref]|人在看板上核查、比对禁打清单[@mv_target_workbench]|可覆写字段清单未公开
交战分配|人创建或批准任务；平台按能力目录受领[@la_sdk_task_catalog]|机器按约束推荐资产，人签批[@mv_csis]|配对算法未公开
武器释放|人工下令；代理可拒绝取消[@la_marines_gbad]|不直接控制武器，交火控系统[@mv_vanroo]|ROE 配置与自动交战模式未公开
毁伤评估|系统自动改派 ISR（EDGE23）[@la_blog_edge23]|ISR 跟踪，卡片关闭或回流[@mv_csis]|MSS 评估模块无细节
制度约束|3000.09 适用方式未见公开文件|决策支持定位；问责靠 JP 3-60 签批[@co_gao_3000]|无独立审查记录
!end

{tab:t_tech_hmi}按杀伤链环节对照两系统的人机分工。两系统在发现、定位环节均以机器为主，在识别定性与武器释放环节均由人掌握；差别集中在交战分配和评估环节，Lattice 由能力目录和自动改派承担更多调度，MSS 则以资产推荐交人决定。表中“制度约束”一行两系统均为空白，这是人机协同领域最大的公开缺口。

!photo pcc4_csa_ghost|陆军参谋长在“项目融合—顶点 4”期间听取 Anduril Ghost 无人机能力简报（加州欧文堡，2024 年 3 月）。同期演习开展了人机融合试验，是陆军评估“一人操控多机”模式的场合之一|美国陆军（DVIDS），美国政府作品

【技术判读】**两系统都把武器释放权留给人，人机风险却分处两端：MSS 的风险在机器速度提名导致人工审批密度下降，Lattice 的风险在机器速度执行压缩人工干预窗口。**Lattice 的 SDK 提供了覆写、拒绝、接管等可验证的人机接口，MSS 的人机控制则主要依赖流程与人员配置，Minab 事件说明后者在规模化运行中最先失守。DoDD 3000.09 对两系统的具体适用方式没有公开答案。

## （六）大模型代理在目标链中的角色与争议

### 已证实的能力边界

2023 年起 Palantir 把人工智能平台（AIP）的大模型代理能力引入防务产品。CSIS 提醒，Palantir 2023 年的“AIP for Defense”演示展示的是计划中的未来能力和示意场景，不能等同于已部署功能[@mv_csis]。已证实的层面有两项：北约演示中 AIP 代理可以用自然语言检索检测对象集[@mv_palantir_blog_nato]；北约明确称 MSS NATO 包含大语言模型和生成式 AI，用于情报融合、目标定位、战场态势感知、作战计划和加速决策[@mv_shape_release,mv_bd_nato_2025]。

### 美军 MSS 中的大模型：报道分歧

多家媒体报道，Anthropic 的 Claude 通过 Anthropic 与 Palantir 的合作于 2024 年末接入 Maven，用于目标优先级排序和分析[@mv_rs_iran,mv_aca_iran]。据《华盛顿邮报》2026 年 3 月 4 日报道，在对伊朗作战中，内嵌 Claude 的 MSS 为目标排序、生成坐标并建议武器[@mv_wapo_2026]；二手转述称其生成法律依据草稿，以及“提出数百个目标，进行优先排序并给出精确坐标，再由人类指挥官批准”[@mv_wapo_2026,mv_strat_intl]。“和平愿景”的说法要克制得多：Claude 主要用于把情报报告转成通俗语言[@mv_voh]。

Claude 的现状同样存在冲突。据报道，国防部 2026 年 3 月 4 日把 Anthropic 列为“供应链风险”，要求 6 个月内淘汰，起因是 Anthropic 拒绝把模型用于大规模国内监控和完全自主武器，OpenAI 等公司据报接替；Palantir 首席执行官卡普在 CNBC 上则称 Claude 仍在目标系统中运行[@mv_aca_iran,mv_ie_claude]。Claude 在 MSS 中的具体角色、是否已被替换、由谁接替，均无法从五角大楼或 Anthropic 的一手文件中证实。

Claude 经 Palantir 平台参与行动的报道还见于 2026 年 1 月 3 日委内瑞拉马杜罗抓捕行动。《华尔街日报》称 Claude 通过 Palantir 平台参与，但没有来源明确说使用的是 Maven，具体任务属于机密，Anthropic 不予置评[@mv_swj_maduro,mv_cnbc_karp]。

使用强度有官方数据。五角大楼发言人称，伊朗战事期间 MSS 非密网使用量环比增长 38%，涉密网增长 89%，按 token 计的日峰值增长 4,425%，最高约 200 亿 token/天[@mv_bd_insatiable]。这组数据说明大模型已深度嵌入日常参谋工作，但没有拆分到目标排序、坐标生成等具体用途。

### 架构位置与可审计性

从架构看，大模型作用于本体中的对象与动作：它可以查询对象集、生成排序和草案，“批准打击”等动作仍需人在界面上执行[@mv_palantir_ontology]。大模型层的供应商可以替换，这与“平台加可插拔模型”的结构一致，但替换过程本身是一个风险窗口[@co_ii_claude]。范鲁的分析指出，在“分配并射击”环节射击诸元由 AFATDS 和弹道计算完成，大模型几乎不起作用[@mv_vanroo]。大模型的增益集中在检索、摘要、排序和生成草案一侧。

可审计性是这一层的核心问题。排序依据、坐标来源、法律依据草稿能否回溯到具体情报对象和模型版本，公开资料没有说明。NGA 的机器生成标签适用于 GEOINT 产品[@mv_bd_nohands]，未见其覆盖 MSS 中大模型生成的排序和草案。

### Lattice 一侧：数据层而非推理层

Lattice 在大模型应用中承担数据层角色。DIU 2025 年 3 月启动的 Thunderforge 项目由 Scale AI 牵头，为印太司令部和欧洲司令部开发 AI 辅助的作战与战役规划，Lattice 提供数据共享层，配合微软和 Scale 的大模型，采用“始终在人类监督下”的代理式工作流[@la_ds_thunderforge,la_diu_thunderforge,la_scale_thunderforge]。2026 年 Lattice 开发者平台新增面向 AI 编程智能体的“SDK skills”，用于降低应用开发门槛[@la_changelog]。未见 Lattice 在边缘交战链中嵌入大模型做决策的公开证据。

【技术判读】**大模型已进入美军目标链的“排序与草拟”环节，并以每日约 200 亿 token 的规模运行，但其对具体目标的贡献、输出的可追溯性和供应商更替状态均无一手证据。**我部研判，大模型层是 MSS 体系中透明度最低、治理制度最滞后的一层：NGA 的模型认证和机器生成标签均未覆盖这一层，3000.09 也未对其作出规定。Lattice 目前停留在为大模型提供数据的位置，尚未把大模型引入边缘交战决策。

## （七）跨密级交付、部署与安全

### Palantir：Apollo 与多安全域

Palantir 平台的跨环境交付依靠 Apollo。Apollo 是持续交付平台，负责管理承载 Foundry 和 AIP 服务的底层基础设施[@mv_palantir_platforms,mv_apollo_wp]；二手资料称其可运行在本地数据中心、边缘硬件和涉密网络上[@mv_mlq]。对军事用户而言，Apollo 的作用是让同一套软件在非密云、秘密网、北约网络等多个隔离环境中保持版本一致和持续更新。

MSS 的部署形态有三项可确认事实。NGA 称 Maven 跨“三个安全域”运行，通过 35 个以上军种和作战司令部工具服务约 2 万名活跃用户（2025 年 5 月）[@mv_bd_geoint2025]，原文未说明具体是哪三个网络，没有公开来源证实 MSS 在 JWICS 上有实例。海军陆战队通过企业许可，在 SIPRNet 影响等级 6（IL6）云上“无限量访问”MSS[@mv_ds_maradmin,mv_usmc_release]。MSS NATO 于 2026 年 6 月 22 日达到全面作战能力，获准在北约机密网络运行，数据存放在北约自有数据中心[@mv_shape_foc]。伊朗战事期间非密网与涉密网使用量分别增长 38% 和 89%，印证了 MSS 同时运行在不同密级的网络上[@mv_bd_insatiable]。

MSS 托管在哪家商业云、是否经由联合作战云能力（JWCC）合同，没有公开信息。Feinberg 备忘录提到研究与工程副部长将接任 MSS“商业云基础设施”的授权官，说明 MSS 至少部分运行在商业云上[@mv_ds_feinberg2]。2024 年 12 月两家合作公告描述的数据链路是：战场数据由 Lattice 和 Menace 采集传输，进入 Palantir AIP 为 AI 训练做准备，覆盖 SCI/SAP 等最高密级[@la_bnn_palantir,la_bw_palantir]。

### Lattice：字段级密级与认证空白

Lattice 的安全设计在数据模型和认证层可以确认。data_classification 组件给每个实体一个默认密级，并允许在 fields 列表中为单个字段设置不同密级，字段级设置“始终优先于默认值”；密级分为非密、受控非密、秘密、机密、绝密五级，另有附加控制标记，SDK 的示例是“TOPSECRET//NOFORN//FISA”被解析为第 5 级，附加标记为 NOFORN 和 FISA[@la_sdk_classification,la_sdk_class_info,la_sdk_class_level]。认证采用 OAuth2 客户端凭证流程，客户端以 client_id 和 client_secret 换取短时令牌[@la_sdk_ref,la_sdk_readme]。

逐字段密级加 egressable 标识，使同一目标实体的位置、型号判断、来源可以分别标密，外发给盟军时只放行可放行字段。数据模型“能表达”多级安全，不等于系统“已获准”跨密级运行。Lattice 的授权运行等级、是否达到 IL5 或 IL6、能否在 SIPR 或 JWICS 上运行、采用何种经认证的跨域解决方案（CDS），均无公开资料[@la_sdk_classification]。MSS 的联盟“可释放性”机制，即按标签控制哪些数据可共享给哪些盟友，同样没有公开细节。

!photo pcc6_2|“项目融合—顶点 6”演习现场（加州欧文堡，2026 年 7 月）。第 4 步兵师在该演习前以 NGC2 完成整师上线，多厂商应用共用数据层的安全认证问题在原型阶段即被陆军首席技术官列为“极高风险”|美国陆军（DVIDS），美国政府作品

MSS 的授权运行与治理关系在 2026 年重新划定。Feinberg 备忘录要求把 MSS 转为正式采购项目，系统管理权从 NGA 转到 CDAO 下新设的 MSS 项目办公室，所有 MSS 合同转入陆军企业协议载体，研究与工程副部长接任商业云基础设施的授权官[@mv_ds_feinberg1,mv_ds_feinberg2]。2026 年 8 月任命的项目主任索尔斯伯里上校，任务之一是推动 MSS 与 C2 的整合[@mv_ds_solsbury]。北约一侧由 NCIA 采办、SHAPE 运行 MSS NATO[@mv_ncia_2025]。Lattice 没有对应的单列项目办公室和授权官信息，其运行授权分散在嵌入它的各个项目之中[@co_army_291074]。

### 陆军首席技术官备忘录

两系统联合方案最直接的安全证据是一份负面评估。2025 年 9 月 5 日，陆军首席技术官 Gabriele Chiulli 在备忘录中写道，NGC2 原型应被视为“极高风险”，因为对手很可能获得“持续、无法察觉的访问”；他写道：“我们无法控制谁看到什么，无法看到用户在做什么，也无法验证软件本身是安全的。”[@la_reuters_memo,co_reuters_memo]据报道，备忘录指出任何授权用户都可不受限制地访问全部应用和数据，第三方应用未经审查，一个应用有 25 个高危漏洞，另有三个应用各有 200 多个缺陷待审[@co_whbl_memo,la_yahoo_memo]。

各方回应是：Anduril 称这是“过时的快照”；Palantir 称“在 Palantir 平台中没有发现漏洞”；陆军首席信息官 Leonel Garciga 称备忘录属于分诊流程的一部分，陆军随后表示关键缺陷已缓解[@la_bd_memo,co_aol_memo]。Palantir 股价当日下跌约 5%—7%[@co_tv_pltr_fall]。截至 2026 年 10 月，未见公开的整改结论文件。陆军在九个月后把“Lattice 加 Foundry”定为 NGC2 通用数据层基线[@co_ds_2606_baseline]，并以 18 亿美元合同推向第 I 军[@co_ds_2610_ngc2]。

备忘录指出的三类问题（访问控制、用户行为可见性、第三方应用供应链）是“开放平台加多家应用”架构的固有风险。当该架构成为全军基线后，单点漏洞的影响范围从一个师扩大到整个陆军；若 MSS 的目标输出经 NGC2 数据层下达至 Lattice 边缘效应器，任一第三方应用的漏洞都可能成为从企业层到效应器的攻击路径[@co_reuters_memo]。

【技术判读】**MSS 已有 IL6、北约机密网等可确认的多域部署，Apollo 提供了跨隔离环境的交付机制；Lattice 在数据模型层预置了字段级密级和外发控制，但系统级认证完全不透明。**陆军首席技术官备忘录是两系统联合方案唯一一份来自军方内部的正式安全评估，结论为“极高风险”，此后的“已缓解”表态缺乏公开整改文件支撑。我部研判，安全认证是两系统由原型转入全军基线过程中证据最薄弱的环节。

## （八）开放接口与生态

### Lattice SDK：开放接口、封闭实现

Lattice SDK 于 2024 年 12 月 10 日公开发布[@la_dd_sdk]。开发者文档说明，v1 原生支持 gRPC，v2 使用 OpenAPI，Anduril 建议升级到 v2，v2 新增 StreamEntities[@la_changelog_20250724,la_docs_java]。SDK 语言覆盖 Python、JavaScript/TypeScript、Java、Go、C++ 和 Rust；2025 年 7 月 24 日 C++ 仓库归档，protobuf 定义改由 Buf Schema Registry 托管；2026 年 10 月 5 日发布 Rust SDK[@la_github_anduril,la_sdk_cpp,la_changelog]。Python SDK 由 Fern 工具从 OpenAPI 规范生成[@la_fern_mirror]。2026 年开发者平台新增 Developer Console、Schema Registry 和 Video API，Video API 于 2026 年 9 月 9 日进入预览[@la_changelog]。

v2 公开接口分为实体、任务、对象、认证、视频五组，定义了三种标准接入模式：传感器或 C2 适配器作为生产者发布实体；用户界面或分析程序作为消费者订阅实体；机器人或效应器作为代理，先发布带能力目录的资产实体，再接收执行、取消和完成请求并回报状态[@la_sdk_ref]。三种模式划分了第三方接入路径：传感器厂商做生产者，应用开发者做消费者，无人平台和武器厂商做代理。

第三方接入有三项实例。陆军 IBCS-M 为期 7 天的尤马试验中，Lattice 在数小时内接入了一个此前未公开的传感器和效应器，实弹拦截 4 中 4[@la_ds_ibcsm]；中央司令部“沙漠守护者 1.0”演习中，参演官兵依靠 API 和 SDK 文档集成自己的系统，部分是实时完成的[@la_ocbj_partners]；2026 年 10 月 1 日 ORIGIN 公司 BLAZE 拦截器以代理模式集成进 Lattice[@la_overt_blaze]。

许可条款决定了这套 SDK 的性质。许可是有限、可撤销、免版税的，只能用于为“兼容的 Lattice 实现”开发应用，明确禁止用它构建其他 SDK 或不兼容的实现[@la_sdk_license,la_buf_license]。政府和第三方获得的是接口使用权，无法据此开发替代实现。陆军把“避免厂商锁定、为传感器和升级留出空间”列为通用数据层的关键考虑[@la_bd_cdl]，许可条款与这一考虑之间存在张力。

开发者计划提供“运行 Lattice Mesh、带模拟数据的环境”[@la_docs_overview]；Anduril 招聘信息称，其合作伙伴“从创新初创公司到防务巨头和世界各国军事组织”都有[@la_gc_jobs]。SDK 是否收费、开发者沙箱的准入方式和其中的模拟资产，本轮均未查明。

### A-GRA：唯一有记录的开放标准

政府参考自主架构（A-GRA）是 Lattice 唯一有明确记录的开放标准。Anduril 称 LMA 完全符合 A-GRA；YFQ-44A 在一次飞行中既运行 Shield AI 的 Hivemind，也运行 Anduril 的 LMA，并通过早期 A-GRA 实现在两套软件之间切换[@la_aviationist_hivemind]。这是美军在自主软件层面保持可替换性的直接证据。空军通过 A-GRA 使自主软件竞争持续到 2027 年，Lattice 需与 Shield AI、通用原子、洛克希德等长期竞争[@co_circleville_cca,co_aviationist_2603]。

!photo yfq44_edwards|空战司令部人员与 Anduril 技术人员在爱德华兹空军基地维护 YFQ-44A（2026 年 4 月）。该机型曾在一次飞行中通过早期 A-GRA 在 Shield AI Hivemind 与 Anduril LMA 两套自主软件之间切换|美国空军 Ariana Ortega 摄，美国政府作品

### MSS 一侧：Open DAGIR 与本体专有

MSS 的开放性体现在应用层和模型层。北约描述 MSS NATO 的开放架构可接入第三方 AI 模型、仿真工具和应用[@mv_shape_release]；CDAO 的 Open DAGIR 计划把其他厂商的应用接到 MSS 数据层[@mv_bd_opendagir]；NGA 管线让模型供应商通过标准化标注与评估进入平台[@mv_bd_2024_09_label]。本体本身是专有的，未见公开的本体模式规范。

!table t_tech_open|两系统开放性对照|本报告依据 SDK 许可、产品文档、北约与 CDAO 公开资料整理|28,44,44,44
维度|Lattice|MSS|我部判读
公开接口|SDK 2024-12 发布，v1 gRPC、v2 OpenAPI，六种语言[@la_dd_sdk,la_github_anduril]|无公开 SDK；开放架构可接第三方模型与应用[@mv_shape_release]|Lattice 接口透明度高于 MSS
第三方接入路径|生产者、消费者、代理三种模式[@la_sdk_ref]|Open DAGIR 应用接入；检测对象写入本体[@mv_bd_opendagir,mv_palantir_blog_nato]|两者都开放外围、控制核心
许可与实现|有限、可撤销，只限兼容实现[@la_sdk_license]|本体专有，模式规范未公开|替代实现均不可行
开放标准|A-GRA 已证实；Link 16 概念入模，收发未证实[@la_aviationist_hivemind,la_sdk_tracked]|未见对外标准声明|A-GRA 是唯一由政府主导的可替换点
集成速度证据|IBCS-M 数小时接入新传感器与效应器[@la_ds_ibcsm]|北约从提出需求到签约约 6 个月[@co_ds_2504_nato]|口径不同，不可直接比较
两系统互通|无公开映射文档[@co_ds_2606_baseline]|无公开映射文档|NGC2 中依赖未公开的集成层
!end

{tab:t_tech_open}对照了两系统在接口、接入路径、许可、标准和互通五个维度的开放程度。

### 生态格局

两家的生态边界在 2026 年出现交叉。在陆军 NGC2 中，两家分层合作：Lattice 承担边缘网格与实体层，Foundry 承担云端数据平台，Raft 提供数据与服务注册、数据转换和联邦工具[@co_ds_2606_baseline,co_bd_2606_baseline]。在北约增强型空中指挥控制（eAirC2）中，Anduril（以 Lattice 参评）、Palantir 与法国 Athea 正面竞争，约 9 个月评估期后择一长期实施[@co_ncia_eairc2,la_ncia_nato]。CDAO 同时持有 MSS 与 Lattice 边缘数据网格合同[@co_ds_cdao_mesh]。没有 GAO 报告、国防授权法条款或国会听证专门讨论 NGC2 或 MSS 的数据权利与接口所有权问题[@la_bd_cdl]。

【技术判读】**Lattice 的开放程度在接口层高于 MSS，在实现层与 MSS 同样封闭；两系统都以“开放外围、控制核心”构建生态。**A-GRA 证明了政府可以在自主软件层强制保持可替换性，但这一做法尚未延伸到 C2 数据层和目标工作流层。我部研判，NGC2 把“Lattice 加 Foundry”定为全军基线后，两家私有数据模型之间未公开的映射层将成为未来替换成本最高的部分。

:::judge 关键技术研判要点
- Lattice 的核心技术资产是面向 DDIL 的实体同步与任务确认机制，专利与 SDK 证据完整，抗干扰实战效果未获证实。
- MSS 的核心技术资产是本体对象化与看板式目标流程，效率增益来自流程并行化，识别精度的唯一公开数据低于人工。
- 航迹融合方面，Lattice 有明文的关联、去关联、所有权与过期规则；MSS 缺少底层记录时效校验，Minab 事件即源于此。
- NGA 模型管线在标注、集成、认证、产品标签上形成了制度化治理，但这一治理未覆盖 MSS 中的大模型排序与坐标生成。
- 人机关系上，两系统均保留人的武器释放权；MSS 的风险在审批密度下降，Lattice 的风险在干预窗口压缩，3000.09 的适用方式均无公开文件。
- 大模型层是透明度最低的一层，Claude 的角色与替换状态缺乏一手证据，每日约 200 亿 token 的使用规模缺乏用途拆分。
- 安全认证是两系统由原型转为全军基线过程中证据最薄弱的环节，陆军首席技术官“极高风险”备忘录未见公开整改结论。
- 两系统都“开放外围、控制核心”，实体与对象之间没有公开映射，是联合链路技术风险与锁定风险最集中的接口。
:::
