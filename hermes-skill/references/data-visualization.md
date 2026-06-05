# 自包含 HTML 数据可视化

## 背景约束

当前产出为 self-contained HTML（仅 Google Fonts CDN 外部依赖）。
design-details.md 中已有占位："图表（当前暂不输出，保留未来）"。

本文件记录数据图表/仪表盘在自包含 HTML 中的实现方案和设计规则。

## 技术选型：Inline SVG > 其他

| 方案 | 外部依赖 | DPI 缩放 | 可主题化 | 自包含 |
|---|---|---|---|---|
| **Inline SVG** | 零 | ✅ 矢量无限 | ✅ CSS vars 直接继承 palette | ✅ |
| Embed Chart.js | ~100KB inline script | ✅ | ⚠️ 需额外调色 | ✅ 但 bloated |
| Canvas 绘图 | 零 | ❌ 位图模糊 | ⚠️ 手动代码 | ❌ 需 JS |
| Seedream 等 AI 生图 | API key | ❌ 位图 | ❌ 风格不统一 | ❌ |
| Chart.js CDN | 外部加载 | ✅ | ⚠️ | ❌ 破坏约束 |

**结论：Inline SVG 是唯一符合"零外部依赖 + 矢量 + 继承 palette"的方案。**

## 图表类型与选择逻辑

数据特征 → 自动匹配图表类型：

| 数据特征 | 图表类型 | 优先级 | SVG 实现复杂度 |
|---|---|---|---|
| 类别对比（多个品类/方案的值） | 柱状图（水平/垂直） | P0 | ⭐ 低 |
| 时间序列趋势（月份/季度变化） | 折线图 | P0 | ⭐⭐ 中 |
| 占比/份额 | 环形图（非饼图，更干净） | P1 | ⭐⭐ 中 |
| 多维度评分对比 | 雷达图 | P2 | ⭐⭐⭐ 中高 |
| 二元分布（规模 vs 效率） | 散点图/气泡图 | P3 | ⭐⭐⭐ 高 |
| 时段-场景交叉分析 | 热力图 | P3 | ⭐⭐ 中 |
| KPI 与目标对比 | 子弹图/进度条 | P1 | ⭐ 低 |

**实现优先级：P0 优先（柱状 + 折线），覆盖 80% 场景。**

## 与现有设计体系集成

### 色值继承

图表颜色支持通过 `--palette` 参数从外部传入色值列表，格式：`#c1,#c2,#c3,...`。
不传则使用默认 IBM Carbon 蓝色系。

v1.5 目标：自动从 color-harmony.md 推导的色值继承，不再硬编码。

```css
/* 远期目标（v1.5）：
--chart-color-1: var(--primary-500);
--chart-color-2: var(--primary-300);
--chart-color-3: var(--accent-500);
--chart-grid: var(--border-color);
--chart-text: var(--text-secondary);
*/
```

### 样式约束与 IBM Carbon 一致

```
- 直角（0px border-radius，chart 柱子/饼图无圆角）
- 无投影（no drop-shadow on bars/points）
- 网格线用淡色（1px solid, opacity 0.15）
- 字体用当前 font-family（继承页面字体）
- 标签字号用 --text-xs 或 --text-sm（继承模度比例）
```

### 可访问性

- 每个 SVG 图表加 `<title>` 和 `<desc>`（无障碍描述）
- 柱状图/折线图支持 `<text>` 数据标签（精确值）
- 色盲友好：形状/图案标识 + 色值自检（WCAG AA 对比度）

## 集成方式

在 client-proposal-html 中作为按需加载能力：

```
新增 PAGE_TYPE: data-dashboard（数据仪表盘）
  适用：需要多图表组合展示的数据驱动提案

或作为已有类型的补充能力：
  comparison-matrix → 可选嵌入柱状图/雷达图（数据趋势对比）
  industry-report   → 可选嵌入折线图（趋势变化）
  guide             → 可选嵌入子弹图（目标进度）
```

图表和现有表格的关系不是替代，是互补——精确值用表格，趋势/分布用图表（Cleveland 感知原则）。

**重要：** 图表应在 2B+3 Recommendation Scoring 完成后再生成。评分矩阵决定了哪些维度的数据需要可视化，图表服务于推荐结论，而不是独立展示数据。

## 仪表盘布局

多图表组合时，使用 CSS Grid 2-3 列布局：

```
┌──────────────┬──────────────┐
│  柱状图      │  折线图      │
│  市场分布    │  季度趋势    │
├──────────────┼──────────────┤
│  环形图      │  结论/CTA    │
│  份额占比    │  核心发现    │
└──────────────┴──────────────┘
```

每张图表对应一个卡片（card），沿用页面现有卡片样式（Pico CSS）。

## 与 Seedream / AI 生图的关系

| 场景 | 方案 | 理由 |
|---|---|---|
| 数据图表（柱/线/饼/雷达） | **Inline SVG** | 精确、矢量、可主题化 |
| 概念图/场景示意图 | Seedream 等 | 装饰性、创意方向 |
| 封面/配图 | Seedream 等 | 对外内容创作 |

**不要混淆：数据图表追求精确和一致性，AI 生图追求表达力和意境。两者不互换。**

## 参考链接

- design-details.md（Tufte 数据-墨原则、Cleveland 感知精度表）
- color-harmony.md（色系推导）
- design-tokens.md（受众 Token 策略和参考产品色值）
