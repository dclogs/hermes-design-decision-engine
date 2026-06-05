---
name: client-proposal-html
description: "Design-decision engine for enterprise HTML pages. 10-discipline reasoning framework + Layout Intelligence (2B+4) + Decision Assurance (2B+3, criterion-first + rubric + evidence + sensitivity + weight_rationale) + Report Intent pipeline (decision/education/research) + layer annotations (layer/maturity) + 3 global conclusion quality checks (Stakeholder / Novelty / Actionability). Output: comparison matrices, analysis reports, transformation guides. Zero-dependency, Feishu delivery."
version: 1.7.0
author: Hermes Agent
license: MIT
tags: [design, proposal, html, comparison, audience-adaptation, enterprise, feishu, layout, assurance, rubric, intent, layer-annotation]
---

# Client Proposal HTML Generator

**设计决策引擎，非模板库。** 每次从零推理：受众 → 数据 → 理论推导 → 真实产品校准配色。只输出 3 种类型（对比表/分析报告/指南），学科框架保证首版质量，不走"套模板"路线。

零外部依赖（仅 Google Fonts CDN）。飞书文件上传交付。

---

## 开源版本

本 skill 的学科框架、参考文件和质量门禁体系已提取为独立方法论文档，发布在开源仓库：
**https://github.com/dclogs/hermes-design-decision-engine**

`methodology/` 目录下的 5 篇文档不依赖 Hermes Agent 即可阅读和使用。外部贡献者可以：
- 在 methodology/ 层面改进学科框架本身（领域知识贡献）
- 在 hermes-skill/ 层面改进 agent 实现（Hermes 用户贡献）
- 通过 examples/ 提交实际产出案例

详见开源仓库的 CONTRIBUTING.md。

---

## 学科框架原理（为什么这么做）

本 skill 按三层结构组织规则，避免把所有逻辑平铺在一层：

**全局层（Global）**——所有类型通用，锁定结论质量
Supply/Demand/Market 调研维度 · Novelty Check · Actionability Check · Stakeholder Check · Preflight · Final Validation

**类型层（Type-Specific）**——按输出类型定制
comparison-matrix → Recommendation First · industry-report → SCQA + Insight · guide → SCQA + Roadmap · hardware-compare → TCO/兼容性/运维性

**经验层（Experience）**——通过 output-tracker 累积真实失败案例，不固化到主流程

10 个学科扮演三个角色：

**1. 对抗均值坍缩**
LLM 被问到"生成一个专业对比页"时，输出的是训练数据中所有专业页的统计平均。这个平均不会太差，但永远到不了卓越——因为优秀设计不在均值处，而在特定语境的离群点。每个学科施加一个约束条件（经济学→动机基调、统计学→数据可信度、伦理学→来源标注），约束越多，输出偏离统计均值的程度越大——恰好是我们需要的，因为设计品质不来自"更像平均值"，来自"更适合特定语境"。

**2. 隐性知识外部化**
人类设计师靠二十年经验积累的直觉做决策。"这个蓝太企业了"——她说不出精确理由，但她是对的。AI agent 没有隐性知识。学科框架用显性推理替代：色彩推导用色相环定位+饱和度控制+产品对比替代"感觉这个蓝不对"；信息密度用心理学选择超载限制替代"信息太挤了"；论证结构用 Minto 金字塔替代"这个报告不够专业"。

**3. 元认知监控**
最关键的差异：agent 在每一步自问"数据够吗？confidence 够吗？这个配色放到 Stripe/Notion 旁边显得过时吗？output-tracker 里满 20 条失败记录了吗？"——每一层都不是"更复杂的规则"，而是一个自省节点：评估当前状态，决定是否切换路径（降级对比方式、走 fallback、触发根因分析）。这和人类"做到一半觉得不对劲，停下来重新想"是同一个认知过程，只是被显式编码了。

---

## 一、快速路由（3 步定方向）

**Step 1 — 页面类型 + 报告意图**

两份独立配置，共同驱动 pipeline 选择：

```yaml
# 页面形态（长什么样）
page_type:
  comparison-matrix  → 方案对比（扁平 IA，详见 references/information-architecture.md）
  industry-report    → 行业分析（层级 IA，详见 references/information-architecture.md）
  guide              → 转型指南（步骤 IA，详见 references/information-architecture.md）
  architecture       → 委托 architecture-diagram skill 生成

# 报告意图（为什么生成）
report_intent:
  decision           → 选方案/做决策（强制评分+审计+sensitivity）
  education          → 认知建立/技能提升（跳过评分，输出概念+路径）
  research           → 行业分析/趋势研究（强调 evidence chain，跳过评分）
```

**pipeline 选择器（根据 report_intent）：**

| intent | 2A | 2B | 2B+1 | 2B+2 | 2B+3 评分 | 2B+3b 敏感度 | 2C | 2B+4 | 2D+ 检查 | 2E |
|--------|----|----|------|------|---------|------------|----|------|---------|----|
| decision | ✅ | ✅ | ✅ | ✅ | **强制** | **强制** | ✅ | ✅ | ✅+Audit | 含评分矩阵+sensitivity |
| education | ✅ | ✅ | ✅ | ⚠️ 可选 | **跳过** | **跳过** | ✅ | ✅ | ✅ | 概念图+学习路径+场景矩阵 |
| research | ✅ | ✅ | ✅ | ⚠️ 可选 | **跳过** | **跳过** | ✅ | ✅ | ✅+Evidence | 证据链+趋势分析 |

**Step 2 — 风格与数据决策**
```
① 数据够吗？→ 不够换题  ② 受众？→ 银行/学校/教育局/科技
③ 动机？→ 避险/增益/成本  ④ 场景？→ 投屏/打印/手机
⑤ 对比类型？→ Type1 PK / Type2 场景最佳实践 / Type3 行业对标
⑥ IA 结构？→ 扁平/层级/步骤（加载 references/information-architecture.md）
```

**Step 3 — 节奏分支**
```
工期紧+有同受众样稿 → 改内容复用（5 分钟）
工期紧+无样稿      → 速查+必查 5 项（15 分钟）
工期不紧           → 走完整流程（下文 二~四）
```

---

## 二、完整执行流程（工期不紧时按序走）

### 2A 数据调研与核实

**如果用户已提供完整的方案描述和数据（含评分依据、成本估算），跳过此步骤，直接进入 2B。** 仅在数据缺失或需要外部验证时才启动调研。

```
需求 → 风险分级（Low 一次搜索 / Medium 两步法 / High 全流程+审计）
  → 调研：delegate_task 并行搜索
    调研维度（所有类型必覆盖，按类型映射）：
      - Supply Side  — 厂商/产品/技术路线
      - Demand Side  — 客户/预算/招标/运维/风险
      - Market Side  — 行业趋势/竞争格局/市场数据
    类型映射：
      comparison-matrix → 方案提供商 / 使用部门 / 行业实践
      industry-report   → 厂商 / 客户 / 行业
      guide             → 方案方 / 执行团队 / 行业标杆
      hardware-compare  → 厂商 / 运维人员 / 竞品生态
  → 核实：独立核查每个断言（子 agent 数据不可直接信任）
  → 数据审计表（✅高/⚠️中/❌不存在→丢弃）
    → 数据不足？降级对比方式或告知换题
```

调研后选对比方式：Type1 水平 PK → 量级对等才用；Type2 场景最佳实践 → 默认推荐；Type3 行业对标 → 有明确标杆时用。

### 2B 受众确认与参数

从 references/audience-layout-tokens.md 加载受众参数（配色基线/字号/行高/圆角/页宽）。确认：

```
□ 受众画像对了？  □ 决策链画全了？
□ 展示场景（投屏/打印/手机）确定？
```

### ⚠️ 2B+ Fallback 触发检查

分两类触发：

**Input Failure（输入问题）**
```
数据不足 / 受众模糊 / 行业陌生 / 案例缺失 / 色彩推导卡住 →
加载 references/fallback-mode.md 走保底路径
```

**Reasoning Failure（推理失败）**
```
IA 无法拆分 / MECE 分组失败 / 配色无法收敛 /
符号冲突无法解决 / 推荐方案无法得出 →
加载 references/fallback-mode.md 走保底路径
```

任一为是，或 confidence < 60% → 走 fallback。Fallback 输出 80 分作品，非 40 分。异议框会标注原因。

### 2B+1 信息架构确认

根据 Step 1 选择的 IA 类型，加载 `references/information-architecture.md`：

```
□ 内容清单通过（主流程 / 支撑 / 参考三层分离）
□ 标签系统通过（命名三问：猜得到内容？语言统一？分类明确？）
□ 导航层级按输出类型确认
□ 扫描路径 3 秒测试通过（决策者路径逐步确信）
```

### 2B+2 Data Expression Decision（IA 后、配色前，数据驱动表达选择）

**不要在这里画图。只做决策。**

输入：已核实的数据集、受众画像、页面类型
输出：table / chart / chart+table

**Step 0 — metric_selection（选对指标）**

先于图表类型选择。确认受众最关心的核心指标，避免"图对但指标不对（Metric Error）"。

```
受众是谁？（已在 2B 确定）
决策目标是什么？
该受众最关心的 2-3 个核心指标是什么？

  → 这些指标有数据支撑吗？
    有 → 指标保留，用于后续表达
    没有 → 标注⚠️降级，或告知无法支撑

  → 是受众关心的指标 → 进入下一步
  → 不是受众关心的指标 → 丢弃，不要为了展示数据而展示
```

记录到 output-tracker：

```yaml
metric_selection:
  audience_role: 校领导/CIO/财务/...
  decision_goal: "..."
  critical_metrics: ["指标A", "指标B", "指标C"]
  metric_data_confidence: ✅ / ⚠️ / ❌
```

**Step 1 — 判断数据是否需要可视化**

```
存在值得可视化的数据？
  → 否 → 继续（纯表格，跳过此步骤的后续）
  → 是 → 进入 Step 2
```

**Step 2 — 数据类型 → 推荐图表**

```
数据特征 → 图表类型（当前支持 4 种，通过 scripts/chart_svg.py 生成 SVG）：
  类别比较     → bar（柱状图）
  时间趋势     → line（折线图）
  占比/份额    → donut（环形图，非饼图，更干净）
  多维评分对比  → radar（雷达图）

规则：
  - 精确值重要 → 表格（不选图表）
  - 趋势重要   → 图表
  - 两者都重要 → chart+table（图表在前，数据表在后）
  - 数字 ≤ 3 个 → 直接写文字（不画图）
  - 先推荐再执行 → 记录 chart_decision 到 output-tracker 后再生成
```

**Step 3 — 输出决策**

```yaml
data_expression:
  mode: table / chart / chart+table
  chart_type: bar / line / donut / radar / none
  chart_count: 1-3（单页面最多 3 张图）
```

记录到 output-tracker（见 `references/output-tracker.md` 的 chart_decision 字段）。

**实现方式：** 需要图表时，执行 `scripts/chart_svg.py <type> --data JSON` 生成 SVG 字符串，直接嵌入 HTML。零外部依赖，纯 Python 实现。

### 2B+3 Decision Engine（决策引擎）

**适用范围：** 仅当 `report_intent: decision` 时强制执行。`education` 和 `research` 类型跳过此步骤。

**前置条件：**
- ✅ `report_intent: decision` → 走完整评分+审计流程
- ❌ `report_intent: education` → 跳过 2B+3，直接输出概念框架+学习路径
- ❌ `report_intent: research` → 跳过 2B+3，直接输出 evidence chain+趋势分析

在推荐结论产生前，建立 **criterion-first 的可审计评分推理链**。每个评价维度（criterion）自带评分+依据+证据等级。后续的排名、推荐和敏感度分析全部由 criterion 数据自动推导。

**前置加载：** `references/decision-assurance.md`

---

**Step 1 — 定义评价体系（Decision Layer）**

根据受众（2B 确定）和决策目标，列出 5±1 个评价维度，分配权重（合计 100%）：

**Layer 标注说明：**
- `# layer: decision` → 选择逻辑本身（维度、权重、评分）
- `# layer: assurance` → 证明结论可信（证据等级、评分卡来源、敏感度）
- `# layer: presentation` → 展示方式（布局参数）
- `maturity: stable / beta / experimental` → 该字段经过多少真实案例验证

```yaml
decision_framework:                # layer: decision | maturity: stable
  goal: "3000万预算内完成省级政务云数据库选型"
  criteria:
    - name: 国产化适配                # layer: decision | maturity: stable
      weight: 35                     # layer: decision | maturity: stable
      weight_rationale: "..."        # layer: decision | maturity: beta
    - name: 高可用能力
      weight: 20
      description: "RPO/RTO/多活/灾备能力"
    - name: 运维成本
      weight: 15
      description: "DBA人力+许可费+驻场服务费用"
    - name: 生态兼容
      weight: 15
      description: "Oracle/MySQL语法兼容+第三方工具链"
    - name: 迁移风险
      weight: 15
      description: "SQL改造量+数据迁移复杂度+停机窗口"
```

**维度选择规则：**
- 每个维度必须有数据支撑（criteria.scores[].evidence 标注来源）
- 维度不能重叠（MECE）
- 权重反映受众优先级
- **每个权重必须附带 weight_rationale**，说明"为什么是这个百分比"（所有权重推导一律标为 ESTIMATE——权重设定本身无法成为 FACT）

---

**Step 2 — Criterion-First 评分（Decision + Assurance 融合）**

每个 criterion 下，先定义评分卡（rubric），再将事实匹配到具体档位得出分值。

**关于评分卡的定位：** rubric 不承诺评分绝对正确。它只承诺评分可追溯、可反驳。当有人质疑分数时，讨论的是"事实落在这个档位是否合理"，而非"你为什么给这个数字"。详见 `references/decision-assurance.md`。

**先定义评分卡（rubric）：**
```yaml
criteria:
  - name: 国产化适配
    weight: 35                                                         # layer: decision | maturity: stable
    weight_rationale: "省级政务云，政策合规为第一优先级。参照同类项目权重区间(30-40%)取中间值"  # layer: decision | maturity: beta
    rubric:                                                            # layer: decision | maturity: stable
      - match: "信创目录核心 + EAL4+认证 + 多省案例"
        score_range: [95, 100]
      - match: "信创目录内 + 省级案例已验证"
        score_range: [80, 90]
      - match: "信创目录外但有替代发行版"
        score_range: [60, 75]
      - match: "非国产/纯外资"
        score_range: [0, 10]
    rubric_level: 经验评分卡                                            # layer: assurance | maturity: beta
    rubric_source: "基于政务云采购公开信息归纳"                            # layer: assurance | maturity: experimental
```

**再按 rubric 档位匹配打分：**
```yaml
    scores:
      达梦DM8:
        value: 100                                                     # layer: decision | maturity: stable
        rubric_match: "信创目录核心 + EAL4+认证 + 20+省级案例"            # layer: assurance | maturity: beta
        rationale: "信创目录核心产品，EAL4+认证，20+省级案例"               # layer: decision | maturity: stable
        evidence:                                                        # layer: assurance | maturity: stable
          level: FACT
          sources: ["工信部目录", "政府采购公示"]

      OceanBase:
        value: 90                                                      # layer: decision | maturity: stable
        rationale: "信创目录内，浙江/江苏省级案例"                          # layer: decision | maturity: stable
        evidence:                                                        # layer: assurance | maturity: stable
          level: FACT
          sources: ["信创目录", "政务案例"]

      PostgreSQL:
        value: 80                                                      # layer: decision | maturity: stable
        rationale: "原生PG不在目录，openGauss发行版已入"                   # layer: decision | maturity: stable
        evidence:                                                        # layer: assurance | maturity: stable
          level: ESTIMATE
          sources: ["信创目录", "行业分析"]

      Oracle:
        value: 5                                                       # layer: decision | maturity: stable
        rationale: "非国产，信创不合规"                                   # layer: decision | maturity: stable
        evidence:                                                        # layer: assurance | maturity: stable
          level: FACT
          sources: ["信创政策文件"]

  - name: 高可用能力
    weight: 20
    weight_rationale: "省级政务云要求RPO<30分钟，高可用是关键技术指标。参照金融类项目标准(15-25%)取中值"
    rubric:
      - match: "全分布式 + RPO=0 + 多活"
        score_range: [85, 95]
      - match: "成熟集群 + 主备自动切换"
        score_range: [70, 80]
      - match: "标准主备 + 手动切换"
        score_range: [55, 65]
      - match: "无HA能力"
        score_range: [0, 30]
    rubric_level: 经验评分卡
    scores:
      达梦DM8:
        value: 70
        rationale: "主备架构=60 + 集群能力=10"
        evidence:
          level: ESTIMATE
          sources: ["技术文档", "行业评测"]

      OceanBase:
        value: 88
        rationale: "全分布式多副本，RPO=0"
        evidence:
          level: FACT
          sources: ["官方文档", "浙江案例"]

      PostgreSQL:
        value: 78
        rationale: "流复制+Patroni集群"
        evidence:
          level: FACT
          sources: ["社区文档", "行业实践"]

      Oracle:
        value: 92
        rationale: "成熟RAC，多活方案完善"
        evidence:
          level: FACT
          sources: ["产品文档"]
```

**证据等级（evidence.level）定义：** 详见 `references/decision-assurance.md`

| 等级 | 含义 | 示例 |
|------|------|------|
| FACT | 有公开来源可验证的断言 | 信创目录、政府采购公告、官方文档 |
| ESTIMATE | 基于行业数据的合理推断 | TCO估算、运维人力成本 |
| ASSUMPTION | 缺乏数据，基于经验的假设 | 未来扩展性预期 |

**评分卡等级（rubric_level）定义：**

| 等级 | 含义 | 示例 |
|------|------|------|
| 公开评分卡 | 有行业公认的评分标准 | Gartner Magic Quadrant、信创目录等级、政府采购评分细则 |
| 经验评分卡 | 基于行业经验的合理分档 | 用户体验评分、运维复杂度档位 |
| 推导评分卡 | 无公开标准，agent 自建分档 | 厂商生态绑定程度、扩展性预期 |

---

**Step 3 — 加权总分**

```yaml
candidates:
  - name: 达梦DM8
    weighted_score: 76.0
    score_breakdown: "100×0.35 + 70×0.20 + 65×0.15 + 70×0.15 + 45×0.15"
  - name: OceanBase
    weighted_score: 74.6
  - name: PostgreSQL
    weighted_score: 74.7
  - name: Oracle
    weighted_score: 45.3
```

**Step 3b — 敏感度分析（Sensitivity，Phase 1）**   # layer: assurance | maturity: beta

自动计算：每个 criterion 的权重下降到多少时，推荐第一名被超越。

```yaml
sensitivity:
  - criterion: 国产化适配
    baseline_weight: 35
    breakpoint: 22
    effect: "PostgreSQL 超越达梦排第一"
    insight: "核心敏感维度——若政策要求放松，推荐结果不稳"

  - criterion: 运维成本
    baseline_weight: 15
    breakpoint: 32
    effect: "OceanBase 超越达梦排第一"
    insight: "阈值高，实际不太敏感"
```

**敏感度计算规则：** 固定其他维度权重和评分不变，逐维度降低目标权重至 5%，每降 5% 重算排名。记录排名首次翻转时对应的权重值（breakpoint）。

---

**Step 4 — 产出推荐**

按总分排序，推荐最高分方案。页面输出包含：

```
评分矩阵（含 evidence badge + 评分依据列）
  → 推荐框
    → 敏感度注释（"国产化权重低于22%时排名翻转"）
      → 注意：总分接近（差距 < 5 分）时附定性判断
```

**评分矩阵表输出要求：**
- 表头：评估维度 | 权重 | 方案A | 方案B | 方案C | 方案D
- 每列评分下方标注 evidence level 标签（FACT / ESTIMATE / ASSUMPTION）
- 每列评分附带依据（rationale），输出为「评分依据列」
- 最后一行为加权总分行，推荐方案加粗/高亮
- 总分接近（差距 < 5 分）时附注说明

**Evidence Badge 输出格式：**
```html
<span class="evidence-badge evidence-fact">FACT</span>
<span class="evidence-badge evidence-estimate">ESTIMATE</span>
<span class="evidence-badge evidence-assumption">ASSUMPTION</span>
```

**敏感度注释输出格式：**
```html
<div class="sensitivity-note">
  <strong>敏感度提示：</strong>
  国产化适配权重从 35% 降至 22% 时，推荐结果翻转。
</div>
```

**注意：** 推荐可信度（Recommendation Confidence）和 Criterion Confidence 属于 Phase 2，当前版本不输出。

### 2C 色彩推导（生成 HTML 前必过）

**Step 1 理论 → 方向**
经济学+社会学决定冷暖/正式度/情感基调（避险→保守色系，增益→活力色系）。

**Step 2 工具 → 色值**
Open Color 同色系色阶推导 6 色值（含品牌色/背景色/文字色/边框色）。

**Step 3 案例校准 → 别跑偏**
先查 `references/design-tokens.md`：按受众场景匹配 Token 策略（Conservative/Enterprise/Modern SaaS/Reading/Comparison），从对应参考产品提取精确色值。
如果场景不在表中，再加载 `popular-web-designs` 找同领域产品对比。

```
推导色系：蓝 #2563EB + 深灰表头
对比 Stripe：紫 #635BFF + 白底 + 浅边框（会不会太重？）
对比 飞书：   蓝 #3370FF + 白底 + 无深色块（会不会太土？）
对比 Notion： 蓝 #0075DE + 暖白 #F6F5F4（会不会过时？）

自查：我的配色放到 Stripe/Notion 旁边，显得"过时"或"太企业"吗？
→ 如果是 → 浅化/减少深色块，颜色只做小面积点缀和边框
```

**Step 3 的角色是否定性检查（校准），不是肯定性生成（抄袭）。** popular-web-designs 负责发现「这个色值是不是像 2015 年的」，不负责告诉你「你应该用什么色值」。

常见校准发现的问题：
```
深黑表头 → 白底+品牌色 2px 下边框（Stripe/飞书/Notion 共识）
大块品牌色背景 → 品牌色只用在 badge/边框/图标（Apple/Linear 共识）
深色表头填充 → 白色背景+品牌色下划线（GitHub/Airtable 共识）
```

**Step 4** WCAG 验算所有关键颜色对（≥4.5 AA 通过）。
**Step 4b** 非白底上换 `color:inherit; opacity:0.85` 替代 `var(--text-muted)`。

### 设计参考路径

```
色值校准：
  优先 → references/design-tokens.md
     流程：受众场景 → 匹配 Token 策略 → 查产品色值
  兜底 → popular-web-designs（场景不在 5 类中时）
布局/结构灵感：
  必读 → popular-web-designs
     看什么：卡片阴影层叠方式、Feature section 间距、列表项对齐、正文行宽
```

### 2B+4 布局策略决策（Layout Decision）

**位置：** 2C（配色）之后、2D（Preflight）之前。

**作用：** 决定「信息如何在页面上排列以最大化说服力」。这一步不是 CSS 微调，而是策略层面的编排决策。

**输入读取：**
```yaml
page_type:   从 Step 1 继承（comparison-matrix / industry-report / guide）
audience:    从 2B 继承（校领导 / 财务 / CIO / 后勤 / 教育局）
scenario:    从 2B 继承（投屏 / 打印 / 手机 / 邮件）
data_volume: 从 2A 推断（丰富 / 中等 / 有限）
has_scoring: 2B+3 是否生成了评分矩阵
has_charts:  2B+2 决定的图表数量（0-3）
```

**执行：**
1. 加载 `references/layout-strategy.md`，按决策规则表推导 `layout_strategy` 字典
2. 确认 kpi_strip 启用条件（数据充足 + 决策者受众 + 场景合适）
3. 根据数据质量决定是否降级（数据不足 → 禁用 kpi_strip + hero_type=neutral）

**输出：**
```yaml
layout_strategy:
  page_pattern: executive_summary    # 可选: executive_summary / comparison_first /
                                     #       roadmap_planning / problem_solving / compliance_report
  hero_type: recommendation          # recommendation / data / problem / neutral
  hero_weight: heavy                 # heavy / medium / light
  kpi_strip:
    enabled: true                    # true / false
    metrics: []                      # 从 metric_selection 继承，最多 4 个
  title_system:
    levels: 3                        # 3 / 4
    numbering: true                  # true / false
  chart_layout: insight_driven       # insight_driven / standalone / embedded
  section_density: medium            # compact / medium / spacious
  visual_hierarchy: strong           # strong / moderate / flat
  visual_priority: decision          # decision / data / balanced
  #   decision: 结论区权重 ≥ 数据区，适合决策层投屏
  #   data:     数据区可占更多页面空间，适合技术评审
  #   balanced: 通用混合受众
```

**output-tracker 记录（新增 layout 字段）：**
```yaml
layout:
  page_pattern: executive_summary
  hero_type: recommendation
  kpi_strip_enabled: true
  title_system_levels: 3
  numbering: true
  chart_layout: insight_driven
  section_density: medium
  visual_hierarchy: strong
  visual_priority: decision
```

**决策速查（数据充足时）：**
| 受众 | page_pattern | hero_type | hero_weight | kpi_strip | visual_priority |
|------|-------------|-----------|-------------|-----------|----------------|
| 校领导/院长 | executive_summary | recommendation | heavy | enabled | decision |
| 财务 | executive_summary | data | heavy | enabled | decision |
| CIO（比价） | comparison_first | neutral | medium | disabled | balanced |
| CIO（评估） | executive_summary | recommendation | medium | disabled | balanced |
| 后勤 | roadmap_planning | data | medium | disabled | balanced |
| 教育局 | executive_summary | recommendation | heavy | enabled | decision |

**数据不足时一律强制降级：** kpi_strip=disabled, hero_type=neutral, hero_weight=light

### ✅ 2D 生成前确认（Preflight Check）

飞机起飞前不做重复检查——确认上游就绪即可。

```
□ Color Ready — 色值已推导+校准 → yes/no
□ Layout Ready — layout_strategy 已输出 + IA 结构确认 → yes/no
□ Audience Ready — 受众参数已加载 → yes/no
```

三项全 yes → 进入 2E。任意 no → 返回对应步骤修复。

### ✅ 2D+ 结论质量检查（全局，所有类型通用）

生成任何结论性陈述（核心发现、推荐理由、方案建议）前，经过三道检查：

```
1. Stakeholder Check
   这个结论覆盖了哪些利益相关方视角？
   □ Supply Side（供给方/厂商）
   □ Demand Side（需求方/客户/使用者）
   □ Market Side（市场/行业）
   缺任何一侧 → 这个结论可能偏颇，补搜后再下结论

2. Novelty Check
   如果删掉这句话中的数据/案例，它是否仍然成立？
   成立 → 大概率是常识，降级或重写
   不成立 → 可能是有效洞察，保留

3. Actionability Check
   这个结论会改变受众的决策吗？
   会 → 保留
   不会 → 伪洞察，删除或重写
```

执行方式：生成所有结论后，逐条过三道检查。全通过才输出到页面。

### 2E 输出 & 润色

**输出格式** — 策略驱动的 section 编排。

2B+4 输出的 `layout_strategy` 决定了页面骨架（skeleton），2E 按骨架顺序渲染每个 section。skeleton 定义详见 `references/layout-strategy.md`。

**section 渲染规则：**
```yaml
page_pattern: executive_summary
sections:
  - hero_section          # L1 标题 + 推荐结论（hero_type=recommendation 时嵌入推荐框，不展示重复数字）
  - kpi_strip             # 大数字卡片（可选，与 hero 不重复）
  - recommendation_box    # 推荐方案（仅 hero_type≠recommendation 时独立渲染）
  - scoring_matrix        # 评分表（如果有评分数据）
  - chart_insight_row     # 图表 + 洞察绑定（1-3 组，每组 chart+insight 绑定，不超过 3 张图）
  - detail_section        # 详细数据/证据
  - roadmap_section       # 实施路线（可选）
  - risk_section          # 风险评估
  - objection_box         # 预期异议
  - footer_section        # 来源声明
```

每个 section 渲染时读取 `layout_strategy` 中的参数（hero_type / hero_weight / section_density / visual_hierarchy / title_system / kpi_strip / chart_layout）控制具体的 HTML 样式。

**page_pattern 速查：**

| pattern | 适用场景 | 核心 section 顺序 |
|---------|---------|-------------------|
| executive_summary | 决策层提案/投资决策 | hero → kpi → recommendation → evidence |
| comparison_first | 选型/比价 | hero → comparison → recommendation |
| roadmap_planning | 分期建设/转型 | hero → current_state → roadmap |
| problem_solving | 根因分析/优化 | hero → problem_analysis → solution |
| compliance_report | 等保/合规 | hero → gap_analysis → risk_matrix → recommendation |

**对比表渲染（page_pattern=comparison_first 或含 scoring_matrix）：**

对比表渲染要求（criterion-first 数据模型输出）：
- 表头：评估维度 | 权重 | 方案A | 方案B | 方案C | 方案D
- **每列评分下方标注 evidence level 标签**（FACT / ESTIMATE / ASSUMPTION）
- **每列评分附带依据**（rationale），在评分下方以小字展示
- 最后一行为加权总分行，推荐方案加粗/高亮
- 每个评分加注来源标注（✅/⚠️/❌），不隐藏不确定性
- 总分接近（差距 < 5 分）时附注说明："分数接近，结合XXX因素综合判断"

**Evidence Badge CSS：**
```css
.evidence-badge {
  font-size: 10px; font-weight: 600;
  padding: 1px 6px; border-radius: 2px;
  display: inline-block; margin-left: 4px;
}
.evidence-fact { background: #D1FAE5; color: #065F46; }
.evidence-estimate { background: #FEF3C7; color: #92400E; }
.evidence-assumption { background: #FEE2E2; color: #991B1B; }
```

**评分矩阵单元格 HTML 骨架（含 evidence badge + rationale）：**
```html
<td>
  <div class="score-value">100</div>
  <div class="score-evidence">
    <span class="evidence-badge evidence-fact">FACT</span>
  </div>
  <div class="score-rationale">信创目录核心产品</div>
</td>
```

**敏感度注释 HTML 骨架：**
```html
<div class="sensitivity-note" style="margin-top:12px; padding:12px 16px; background:#F0F9FF; border-left:3px solid var(--brand); font-size:13px;">
  <strong>敏感度提示：</strong>
  国产化适配权重从 35% 降至 22% 时，PostgreSQL 超越达梦排第一。
  若政策要求明确，推荐结论稳定。
</div>
```

**industry-report 和 guide 类型（SCQA 结构）：**

**industry-report（SCQA）**
```
header（SCQA 序言）
  → 核心结论（3-5 条关键发现）
    每条必须包含：
       - 具体数据点或案例证据
       - 数据来源标注（✅/⚠️/❌）
       - 推理链（数据 → 判断 → 结论）
      Novelty Check：如果删掉数据，这句话是否仍然成立？
        - 成立 → C级常识（即使有数据，结论也是已知的）
        - 不成立 → A或B级洞察
    反例："AI重塑价值链"（无数据，C级常识）
    正例："AI食堂场景渗透率已达40%，年增速超50%（来源：行业研报⚠️），竞品尚未大规模布局"
    → 多章节（section, MECE 分组）
      → 异议框
        → footer
```

**guide（SCQA）**
```
header（SCQA 序言）
  → 核心结论（转型目标 + 关键阶段）
    每条核心结论同 industry-report：数据点 + 来源 + 推理链
    → Phase 1-3（每阶段结论先行，步骤横向归纳）
      → 异议框
        → footer
```

类型选择后加载 `references/layout-patterns.md`、`references/templates/` 和 `references/pyramid-principle.md`。

**Recommendation 结构化（industry-report 和 guide 类型必做）：**
```
每条建议必须包含：
  - 时间轴：未来 12 个月（短期）/ 未来 24 个月（中期）
  - 优先级排序（P0/P1/P2）
  - 预期效果 + 所需资源 + 风险提示
  - No-Regret Move（可选）：即使判断错了也值得做的动作
    例：建设统一数据底座——无论AI方向怎么变化，数据治理都不会浪费

Actionability Check（每条建议自问）：
  这个结论会改变决策吗？
  - 会 → 保留
  - 不会 → 伪洞察，改写或删除
```
**预期异议框**：主内容后、footer 前。黄色警告框，列事实不指令。

**润色 10 项**
```
□ 直角太硬？   □ 颜色刺眼？   □ text-muted 在非白底上？
□ hover/focus 完整？  □ 留白均匀？  □ 字体层级可辨？
□ 叙事弧线完整（问题→冲突→方案）？接受美学三路径指向同一结论？
□ 4px 网格对齐 + 模度比例正确 + 微调表已用（默认微调值，非安全值）？
□ 符号自检：颜色/位置/间距的符号意义与功能一致？
□ CSS 色值有来源可追溯（design-tokens.md / popular-web-designs）？
```

**渲染质量自检：** 加载 `references/rendering-quality.md`，逐条确认后交付。

### 2E+ 最终验证（7 项总闸门）

```
□ Data     — 数据已核实，来源可追溯
□ Structure — IA 结构确认 + 金字塔论证结构符合 MECE
□ Layout   — layout_strategy 已输出，section 编排符合 page_pattern
□ Assurance — 评分矩阵已标注 evidence level（FACT/ESTIMATE/ASSUMPTION）+ 敏感度分析已生成（仅 comparison-matrix 类型）
□ Audience — 受众参数已加载（配色/字号/行高/圆角）
□ Color    — 色值已推导+校准+WCAG 通过
□ Accessibility — CTA ≥44px, hover/focus 完整, 留白均匀
□ Quality  — 所有结论性陈述已通过 2D+ 三道检查（Stakeholder / Novelty / Actionability）
□ Recommendation — 结论先行，异议框在 footer 前；industry-report/guide 类型补充时间轴+优先级
```

全部通过才进入 2F。任意一项未通过 → 返回对应步骤修复。

### 2F 归档 & 交付

`/root/hermes-output/YYYY-MM-DD_项目名/` 下写 `report.html` + `meta.md`。

飞书发送：`source ~/.hermes/.env` 后用文件上传 API（im/v1/files），不可用 MEDIA: 标签。

**交付后：** 记录问题到 `references/output-tracker.md`（只记失败，完美不记）。累计 20 条做一次根因分析。

---

## 三、学科框架（快速参考）

| 学科 | 一句话 | 字段体现 |
|------|--------|---------|
| 经济学 | 动机决定基调（避险/增益/成本） | 推荐框语气 |
| 社会学 | 决策链+场景决定复杂度 | 行数/字体 |
| 心理学 | 锚定/近因/选择超载 → 限制行数 | ≤10 行 |
| 体验设计 | Fitts/Hick/Jakob + 可供性 | 自检清单 |
| 语言学 | 用读者语言命名维度 | 动作短语 |
| 统计学 | 三检验（可比/时效/显著）+ 四精度 | 数据标注 |
| 伦理学 | 标来源、不省略、分观点/事实 | 三级标注 |
| 叙事设计 | 叙事弧线+接受美学+戏剧学三视角 | 润色检查 |
| 数学美感 | 模度比例+4px网格+微调表（安全→舒服值） | 润色检查 |
| 符号学 | 非语言符号系统（颜色/位置/间距的隐含意义） | 符号自检 |

详见：`references/decision-biases.md` / `references/ux-heuristics.md` / `references/cognitive-load-and-flow.md` / `references/narrative-design-examples.md` / `references/design-details.md` / `references/information-architecture.md` / `references/pyramid-principle.md`

> 开发者工具：`references/discipline-evaluation-framework.md` 记录了学科评估方法论和架构评审分类法，用于 skill 迭代而非运行时加载。

**流程方法论（2）**——学科回答"为什么"，方法论回答"怎么做"：

| 方法论 | 一句话 | 流程节点 |
|--------|--------|---------|
| 信息架构（IA） | 信息怎么组织、怎么命名、怎么分组 | Step 1 → 2B+1 |
| 金字塔原理（Minto） | 结论先行、MECE 分组、逐层展开 | 2E 输出格式 → 自检

**论证结构**：使用金字塔原理（Minto），结论先行 → MECE 分组 → 逐层展开。详见 `references/pyramid-principle.md`。

**设计哲学**：
```
① 信息服务于决策（不加装饰，推荐列 pop out）
② 先层级后样式（CSS 顺序：sticky→高亮→普通→图例）
③ 受众决定密度（紧迫紧凑，宽松留白）
④ 一致性建立信任（差异只在有意义处，padding 统一）
⑤ 每个数都有归属（每个 CSS 值都要有理由）
⑥ 从已知推未知（新受众=已知受众风+色相偏移+圆角微调）
⑦ 四层分离：Thinking Layer（学科框架·内部推理质控）→ Decision Layer（criterion-first评分·可输出权重+分值+排名）→ Assurance Layer（evidence等级+敏感度·可审计推理过程）→ Layout Layer（section编排·决定信息物理排列）。每层产出独立可审计，不将内部推理结果直接等同于对外证据。
⑧ 评分可追溯：每个权重附带 weight_rationale，每个分数附带 rubric_match + evidence.level。权重不是直觉分配，分数不是经验估算——每一步都有推导理由。

```

**学科间关系**：体验设计负责功能正确（绿色=推荐），符号学负责文化审核（确认绿色在受众文化中无负面含义）。默认体验设计优先，仅当存在明确文化冲突时符号学覆盖。流程：UX → 生成 → 符号学审核。

**架构演进对照**：\n```text\nv1.0-v1.3   学科框架 → HTML           （Thinking → 直接输出，缺两层）\nv1.4         + Recommendation Scoring （Decision Layer 雏形）\nv1.5         + Layout Intelligence    （Layout Layer 就绪）\nv1.6         + Decision Assurance     （Assurance Layer Phase 1）\nv1.7         + Report Intent + Layer Annotations（Pipeline 选择器 + 层边界标记）\n```
每层的引入均由 output-tracker 积累的失败案例驱动，非预先设计。见 `references/development-roadmap.md`。

---

## 四、自检清单

```
□ 数据已核实（含风险分级 + 审计表）
□ metric_selection 已确认——该受众关心的核心指标选对了？（不是选了个有数据的指标，而是选了对决策有用的指标）
□ 2B+3 评分矩阵已生成（comparison-matrix 类型必做，其他类型可选）
□ 2B+3 权重推导理由已标注（每个 criterion 附带 weight_rationale）
□ 2B+3 评分卡已匹配（每个 score 附带 rubric_match + evidence.level）
□ 2B+3 evidence level 已标注（每个评分附带 FACT/ESTIMATE/ASSUMPTION）
□ 2B+3 sensitivity 已生成（breakpoint + effect，仅 comparison-matrix 类型）
□ 2B+4 layout_strategy 已输出
□ 图表数量不超过3张（2B+2 输出 has_charts 后经强校验通过）
□ 是否走 Fallback？是 → fallback-mode.md 已加载，异议框已标注原因
□ IA 结构已确认（扁平/层级/步骤）+ 扫描路径 3 秒测试通过
□ layout-strategy.md 已加载，section 编排符合 page_pattern
□ 推荐框/hero/kpi_strip 的视觉层级符合 visual_hierarchy 设置
□ 所有结论性陈述已通过 2D+ 三道检查（Stakeholder / Novelty / Actionability）
□ 论证结构符合金字塔原理（结论先行 + MECE 分组）
□ 叙事弧线检查通过（问题→冲突→方案）
□ 核心发现已检查 insight_quality：A（新洞察）或 B（数据总结），非 C（常识复述）
□ 4px 网格对齐 + 微调表已用（默认微调值，非安全值）
□ 符号自检通过：颜色/位置/间距的符号意义与功能一致（加载 language-and-labeling-rules.md 符号学章节）
□ 色值来源已确认（design-tokens.md / popular-web-designs 二选一）
□ popular-web-designs 布局结构已参考
□ 对比方式已选（Type1/2/3），数据不对称不用 Type1
□ 受众确认 + 参数按速查表
□ 维度三筛通过 ≤10行，cell-desc 有 So What
□ CTA ≥44px（Fitts）？选项 ≤10 维度 + ≤5 CTA（Hick）？
□ 标准布局（Jakob），不搞创新
□ 结论先行，HTML 自包含
□ 数据来源三级标注（✅/📊/⚠️）
□ text-secondary ≠ text-muted
□ 无双层缩进，source .env 再发飞书
□ 异议框在 footer 前
```

---

## 五、实操陷阱速查

| 类别 | 陷阱 | 解决 |
|------|------|------|
| 数据 | 子 agent 报错厂商/数据 | 两步调研，不信任未核实断言 |
| 数据 | Type1 PK 但数据量级不对等 | 换 Type2 场景对比 |
| 设计 | 配色太重（深黑表头/大色块） | popular-web-designs 品牌参考验证 |
| CSS | overflow-x:auto 导致 sticky 失效 | html {overflow-x:auto} 兜底 |
| CSS | text-muted 在非白底上 | color:inherit; opacity:0.85 |
| 技术 | 飞书发图用 MEDIA: | 必须文件上传 API |
| 技术 | curl 国内网站走代理 | `--noproxy '*'` |
| IA | 信息不分层级，全部平铺 | IA 三步确认：清单→标签→层级 |
| 论证 | 理由重叠或遗漏（非 MECE） | 加载 pyramid-principle.md 做 MECE 自检 |
| 符号 | 颜色/位置的符号意义与功能矛盾（如红色推荐） | 加载 language-and-labeling-rules.md 符号学章节做符号自检 |
| 伦理 | 编造数据/省略劣势 | 劣势 badge-warning 标注 |
| 推理 | Metric Error——指标选对了但"对谁选"错了（如校领导场景用一次性投入而非TCO） | 2B+2 Step 0 metric_selection：受众关心的指标 ≠ 有数据的指标 |
| 推理 | 雷达图评分无数据来源，不可审计 | 每项评分标注来源（✅/⚠️/❌），来源缺失的维度不纳入评分矩阵 |
|| 推理 | 评分来源不透明，无法回答"为什么是70分" | 2B+3 Step 2 每个评分附带 rationale + evidence.level |
| 推理 | 权重敏感度未知，无法回答"如果权重变了排名变吗" | 2B+3 Step 3b 敏感度分析，记录 breakpoint + effect |
| 推理 | 证据等级混淆（把估算当事实输出） | decision-assurance.md 的 FACT/ESTIMATE/ASSUMPTION 分类规则 |
| 布局 | Hero 和 KPI Strip 数字重复（hero_kpi_duplication） | hero_type=recommendation 时 hero 不展示 stats，全部转到 kpi_strip |
| 布局 | 推荐结论被压在第三屏（recommendation_below_fold） | hero_type=recommendation 时 hero 嵌入 recommendation_box |
| 布局 | 多图 grid 无独立 insight（chart_insight_decoupled） | insight_driven 模式下每个 chart 必须有独立 insight_card |
| 布局 | 图表过多（>3张）挤占结论区（data_visuals_dominate_decision） | 图表数量强制 ≤3，降级为组合图或表格 |
| 布局 | 图表数量正确但未校验超过上限 | 2B+2 输出 has_charts 后在 2B+4 前做数量强制校验 |

---

## 六、预加载清单（按页面类型 + 标签）

标签含义：**ESSENTIAL** = 每次必读 · **OPTIONAL** = 需要时再读 · **RARE** = 很少用到

**页面无关（ESSENTIAL — 每次必读）**
①design-tokens（方向策略） ②color-harmony（色值推导） ③font-ordering（字体） ④audience-layout-tokens（受众参数） ⑤layout-strategy（布局策略决策） ⑥decision-assurance（决策保证体系）

**页面无关（OPTIONAL — 需要时加载）**\n⑦open-source-design-resources ⑧ux-heuristics ⑨affordance-checklist ⑩decision-biases ⑪traps-and-recipes ⑫narrative-design-examples（叙事设计参考） ⑬design-details（数学美感+微调表+数据可视化） ⑭information-architecture（IA 结构参考） ⑮pyramid-principle（咨询方法论） ⑯language-and-labeling（符号学+语言学） ⑰data-visualization（自包含 HTML 图表方案——需图表输出时加载） ⑱rendering-quality（渲染质量自检清单）

**页面无关（RARE — 极少用到）**\n⑲cognitive-load-and-flow

**外部 skill（ESSENTIAL — 每次必读）**\n⑳popular-web-designs（布局结构灵感 + 颜色兜底校准）

---

**比较表（额外加载）**
affordance-checklist · pre-note-template · design-details · pyramid-principle（论证结构自检）

**分析报告（额外加载）**
layout-patterns · templates/（HTML 骨架）· data-verification-workflow · information-architecture（层级 IA）· pyramid-principle（金字塔论证）

**所有参考文件：** `references/` 目录下 25 个文件 + `CHANGELOG.md` + Hermes skill `popular-web-designs`。
- `data-visualization.md`（自包含 HTML 图表方案 — 类型选择逻辑、Inline SVG 实现路径、与现有 palette 集成方式、AI 生图边界说明）
- `scripts/chart_svg.py`（零外部依赖 SVG 图表生成 — 支持 bar/line/donut/radar，支持 --palette 参数）
- `development-roadmap.md`（发展路线图 — v2.x/v3.x 架构方向，来自用户 2026-06-05 分析）
