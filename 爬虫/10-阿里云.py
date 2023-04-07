import requests

URL = "https://developer.aliyun.com/developer/api/evaluation/getNewEvaluationList"

params = {
    "askGroupId": 1032,
    "albumId": 37,
    "pageNum": 2,
    "pageSize": 20
}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

resp = requests.get(url=URL,params=params,headers=headers,verify=False)

print(resp.json())
