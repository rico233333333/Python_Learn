import requests

url = "https://www.sogou.com/web?query=周杰伦"

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)  # 返回值返回http协议的响应状态代码

print(resp.text)
