from urllib import request

'''
参数
1.url:请求地址
2.filename:文件保存路径和文件名
3.reporthook:回调函数，用于监听下载进度
'''

url = 'https://res.wx.qq.com/mpres/htmledition/images/wxopen/wap_mockup_top@2.png'

# resp = request.urlopen(url)
#
# with open('111.png', mode='wb') as f:
#     f.write(resp.read())  # with语句保存文件

resp = request.urlretrieve(url,'./222.png')
