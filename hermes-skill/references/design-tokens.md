# Design Tokens（受众场景 → 方向选择）

**只回答「选哪个方向」。** 具体色值/字号/行高/间距在 color-harmony / font-ordering / audience-layout-tokens 中定义。

---

## Conservative（保守型）

|  |  |
|--|--|
| **适用** | 银行 / 金融 / 政府 / 教育局 / 国企 |
| **目标** | 信任感 > 个性感 |
| **参考** | IBM Carbon · Microsoft Fluent · Oracle |
| **策略** | compact · high_contrast · low_radius |
| **避免** | 玻璃拟态 · 大面积渐变 · 霓虹色 |

---

## Enterprise（企业型）

|  |  |
|--|--|
| **适用** | 高校 / 大型企业 / 信息中心 / IT 部门 |
| **目标** | 专业 + 易读 |
| **参考** | 飞书 · Notion · Atlassian · Airtable |
| **策略** | medium · balanced_contrast · mid_radius |
| **避免** | 极简主义 · 纯黑文字 · 突兀品牌色 |

---

## Modern SaaS（现代产品型）

|  |  |
|--|--|
| **适用** | AI 产品 / 软件厂商 / 技术公司 |
| **目标** | 高级感 > 保守感 |
| **参考** | Stripe · Linear · Vercel |
| **策略** | airy · moderate_contrast · high_radius |
| **避免** | 厚重阴影 · 复杂表格 · 信息过载 |

---

## Reading（阅读型）

|  |  |
|--|--|
| **适用** | 行业报告 / 白皮书 / 研究分析 |
| **目标** | 长时间阅读不累 |
| **参考** | Medium · Mintlify · Notion Docs |
| **策略** | wide_line_height · narrow_width · minimal_accent |
| **避免** | 高密度表格 · 大幅插图 · 多色块 |

---

## Comparison（决策型）

|  |  |
|--|--|
| **适用** | 厂商对比 / 产品 PK / 采购建议 |
| **目标** | 突出差异，帮助决策 |
| **参考** | Gartner · G2 · Stripe Pricing |
| **策略** | high_contrast_rows · sticky_first_col · pill_badge |
| **避免** | 模糊等级 · 隐藏劣势 · 无推荐列 |

---

## 使用方式

```
受众：温州教育局
→ 匹配 Conservative
→ 策略：compact · high_contrast · low_radius
→ 参考 Carbon / Fluent 找具体色值（查 color-harmony.md）
→ 理论推导的深蓝 #1e40af，对比 Carbon #0f62fe → 会不会太重？
→ 浅化后写 CSS → WCAG 验算
```

**先定场景 → 再定策略 → 最后查色值。** 这个文件只定方向，色值由 color-harmony.md 负责。
