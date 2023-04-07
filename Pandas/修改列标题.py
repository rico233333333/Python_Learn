# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 00:12:35 2022

@author: lichade
"""

# 修改数据
import pandas as pd

pd.set_option("display.unicode.east_asian_width",True)

data = [[65,75,65],[78,97,68]]
index = ["A","B"]
columns = ["a","b","c"]
df = pd.DataFrame(data = data , index = index ,columns = columns)
print(df)
# 修改列数据
"""
修改 列标题主要有两种方法

一种是 DataFrame里的colunms属性
第二种是 rename()方法
"""
# 第一种
df.columns = ["d","e","f"]
print(df)
# 第二种
df.rename(columns = {"d":"D","e":"E","f":"F"} ,inplace = True)
print(df)