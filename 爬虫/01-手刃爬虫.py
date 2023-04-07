from urllib.request import urlopen
# 导入了urllib库中的request类中的urlopen方法

url = "http://www.baidu.com/"

resp = urlopen(url)

print()

print(resp.read().decode("utf-8"))

with open(r"D:\CODE\python_project\src\爬虫\爬虫上课学习\baidu.html", mode="w", encoding='utf-8') as f:
    f.write(resp.read().decode("utf-8"))

print("over!!!")
