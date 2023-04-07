import requests

url = "https://movie.douban.com/j/chart/top_list"
herders = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

for i in range(0, 20):
    num = 20 * i

    # 重新封装参数
    params = {
        "type": 24,
        "interval_id": "100:90",
        "action": "",
        "start": num,
        "limit": 20
    }

    resp = requests.get(url, params=params, headers=herders)
    print(resp.json())
    print(resp.text)
    # with open("./file.excel",mode="a") as f:
    #     for i in resp.json():
    #         f.write(i)

    resp.close()
