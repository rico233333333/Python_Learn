# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:35:52 2022

@author: lichade
"""

import pandas as pd
s1 = pd.Series([1,2,3],index=["大学物理","大学英语","数据分析"]) 
# 此处index标签里面对应的是Sercise对象每一个元素对应的所有 ，如果不设置默认是0，1，2……
print(s1)
import pandas as pd
# 创建Series对象
DATA = [90,78,80]
Index = ["数学","英语","语文"]
SER = pd.Series(DATA,index = Index)
# 更改index数据
Index = ["A","B","C"]
SER.index = Index
# 为Series添加name属性
SER.name = "为Series添加的name属性"
# 为index添加的name属性
SER.index.name = "为index添加的name属性"

print('{0:#^60}'.format('输出Serise对象'))
print(SER)

# Series的标签索引
print('{0:#^60}'.format('索引单个标签使用[]'))
print(SER["A"],"索引单个标签")
print('{0:#^60}'.format('索引多个标签使用 [[]] 这种嵌套方式'))
print(SER[["A","C"]],"索引多个标签")
# Series的位置索引
print('{0:#^60}'.format("位置索引[] 此处索引不可以是[-1]"))
print(SER[0])
print("{0:#^60}".format("位置索引多个标签[[]]"))
print(SER[[0,2]])
print("{0:#^60}".format("索引切片 包头包尾"))
print(SER["A":"C"])
print("{0:#^60}".format("位置切片 包头不包尾"))
print(SER[0:2])
# 利用.index属性输出
print("{0:#^60}".format("利用.index属性输出索引"))
print(SER.index)
# 利用.values属性输出值
print("{0:#^60}".format("利用.values属性输出值"))
print(SER.values)
# 利用.shape属性输出Series对象的形状
print("{0:#^60}".format("利用.shape属性输出Series对象的形状"))
print(SER.shape)
