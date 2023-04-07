import requests,re,csv

URL = "https://movie.douban.com/top250"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

resp = requests.get(URL,headers=headers)

obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>.*?(?P<time>\d+).*?</p>.*?<div class="star">.*?<span class="rating_num" property="v:average">(?P<evaluation_score>.*?)</span>.*?<span>(?P<people_num>.*?)人评价</span>',re.S)

list = []
num = 0
page = resp.text

f = open("data.csv",mode = "w" ,encoding= "utf8",newline='')

print("正在生成迭代器...")
for i in obj.finditer(page):
    num = num + 1
    print("第"+str(num)+"次正在提取中...")  # ,i.group("englishname"),i.group("evaluation_score"),i.group("appraise_people_num")
    list_iter = [i.group("name"),i.group("time"),i.group("evaluation_score"),i.group("people_num")]
    list.append(list_iter)
    print("第"+str(num)+"次执行成功!")

print("最终数据列表：")
print(list)

a = csv.writer(f)
a.writerows(list)
f.close()
