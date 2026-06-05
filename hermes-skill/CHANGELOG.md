# Changelog

All notable changes to the `client-proposal-html` skill are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] — 2026-06-05

### Added

- **2D+ 结论质量检查（全局步骤）** — 位于 Preflight 和 2E 之间，所有输出类型通用。包含三道检查：
  - Stakeholder Check：结论覆盖了供给方/需求方/市场方三方视角？
  - Novelty Check：删掉数据后结论是否仍然成立？
  - Actionability Check：这个结论会改变决策吗？
- **2E+ 最终验证第 7 项「Quality」** — 验证所有结论性陈述已通过 2D+ 三道检查
- **No-Regret Move** — Recommendation 结构化中新增可选字段：即使判断错了也值得做的动作
- **Actionability Check（建议级）** — 每条建议生成后自问"这个结论会改变决策吗？"，不会则改写或删除

### Changed

- **2A 调研维度升级为全局规则** — 从仅限 industry-report/guide 类型，改为所有类型必覆盖。新增类型映射表（comparison-matrix / industry-report / guide / hardware-compare），每种类型对应不同的 Supply/Demand/Market 三方视角
- **industry-report 核心发现强制三要素** — 每条核心发现必须包含：具体数据点或案例证据 + 数据来源标注（✅/⚠️/❌）+ 推理链（数据→判断→结论），附正反示例
- **Recommendation 结构化** — 新增时间轴（12个月/24个月）+ 优先级排序（P0/P1/P2）+ 预期效果/所需资源/风险提示三要素
- **output-tracker 分类体系** — 从 6 项扩展到 9 项，新增 `quality` 分类，`insight` 标注为"建议合并到 quality"
- **insight_quality 分级客观化** — A/B/C 三级增加了操作定义：A=数据支持+非共识（新洞察），B=数据支持+共识（数据总结），C=常识复述

### Removed

- **框架表第 4 列「对应原理角色」** — 经 ChatGPT 评审确认：Agent 不用的字段就是作者视角，应删除

### Deprecated

- **insight 分类** — 建议合并到 quality，后续版本可能移除
- **discipline-evaluation-framework.md** — 标记为开发者工具，从预加载清单和"详见"行移除，仅以注释形式保留引用

---

## [1.1.0] — 2026-06-05

### Architecture Review (ChatGPT)

完整架构评审后实施 8 项改动，按优先级分为四档：

#### P0 — Agent 行为直接缺陷

- **SCQA 与对比表解耦** — comparison-matrix 去掉 SCQA 序言，改为 Recommendation First（标题→推荐结论→关键差异→详细对比）。SCQA 仅保留给 industry-report 和 guide 类型

#### P1 — Agent 行为质量

- **2E+ 最终验证总闸门** — 在 2F 归档前新增 6 项总闸门（Data/Structure/Audience/Color/Accessibility/Recommendation），全部通过才进入交付
- **Fallback 补充 Reasoning Failure** — 触发条件从 Input Failure 5 项扩展为 Input Failure（已有）+ Reasoning Failure（5 项新增：IA 无法拆分/MECE 失败/配色无法收敛/符号冲突无法解决/推荐无法得出）
- **学科间关系明确** — 新增"学科间关系"段落：体验设计负责功能正确（绿色=推荐），符号学负责文化审核。默认 UX 优先，仅存在明确文化冲突时符号学覆盖。流程：UX → 生成 → 符号学审核

#### P2 — 流程清晰度

- **IA/金字塔增加"流程方法论"小节** — 在框架表下方新增"流程方法论（2）"表格，注明"学科=为什么，方法论=怎么做"，将信息架构和金字塔原理从隐式流程变为显式引用
- **2D 从"硬校验"改为"Preflight Check"** — 去掉与上游重复的色值/布局校验，改为 3 项 yes/no 确认（Color/Layout/Audience Ready），类似飞机起飞前检查单

#### P3 — 文档清理

- **预加载编号修正** — "额外加载"部分去掉已错乱的编号（⑦⑧⑨⑩⑪⑫⑬），改用 `·` 分隔直接列文件名
- **学科数量统一** — 顶部描述从"9 个学科"改为"10 个学科"
- **discipline-evaluation-framework.md 降级** — 从 OPTIONAL 预加载移除

### Added

- **符号学（Semiotics）** — 作为第 10 个学科加入框架表，覆盖非语言符号系统（颜色/位置/间距的隐含意义）
- **学科框架原理章节** — 在路由前新增原理说明，解释 10 个学科扮演的三个角色（均值对抗/隐性知识外部化/元认知监控）

### Changed

- **语言学和符号学合并 reference** — 符号学内容作为 `language-and-labeling-rules.md` 的新章节加入，不单独成文件
- **叙事设计和数学美感提级** — 从 reference 文件升格到框架表，同时加入润色 10 项和自检清单
- **论证结构升级** — 从"三段论（维度名→数据→建议）"升级为"金字塔原理（Minto）：结论先行→MECE 分组→逐层展开"

### Added (references)

- `references/information-architecture.md` — 四步 IA 决策树（内容清单→标签系统→导航层级→扫描路径）+ 空间句法补充
- `references/pyramid-principle.md` — 金字塔原理完整指南（SCQA 序言→结论先行→MECE 分组→纵向/横向逻辑）

### Absorbed (into existing references)

- **物理隐喻 + 历史叙事** → 吸收到 `narrative-design-examples.md`
- **数据-墨原则 + 图表选择** → 吸收到 `design-details.md`
- **Gestalt 原理** → 吸收到 `affordance-checklist.md`
- **空间句法** → 已在 `information-architecture.md` 编写时吸收

---

## [1.0.0] — 2026-06-04

### Initial Release

首个稳定版本，经过 v1 → v27 的内部迭代。

#### Framework

- **7 学科框架**：经济学·社会学·心理学·体验设计·语言学·统计学·伦理学
- **3 个隐性学科**：叙事设计（narrative-design-examples.md）、数学美感（design-details.md）、决策偏见（decision-biases.md）
- **设计哲学 6 条**：信息服务于决策 / 先层级后样式 / 受众决定密度 / 一致性建立信任 / 每个数都有归属 / 从已知推未知
- **论证结构**：三段论（维度名→数据→建议），弱势维度放中间

#### Flow

- **快速路由（3 步）**：页面类型识别 → 风格与数据决策 → 节奏分支
- **2A 数据调研与核实**：风险分级 + 两步调研法 + 数据审计表
- **2B 受众确认**：audience-layout-tokens.md 参数加载
- **2B+ Fallback 触发**：5 项 Input Failure 条件
- **2C 色彩推导**：理论→工具→案例校准→WCAG 四步推导
- **2D 生成前硬校验**：色值来源 + 布局结构确认
- **2E 输出与润色 7 项**：三类型输出格式 + 润色检查
- **2F 归档与交付**：Feishu 文件上传 API

#### References

- 17 个 reference 文件 + 3 个 HTML 骨架模板
- 预加载清单（ESSENTIAL / OPTIONAL / RARE 三级）
- output-tracker 质量追踪

---

## 版本路线

| 版本 | 日期 | 核心变化 | 文件数 |
|------|------|---------|--------|
| v1.0.0 | 2026-06-04 | 学科框架 + 完整执行流程 | 17 .md + 4 .html |
| v1.1.0 | 2026-06-05 | 架构评审 8 项 + 10 学科 + 流程方法论 + 最终验证 | 19 .md + 4 .html |
| v1.2.0 | 2026-06-05 | 3 全局结论质量检查 + 调研三侧通用化 + Recommendation 结构化 | 19 .md + 4 .html |
