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

insight_quality 分级标准（客观化）:
  A: 数据支持 + 结论不是行业共识（新洞察）
  B: 数据支持 + 结论属于行业共识（数据总结）
  C: 没有新信息，属于常识复述

Novelty Check: 如果删掉数据，这句话是否仍然成立？
  成立 → C。不成立 → A或B。

Actionability Check: 这个结论会改变决策吗？
  不会 → 伪洞察，优先记录和修复。

=== 推荐记录格式，用于 insight 问题 ===
- category: insight
  cause: "核心发现'AI重塑价值链'无数据支撑，属于C级常识复述"
  fix:    "每条核心发现强制引用数据点+来源+推理链"
```

## 记录格式

每条记录强制三字段，各 ≤50 字：

```yaml
- category: color
  cause: "推导色系偏冷，银行审计场景要求暖调保守色"
  fix:    "经济学术司确定动机时标定『避险』→ 自动走暖调"
```

## 单次输出记录

```yaml
---
date: 2026-06-05
output: AI大模型对比_v3
type: comparison-matrix
audience: AI初学者
issues:
  - category: recommendation
    cause: "推荐列高亮但无『推荐理由』总结行"
    fix:    "对比表末行加『综合建议』行，badge标注推荐方案"
  - category: color
    cause: "推导品牌紫蓝 #6366F1 在投屏场景下偏暗"
    fix:    "2C Step3 增加『投屏场景→色值提明度10%』规则"
rating: acceptable
---
```

## 统计入口（≥10 条后执行）

```bash
# 统计各 category 出现次数，降序排列
grep -oP '(?<=category: ).*' output-tracker.md | sort | uniq -c | sort -rn

# 筛选某类型的失败
grep -A2 'category: color' output-tracker.md
```

## 触发机制

- 每 10 条 → 打印当前 top 3 失败类别
- 每 20 条 → 做一次根因分析，决定下个版本迭代方向
- 每 50 条 → 做一次 skill 架构健康度检查

## 具体操作

```sh
# 看 top 3
grep 'category:' ~/.hermes/skills/creative/client-proposal-html/references/output-tracker.md | \
  sort | uniq -c | sort -rn | head -3

# 看某类的所有记录
grep -B1 -A4 'category: color' ~/.hermes/skills/creative/client-proposal-html/references/output-tracker.md
```
