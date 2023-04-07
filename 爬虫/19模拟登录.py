import requests

url = 'https://user.17k.com/ck/author/shelf'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

params = {
    'page': 1,
    'appKey': 2406394919
}

data = {
    'Cookie': 'GUID=37928428-2ec0-419a-928c-edf1698e101d; c_channel=0; c_csc=web; Hm_lvt_9793f42b498361373512340937deb2a0=1662210054,1662516769,1662556395; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F13%252F93%252F00%252F98010093.jpg-88x88%253Fv%253D1662209441000%26id%3D98010093%26nickname%3D%25E6%25B9%2598%25E6%25B1%259F%25E6%2598%2582%25E8%25B4%25B5%25E7%259A%2584%25E9%25B3%2597%25E9%25B1%25BC%26e%3D1678108636%26s%3D84de49cab9362e72; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2298010093%22%2C%22%24device_id%22%3A%221830370991726-03b48469d56098-c4e7526-3686400-18303709918f53%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2237928428-2ec0-419a-928c-edf1698e101d%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1662557732'
}

session = requests.session()

resp = session.get(url, data=data, headers=headers, params=params)

resp.encoding = 'utf-8'

print(resp.text)

# url = 'https://user.17k.com/ck/author/shelf'

# headers = {
#     'Cookie': 'GUID=37928428-2ec0-419a-928c-edf1698e101d; c_channel=0; c_csc=web; Hm_lvt_9793f42b498361373512340937deb2a0=1662210054,1662516769,1662556395; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F13%252F93%252F00%252F98010093.jpg-88x88%253Fv%253D1662209441000%26id%3D98010093%26nickname%3D%25E6%25B9%2598%25E6%25B1%259F%25E6%2598%2582%25E8%25B4%25B5%25E7%259A%2584%25E9%25B3%2597%25E9%25B1%25BC%26e%3D1678108636%26s%3D84de49cab9362e72; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2298010093%22%2C%22%24device_id%22%3A%221830370991726-03b48469d56098-c4e7526-3686400-18303709918f53%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2237928428-2ec0-419a-928c-edf1698e101d%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1662564756',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }

# resp = requests.get(url=url, headers=headers)

# print(resp.text)

# print(resp.headers)

# print(resp.cookies)

# print(resp.status_code)
