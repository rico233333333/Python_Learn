import requests
from threading import Thread

url1 = 'https://xiaohua.zol.com.cn/new/1.html'

url = 'https://xiaohua.zol.com.cn/?pid=307&type=3071&sign=&desturl=&linkid=lauvhcxuva0&apitype=0'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
}

resp = requests.get(url1,headers=headers)
print(resp.text)