# 渲染质量标准（Rendering Quality）

## 定位

本文件收集 2E 执行层的视觉质量规则。这些规则**不进入决策层**（2B+2/2B+3/2B+4 的数据模型），也不属于学科框架，而是 HTML 渲染时的自检清单。

**规则来源：** output-tracker 中同类 failure_reason 累计 ≥ 5 条后提炼。不提前设计。

---

## 图表配对

- [ ] 同一行配对显示的多个 chart-unit，使用相同的 SVG height 参数（chart_svg.py --height 值一致）
- [ ] 每张图必须有自己的独立 insight_card（insight_driven 模式）
- [ ] insight 文字 ≤ 2 句，超长截断
- [ ] 单页面图表总数 ≤ 3 张（超过时降级为表格）

## 卡片与页面对齐

- [ ] 同行的 chart-unit / kpi-card 使用相同的 padding 值
- [ ] grid 布局（chart-pair / radar-grid）中的各列顶部对齐，无下沉
- [ ] 表格相邻行无残留空列
- [ ] 卡片内容不足时，不出现空白残留（flex 布局或 min-height 兜底）

## 文字与排版

- [ ] SVG 中的中文标签不溢出（text-anchor 和 rotate 按 chart_svg.py 规则）
- [ ] evidence badge 不与分数重叠（分值在上，badge 在下）
- [ ] 标题不出现意外换行（white-space: nowrap + text-overflow: ellipsis）
- [ ] 正文行高统一（1.6-1.7），不混用

## 颜色与可访问性

- [ ] 所有关键颜色对通过 WCAG AA ≥ 4.5（色值推导阶段已校验）
- [ ] 非白底上的文字使用 `color: inherit; opacity: 0.85`，不引用 `--text-muted`
- [ ] 所有可点击/可交互元素最小触控区域 ≥ 44px（Fitts 定律）
- [ ] focus/hover 状态有视觉反馈

## 数据标注

- [ ] FACT/ESTIMATE/ASSUMPTION badge 样式统一（字体/间距/圆角一致）
- [ ] 评分依据（rationale）使用 `--text-muted` 色，不喧宾夺主
- [ ] 来源标签（✅/⚠️/❌）与 evidence badge 不重复

## 响应式

- [ ] 宽度 ≤ 768px 时，grid 自动切为单列（已设置 @media 断点）
- [ ] 长表格支持横向滚动（overflow-x: auto）
- [ ] sticky 首列在滚动时正常生效（需 html {overflow-x: auto} 兜底）

---

## 规则更新流程

1. output-tracker 同类 failure_reason 累计 → 5 条
2. 提炼为渲染规则 → 写入本文档对应章节
3. 2E 渲染时新增对应校验
4. 旧 failure 标记为已修复
