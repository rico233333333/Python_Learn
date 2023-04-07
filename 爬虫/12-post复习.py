import requests

# URL = "http://www.xinfadi.com.cn/getPriceData.html"
#
# data = {
#     "limit": 20,
#     "current": 2,
#     "pubDateStartTime": "",
#     "pubDateEndTime": "",
#     "prodPcatid": "",
#     "prodCatid": "",
#     "prodName": ""
# }
#
# resp = requests.post(URL,data=data)
#
# print(resp.json())

url = 'https://fanyi.baidu.com/v2transapi'

headers = {

}

data = {
    'from': 'zh',
'to': 'en',
'query': '我爱你',
'transtype': 'realtime',
'simple_means_flag': 3,
'sign': 47194.285547,
'token': '01e5dc4288d545caedf614f562d6d75e',
'domain': 'common'
}

resp = requests.post(url,data = data)

print(resp.json())
