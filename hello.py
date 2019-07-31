import requests
import json

# api路径
url = "http://127.0.0.1:5000/users"

parms = {
    'user': 'abc',  # 发送给服务器的内容
    'pwd': '456'
}

headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}

res = requests.post(url, data=parms, headers=headers)  # 发送请求

text = res.text
print(json.loads(text))

