from urllib import request


'''
Handler处理器
常见headler 处理器
# 以下都是重写对象
HTTPHeadler()  # 处理普通http请求
HTTPSHeadler()  # 处理https请求
ProxyHeadler()  # 处理请求时的数据
HTTPCookieProcessor()  # 处理请求中带有的cookie
HTTPBasicAuthHandler()  # 处理web授权验证

创建一个自定义opener对象 相当于request中的urlopen()

使用opener对url发送请求
'''
