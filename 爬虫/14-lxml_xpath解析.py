from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>槽</name>
    <price>1.23</price>
    <nick>抽</nick>
    <author>
        <nick id = '123'>抽1</nick>
        <nick id = '1245'>抽2</nick>
        <nick id = '12312'>抽3</nick>
        <nick class = 'kajsh'>抽4</nick>
        <nick class = 'kasjhdkknxksd'>抽5</nick>
        <nick class = 'kjshkdsbvd'>抽6</nick>
        <div>
            <nick id = 'ppp'>抽7</nick>
            <nick id = 'uuu'>抽8</nick>
            <nick class = 'aaa'>抽9</nick>
            <nick class = 'bbb'>抽10</nick>
        </div>
        <span>
            <nick class = 'eee'>100chou</nick>
        </span>
    </author>
</book>
"""

tree = etree.XML(xml)
# data = tree.xpath("/book")  # /表示层级关系 第一个/代表根节点  此处返回此对象的内存地址
# data = tree.xpath('/book/author')  # 此处返回此对象的内存地址
data = tree.xpath('/book/author/nick/text()')  # 此处提取nick标签中的文本 若是想拿到文本必须在子节点后/text()
# data = tree.xpath('/book/author//nick/text()')  # 此处提取author标签中所有nick中的text文本  // 查找后代
# data = tree.xpath('/book/author/*/nick/text()')  # /*/查找任意属性值  * 任意节点 通配符
# data = tree.xpath('/book//nick/text()')  # 匹配父节点之下的所有nick标签
print(data)
