import requests
from concurrent.futures import ThreadPoolExecutor

URL = 'http://www.xinfadi.com.cn/getPriceData.html'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
    'Referer':'http://www.xinfadi.com.cn/priceDetail.html'

}

params = {
    'limit':"20",
    'current':'',
    'pubDateStartTime':"",
    'pubDateEndTime':"",
    'prodPcatid':"",
    'prodCatid':"",
    'prodName':""
}

# 对发送的POST请求的current参数进行修改，封装参数创建全局变量进行通信

def params_resp(ls,page_num):
    params['current'] = str(page_num)
    resp = requests.post(url = URL , headers = headers , params=params)
    ls.append(resp.json())
    print(resp.text)


if __name__ == "__main__":
    ls = []  # 定义全局变量列表
    # 创建线程池
    with ThreadPoolExecutor(500) as t:
        for num in range(18663):
            t.submit(params_resp,page_num = num,ls = ls)
    print(ls)

