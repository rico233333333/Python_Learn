import requests,re

# findall()函数 匹配字符串所有符合正则表达式的内容
re_str = re.findall(r"\d+","我的电话号码是10086我的电话号码是10086,121231231,123190182739,klasjhdkja,129387283")  # 三个参数 第一个参数填写对应的正则表达式 第二个参数填写电话号码 返回值为列表
print(re_str)

# finditer()函数 返回一个匹配字符的迭代器
it_str = re.finditer(r"\d+","我的电话号码是10086,121231231,123190182739,klasjhdkja,129387283")
for i in it_str:
    print(i)
    print(i.group())  # 我们可以通过.group()函数拿到迭代器中的匹配结果，而不是类的内存表示
print("".format())

# re.search() 返回对象为match对象，想从match对象中拿数据得结果.group()函数
# 找到一个结果就返回数据
it_list = re.search(r"\d+","我的电话号码是10086,121231231,123190182739,klasjhdkja,129387283")
print(it_list)

# re.match()函数 从头开始匹配 若是未达到条件（报错） 'NoneType' object has no attribute 'group'  返回match类型数据
# 只返回开头的匹配到的第一个数值
# 解决方法 改善匹配字符串，从头可以匹配到字符串即可
# list = re.match(r"\d+","我的电话号码是10086,121231231,123190182739,klasjhdkja,129387283")
list = re.match(r"\d+","10086,121231231,123190182739,klasjhdkja,129387283")
print(list.group())

# 预加载正则
obj = re.compile(r"\d+")
# 可以在全局变量obj存储一段正则表达式  可以调用任何正则函数（除了它本身）
for i in obj.finditer("10086,121231231,123190182739,klasjhdkja,129387283"):
    print(i.group())
