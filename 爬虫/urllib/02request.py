from urllib import request, response

url = 'http://www.pyqt5.cn'

resp = request.urlopen(url)


print(resp.status)  # 返回状态码

print(resp.reason)  # 返回状态信息

print(resp.msg)  # 请求成功返回OK

print(resp.version)  # 返回http版本信息

# .read()方法返回字节码文件 且只能调用一次  第二次使用不返回数据
print(resp.read().decode('utf8'))

# .getheaders()方法 返回请求头信息
print(resp.getheaders())  # 列表类型

# .getheader(key)方法 返回指定键的响应头信息
print(resp.getheader('Date'))  # 此处检索Data

# .getcode()方法 返回http状态码
print(resp.getcode())

# .geturl()方法 返回检索的URl
print(resp.geturl())

# .readinto()方法 返回网页头信息
print(resp.readinto())

# .fileno()方法 返回文件的检索信息
print(resp.fileno())
