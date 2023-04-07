# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 22:28:23 2022

@author: lichade
"""

# 抽取连续多行数据

import pandas as pd

data = [[100,120,130],[120,123,134],[110,111,112],[123,98,90]]
index = ["李科","冯涛","桂家波","考神"]
columns = ["语文","数学","英语"]
df = pd.DataFrame(data = data , index = index , columns = columns)
print(df)
# 抽取连续的多行数据
df1 = df.iloc[0:3:2]  # iloc 包头不包尾 与 列表的切片差不多
print(df1)
df2 = df.loc["李科":"桂家波"]  # loc 包头包尾 loc针对自定义标签与索引
print(df2)