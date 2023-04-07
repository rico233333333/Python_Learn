# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:38:06 2022

@author: lichade
"""

# pandas 导入CSV文件
import pandas as pd

df1 = pd.read_csv("C:/Users/lichade/Desktop/数据统计.csv",encoding = "UTF-8")
df1 = df1.head(5000)
print(df1)

# 导入txt文档
df2 = pd.read_csv()