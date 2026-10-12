# 源稿写作规范（排版引擎标记语法）

成品由 `build.py` 把本目录的 .md 源稿排成 docx / PDF / HTML。请严格使用以下标记，其他 Markdown 语法（链接、`-` 列表、`|` 表格、`**` 以外的强调）**一律不支持**。

## 结构
- `# 一、章名` —— 章（用汉字序号，后接顿号）
- `## （一）节名` —— 节（进目录）
- `### 小标题` —— 小标题（不进目录）
- 普通段落：段与段之间空一行；一段写在一行或连续多行都可以。
- 以 `【提示语】` 开头的段落，提示语自动用黑体，例如：`【证据等级】……`
- 行内：`**加粗**`；`{red:需要警示的文字}`；`{fig:key}` 引用图号；`{tab:key}` 引用表号。
- 引注：`[@key]` 或 `[@key1,key2]`，key 必须在本文件对应的 refs JSON 中定义（见下）。每个关键事实、数字都要带引注，放在句末标点前。

## 框
```
:::lead
导读文字（一段）
:::

:::judge 研判要点
- 第一条
- 第二条
:::
```

## 图
- 自绘图（已绘好，直接引用）：`!fig key|key.png|图题|来源说明|宽度mm`
  例：`!fig d_lattice_arch|d_lattice_arch.png|Lattice 分层架构示意|本报告依据 Anduril SDK 与专利绘制|160`
- 实物照片：`!photo 照片id|图题|来源/版权说明`
  照片 id 取自 `_photo_ids.txt`（第一列）。只用与上下文确实相符的照片；每张照片只用一次。

可用自绘图 key（文件名 = key.png）：
- d_lattice_arch　Lattice 六层架构 + 部署形态
- d_lattice_entity_task　实体组件模型 + 任务生命周期状态机
- d_lattice_killchain　Lattice 探测—评估七步交战流程与人机关系
- d_maven_arch　Maven/MSS 七层架构
- d_maven_workflow　Target Workbench 看板式 F2T2EA 目标工作流
- d_maven_governance　Maven 管理归属演变（2017—2026）
- d_timeline　两系统竖排双栏大事记
- d_division　Palantir（企业与决策）—Anduril（边缘与执行）分层分工图
- d_ngc2　陆军 NGC2 三层架构与里程碑
- d_national　美国国家层面无人/AI 作战布局（五层 × 五项）
- c_anduril_contracts　Anduril 主要合同（横向对数条形，按时间）
- c_anduril_funding　Anduril 融资、估值与营收
- c_maven_scale　MSS 用户数与合同上限/预算
- c_palantir_contracts　Maven 与 Palantir 防务主要合同
- c_palantir_revenue　Palantir 美国政府收入 2019—2026H1
- m_world　两系统全球部署与案例分布图

## 表
```
!table key|表题|来源说明|列宽mm,列宽mm,列宽mm
表头1|表头2|表头3
单元格|单元格|单元格
!end
```
- 列宽合计约 160mm。单元格内不能出现 `|`。单元格可带 `[@key]` 引注。

## 引注库（refs JSON）
每个写作分工各自一个文件，key 加分工前缀避免冲突（`la_` / `mv_` / `co_`）：
```json
{
  "la_sdk_ref": {"author": "Anduril Industries", "title": "lattice-sdk-python reference.md", "title_cn": "Lattice Python SDK 接口参考", "publisher": "GitHub", "date": "2026-10-05", "url": "https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md"}
}
```
- `title` 用原文标题；`title_cn` 中译；`date` 用 YYYY-MM-DD（不详可写 YYYY 或留空）。URL 必须来自研究笔记，不得编造。

## 特情体例补充（《析光》特情定版，必须遵守）
- 本单位一律自称"我部"（不用"我院"）；章号一律简体汉字"一、二、三……"。
- 加粗范围：观点句（总体判断、综合研判、建议首句）与核心关键词。
- 每张表、每幅图下方都要有来源（引注或"本报告整理"）；正文事实性段落句末带引注。
- 对标与案例要写问题面（失败、延误、争议），用客观、建设性语言陈述。
- 口语化表述改为书面语；全角标点。
- 照片：`!photo id|图题|来源`，图题写清是什么、何时何地；只用 `_photo_ids_unused.txt` 中列出的未用照片（每张只用一次）。
