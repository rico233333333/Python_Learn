# 登录得到cookie
# 带着cookie去请求到书架的url  也就是书架上的内容】

# 必须把上面的两部连起来操作
# 我们可以使用  session进行请求 session可以理解成一连串的请求，在这个过程中的cookie不会丢失

import requests

url = 'https://www.zhihu.com/api/v3/account/api/login/qrcode'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

params = {  # 此处放置密码等
    'expires_at': 1662564284,
    'token': "MmNlNWYxYmQtMjMy"
}

data = {  # 此处直接封装cookie
    'cookie': '_zap=1cdc3ad2-c883-4198-8379-07624bbd2dcb; d_c0=ADDX8gv9gBWPTptR7yL6GuxCF6BUUd1JET4=|1662213522; _xsrf=bbfc9a75-3635-471a-948b-0fda31b30f09; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1662213522,1662554761; SESSIONID=SbzBmZjOzjO36pZArScvH0GNUdScEeS0gfGBrcqoElO; __snaker__id=fcgaIYRh0Z0M6wNU; JOID=WlEcA0z5mzkndC34APFl70C_N3AUq_lKYhZ2kkaM8HYdRVKjQXEAL0x6LPEOa_EJKm1NdthcbbOoGXwShPYyT84=; osd=UVASB0Pymjcjeyb5DvVq5EGxM38fqvdObR13nEKD-3cTQV2oQH8EIEd7IvUBYPAHLmJGd9ZYYripF3gdj_c8S8E=; gdxidpyhxdE=%2BNH6ccQdpt4n5oU9ZUcgnoh3QpWoRw%5CZPNZ0yGI6LQQb9mfrMP%2BLXclnNfE01Iukx5u6%2F5XSejaBH5VLwaAXyv7ifr4nxau4KiUcxATuSh%5CfPupSguS6uctOs3OgNxRI4ogBemk%2FQbA51%2F9q9vGcesGfPW05lZbsx0TWBec%5CkNjtVcSz%3A1662555662050; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=Vljy4pQToRkubuIQtHXcDj%2F%2BSg8HMUmTRkDZIYNb8SUd7o6etg3TvgYy3MSvvGykf%2FdllKu2%2FQs0YZzXJSZJYPO4mSUyk0IWfPV9XLEjf44HmJhEy7Ir%2BZj%2BIcTCtQH5QVQ%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee96b440a1b3ab89cf468cbc8eb6c54a868a9e87c160bc97e597ae4afbeeb7baf72af0fea7c3b92a96b4a69ab77c938ca1b3ea7fa2ab87b2f7449cbd8c8bae2191b9f8a9d05faf8c9e8cc7528b878283bb5997bcf990b56fb8b9fdb5f56d9ba7fdaed27eb699b78ce525a8b4a4acf83aed8fbdd1dc52ba8886b4d9429b9081d5f05997a7a5d1cc5da6909adadb4887b6aad5b744af96a8a6fc3d8baee5bbe9218bbd9ca4f75b8ceb9fb7d437e2a3; YD00517437729195%3AWM_TID=6XgFYdqfOQZAVFBAUQeQC1M%2Bv%2FA8iyIp; captcha_session_v2=2|1:0|10:1662554786|18:captcha_session_v2|88:cVJ3QlFXdGt3Z09KS2owbEZzUEFKN29ocnZMRHErYWtUL1RHYnZLZU9ZZFdGVGZlbnFuL2RyUzdpeHhJblVHZQ==|714f884b6b7453dd258d817849bd7a61c8bd76f9f92aa3488f150faafb71acd5; captcha_ticket_v2=2|1:0|10:1662554819|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfZnptLWFpUlNjaTZ1S29ZdGhsdU96S0ZrQUlkYmxCdTVwLXp2cEJYcV9XZk5sX0lzTGxUWGl6SHhHdlEtQlNDcGVQU0FRSHRrUlV3VjRoQUZIOE8ua2k0SFF0SUR3T3BrSEcua3lPUkRpa0RGTWJGaWRBd1RoU3BITXZmVFJPaWtwTG5VMHJJbUNiSGNabVlDZEtUcWY4cVVneGlRdlZHOWREdjJiMGhIQTZNNS1qNXpudGo2dWc1eDRhbEw1cUw2cWFqcEhGbGFHUGhmaVVyYm81Vi50eTBZRktEMXdDV3h6ZDZiSW5mZU9DNVNTSnRLZmFILjY4djBVUC5WNndvSXpBMVhUQTBUVWNiUm1WYXpBOHE4ZjFfcW9UR1NXN0xkTFlvWEFaOVRfOVppbFdQLXRjZWdVcWdhaDBtdkswTW9NWkdFa3hqbWRvY1B0TGFWZXBlcGd6RUlDb1FOMk9NWXdDSklSR3VUTHFKWXMycTc5eE8uV1B4WndSSlU2azg2TjhSN0VKanNmQXNpdG1Za2VYR2swMkJ6TEdlczh5TGN0ZmdsSEVPZnJuSUxpMHlZdjh5TlFxTWY2cW9WYW1GNW1qbDEwak1qUWJvVGNtd20uZlNTX0pSc1pRZGhsMVhTelFKTkFLc0kwaV9LUEVSOW1IbDZsQ21PSHhYMyJ9|8e55c1d823ac44ab2cf9e7d7ca444b870b364a4b8e9b403bb2276731007f48de; z_c0=2|1:0|10:1662554851|4:z_c0|92:Mi4xelRUT0hBQUFBQUFBTU5meUNfMkFGU1lBQUFCZ0FsVk40LUFGWkFCdGxTd25md01lWUhYMUltXzBNZngzZmVDT1R3|7fcfffddb46f3a7ac092a68d42a6593b96e3944fbcf4555a7739057e9459be75; q_c1=ec943ebbe6b34b64a6c7c581844e5349|1662554852000|1662554852000; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1662554853; tst=r; NOT_UNREGISTER_WAITING=1; KLBRSID=031b5396d5ab406499e2ac6fe1bb1a43|1662555246|1662554760'
}

# session 代表会话
session = requests.session()

resp = session.get(url=url, data=data, headers=headers)

resp_data_url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend'

params111 = {
    'session_token': 'ea536859f626c09b30a390daddbce56c',
    'desktop': 'true',
    'page_number': 2,
    'limit': 6,
    'action': 'down',
    'after_id': 5,
    'ad_interval': -10
}

resp_data = session.get(url=resp_data_url, params=params111)
print(resp_data.text)

print(resp.url)
