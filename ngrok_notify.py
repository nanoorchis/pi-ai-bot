#!/usr/bin/env python3
import os
import json
import urllib.request

env_file="/home/j/Documents/pi-ai-bot/feishu_bot.env"
config={}#字典新建用花括号

print(f"------------------------------------------------------------")#建个分隔符，表示开始了。
print(f"配置文件存在吗？ {os.path.exists(env_file)}")#print中f配合花括号用，花括号中直接放变量。

with open(env_file,'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()#把key和value都去掉空格后放到config字典里。
            print(f"{key.strip()}={value.strip()}")

#验证按名字取值
app_id=config.get("FEISHU_APP_ID")
app_secret=config.get("FEISHU_APP_SECRET")
print(f"app_id={app_id}")
print(f"app_secret={app_secret}")

#构造飞书的请求体
playload={"app_id":app_id,"app_secret":app_secret}
json_str=json.dumps(playload)
body=json_str.encode("utf-8")

#构造请求
url="https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
headers={"Content-Type":"application/json"}
req=urllib.request.Request(url=url,data=body,headers=headers)

#发送请求并获取响应
resp = urllib.request.urlopen(req,timeout=30)
resp_bytes = resp.read()

#解析响应
result = json.loads(resp_bytes.decode("utf-8"))
print(f"返回码：{result.get('code')}")
print("tenant_access_token:",result.get("tenant_access_token"))

