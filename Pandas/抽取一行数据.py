# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 21:10:45 2022

@author: lichade
"""

# 导入Excel数据 进行抽取
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)
df1 = pd.read_excel("C:/Users/lichade/Desktop/数据统计.xlsx",sheet_name= 0)
data = [[148,148,140],[105,88,115],[109,120,130],[112,115]]
name = ['李科','桂家波','冯涛','重修人员（缺考）']
columns = ['语文','数学','英语']
df1 = pd.DataFrame(data = data,index=name,columns=columns)
print(df1)
print("{0:#^80}".format("分隔线"))
# 抽取一行数据 主要使用loc属性
df2 = df1.loc["重修人员（缺考）"]
print(df2)
print("{0:#^80}".format("分隔线"))
df3 = df1.iloc[3]  # 使用iloc抽取数据
print(df3)