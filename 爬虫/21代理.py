import requests

# 代理原理 通过第三方机器发送请求

# 代理
proxies = {  # 此处传参
    'https':'http://120.194.55.139:6969'
}
url = 'http://www.sogou.com/web?query=%E5%91%A8&_asf=www.sogou.com&_ast=&w=01019900&p=40040100&ie=utf8&from=index-nologin&s_from=index&sut=1456&sst0=1663117613142&lkt=0%2C0%2C0&sugsuv=1663117605896432&sugtime=1663117613142'
resp = requests.get(url = url,proxies = proxies)
resp.encoding = 'utf8'
print(resp.text)
