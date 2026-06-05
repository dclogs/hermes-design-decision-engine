# 发展路线图（Development Roadmap）

本文档记录用户在迭代过程中提出的架构级方向，供后续开发决策参考。不是当前运行时的必读内容。

---

## 当前能力边界（v1.x — Presentation Layer）

**已完成：**
- 页面结构（IA / 导航层级）
- 配色系统（色彩推导 + 案例校准 + WCAG）
- 卡片/表格/图表（bar/line/donut/radar SVG）
- 数据表达选择（2B+2 Data Expression Decision）
- 评分引擎（2B+3 Recommendation Scoring）
- **布局策略决策（2B+4 Layout Decision）** — v1.5.0 新增

用户自评当前输出品质：
| 维度 | 分数 |
|------|------|
| 信息结构 | 70-80 |
| 决策逻辑 | 80-90 |
| 数据表达 | 75-85 |
| 视觉层级 | 60-70（2B+4 实施后待实机验证） |

---

## v2.x — Proposal Engine（方案推理层）

### 目标
从「页面生成器」升级为「方案引擎」——识别方案类型、适配受众角色、追溯数据来源。

### 1. Proposal Archetype Detection（方案原型检测）

**位置：** Step 1（需求分析）之后、IA 之前。

**理由：** Archetype 决定了 IA 的顶层结构。投资决策的 IA 是 ROI → 风险 → 推荐；选型的 IA 是维度 → 评分 → 比较；路线图的 IA 是现状 → 分期 → 里程碑。放在 IA 之后再检测就晚了。

**已识别的原型：**
| Archetype | 典型场景 | 核心问题 | 结构特征 |
|-----------|---------|---------|---------|
| Investment Decision | 新能源改造 / 基建 / 采购 | 投多少 / 多久回本 / 风险如何 | ROI → 风险 → 推荐 |
| Vendor Selection | Oracle vs 达梦 / 华为云 vs 阿里云 | 选谁 / 为什么 | 维度 → 评分 → 对比 |
| Roadmap Planning | 数字化转型 / 智慧校园 / 数据治理 | 怎么分阶段推进 | 现状 → 分期 → 里程碑 |
| Problem Solving | 故障率高 / 性能差 / 投诉多 | 根因是什么 / 怎么解决 | 问题 → 根因 → 方案 |
| Compliance / Governance | 等保整改 / 安全建设 / 内控 | 差距在哪 / 怎么整改 | 差距 → 风险 → 路线 |

**实现思路：**
```yaml
input:
  建设智慧校园
detected_archetype:
  roadmap_planning
```

Archetype 决定：
- IA 结构（扁平/层级/步骤）
- metric_selection 的默认维度
- 推荐结论的形式（ROI / 评分 / 路线 / 根因）
- 2E 的 skeleton 选择优先级

### 2. Audience Model（受众适配模型）

**核心洞察（用户提供）：** 同一方案给不同人看，完全不是同一份报告。

| 受众 | 关注点 | 默认选择 |
|------|--------|---------|
| 校长 | 预算 / 回本 / 风险 | page_pattern=executive_summary, hero_type=recommendation |
| 财务 | 现金流 / 折旧 / 融资 | page_pattern=executive_summary, hero_type=data |
| 后勤 | 施工 / 运维 / 兼容性 | page_pattern=roadmap_planning |
| CIO | 架构 / 集成 / 可扩展 | page_pattern=comparison_first |
| 教育局 | 双碳 / 示范校 / 社会效益 | page_pattern=executive_summary, hero_type=recommendation |

**初步方案（用户建议）：**
```yaml
audience:
  principal
  finance
  operations
  government
  technical
```

然后 `metric_weight` 和 `layout_strategy` 随受众变化。

**实施前提：** 数据模型（data 层）需要与 audience 解耦。相同的数据集，不同的 audience 选择不同的指标子集和叙事顺序。

### 3. Evidence Layer（证据追溯层）

**痛点：** 当前报告是 结论 → 理由，未来企业客户会问"数据从哪里来"。

**目标：** Traceable Recommendation（可追溯推荐）。

```text
回收期 5.4年
  ↓ 点击展开
  计算过程：...
  依据：某高校案例 | 行业报告 | 招标数据
```

**两种实现路径（用户提出的权衡）：**
1. **强约束路径：** 要求用户 prompt 附带数据来源 → 降低使用门槛，但可信度高
2. **自适应路径：** 模型自动标注置信度和数据估计依据 → 降低门槛，但可信度打折

**当前草稿决策：** 两种模式并存。先自适应，等用户反馈明确数据可信度是痛点后再加强约束。

---

## v3.x — Decision Narrative Engine（决策叙事引擎）

### 目标
从「有数据的报告」升级为「有说服力的叙事」——符合行业类型、受众角色、决策逻辑。

### 1. Narrative Pattern Library（叙事模式库）

用户抽象出的通用叙事链：

```yaml
story_pattern:
  urgency     # 为什么要现在做
  opportunity # 有什么机会
  comparison  # 有哪些选择
  recommendation # 推荐什么
  execution   # 怎么执行
```

无论是数据库迁移、新能源改造、ERP 建设，都遵循同一叙事骨架。

### 2. Recommendation Engine 深化

当前（v1.5.0）已有 2B+3 Scoring Engine（加权评分）。未来扩展：
- 方案优劣势自动摘要（从评分矩阵反推）
- "如果不选推荐方案"的假设分析（what-if）
- 置信度区间（不假装数字精确到小数点后两位）

### 3. Traceable Recommendation 产品化

- 证据链可折叠/可展开（accordion pattern）
- 数据来源超链接化
- 置信度视觉化（✅/⚠️/❌ 颜色编码持续优化）

---

## 总体路线

```
v1.x — HTML 生成器（当前）
  └─ 页面结构 ✓
  └─ 配色系统 ✓
  └─ 图表系统 ✓
  └─ 数据表达 ✓
  └─ 评分引擎 ✓
  └─ Layout Intelligence ✓（v1.5.0）

v2.x — Proposal Engine（下一步）
  └─ Archetype Detection（P0）
  └─ Audience Model（P1）
  └─ Evidence Layer（P2，验证期需求后决定）

v3.x — Decision Narrative Engine（长期）
  └─ Narrative Pattern Library
  └─ What-if Analysis
  └─ Traceable Recommendation 产品化
```

---

## 每次迭代的验证方式

每次架构变更后：
1. 生成一份实际报告（使用 v1.3.0 验证过的数据源）
2. 发飞书 HTML → 用户截图看效果
3. 记录问题到 output-tracker
4. 累计 20 条做根因分析
5. 下一轮迭代由 output-tracker 驱动，非预设方向

---

*本文件记录用户（2026-06-05 对话）提出的架构方向，用于后续迭代时保持上下文对齐。*
