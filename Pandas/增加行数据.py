# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 23:52:56 2022

@author: lichade
"""

import pandas as pd
# 增加行数据 
"""
只有loc属性以及append()方法
"""
pd.set_option("display.unicode.east_asian_width", True)
# loc 属性
data = [[10,20,30],[23,43,23]]
index = ["李科","桂家波"]
columns = ["语文","数学","英语"]
df = pd.DataFrame(data = data , index = index , columns = columns)
df.loc["李宏轩"] = [23,43,23]
print(df)
# 使用append()方法增加数据
data_1 = [[12,32,56],[21,43,21]]
index = ["冯涛","考神"]
df1 = pd.DataFrame(data = data_1 , index = index , columns = columns)
df2 = df.append(df1)
print(df2)