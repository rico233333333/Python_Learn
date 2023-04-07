# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 11:54:03 2022

@author: Ricardo
"""

# pandas 前期复习
import pandas as pd
# 创建Series对象
# Series组成DataFrame
s1 = pd.Series([12,34,3423])
print(":#^25".format("小试牛刀"))
print(s1)
dict1 = {"张三":[12876,23098,1982]}
print(dict1.keys())
print(list(dict1.values())[0])
s2  =pd.Series({"张三":[12876,23098,1982]})
print(s2)