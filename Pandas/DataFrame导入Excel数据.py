# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 19:47:04 2022

@author: lichade
"""

# pandas 导入数据

import pandas as pd 

EXsheet1 = pd.read_excel("C:/Users/lichade/Desktop/数据统计.xlsx",sheet_name=0)  # 导入Sheet1的数据
pd.set_option("display.unicode.east_asian_width", True)  # 设置对其
EX1 = EXsheet1.head(5020)  # 导入数据的行数
print(EX1)
print("{0:#^80}".format("分隔线"))


# 获取指定行的数据
# print(EX1[数量])
EXsheet1.index_col = 0  # 此处以“配件代码”行索引
EXsheet1_index_ico = EXsheet1
EXsheet1_index_ico_1 = EXsheet1_index_ico.head()
print(EXsheet1_index_ico_1)
print("{0:#^80}".format("分隔线"))


# 如果通过指定的列索引导入Excel数据，需要设置header参数
EXsheet1_index_ico_1.header = 1  # 通过列索引导入Excel数据  # 设置第一行为列索引 
EXsheet1_index_ico_2 = EXsheet1_index_ico_1
print(EXsheet1_index_ico_2)
print("{0:#^80}".format("分隔线"))


EXsheet2 = pd.read_excel("C:/Users/lichade/Desktop/数据统计.xlsx",sheet_name="长沙创普2020年数据")  # 设置了sheet_name属性为 sheet表格的名称
EX2 = EXsheet2.head(4000)  # 导入数据的行数
print(EX2)
print("{0:#^80}".format("分隔线"))


# 导入指定的数据
EXsheet2.usecols = ["配件代码","单价"]  # 此处导入第一列数据
print(EXsheet2)
print("{0:#^80}".format("分隔线"))


EXsheet3 = pd.read_excel("C:/Users/lichade/Desktop/数据统计.xlsx",sheet_name=1 ,usecols=[0,2])
EX3 = EXsheet3.head()
print(EX3)

















