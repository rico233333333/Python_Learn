from urllib import request


# urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
#             *, cafile=None, capath=None, cadefault=False, context=None)
'''
url 代表 请求或者发送的链接   出现中文需要转码
data 若是需要这个 则请求变成了post  bytes类型
timeout  超时设置
cafile 文件认证 CA证书
capath 路径验证 证书路径
context https认证时需要
'''
url = 'http://www.pyqt5.cn/'

resp = request.urlopen(url)
print(resp)  # 他是一个httpresponce 对象

print(resp.read().decode('UTF-8'))  # 不使用decode转码就是一个字节码文件 需要转码
