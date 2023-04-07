from lxml import etree  # 导入包

html = """
<html>

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="Content-Type" content="text/html" />
    <title>自我介绍</title>
</head>

<body>
    <h1>自我介绍</h1>
    <dl>
        <dt>姓名</dt>
        <dd>王xx</dd>
        <dt>性别</dt>
        <dd>男</dd>
        <dt>住址</dt>
        <dd>石家庄市鹿泉区</dd>
        <dt>爱好</dt>
        <dd>打游戏，打游戏，打游戏</dd>
    </dl>
    <li>
        <a href="http://www.baidu.com123">飞机</a>
    </li>
    <li>
        <a href="http://www.baidu.com456">火箭</a>
    </li>
    <li>
        <a href="http://www.baidu.com789">大炮</a>
    </li>
    <p>
        大家好，我像现在将简单介绍一下我自己，我今年21岁，出生于中国东北，
        爱一个人好难，爱俩个人正常，爱三个人好玩，爱四个人好平凡。
    </p>
</body>

</html>
"""
with open("./baidu.html", mode='w', encoding='utf8') as w:
    w.writelines(html)

tree = etree.parse(r'D:/CODE/python_project/baidu.html')  # 加载html文档  预加载的html文档不得出现任何错误
# result = tree.xpath('/html/body/dl/dt[1]/text()')  # 此处拿第一个dt标签对应的属性值需要注意的是，xpath的索引从1开始 在对应检索标签后添加[1]代表只拿匹配到的第一个标签的值
# result = tree.xpath('/html/body/a[@href="http://www.baidu.com789"]/text()')  # 此处对应标签[@属性 = "值"]/text()  这样可以提取对应标签 属性的筛选
# print(result)
html_body_li = tree.xpath('/html/body/li')  # 此处返回一个列表
# print(html_body_li)
for li in html_body_li:
    # print(a.xpath("/a/text()"))
    # 从每一个a标签中提取文字信息
    result = li.xpath('./a/text()')
    print(result)  # 在a标签中继续查找，也叫作相对查找  ./a/text()
    result2 = li.xpath('./a/@href')  # 获取属性值 @href
    print(result2)
