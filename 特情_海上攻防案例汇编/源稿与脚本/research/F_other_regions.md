# F组调研说明：波罗的海/北海、印度洋/阿拉伯海、加勒比、非洲沿岸、地中海中西部、南亚、红海补充

JSON：`F_other_regions.json`（24个案例：第一轮18个保留不动并补全，第二轮新增6个）。第一轮约29次检索后额度用尽；第二轮使用12次WebSearch（4次限定commons.wikimedia.org查图，8次查新案例），WebFetch不可用，因此所有事实仍来自检索结果的摘要与链接，未打开原文页面。未取得之处在字段中写“未检索到公开记录”或“待核”。新增案例带`"round": 2`字段，原18案带`"round": 1`。

## 1. 收录案例（24个）

| # | case_key | 类别 | 可信度 | 轮次 |
|---|---|---|---|---|
| 1 | bs_balticconnector_2023_10_08 | 海上小岛（离岸/海底设施） | B | 1 |
| 2 | bs_eagle_s_estlink2_2024_12_25 | 海上小岛 | B | 1（补图） |
| 3 | bs_baltic_sentry_2025_01_14 | 远海机动编组（防卫态势） | B | 1（补图、补2026年状态） |
| 4 | bs_jaguar_su35_2025_05_13 | 远海机动编组（灰色地带） | B | 1 |
| 5 | bs_fitburg_2025_12_31 | 海上小岛 | B | 1 |
| 6 | bs_sweden_shadow_fleet_2026_03_05 | 远海机动编组（灰色地带） | B | 1 |
| 7 | bs_denmark_drones_2025_09_22 | 岛屿防卫 | B | 1（补图） |
| 8 | bs_belgium_drones_2025_11_06 | 周边港口 | C | 1 |
| 9 | io_chem_pluto_2023_12_23 | 远海机动编组（单舰） | B | 1 |
| 10 | io_lila_norfolk_2024_01_04 | 远海机动编组 | B | 1（补图分类页） |
| 11 | io_ruen_2024_03_16 | 远海机动编组 | B | 1（补图、改交叉引用） |
| 12 | sa_sindoor_vikrant_karachi_2025_05 | 远海机动编组（威慑） | C | 1（补图） |
| 13 | ca_southern_spear_boats_2025_09_02 | 远海机动编组（攻方视角） | B | 1（补图、补2026年后续） |
| 14 | ca_venezuela_port_strikes_2026_01_03 | 周边港口 | B | 1（补图分类页） |
| 15 | ca_tanker_blockade_marinera_2025_12_2026_01 | 远海机动编组（灰色地带） | B | 1（补“Verónica”号） |
| 16 | med_conscience_malta_2025_05_02 | 远海机动编组 | C | 1 |
| 17 | med_sumud_sidi_bou_said_2025_09_09 | 周边港口 | C | 1 |
| 18 | med_arctic_metagaz_2026_03_03 | 远海机动编组 | C | 1 |
| 19 | bs_kiel_drones_2025_09_25 | 周边港口（灰色地带） | B | 2 新增 |
| 20 | bs_gotland_bornholm_2024_2026 | 岛屿防卫（态势） | C | 2 新增 |
| 21 | io_abdullah_2024_03_12 | 远海机动编组（单舰被劫） | B | 2 新增 |
| 22 | sd_port_sudan_2025_05_04 | 周边港口 | B | 2 新增 |
| 23 | bs_charles_de_gaulle_drone_2026_02_25 | 远海机动编组（防御成功） | B | 2 新增 |
| 24 | ca_cuba_fuel_interdiction_2026_02_2026_09 | 远海机动编组（灰色地带） | B | 2 新增 |

没有A级案例：所获资料均为新闻报道与单方官方说法，没有取得官方原文或卫星影像（路透社2025-05-06苏丹港卫星图像仅见报道转述）的交叉印证。

## 2. 第二轮新增案例的归类与使用提示

- **基尔（19）**：任务要求查“基尔海军基地/港口无人机”。检索到的是2025年9月25—26日基尔一带多组无人机飞越TKMS潜艇造船厂、基尔峡湾、基尔运河、电厂、医院、州议会和海德炼油厂；次日罗斯托克海军司令部附近、桑尼茨军事基地也有目击。**所获报道均未提到基尔海军基地本身，也无国防部/海军原始通报**，故按“基尔港区与造船厂”收录，outcome为灰色地带对峙，不宜写成“海军基地遭袭”。
- **哥特兰/博恩霍尔姆（20）**：是态势案例，不是单一攻击事件。内容为博恩霍尔姆测量站GNSS干扰次数（2024年11次、2025年16次、2026年30次，经乌克兰媒体转述）、“极光26”演习（约18,000人，12个北约国家+乌克兰，bluewin）、瑞典议会一份议员动议。哥特兰防务投入“逾2亿欧元”“IRIS-T 2028年交付”等数字仅见于聚合站转引Politico，已标“待核”。**博恩霍尔姆驻军规模、该岛无人机闯入记录、奥兰群岛均未检索到**。可信度定C。
- **“阿卜杜拉”号（21）**：2024-03-12被劫，2024-04-14获释，赎金500万美元为海盗口径、船东未确认。outcome按“遭偷袭受损”填写（船被劫持，无强攻解救）。与案例11（“鲁恩”号）同周发生，已互相引用。
- **苏丹港（22）**：先查C2_redsea_merchant_ports.json及其md，**C2组只在待检索清单中列出苏丹港，未收案例**，故本组收录。主要来源是Daily Maverick、AP稿转载、Dabanga等；无人机型号、数量、伤亡数字均未检索到。该案偏离胡塞主线，如C2后续补收，请合并去重（region已填红海-亚丁湾）。
- **“戴高乐”号无人机（23）**：瑞典以电子对抗压制疑似俄罗斯无人机，防御成功。USNI（2026-02-27）、Kyiv Post（2026-02-26）等；Marine Insight一条结果标题未显示，已不收录。
- **古巴燃料拦截（24）**：2026年1月之后加勒比的海上事件主要是两类：（a）“南方之矛”小艇打击继续，累计数字已在案例13更新（2月13日3人、4月19日3人、5月4日2人）；（b）海岸警卫队对古巴运油船的拦截，新立案例24。**“Grace”号拦截日期**：海岸警卫队声明摘要称9月5日，而WSAU、AJOT转载《纽约时报》报道的日期是10月2日前后，相隔约四周，已在案例中标“待核”。
- 案例13的更新中，“福特”号2026年2月中旬离开加勒比转往中东，仅见于检索摘要对《星条旗报》的转述，具体篇目未取得，已标“待核”。

## 3. 口径冲突最严重的几处

1. **印巴“朱砂行动”海上部分（案例12）**：印方称“维克兰特”号编组距打击卡拉奇仅数分钟；巴基斯坦海军参谋长称已把印度航母“困住”；事实核查称“航母袭击卡拉奇”传言系影像错配。双方均无独立证据。
2. **苏丹港（案例22）**：苏丹军方指向快速支援部队（RSF），RSF在所引报道发表时未声称负责；苏丹常驻联合国大使称5月4日打击来自阿联酋在红海的基地，阿联酋否认并谴责。路透社称不清楚爆炸是否在弗拉明戈海军基地附近。伤亡数字无独立汇总。
3. **“戴高乐”号（案例23）**：瑞典武装部队称无人机自俄罗斯“日古列夫斯克”号电子侦察船起飞；克里姆林宫称“荒谬”。发现距离，法方称约10公里，其他报道约13公里（约7海里）；日期2月25日与26日并存。
4. **“北极甲烷气”号（案例18）**：俄方称乌克兰无人艇自利比亚海岸发射；乌克兰未声称负责；利比亚搜救机构称沉没，意大利海军称仍漂流。
5. **“良知”号与西迪布赛义德港（案例16、17）**：船队称无人机袭击，突尼斯当局否认探测到无人机，称起火或为烟头所致。
6. **“鹰S”号（案例2）**：赫尔辛基地方法院（2025-10-03）以无管辖权驳回，上诉法院（据2026年9月报道）推翻并重启。Commons船舶分类页（据检索摘要）称该船2025年已拆解，与扣押、诉讼状态的关系待核。
7. **“新新北极熊”号（案例1）**：芬兰称证据指向该船、意图待判；中方称风暴中意外锚击，并在香港以刑事损毁起诉船长。
8. **“阿卜杜拉”号（案例21）**：赎金500万美元为海盗口径；船东只确认获释；赎金交付方式有“飞机空投入海”与“直升机投放”两说；劫持位置有600海里与550海里两种口径。
9. **美军加勒比打击（案例13）**：累计打击与死亡数在CBS、《星条旗报》、USNI、AP之间口径不同；美方未公开确凿证据。

## 4. 待检索清单（仍未执行）

### 4.1 尚未收录的候选事件

| 事件 | 待查问题 | 建议检索关键词 |
|---|---|---|
| 比利时泽布吕赫/安特卫普港无人机 | 是否确有港口目击、日期 | `Zeebrugge drone sighting November 2025`、`Antwerp port drones Belgian defence` |
| 乌斯季卢加/普里莫尔斯克港遭无人机袭击 | 乌克兰对波罗的海港口的打击、日期、损失 | `Ust-Luga drone attack`、`Primorsk port drones 2026` |
| 2026年波罗的海其他事件 | 瑞典之外的登检、电缆事件、爱沙尼亚处置 | `Estonia shadow fleet boarding 2026`、`Gulf of Finland 2026 cable damage` |
| 奥兰群岛、博恩霍尔姆驻军 | 兵力与无人机/GNSS事件 | `Aland islands Russia 2025 demilitarised`、`Bornholm garrison drone sighting` |
| 德国基尔海军基地专门通报 | 联邦国防军是否通报、反无人机处置 | `Marinestützpunkt Kiel Drohnen Bundeswehr Stellungnahme`、`Marine Eckernförde Drohne 2025` |
| 索马里海盗回潮其他案例 | 2023-12至2026年的登船、被劫、海军应对 | `Somali pirates 2025 hijack dhow`、`EUNAVFOR Atalanta 2025 piracy` |
| 几内亚湾海盗与港口、离岸平台防卫 | 2024—2026年的重要事件 | `Gulf of Guinea piracy 2025 IMB`、`Bonny OR Brass terminal attack` |
| “梅尔辛”号油轮在达喀尔外海爆炸（2025年11月） | 是否确有其事、归因 | `Mersin tanker explosions Dakar Senegal November 2025` |
| 苏丹港后续袭击与港口防空 | 无人机型号、数量、伤亡、后续几轮袭击 | `Port Sudan drone May 2025 casualties Flamingo base`、`Port Sudan air defence 2025` |
| 莫桑比克卡布德尔加杜海岸/港口 | 是否属本组范围 | `Mocimboa da Praia port attack 2025` |
| 特立尼达和多巴哥与委内瑞拉海上摩擦 | 若属“岛屿防卫”场景 | `Trinidad Tobago US radar 2025` |
| 古巴方向其他事件 | 被拦截船只总数、俄罗斯油轮护航、海岸警卫队声明原文 | `Coast Guard Cuba interdiction statement Grace`、`Cuba oil blockade tanker count 2026` |
| 美军“9月2日”打击的官方叙述 | 美方原始通报、死亡人数 | `September 2 boat strike Hegseth second strike survivors` |

### 4.2 已收案例的待补问题

- 案例1：管线停输时长与修复费用；船东/管理方；中方“风暴”说法的气象与航迹核验。
- 案例2：Estlink 2实际修复成本与时间；赫尔辛基上诉法院裁决书；是否再上诉最高法院。
- 案例3：北约“波罗的海哨兵”的参与舰艇、无人艇型号与数量、事件数。
- 案例4：爱沙尼亚、俄方官方原文；该船是否被检查。
- 案例6：“卡法”“海鸮”两起的日期与细节；爱沙尼亚停止登检是否属实。
- 案例7：丹麦调查结论、归因；国防部原始通报；是否有军舰参与。
- 案例8：杜尔、安特卫普港无人机的数量、日期与官方归因。
- 案例9：印度海军/国防部官方新闻稿（PIB）、伊朗口径。
- 案例10、11：印度海军官方新闻稿原文、孟买审判结果。
- 案例12：印度海军官方通报、巴基斯坦ISPR表态、卡拉奇港卫星影像。
- 案例13、14：加勒比小艇被击沉数、美方弹药与平台；委内瑞拉伤亡与港口损失、美方官方简报。
- 案例15：被扣油轮清单与后续处置（“Verónica”号为第六艘，仅见标题）。
- 案例16、17：马耳他政府声明原文、突尼斯调查结论。
- 案例18：“北极甲烷气”号最终处置；与乌克兰组去重。
- 案例19（基尔）：无人机来源、检察机关结论；基尔海军基地是否受影响。
- 案例21（“阿卜杜拉”号）：被劫后有哪国海军接近该船；护送其到阿联酋的两艘军舰身份。
- 案例23（“戴高乐”号）：无人机是否缴获；电子对抗装备型号；瑞典对《通行条例》的调查结论。

### 4.3 图片

**第二轮Commons检索结果（4次）**

已取得并在检索结果中真实见到URL的Commons File: 页（`verified: true`，但仅据文件名与检索摘要，未打开页面核对作者与许可）共11个：

- 案例2（“鹰S”号）：`File:Crude_oil_tanker_Eagle_S_at_Porvoo_2024-12-31_a.jpg`（本案最有价值的一张，2024-12-31被扣后锚泊波尔沃外）、`File:Eagle_S_on_the_map_of_MarineTraffic,_in_relation_to_the_Estlink_2_incident.png`、`File:Estlink_map.png`。
- 案例3（波罗的海哨兵）：`File:U_S_Marines_support_Finland_in_NATO's_Baltic_Sea_surveillance_(8883866).jpg`、`File:NATO_ships_take_part_in_BALTOPS_20_MOD_45167293.jpg`（2020年演习背景图）。
- 案例7（丹麦）：`File:Holmen_Naval_Base,_Copenhagen,_20220618_1503_7220.jpg`（背景图）。
- 案例11（“鲁恩”号）：`File:The_Indian_Navy_destroyer_INS_Kolkata_(D63)_and_the_British_Navy_destroyer_HMS_Defender_(D36)_steam_alongside_...JPG`、`File:IAC1_Vikrant_(R11)_with_INS_Kolkata_(D63)_during_sea_trial.jpg`（均为舰艇通用照，非现场）。
- 案例12（“维克兰特”号）：同一张“维克兰特”号海试照。
- 案例13（“福特”号）：`File:USS_Gerald_R_Ford_Conducts_Sea_and_Anchor_(8917661).jpg`、`(8917662).jpg`（舰艇通用照，非加勒比部署期间）。

未核实（`verified: false`）：案例11的 `Indian Navy MARCOS rescuing hijacked Bulgaria-owned vessel MV Ruen.jpg`，只在检索摘要中见到文件名，未见文件页URL，使用前须到Commons核对。

Commons分类页（存于各案例的`image_categories`字段，共12条，均在检索结果中见到URL）：`Category:Estlink_2_incident`、`Category:IMO_9329760`、`Category:INS_Kolkata_(D63)`、`Category:Kolkata_class_destroyers`、`Category:Indian_Navy`、`Category:INS_Chennai_(D65)`、`Category:INS_Vikrant_(ship,_2013)`、`Category:USS_Iwo_Jima_(LHD-7)`、`Category:General_views_of_USS_Iwo_Jima_(LHD-7)`、`Category:Absalon-class_(Denmark)`、`Category:2026_drone_incursions_into_the_Baltic_states_and_Finland`。后续取图时，建议打开这些分类页挑选2025—2026年的具体文件。

**Commons上未找到的**：Balticconnector/“新新北极熊”号、“化学冥王星”号（Chem Pluto）、“鲁恩”号被劫现场、2025年加勒比部署期间的“福特”号与“硫磺岛”号具体文件（仅见“硫磺岛”号分类页，其中摘要称含2025年第22海军陆战远征队相关文件）、丹麦哥本哈根机场无人机事件相关文件、哥本哈根/丹麦护卫舰（检索摘要称无法确认丹麦护卫舰参与）。第一轮的5条页面图注线索（案例1、15、16、18）仍为`verified: false`，授权须另行取得。

新增的案例19—24没有找到可用图片（未专门检索）。

## 5. 方法与局限

- 全部案例仅使用WebSearch检索结果（含检索工具对结果的摘要）；WebFetch不可用，一手文件（官方新闻稿、法院文书）几乎都未读到，只能引用报道。
- 检索摘要中凡来自聚合站（Ground News、Telegram聚合页、Torre News）的内容，仅作线索并已在来源中注明；至少有一份新增案例的关键数字（案例20的哥特兰投入）仅来自聚合站，已标待核。
- 日期：`date`字段只在URL或检索摘要明确给出时填写，其余留空并在`date_note`中写“约某时”。标题凡检索结果显示为小写slug的，已按URL还原，使用前请抽检。
- 部分新增案例的来源标题、日期来自检索结果摘要对同一页面的转述（如苏丹港的Jordan Times、Dabanga；Cuba案的Maritime Executive三篇），未打开原文，细节可能与原文有出入。
- 本轮12次检索额度已用完；仍可补的重点在4.1节“基尔海军基地专门通报”“苏丹港无人机型号与伤亡”“古巴拦截清单”三项。
