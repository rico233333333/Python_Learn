import requests,re,csv,base64

for i in range(1,18):
    if i == 1:
        URL = "https://www.dy2018.com/html/bikan/"  # 封装URL
    else :
        URL = "https://www.dy2018.com/html/bikan/index_"+str(i)+".html"

    resp = requests.get(url=URL,verify=False)  # verify = Flase  代表去掉安全验证
    resp.encoding = "gb2312"
    print("第"+str(i)+"次爬取成功")
    obj = re.compile(r'<table width="100%" border="0" cellspacing="0" cellpadding="0" class="tbspan" style="margin-top:6px">.*?<b>.*?<a href="(?P<html_url>.*?)" class="ulink" title="(?P<title>.*?)">.*?</a>.*?</b>',re.S)  #.*?title="(?P<time_year>.*?)年(?P<title>.*?)">.*?</a>.*?日期：(?P<time>.*?).*?点击：(?P<number>\d+)

    son_re = re.compile(r'<tr>.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<URL>.*?)</a></td>.*?</tr>',re.S)

    for j in obj.finditer(resp.text):
        son_utl = "https://www.dy2018.com"+j.group("html_url")
        title = j.group("title")
        print(son_utl)
        son_resp = requests.get(son_utl)
        son_resp.encoding = "GB2312"
        son_re_list = son_re.findall(son_resp.text)
        print(son_re_list)
        son_resp.close()

    resp.close()
