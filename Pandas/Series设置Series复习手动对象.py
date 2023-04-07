# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 14:50:55 2022

@author: lichade
"""

# pandas Series 复习
import pandas as pd

a = pd.Series([88,90,76],index = ["li","zhang","wang"])
print(a)
b = pd.Series([22,33,44])
print(b)
print(b[0])  # Serise 位置索引
print(b[0:2])  # 包头不包尾 Series位置切片
print(a["li"])  # Series 标签索引 单个标签获取索引值
print(a[["li","zhang"]])  # Series 多个标签获取索引值
print(a["li":"wang"])  # Series 索引切片 包头包尾
print(a.index)  # 输出标签 返回一个元组类型的数据
print(a.values)  # 输出所有的值 返回一个列表类型的数据