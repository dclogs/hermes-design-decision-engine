# Fallback Mode（保底设计）

## 触发条件

以下任一成立即触发。**核心原则：判断不出来就别硬判断。**

| 条件 | 阈值 | 说明 |
|------|------|------|
| 数据不足 | 审计表 ✅ 项 < 60% | 撑不起可信结论 |
| 受众模糊 | confidence < 60% | 无法确定决策链/场景 |
| 行业陌生 | confidence < 60% | 找不到同领域案例参考 |
| 案例缺失 | popular-web-designs 无匹配 | 无产品可校准 |
| 色彩推导卡住 | Step 1~4 任一无法完成 | 理论/工具/校准断裂 |

## Fallback 默认值

```yaml
confidence_threshold: 60%     # 低于此值不往下判断，直接保底
layout: executive-report      # 最安全密度，投屏/打印/手机均适用
color: carbon-blue            # IBM Carbon 蓝体系
typography:
  chinese: Noto Sans SC
  latin: IBM Plex Sans
  body_size: 16px
spacing: medium               # padding 24px, gap 16px
border_radius: 0px            # 企业报告风
header_style: white_bg_blue_underline
```

## 输出格式

和正常流程一致。但异议框加一条：

```
⚠ 本方案基于 Fallback Mode 生成（原因：[原因]），
建议补充输入信息后重新生成。
```

## 原则

- Fallback 不是「偷懒不走流程」，是「信息不够时不让 agent 瞎猜」
- Fallback 出 80 分作品，不是 40 分
- 异议框明示原因，不藏不掩
- 后续补充信息后，可基于 Fallback 输出局部微调，不必全部重来
