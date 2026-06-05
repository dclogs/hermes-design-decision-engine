# 字体排序规则

## 拉丁 vs 中文的先后顺序

`font-family` 的解析顺序是从左到右，先匹配到的字体先渲染。
中文字体（Noto Sans SC / PingFang SC）优先时，整个页面视觉更暖、更圆润。
Latin 字体（Inter / Source Sans 3）优先时，页面更冷、更精确。

## 受众决定排序

| 受众 | 字体排序 |
|------|---------|
| 学校/教育 | `'Noto Sans SC', 'Inter', 'PingFang SC', 'Microsoft YaHei', sans-serif` |
| 银行/金融 | `'Inter', 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', sans-serif` |
| 教育局/政府 | `'Inter', 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', sans-serif` |
| 科技/SaaS | `'Inter', 'Noto Sans SC', sans-serif` |

## 例外

如果客户品牌规范指定了特定字体（如 IBM Plex Sans），优先遵循客户规范。
