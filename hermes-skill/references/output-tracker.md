# 输出质量追踪

只记失败。完美不记。

## 分类体系（与最终验证 7 项对齐 + 补充）

```
data          → 数据可信度问题
structure     → IA/论证结构/MECE 问题
audience      → 受众画像/场景判断错误
color         → 配色/校准/WCAG 问题
accessibility → CTA/留白/hover-focus 问题
quality       → 结论未通过 Stakeholder/Novelty/Actionability 检查
recommendation→ 结论缺失/不明确/异议框问题
narrative     → 叙事弧线/接受美学问题
language      → 术语/命名/符号学问题
insight       → 洞察深度不足（建议合并到 quality）
chart_decision   → 图表选择/指标选择/可视化效果问题
layout           → 布局策略问题（page_pattern / hero / kpi / chart_insight / visual_priority）
```

### layout_failure 分类标准（来自 v1.5.0 首次实机验证）

```yaml
hero_kpi_duplication:
  desc: "Hero 和 KPI Strip 展示重复数字，用户滚动300px内看到两次相同指标"
  fix: "hero_type=recommendation 时 hero 不展示 stats，全部转到 kpi_strip"

recommendation_below_fold:
  desc: "推荐结论被压在第三屏，executive_summary 打开3秒内看不到推荐"
  fix: "hero_type=recommendation 时 hero 嵌入 recommendation_box，不独立成 section"

chart_insight_decoupled:
  desc: "多个 chart 放在 grid 中但无独立 insight 配对"
  fix: "insight_driven 模式下每个 chart 必须有独立 insight_card，禁止 standalone grid"

data_visuals_dominate_decision:
  desc: "图表区（如 4 张雷达图）吃掉 35%+ 页面，决策结论仅占 15%"
  fix: "图表限制 ≤3 张；visual_priority=decision 时图表区 ≤25% 页面"

wrong_page_pattern:
  desc: "page_pattern 与内容原型不匹配（如 vendor_comparison 用了 executive_summary）"
  fix: "引入 proposal_archetype 输入层修正"
```

### insight_quality 分级标准（客观化）

```
A: 数据支持 + 结论不是行业共识（新洞察）
B: 数据支持 + 结论属于行业共识（数据总结）
C: 没有新信息，属于常识复述
```

### metric_selection 字段（来自 2B+2 Step 0）

```yaml
metric_selection:
  audience_role: 校领导/CIO/财务/...
  decision_goal: "..."
  critical_metrics: ["指标A", "指标B", "指标C"]
  metric_data_confidence: ✅ / ⚠️ / ❌
```

### chart_decision 字段（来自 2B+2 后续步骤）

```yaml
chart_decision:
  page_type: comparison-matrix / industry-report / guide
  data_type: 类别对比 / 时间趋势 / 占比 / 多维评分
  chart_selected: bar / line / donut / radar / none(表格)
  chart_source: 自动推荐 / 手动指定
  outcome: correct / incorrect
  note: "决策正确/错误的原因"
visualization_effect:
  underused / appropriate / overused
```

### layout 字段（来自 2B+4）

```yaml
layout:
  page_pattern: executive_summary / comparison_first / roadmap_planning / problem_solving / compliance_report
  hero_type: recommendation / data / problem / neutral
  kpi_strip_enabled: true / false
  title_system_levels: 3 / 4
  numbering: true / false
  chart_layout: insight_driven / standalone / embedded
  section_density: compact / medium / spacious
  visual_hierarchy: strong / moderate / flat
  visual_priority: decision / data / balanced
  outcome: correct / partial / incorrect
  note: "布局策略是否适合受众和场景"
  failure_reason: ""                    # 如：hero_kpi_duplication / recommendation_below_fold / chart_insight_decoupled / data_visuals_dominate_decision / wrong_page_pattern
  improvement_hint: ""                 # 如：switch_to_roadmap_planning / enable_kpi_strip / merge_hero_recommendation / add_chart_insight_pairing

### assurance 字段（来自 2B+3 Decision Engine）

```yaml
assurance:
  evidence_generated: true / false
  sensitivity_generated: true / false
  rubric_complete: true / false          # 每个 criterion 是否有 rubric + rubric_match
  weight_rationale_complete: true / false # 每个权重是否有 weight_rationale
  note: "evidence 覆盖率和敏感度分析完成情况"
```
```

## 记录格式

```yaml
- category: color
  cause: "推导色系偏冷，银行审计场景要求暖调保守色"
  fix:    "经济学术司确定动机时标定『避险』→ 自动走暖调"
```

## 单次输出记录

```yaml
---
date: 2026-06-05
output: AI智慧校园决策报告
type: comparison-matrix
audience: 校长办公会
issues:
  - category: data
    cause: "雷达图评分无数据来源（85/80/55/50/45），属于主观赋值"
    fix:    "未通过三检验的数据维度不纳入雷达图"
  - category: quality
    cause: "推荐结论直接跳结论→理由，缺乏评分引擎"
    fix:    "comparison-matrix 增加加权评分表作为推荐前置步骤"
  - category: chart_decision
    cause: "柱状图使用一次性投入而非3年TCO，metric_selection 错误"
    fix:    "2B+2 增加 metric_selection 子步骤"
  - category: color
    cause: "图表颜色（蓝色）脱离页面设计系统（橙色）"
    fix:    "chart_svg.py 添加 --palette 参数"
chart_decision:
  page_type: comparison-matrix
  chart_selected: bar, radar ×4
  outcome: partial_success
  note: "metric_selection 错误（一次性投入vsTCO）"
rating: B
layout:
  page_pattern: executive_summary
  hero_type: recommendation
  kpi_strip_enabled: true
  title_system_levels: 3
  numbering: true
  chart_layout: insight_driven
  section_density: spacious
  visual_hierarchy: strong
  outcome: pending_review
  note: "v1.5.0 首次实机测试，待确认投屏效果"
  failure_reason: ""
  improvement_hint: ""
---
date: 2026-06-05
output: 省级政务云数据库选型（测试 v1.5.0）
type: comparison-matrix
audience: 省级政务云技术负责人/CIO
chart_decision:
  page_type: comparison-matrix
  chart_selected: radar ×4, bar ×1
  outcome: correct
  note: "radar + bar 覆盖能力对比和TCO对比，数据来源已标注"
layout:
  page_pattern: executive_summary
  hero_type: recommendation
  hero_weight: heavy
  kpi_strip_enabled: true
  title_system_levels: 3
  numbering: true
  chart_layout: insight_driven
  section_density: spacious
  visual_hierarchy: strong
  outcome: pending_review
  note: "v1.5.0 首次实机验证"
  failure_reason: "hero_kpi_duplication | recommendation_below_fold | chart_insight_decoupled | data_visuals_dominate_decision"
  improvement_hint: "hero合并recommendation_box | KIP与Hero去重 | insight_driven改为每个chart+insight绑定 | 降低雷达图区块权重 | 考虑proposal_archetype=vendor_comparison匹配comparison_first"
---
date: 2026-06-05
output: 企业私有云建设方案比选（测试 v1.6.0）
type: comparison-matrix
audience: 企业CIO/CTO
chart_decision:
  page_type: comparison-matrix
  chart_selected: radar ×1, bar ×1
  outcome: correct
  note: "2张图各配insight，低于3张上限"
layout:
  page_pattern: executive_summary (A1)
  hero_type: recommendation
  hero_weight: heavy
  kpi_strip_enabled: true
  title_system_levels: 3
  numbering: true
  chart_layout: insight_driven
  section_density: spacious
  visual_hierarchy: strong
  visual_priority: decision
  outcome: pending_review
  note: "v1.6.0 全流程测试。hero合并推荐框，kpi无重复，evidence badge已输出，敏感度标注已输出"
  failure_reason: ""
  improvement_hint: ""
assurance:
  evidence_generated: true
  sensitivity_generated: true
  note: "FACT×8, ESTIMATE×12, ASSUMPTION×0。敏感度发现信创合规28%时翻转"
---
date: 2026-06-05
output: 企业运维AI选型与成长指南（v1.6.0 education）
type: guide
report_intent: education
audience: 企业运维人员
layout:
  page_pattern: executive_summary
  hero_type: problem
  hero_weight: medium
  kpi_strip_enabled: true
  title_system_levels: 3
  numbering: true
  chart_layout: insight_driven
  section_density: medium
  visual_hierarchy: strong
  visual_priority: decision
  outcome: pending_review
  note: "guide类型+education intent，跳过2B+3评分引擎。输出概念框架+学习路径+场景矩阵"
  failure_reason: ""
  improvement_hint: ""
assurance:
  evidence_generated: false
  sensitivity_generated: false
  note: "education intent 不要求 evidence+sensitivity"
layer_distribution:
  decision: 2
  assurance: 0
  presentation: 6
  maturity:
    stable: 5
    beta: 1
    experimental: 1
  note: "education intent，assurance 层字段为0，符合预期"
```
type: comparison-matrix
audience: 企业CIO/CTO
chart_decision:
  page_type: comparison-matrix
  chart_selected: radar ×1, bar ×1
  outcome: correct
  note: "2张图各配insight，低于3张上限"
layout:
  page_pattern: executive_summary (A1)
  hero_type: recommendation
  hero_weight: heavy
  kpi_strip_enabled: true
  title_system_levels: 3
  numbering: true
  chart_layout: insight_driven
  section_density: spacious
  visual_hierarchy: strong
  visual_priority: decision
  outcome: pending_review
  note: "v1.6.0 全流程测试。hero合并推荐框，kpi无重复，evidence badge已输出，敏感度标注已输出"
  failure_reason: ""
  improvement_hint: ""
assurance:
  evidence_generated: true
  sensitivity_generated: true
  note: "FACT×8, ESTIMATE×12, ASSUMPTION×0。敏感度发现信创合规28%时翻转"
```
```

## 触发机制

- 每 10 条 → 打印当前 top 3 失败类别
- 每 20 条 → 做一次根因分析
- 每 50 条 → 做一次 skill 架构健康度检查

## Layer 分布统计（每次输出后更新）

记录本次输出中各层字段的数量，用于跨案例的趋势分析：

```yaml
layer_distribution:
  decision: 12          # 本次输出中属于 decision 层的字段数
  assurance: 8          # 本次输出中属于 assurance 层的字段数
  presentation: 7       # 本次输出中属于 presentation 层的字段数
  maturity:
    stable: 15          # 经过多个案例验证的字段数
    beta: 5             # 出现2-3次的字段数
    experimental: 2     # 首次出现的字段数
  note: "assurance 字段持续增长，关注是否稳定后可拆层"
```