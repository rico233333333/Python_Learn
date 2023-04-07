# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 08:47:28 2022

@author: lichade
"""

# 抽取指定列的数据

import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
data = [[100,120,130],[120,123,134],[110,111,112],[123,98,90]]
index = ["李科","冯涛","桂家波","考神"]
columns = ["语文","数学","英语"]
df = pd.DataFrame(data = data , index = index , columns = columns)
print(df)

# 直接使用列名
df1 = df[["语文","英语"]]
print(df1)

# loc属性
df2 = df.loc[:,["语文","英语"]]
print(df2)

# iloc属性
df3 = df.iloc[:,[0,2]]  
print(df3)