# 布局策略决策（Layout Strategy Decision）

## 为什么需要这一步

现有流程从 IA（信息分组）直接到 HTML（页面生成），中间缺少一个显式步骤：

**信息怎么在物理页面上排列，才能最大化说服力？**

IA 回答了"内容如何分组"——这是信息结构问题。

Color 回答了"用什么颜色"——这是视觉基调问题。

但下面这些决定无人问津：

- 推荐框放在页面顶部还是数据后面？
- KPI 用大数字卡片横向排列，还是嵌入正文？
- 图表是并排放还是和洞察配对放？
- 标题分几级？是否需要编号前缀？
- 页面入口用什么视觉重量——标题 alone 还是标题 + 大数字 + 推荐三合一？

这些决定的集合 = Layout Decision。

---

## 一、流程定位

```
2B+2  Data Expression   → 决定了有哪些图表/表格（数据类型问题）
2B+3  Recommendation    → 决定了推荐结论的数据模型（评分问题）
2C    Color             → 决定了视觉基调（配色问题）
                        ↓
    [2B+4] Layout Decision  ← 新增
                        ↓
2D    Preflight         → 检查布局就绪
2E    HTML Generation   → 策略驱动的 section 编排
```

Layout Decision 根据以上所有上游输出的总和，决定输出一个 **layout_strategy** 字典，直接驱动 2E 的 HTML 渲染。

---

## 二、数据模型

```yaml
layout_strategy:
  # ── 页面骨架选择 ──
  page_pattern: executive_summary    # 哪个 skeleton
  #   available: executive_summary / comparison_first /
  #              roadmap_planning / problem_solving / compliance_report

  # ── Hero 区域 ──
  hero_type: recommendation          # recommendation / data / problem / neutral
  hero_weight: heavy                 # heavy / medium / light（影响字号/间距/装饰）

  # ── KPI Strip ──
  kpi_strip:
    enabled: true                    # true / false
    metrics: []                      # 从 metric_selection 继承，最多 4 个
    #   [{value: 540, unit: 万, label: 年节省, color: primary}]

  # ── 标题系统 ──
  title_system:
    levels: 3                        # 3 / 4（L1-L3 或 L1-L4）
    numbering: true                  # true / false（01 / 02 / 03 前缀）

  # ── 图表布局 ──
  chart_layout: insight_driven       # insight_driven / standalone / embedded

  # ── 密度 ──
  section_density: medium            # compact / medium / spacious

  # ── 视觉层级权重 ──
  visual_hierarchy: strong           # strong / moderate / flat

  # ── 视觉重心偏好 ──
  visual_priority: decision          # decision / data / balanced
  #   decision: 结论区（hero+kpi+recommendation）权重 ≥ 数据区（图表）
  #   data:     数据区（图表）可占更多页面空间
  #   balanced: 结论和数据各占约 40%/35%
```

---

## 三、Page Patterns（骨架定义）

每个 pattern 定义为一个有序的 section 数组。HTML 生成器按顺序渲染每个 section。

### Pattern A：executive_summary（咨询报告型）

**适用场景：** 面向决策层的提案/投资决策，受众需要先看结论后看证据。

**根据 hero_type 分两种变体：**

**变体 A1：hero_type=recommendation（推荐结论直接嵌入 Hero）**

```
Sections（按渲染顺序）:
  [hero_section]          L1 标题 + 推荐方案框（标题+理由+关键结论）← 不展示重复数字
  [kpi_strip]             3-4 个大数字卡片（全部关键指标，与 hero 不重复）
  [scoring_matrix]        评分表（如果有评分数据）
  [chart_insight_row]     图表 + 洞察绑定（1-3 组，每组 chart+insight 绑定）
  [detail_section]        详细数据/证据
  [roadmap_section]       实施路线（如果有）
  [risk_section]          风险评估
  [objection_box]         预期异议
  [footer_section]        来源声明 + 免责
```

**变体 A2：hero_type≠recommendation（标准执行摘要）**

```
Sections:
  [hero_section]          L1 标题 + 结论陈述（无推荐框，仅有定位）
  [kpi_strip]             关键指标数字
  [recommendation_box]    推荐方案（独立 section，位于 kpi 之后）
  [scoring_matrix]
  [chart_insight_row]
  [detail_section]
  [roadmap_section]
  [risk_section]
  [objection_box]
  [footer_section]
```

### Pattern B：comparison_first（对比优先型）

**适用场景：** 选型/比价场景，受众先看对比再要结论。

```
Sections:
  [hero_section]          L1 标题 + 一句话定位
  [comparison_table]      对比表（最核心，放在第二屏）
  [kpi_strip]             关键指标数字
  [recommendation_box]    推荐方案（结论在后）
  [chart_insight_row]     图表 + 洞察
  [detail_section]
  [objection_box]
  [footer_section]
```

### Pattern C：roadmap_planning（路线图型）

**适用场景：** 数字化转型/智慧校园/阶段建设，受众关心进度。

```
Sections:
  [hero_section]          L1 标题 + 阶段总览
  [kpi_strip]             总预算/周期/里程碑数
  [current_state]         现状分析
  [roadmap_section]       路线图（核心）
  [recommendation_box]    实施建议
  [risk_section]
  [objection_box]
  [footer_section]
```

### Pattern D：problem_solving（问题解决型）

**适用场景：** 故障分析/性能优化/根因排查。

```
Sections:
  [hero_section]          L1 标题 + 问题陈述（醒目）
  [problem_analysis]      根因分析
  [solution_comparison]   方案对比
  [recommendation_box]    推荐方案
  [implementation_plan]   实施计划
  [risk_section]
  [objection_box]
  [footer_section]
```

### Pattern E：compliance_report（合规报告型）

**适用场景：** 等保整改/安全建设/合规审计。

```
Sections:
  [hero_section]          L1 标题 + 合规总评级
  [gap_analysis]          差距分析表
  [risk_matrix]           风险等级矩阵
  [recommendation_box]    整改建议
  [roadmap_section]       整改路线
  [objection_box]
  [footer_section]
```

---

## 四、Section 类型详解

每个 section 有一个独立的渲染函数，接受 `layout_strategy` 参数控制样式。

### 4.1 hero_section

**输入：** 页面标题、一句话定位/结论、page_type、layout_strategy

**核心规则：hero_type=recommendation 时，hero 兼任 recommendation_box，不展示重复数字。** 所有数字指标转移到 kpi_strip，hero 只展示：
1. L1 标题
2. 推荐框内容（badge + 推荐方案名 + 理由 + 关键结论文字）
3. 不展示 hero_stats（stats 全部交给 kpi_strip）

**根据 hero_type 变化：**

| hero_type | 内容 | 视觉风格 |
|-----------|------|---------|
| recommendation | 推荐方案名 + 推荐理由 + 关键结论文字 | ⚠️ 不展示大数字（stats 转到 kpi_strip）。大字号 + 边框/底色高亮 |
| data | 核心数据（总投资/年节省/回收期） | 大数字 + 小标签 |
| problem | 问题陈述 + 影响范围 | 醒目警告色 + 大字号 |
| neutral | 标题 + 副标题 | 标准标题 |

**根据 hero_weight 变化：**

| weight | L1 字号 | padding | 装饰 |
|--------|---------|---------|------|
| heavy | 36-40px | 64px top/bottom | 2px 下边框 + 装饰线 |
| medium | 28-32px | 48px top/bottom | 2px 下边框 |
| light | 24-26px | 32px top/bottom | 无装饰 |

**HTML 骨架（hero_type=recommendation, weight=heavy）——推荐结论嵌入 Hero：**

```html
<div class="hero hero--recommendation">
  <h1 class="hero__title">省级政务云数据库选型</h1>
  <div class="hero__recommendation">
    <div class="hero__badge">推荐方案</div>
    <div class="hero__option">达梦DM8 + openGauss 双库并行</div>
    <ul class="hero__reasons">
      <li>综合评分 76.0，五维评估排名第一</li>
      <li>3年TCO约800万，预算占用仅27%</li>
      <li>Oracle语法兼容，迁移风险最低</li>
    </ul>
  </div>
  <!-- 无 hero__stats — 全部转到 kpi_strip -->
</div>
```

**HTML 骨架（hero_type=data, weight=heavy）：**

```html
<div class="hero hero--data">
  <h1 class="hero__title">校园新能源改造投资决策</h1>
  <div class="hero__conclusion">推荐实施：光伏 + 储能 + LED</div>
  <div class="hero__stats">
    <div class="hero__stat">
      <span class="hero__stat-value">540</span>
      <span class="hero__stat-unit">万元</span>
      <span class="hero__stat-label">预计每年节省</span>
    </div>
    <div class="hero__stat">
      <span class="hero__stat-value">5.4</span>
      <span class="hero__stat-unit">年</span>
      <span class="hero__stat-label">回收期</span>
    </div>
    <div class="hero__stat">
      <span class="hero__stat-value">2900</span>
      <span class="hero__stat-unit">万元</span>
      <span class="hero__stat-label">总投资</span>
    </div>
  </div>
</div>
```

### 4.2 kpi_strip

**位置：** hero 之后、所有正文之前

**规则：**
- 最多 4 个指标
- 横向排列，flex 或 grid
- 每个指标：大数字（32-48px）+ 单位（14-16px）+ 标签（12-14px）
- 指标从 metric_selection 继承，按优先级排序
- 颜色：visual_hierarchy=strong 时使用品牌色，flat 时使用中性色

**HTML 骨架：**

```html
<div class="kpi-strip">
  <div class="kpi-strip__item">
    <div class="kpi-strip__value">540<span class="kpi-strip__unit">万</span></div>
    <div class="kpi-strip__label">年节省</div>
  </div>
  <!-- × N -->
</div>
```

### 4.3 recommendation_box

**位置：** 取决于 page_pattern：
- executive_summary：kpi_strip 之后
- comparison_first：comparison_table 之后
- roadmap_planning：roadmap 之后

**规则：**
- 视觉冲击力强于其他正文块
- 使用品牌色边框或底色
- 包含：推荐标题 + 推荐理由（3-5 条）+ 预期效果
- visual_hierarchy=strong 时：使用边框/底色高亮 + 特殊图标
- visual_hierarchy=flat 时：标准卡片样式

**HTML 骨架（strong）：**

```html
<div class="recommendation-box recommendation-box--strong">
  <div class="recommendation-box__badge">推荐方案</div>
  <h3 class="recommendation-box__title">组合方案</h3>
  <p class="recommendation-box__subtitle">光伏 + 储能 + LED</p>
  <ul class="recommendation-box__reasons">
    <li>综合评分 72.25，排名第一</li>
    <li>总投资 2900 万，3 年内实现正现金流</li>
    <li>实施风险可控，分三期推进</li>
  </ul>
</div>
```

### 4.4 section_title

**根据 title_system.levels 和 numbering 变化：**

| Level | CSS class | 字号 | 样式 |
|-------|-----------|------|------|
| L1 | `.hero__title` | 36-40px | 页面标题，仅 hero 区使用 |
| L2 | `.section__title` | 22-26px | 章节标题，带/不带编号前缀 |
| L3 | `.section__subtitle` | 18px | 子模块标题 |
| L4 | `.data-block__title` | 14-15px | 数据块标签，muted 色 |

**numbering=true 时 L2 格式：**

```html
<h2 class="section__title">
  <span class="section__number">01</span>
  <span class="section__label">推荐方案</span>
</h2>
```

**CSS 差异：**

```css
/* numbering=true */
.section__number {
  font-weight: 700;
  color: var(--brand-primary);
  opacity: 0.4;
  font-size: 14px;
  letter-spacing: 0.05em;
  display: block;
  margin-bottom: 4px;
}
.section__label {
  font-size: inherit;
}
```

### 4.5 chart_insight_row

**根据 chart_layout 变化：**

| chart_layout | 布局方式 | 说明 |
|-------------|---------|------|
| insight_driven | 图表 + 洞察文字配对 | 每张图配一句关键洞察，先图后文或先文后图交替 |
| standalone | 图表分组展示 | 多图并排/堆叠，无绑定文字 |
| embedded | 图表嵌入表格/卡片 | 图表作为表格/卡片的一部分 |

**insight_driven 的具体格式（推荐）：**

```html
<div class="chart-block">
  <h3 class="chart-block__title">预算构成分析</h3>
  <div class="chart-block__body">
    <div class="chart-block__chart">
      <!-- SVG here -->
    </div>
    <div class="chart-block__insight">
      <div class="insight-card">
        <p class="insight-card__text">72% 资金投入光伏建设</p>
        <p class="insight-card__note">光伏为长期资产，建议分期投入使用</p>
      </div>
    </div>
  </div>
</div>
```

**规则（v1.5.1 强化）：**
- insight_driven 模式下：**每个 chart 必须有自己的独立 insight_card 配对**。不允许将多个 chart 放在 grid 中然后统一加一个 insight。
- 多个图表时交替布局（图→文 / 文→图 间隔排列，避免视觉单调）
- insight 文字不超过 2 句
- **配对显示的两张图表，SVG height 参数必须一致**（配对调用时传递相同 --height 值）
- standalone 模式跳过 insight 部分，直接输出图表
- **图表数量硬限制**（见下方 § 图表数量强制规则）

### 4.6 其他 sections

**comparison_table / scoring_matrix / detail_section / roadmap_section / risk_section / problem_analysis / gap_analysis / risk_matrix / solution_comparison / implementation_plan / current_state / objection_box / footer_section**

这些 section 保持现有渲染逻辑不变，只调整间距/字号以适配 section_density 和 visual_hierarchy。

---

## 五、密度等级（section_density）

| 参数 | compact | medium（默认） | spacious |
|------|---------|----------------|----------|
| section 间距 | 24px | 40px | 64px |
| 正文行高 | 1.5 | 1.7 | 1.9 |
| 单元格 padding | 8px | 12px | 16px |
| 页面 max-width | 960px | 1100px | 1280px |
| 每屏信息量 | 高 | 中 | 低 |

**选择规则：**
- 决策者/投屏 → spacious（少而精，易于阅读）
- 技术评审/打印 → compact（信息密度高）
- 通用/混合 → medium

---

## 六、视觉层级权重（visual_hierarchy）

决定不同页面元素的视觉权重比例：

| 元素 | strong | moderate | flat |
|------|--------|----------|------|
| hero | 2x（加大字号+装饰） | 1.5x | 1x（常规标题） |
| kpi strip | 品牌色+大数字 | 中性色+中数字 | 小标签 |
| recommendation box | 边框/底色高亮 | 标准卡片+边框 | 标准卡片 |
| section title | 编号+加粗+品牌色 | 加粗 | 常规加粗 |
| data blocks | 品牌色点缀 | 灰色点缀 | 无点缀 |
| 正文 | 最小权重 | 最小权重 | 最小权重 |

**选择规则：**
- 决策者受众 + 投屏场景 → strong（引导视线到关键结论）
- 技术受众 + 文档场景 → moderate
- 混合受众 → flat（不偏向任何元素）

---

## ⚠️ 图表数量强制规则

**总则：** 单页面最多 3 张图表。超出时必须降级。

**降级优先级链（从优到劣）：**

```
多张个体图（如 radar×4）
  → 合并为一张组合图（如 grouped bar、radar overlay）
  → 转为对比表格（不带图） → 纯文字（不带表）
```

**具体规则：**

| 原决策 | 超过上限？ | 降级方案 |
|--------|-----------|---------|
| radar × 4（4 方案 5 维度） | ✅ 超过 3 张 | 降级为 single grouped bar chart，或单张 radar overlay |
| bar × 3 + donut × 1 | ✅ 超过 3 张 | 去掉 bar 中最不重要的一张 |
| line × 2 + bar × 1 | ❌ 未超过 | 保留 |
| 任何 chart 类型，但 ≤3 张 | ❌ 未超过 | 保留 |

**2B+2 校验（Data Expression 阶段）：**
```
has_charts = 2B+2 决定的图表数量
→ has_charts > 3 → 自动降级 → 输出降级方案 → 记录到 output-tracker
```

---

## 七、视觉重心偏好（visual_priority）

visual_priority 决定 结论区（hero+kpi+recommendation）与 数据区（图表表格）之间的页面空间分配。

| 模式 | 结论区占比 | 数据区占比 | 适用场景 |
|------|-----------|-----------|---------|
| decision | ≥ 40% | ≤ 25% | 决策层投屏/汇报，快速要看结论 |
| data | ≤ 25% | ≥ 40% | 技术评审/数据审计，需要详查数据 |
| balanced | ~35% | ~35% | 通用混合受众 |

**选择规则：**
- 校领导/政府/财务 → decision（快速决策）
- CIO/技术团队汇报 → balanced（既有结论也要看数据）
- 技术评审/数据审计 → data（数据展示优先）

**对 sections 的具体影响：**

| section | decision | data |
|---------|----------|------|
| hero+recommendation | 全高渲染 | 常规高度 |
| kpi_strip | 大号数字+品牌色 | 中号数字 |
| chart sections | 单页 ≤ 2 张图，缩小渲染 | 可到 3 张，正常渲染 |
| scoring_matrix | 高亮推荐行 | 完整表格 |

---

## 八、决策规则

### 7.1 从上游输入推导 layout_strategy

```yaml
输入:
  page_type:   comparison-matrix / industry-report / guide
  audience:    校领导 / 财务 / 后勤 / CIO / 教育局
  scenario:    投屏 / 打印 / 手机 / 邮件
  data_volume: 丰富 / 中等 / 有限
  has_scoring: true / false         # 2B+3 是否生成了评分
  has_roadmap: true / false         # 是否有实施路线
  has_charts:  0-3                  # 2B+2 决定的图表数量
```

**规则表：**

| 组合 | page_pattern | hero_type | kpi_strip | hero_weight | visual_priority |
|------|-------------|-----------|-----------|-------------|----------------|
| comparison-matrix + 校领导 | executive_summary | recommendation | enabled | heavy | decision |
| comparison-matrix + CIO | comparison_first | neutral | enabled | medium | balanced |
| industry-report | executive_summary | neutral | 取决于数据 | light | balanced |
| guide + 有 roadmap | roadmap_planning | data | enabled | medium | balanced |
| guide + 无 roadmap | problem_solving | problem | disabled | heavy | decision |
| comparison-matrix + 财务 | executive_summary | data | enabled | heavy | decision |
| comparison-matrix + 教育局 | executive_summary | recommendation | enabled | heavy | decision |

**通用默认值：**

```yaml
layout_strategy:
  page_pattern: executive_summary    # 默认走咨询报告型
  hero_type: recommendation          # 默认推荐结论为首
  hero_weight: medium                # 中等视觉冲击
  kpi_strip:
    enabled: false                   # 只在有核心指标时开启
    metrics: []
  title_system:
    levels: 3
    numbering: true
  chart_layout: insight_driven       # 默认图表+洞察配对
  section_density: medium
  visual_hierarchy: strong           # 默认强化层级
  visual_priority: balanced          # 默认平衡
```

### 7.2 kpi_strip 启用条件

全部满足才启用：

1. 有 3-4 个核心指标（从 metric_selection 继承）
2. 受众是决策者（校领导/政府/财务，非技术执行者）
3. 场景是投屏或邮件（非打印）
4. page_pattern 不是 problem_solving

### 7.3 特殊情况——无数据时

当数据不足（2A 确认后 data_volume=有限或不存在），Layout Decision 强制执行：

```yaml
kpi_strip:
  enabled: false
hero_type: neutral
hero_weight: light
section_density: medium
visual_hierarchy: moderate
```

避免「大数字看起来很唬人但数据不靠谱」的情况。

---

## 九、与现有流程的关系

| 现有步骤 | 对 Layout Decision 的输出 | 备注 |
|---------|--------------------------|------|
| 2A 数据调研 | → data_volume 决定 kpi_strip 启用 | 数据不足强制禁用 |
| 2B 受众确认 | → audience 决定 page_pattern + hero_type | 核心输入 |
| 2B+1 IA | → IA 决定了 section 内部的内容结构 | 布局在 IA 之后做编排 |
| 2B+2 Data Expression | → chart_layout + has_charts | 图表布局策略 |
| 2B+3 Recommendation | → has_scoring 决定 scoring_matrix 是否加入 skeleton | |
| 2C Color | → 配色已知，但 layout 不依赖配色 | 布局和配色独立决策 |

---

## 十、典型输出示例

### 校领导投屏场景（executive_summary + decision + strong + spacious）

```yaml
layout_strategy:
  page_pattern: executive_summary
  hero_type: recommendation          # ← 推荐结论嵌入 Hero，不展示重复数字
  hero_weight: heavy
  kpi_strip:
    enabled: true
    metrics:
      - {value: 540, unit: 万, label: 年节省}
      - {value: 5.4, unit: 年, label: 回收期}
      - {value: 2900, unit: 万, label: 总投资}
  title_system:
    levels: 3
    numbering: true
  chart_layout: insight_driven
  section_density: spacious
  visual_hierarchy: strong
  visual_priority: decision           # ← 结论区优先
```

### CIO 技术评审场景（comparison_first + balanced + moderate + compact）

```yaml
layout_strategy:
  page_pattern: comparison_first
  hero_type: neutral
  hero_weight: light
  kpi_strip:
    enabled: false
  title_system:
    levels: 3
    numbering: false
  chart_layout: standalone
  section_density: compact
  visual_hierarchy: moderate
  visual_priority: balanced           # ← 结论和数据平衡
