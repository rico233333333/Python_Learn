# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 22:15:03 2022

@author: lichade
"""

# 创建一个DataFrame对象
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)  # 对齐标签
dataDF1 = [[110,109,11],[120,103,101],[102,12,108]]
indexDF1 = [1,2,3]
columusDF1 = ["语文","数学","英语"]
DF = pd.DataFrame(data=dataDF1,index=indexDF1,columns=columusDF1)
print(DF)
# 创建字典存储数据
# 键 代表列标签
# 值 代表数据
Dict = dict(  
     语文=[107,78,56],
     数学=[90,89,78],
     英语=[98,89,78],
     班级="高三7班"
     )
DF2 = pd.DataFrame(data = Dict,index=[1,2,3])
print(DF2)
for col in DF2.columns:
    print(DF2[col])  # 此处输出Series类型数据
print(DF2.columns)  # 此处返回元组类型 前面的标签为一个列表 后面的是一个dtype = "object"