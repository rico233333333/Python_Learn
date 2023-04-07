# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:05:59 2022

@author: lichade
"""

# 增加行数据
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
data = [[67,77,87],[98,88,87]]
columns = ["语文","数学","英语"]
index = ["冯涛","李科"]
df = pd.DataFrame(data = data , index = index ,columns = columns)
print(df)

# 增加列数据
# 使用loc属性增加数据
df.loc["桂家波"] = [34,54,34]
print(df)
# 增加多行数据
data_1 = [[78,88,98],[79,68,86]]
index_1 = ["林凯翔","李宏轩"]
df_1 = pd.DataFrame(data = data_1 , index = index_1 , columns = columns)
print(df_1)
df2 = df.append(df_1)  # 此处必须创建新的变量
print(df2)