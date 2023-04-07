from urllib import request


'''
parse

编码：urlencode()  里面传入字典类型啥
解码：parse_qs() 解码 成字典类型
解码：parse_qsl() 解码成列表
url拆解：urlsplit()按照指定字符串拆解  urlpase() 按照固定格式拆解字符串
'''

'''
error

error把请求中常见的错误封装到URLError 和 HTTPError这两个类中
URLError封装的错误信息一般是有网络引起的 请求服务器未接收到信息就返回错误
HTTPError封装的错误信息一般是服务器引起的，并且返回错误状态码
'''
