# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 09:10:53 2022

@author: lichade
"""

import pandas as pd

# 抽取指定行指定列的数据

data = [[100,120,130],[120,123,134],[110,111,112],[123,98,90]]
index = ["李科","冯涛","桂家波","考神"]
columns = ["语文","数学","英语"]
df = pd.DataFrame(data = data , index = index , columns = columns)
print(df)

print("{:-^100}".format("这是一条分割线"))
# loc 自定义标签索引
df1 = df.loc[["李科"],["数学"]]  # 行、列
print(df1)
print("{:-^100}".format("这是一条分割线"))

df2 = df.loc["桂家波","英语"]
print(df2)
print("{:-^100}".format("这是一条分割线"))

df3 = df.loc[["冯涛"],["数学","语文"]]
print(df3)
print("{:-^100}".format("这是一条分割线"))

# iloc 位置索引
df3 = df.iloc[0,0] 
print(df3)
print("{:-^100}".format("这是一条分割线"))

df4 = df.iloc[[2],[2]]
print(df4)
print("{:-^100}".format("这是一条分割线"))

df5 = df.iloc[0:2,0:2]
print(df5)
print("{:-^100}".format("这是一条分割线"))

df6 = df.iloc[1,[0,1]]
print(df6)
print("{:-^100}".format("这是一条分割线"))

df7 = df.iloc[:,2]
print(df7)
print("{:-^100}".format("这是一条分割线"))
display(df)

