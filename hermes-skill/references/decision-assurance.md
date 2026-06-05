# 决策保证（Decision Assurance）

## 为什么需要这一层

2B+3 Decision Engine 产出了评分矩阵和推荐排名。但读者收到报告后会问：

> 为什么国产化给 100 分？
> 如果权重变了会怎样？
> 这些数据哪些是事实、哪些是估算？

Decision Assurance 负责为每个评分提供可审计的**证据等级**、**评分依据**和**敏感度分析**。

---

## 一、证据等级体系

### 三级分类

| 等级 | 标签 | 含义 | 示例 |
|------|------|------|------|
| FACT | 绿色 | 有公开来源可验证的断言 | 信创目录、政府采购公告、官方技术文档、产品官网、已公开的招标结果 |
| ESTIMATE | 黄色 | 基于行业数据的合理推断 | TCO估算、运维人力成本预测、基于公开评测数据的性能推断 |
| ASSUMPTION | 红色 | 缺乏可靠数据，基于经验的假设 | 未来扩展性预期、3-5年后的技术演进、供应商长期服务稳定性 |

### 判定规则

**FACT 判定条件（全部满足）：**
1. 数据源是公开可查的（官网、政府公告、权威机构报告）
2. 数据本身是静态的（不依赖假设条件）
3. 不存在合理的质疑空间

**ESTIMATE 判定条件（任一满足）：**
1. 基于公开数据但推导过程有假设（如 TCO = 硬件 + 软件 + 人力，人力为估算）
2. 数据来自非权威来源（行业博客、社区讨论、厂商宣传材料）
3. 数据是动态的，受市场波动影响

**ASSUMPTION 判定条件（任一满足）：**
1. 无公开数据支撑
2. 基于 agent 领域知识的推测
3. 指向未来不可量化的事件

### 误用陷阱

| 错误用法 | 正确做法 |
|---------|---------|
| 把 TCO 估算标为 FACT | TCO 永远是 ESTIMATE，因为涉及人力+硬件+市场波动 |
| 把 "DM8 进入信创目录" 标为 ESTIMATE | 这是公开可查事实 → FACT |
| 把 "3年后扩展性" 标为 ESTIMATE | 没有可靠数据支撑未来趋势 → ASSUMPTION |
| 不加 evidence.level，所有评分用默认值 | 每个评分必须标注，不能跳过 |

### 证据覆盖比率诊断

产出报告后记录 FACT / ESTIMATE / ASSUMPTION 的计数，作为报告质量的辅助指标：

| 比率特征 | 诊断 | 建议 |
|---------|------|------|
| FACT ≥ 60% | 报告基于扎实数据，可信度高 | 正常交付 |
| ESTIMATE ≥ 50% | 半数以上为推断，需要说明假设条件 | 在报告声明中标注"部分数据基于行业估算" |
| ASSUMPTION ≥ 30% | 报告偏向推测性，结论不稳健 | 考虑降低推荐信心水平，或替换缺乏数据支撑的维度 |
| FACT + ESTIMATE = 100%, ASSUMPTION = 0% | 理想状态 | 保持 |
| 全部为 FACT | 可能选择了过于保守的维度，回避了需要判断的关键问题 | 检查是否漏掉了需要推算的维度 |

记录到 output-tracker 的 assurance.note 字段，用于跨报告的趋势分析。

### 在评分矩阵中的展示

```html
<td>
  <div class="score-value">100</div>
  <div class="score-evidence">
    <span class="evidence-badge evidence-fact">FACT</span>
  </div>
  <div class="score-rationale">信创目录核心产品</div>
</td>
```

CSS:

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

---

## 二、敏感度分析（Sensitivity Analysis）

### 为什么需要

评分矩阵依赖权重分配。权重的设定会直接影响推荐结果。

例如：
- 国产化适配权重 35% → 达梦第一
- 国产化适配权重降到 22% → PostgreSQL 反超

读者拿到报告后会问：**如果权重变了结果变吗？**

敏感度分析回答这个问题。

### 计算规则

**算法：**
```
for each criterion in criteria:
    固定其他 criteria 的 weight 和所有 scores 不变
    当前 criterion 的 weight 从 baseline 逐步降至 5%
    每降 5%，重算所有 candidates 的 weighted_score
    记录 ranking 首次翻转时的 weight 值 → breakpoint
    记录翻转效果 → effect
```

**输出格式：**

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
    insight: "阈值高，实际不太敏感（需三倍当前权重才翻转）"
```

### 解读规则

| breakpoint 与 baseline 的关系 | 含义 | 建议 |
|-------------------------------|------|------|
| breakpoint < baseline - 10 | 高度敏感——权重小幅波动可能改变推荐 | 必须标注在报告中，建议附加定性判断 |
| breakpoint 在 baseline ± 10 内 | 中等敏感 | 标注但决策者自行评估风险 |
| breakpoint > baseline + 10 | 低敏感——权重大幅下降才翻转 | 可选标注，推荐结论稳健 |
| 无翻转（weight 降到 5% 仍未翻转） | 该维度对排名无决定性影响 | 不标注 |

### 在页面中的展示

```html
<div class="sensitivity-note" style="margin-top:12px; padding:12px 16px;
     background:#F0F9FF; border-left:3px solid var(--brand); font-size:13px;">
  <strong>敏感度提示：</strong>
  国产化适配权重从 35% 降至 22% 时，PostgreSQL 超越达梦排第一。
  若政策要求明确，推荐结论稳定。
</div>
```

---

## 三、评分卡体系（Scoring Rubric）

### 为什么需要评分卡

证据体系回答了"数据来源是否可信"，但回答不了另一个问题：**"为什么给 100 分而不是 90 分？"**

当前做法是 agent 凭经验直接输出分值，没有可追溯的评分标准。咨询公司的做法是：每个 criterion 先定义评分卡（rubric），再将事实匹配到具体档位。

**重要（定位声明）：**

rubric 不承诺"评分绝对正确"。它只承诺一件事——**评分可追溯、可反驳**。

```
无 rubric：
  分数：100
  → 质疑："我觉得应该 80"
  → 无依据，变成谁嗓门大谁对

有 rubric：
  分数：100，匹配档位"信创目录核心 + EAL4+ 认证"
  → 质疑："达梦只有省级案例没有国家级认证，应掉到第二档"
  → 这是一个可讨论的事实问题（达梦有没有国家级认证）
  → 而非空对空的"我觉得"
```

rubric 是一份**可讨论的评分说明书**。它不终结争议，它让争议有据可依。

### 评分卡设计原则

**原则一：服务于受众关心的内容，而非随意列选项。**

每一个评分卡档位必须来自三个来源之一（按优先级）：

1. **调研阶段（2A）发现的公开事实**——如信创目录等级、政府采购评分细则、厂商认证体系。这是最硬的依据。
2. **受众关心的核心问题（2B 确认）**——如 CIO 关心运维复杂度，就该按"有无成熟运维体系"分档，而不是按"产品知名度"。
3. **无公开标准也无受众明确偏好时**——按行业常识分 5±1 档（MECE + 不重叠）。需要在 rubric_source 中标注"推导"。

**反例（脱离事实的随机分档）：**
```yaml
rubric:
  - match: "很好"       # 什么叫"很好"？
    score_range: [90, 100]
  - match: "比较好"     # 和"很好"什么区别？
    score_range: [70, 85]
```
→ 档位无事实锚点，分档模糊不可审计。

**正例（基于事实的分档）：**
```yaml
rubric:
  - match: "信创目录核心 + EAL4+ 认证 + 多省案例已验证"
    score_range: [95, 100]
  - match: "信创目录内 + 省级案例已验证"
    score_range: [80, 90]
  - match: "信创目录外但有替代发行版方案"
    score_range: [60, 75]
  - match: "非国产/纯外资"
    score_range: [0, 10]
```
→ 每个档位有明确的可核实条件，讨论时直接查事实落在哪一档。

**原则二：档位之间的分界必须能被事实检验。**

```
"有国家级认证" vs "仅有省级案例" → 可以查官方目录 → ✅ 可检验
"技术先进" vs "技术一般" → 无法定义"先进"的阈值 → ❌ 不可检验
```

不可检验的分档不建。至少留一个可查的锚点（如认证等级、案例数量、第三方评测分数区间）。

**原则三：所有权重配比必须附带 `weight_rationale`，说明"为什么是这个百分比"。**

权重推导一律标为 ESTIMATE——权重设定本身无法成为 FACT，但必须有推导理由。`weight_rationale` 的内容应引用受众分析（2B）和调研发现（2A）。

### 评分卡结构示例

```yaml
criteria:
  - name: 国产化适配
    weight: 35
    weight_rationale: "省级政务云，政策合规为第一优先级。参照同类项目权重区间(30-40%)取中间值"
    rubric:
      - match: "信创目录核心 + EAL4+ 认证 + 多省案例"
        score_range: [95, 100]
      - match: "信创目录内 + 省级案例已验证"
        score_range: [80, 90]
      - match: "信创目录外但有替代发行版"
        score_range: [60, 75]
      - match: "非国产/纯外资"
        score_range: [0, 10]
    rubric_level: 经验评分卡
    rubric_source: "基于政务云采购公开信息归纳"

    scores:
      达梦DM8:
        value: 100
        rubric_match: "信创目录核心 + EAL4+ 认证 + 20+省级案例"
        rationale: "信创目录核心产品，EAL4+认证，20+省级案例"
        evidence:
          level: FACT
          sources: ["工信部目录", "政府采购公示"]
```

**关键规则：**
- `rubric[].match` — 事实条件描述，打分时 match 文本直接填入 `scores[].rubric_match`
- `rubric[].score_range` — 该档位的分值区间，取值时在区间内浮动（上限为 100% 符合，下限为刚好符合）
- 每个 score 必须同时携带 `evidence.level`（数据可信度）和 `rubric_match`（匹配的档位描述）——两者独立且互补
- 所有权重和评分卡必须附带 `weight_rationale` + `rubric_source`

### 评分卡等级

和 evidence 体系一样，rubric 本身也有来源等级：

| 等级 | 含义 | 示例 | rubric_source 示例 |
|------|------|------|-------------------|
| **公开评分卡** | 有行业公认的评分标准 | Gartner Magic Quadrant 评估维度、信创目录认证等级、等保等级 | "引用工信部信创目录评分细则" |
| **经验评分卡** | 基于行业经验的合理分档 | 用户体验评价档位（好/中/差）、运维难度分类 | "基于政务云选型经验，分四档" |
| **推导评分卡** | 无公开标准，agent 自建档位 | 厂商生态绑定程度、未来扩展性评级 | "无公开标准，按厂商绑定深度分三档" |

### 与 evidence 体系的关系

```
evidence.level 回答：「数据来源可信吗？」
    ↓
rubric[].match 回答：「这个分数对应什么档位？」
    ↓
两者共同输出：「该打分有可信依据，且分档规则可追溯」
```

评分卡解决了"为什么是 100 不是 90"的问题——因为事实落在这个档位，而不是 agent 感觉差了 10 分。

### 诊断规则

| 状态 | 含义 | 建议 |
|------|------|------|
| 每个 criterion 有 rubric | 评分体系完整 | 正常输出 |
| 有 rubric 但无 weight_rationale | 评分可追溯但权重不可追溯 | 补充 weight_rationale |
| 既无 rubric 也无 weight_rationale | 评分和权重均不可审计 | 回退到 2B+3 Step 1 补充 |

---

## 四、与 2B+3 的数据契约关系

```
2B+3 Decision Engine 产出：
  decision_framework.criteria[]    → 维度定义
  criteria[].weight                → 权重
  criteria[].weight_rationale      → 权重推导理由（为什么这个%）
  criteria[].rubric                → 评分卡（match + score_range 档位）
  criteria[].rubric_level          → 评分卡等级（公开/经验/推导）
  criteria[].scores[].value        → 评分
  criteria[].scores[].rubric_match → 评分匹配的档位文本
  criteria[].scores[].rationale    → 评分依据
  criteria[].scores[].evidence     → 证据等级 + 来源

  candidates[].weighted_score      → 总分
  sensitivity[]                    → 敏感度
```

```
2E 渲染输出：
  评分矩阵表
    → 表头：维度 | 权重 | 方案A | 方案B | 方案C | 方案D
    → 每格：score + evidence badge + rationale
    → 末行：加权总分
  → 推荐框
  → 敏感度注释（如有高度敏感维度）
```

---

## 五、Phase 2 预留

当前版本（Phase 1）不输出：

| 能力 | 说明 | 入口条件 |
|------|------|---------|
| Criterion Confidence | 每个维度可信度的置信数值（0-1） | Phase 1 稳定运行，积累 evidence 使用经验后 |
| Recommendation Confidence | 所有 criterion confidence 的加权聚合 | Criterion Confidence 就绪后 |
