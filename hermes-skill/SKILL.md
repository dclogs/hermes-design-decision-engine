---
name: client-proposal-html
description: "Design-decision engine for enterprise HTML pages. 10-discipline reasoning framework + 3 global conclusion quality checks (Stakeholder / Novelty / Actionability). Each output: audience → data → multi-perspective research → theory → real-product calibration → quality gate → pyramid argument structure. Output: comparison matrices, analysis reports, transformation guides. Zero-dependency, Feishu delivery."
version: 1.2.0
author: Hermes Agent
license: MIT
tags: [design, proposal, html, comparison, audience-adaptation, enterprise, feishu]
---

# Client Proposal HTML Generator

**设计决策引擎，非模板库。** 每次从零推理：受众 → 数据 → 理论推导 → 真实产品校准配色。只输出 3 种类型（对比表/分析报告/指南），学科框架保证首版质量，不走"套模板"路线。

零外部依赖（仅 Google Fonts CDN）。飞书文件上传交付。

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

**Step 1 — 页面类型**
```
需求 → 匹配 PAGE_TYPE:
  comparison-matrix  → 方案对比（扁平 IA，详见 references/information-architecture.md）
  industry-report    → 行业分析（层级 IA，详见 references/information-architecture.md）
  guide              → 转型指南（步骤 IA，详见 references/information-architecture.md）
  architecture       → 委托 architecture-diagram skill 生成
```

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

### ✅ 2D 生成前确认（Preflight Check）

飞机起飞前不做重复检查——确认上游就绪即可。

```
□ Color Ready — 色值已推导+校准 → yes/no
□ Layout Ready — IA 结构 + popular-web-designs 已参考 → yes/no
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

**输出格式** — 按页面类型选择：

**comparison-matrix（Recommendation First）**
```
标题 + 一句话定位
  → 推荐结论（金字塔顶）
    → 关键差异（前 3 行对比，标记核心差异点）
      → 详细对比（≤10 行，sticky 首列，推荐列高亮）
        → 异议框（边界条件）
          → footer
```

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

### 2E+ 最终验证（7 项总闸门）

```
□ Data     — 数据已核实，来源可追溯
□ Structure — IA 结构确认 + 金字塔论证结构符合 MECE
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
```

**学科间关系**：体验设计负责功能正确（绿色=推荐），符号学负责文化审核（确认绿色在受众文化中无负面含义）。默认体验设计优先，仅当存在明确文化冲突时符号学覆盖。流程：UX → 生成 → 符号学审核。

---

## 四、自检清单

```
□ 数据已核实（含风险分级 + 审计表）
□ 是否走 Fallback？是 → fallback-mode.md 已加载，异议框已标注原因
□ IA 结构已确认（扁平/层级/步骤）+ 扫描路径 3 秒测试通过
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

---

## 六、预加载清单（按页面类型 + 标签）

标签含义：**ESSENTIAL** = 每次必读 · **OPTIONAL** = 需要时再读 · **RARE** = 很少用到

**页面无关（ESSENTIAL — 每次必读）**
①design-tokens（方向策略） ②color-harmony（色值推导） ③font-ordering（字体） ④audience-layout-tokens（受众参数）

**页面无关（OPTIONAL — 需要时加载）**
⑤open-source-design-resources ⑥ux-heuristics ⑦affordance-checklist ⑧decision-biases ⑨traps-and-recipes ⑩narrative-design-examples（叙事设计参考） ⑪design-details（数学美感+微调表+数据可视化） ⑫information-architecture（IA 结构参考） ⑬pyramid-principle（咨询方法论） ⑭language-and-labeling（符号学+语言学）

**页面无关（RARE — 极少用到）**
⑮cognitive-load-and-flow

**外部 skill（ESSENTIAL — 每次必读）**
⑯popular-web-designs（布局结构灵感 + 颜色兜底校准）

---

**比较表（额外加载）**
affordance-checklist · pre-note-template · design-details · pyramid-principle（论证结构自检）

**分析报告（额外加载）**
layout-patterns · templates/（HTML 骨架）· data-verification-workflow · information-architecture（层级 IA）· pyramid-principle（金字塔论证）

**所有参考文件：** `references/` 目录下 23 个文件 + `CHANGELOG.md` + Hermes skill `popular-web-designs`。
