from base64 import encode
import requests

url = 'https://pic2.zhimg.com/v2-9d7ab8870f36c0444123d669ad64cd1b_r.jpg?source=1940ef5c'

resp = requests.get(url)

with open('zhou.jpg', mode='wb') as w:
    w.write(resp.content)  # 处理数据下载
