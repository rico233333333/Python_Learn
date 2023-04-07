# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 09:56:50 2022

@author: lichade
"""

# 按照指定的条件筛选数据 进行数据的抽取
import pandas as pd

data = [[100, 120, 130], [120, 123, 134], [110, 111, 112], [123, 98, 90]]
index = ["李科", "冯涛", "桂家波", "考神"]
columns = ["语文", "数学", "英语"]
df = pd.DataFrame(data=data, index=index, columns=columns)
print("{:-^100}".format("输出整张表"))
print(df)
print("{:-^100}".format("输出此表的columns标签"))
print(df.columns)
print("{:-^100}".format("输出此表的index标签"))
print(df.index)
print("{:-^100}".format("输出此表的所有数据"))
print(df.values)

print("{:-^100}".format("对数据按照条件筛选，并打印抽出的数据"))
df1 = df.loc[(df["语文"] > 100) & (df["数学"] > 50)]
print(df1)
print("{:-^100}".format(".iat[x,y]  取其中的一个元素"))
df2 = df.iat[1, 2]
print(df2)
