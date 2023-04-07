import requests

url = "https://fanyi.baidu.com/sug"

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
# }

user_input = "dog"

data = {"kw": user_input}  # post请求里边发送的数据必须放置在字典中

resp = requests.post(url,data=data)

print(resp.json())
