# 实操陷阱与完整代码

## 技术陷阱

### 国内网站被代理墙
```bash
curl -s --noproxy '*' --max-time 10 -L "https://www.hzsun.com"
```

### Bash 内嵌 Python regex 报错
```bash
# 写独立文件执行，不要 heredoc
python3 /tmp/parse.py
```

### Env 变量取不到
```bash
# 必须在一个 shell 上下文
source ~/.hermes/.env && python3 -c "import os; print(os.environ.get('FEISHU_APP_ID'))"
```

## 完整飞书发送代码

```bash
source ~/.hermes/.env && python3 << 'PYEOF'
import os, json, requests
chat_id = 'oc_eb156e88367178d424d9aee43c58e135'
token = requests.post('https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal',
    json={'app_id': os.environ['FEISHU_APP_ID'], 'app_secret': os.environ['FEISHU_APP_SECRET']}
).json()['tenant_access_token']
path = 'output.html'
with open(path, 'rb') as f:
    up = requests.post('https://open.feishu.cn/open-apis/im/v1/files',
        headers={'Authorization': f'Bearer {token}'},
        files={'file': ('对比.html', f, 'text/html')},
        data={'file_name': '对比.html', 'file_type': 'stream'}).json()
file_key = up['data']['file_key']
requests.post(f'https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=chat_id',
    headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'},
    json={'receive_id': chat_id, 'msg_type': 'file',
          'content': json.dumps({'file_key': file_key})})
print('OK')
PYEOF
```

## 设计陷阱

- **颜色不够差异化**：不只换色值，布局/字号/间距/圆角/附加模块全随受众变
- **银行风格冲突**：银行要咨询报告感（白底蓝字/圆角0px/密度高），不要科技官网感
- **Feishu 发图不对**：必须用 im/v1/files API，MEDIA: 标签不支持
