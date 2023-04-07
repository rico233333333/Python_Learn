# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 01:03:12 2022

@author: lichade
"""

# 修改行标签
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

data = [[65,75,65],[78,97,68]]
index = ["A","B"]
columns = ["a","b","c"]
df = pd.DataFrame(data = data , index = index ,columns = columns)
print(df)
df.index = ["C","D"]
print(df)
df.index = list("12")
print(df)

df.rename({"1":5},axis = 0,inplace = True)
print(df)
df.iloc[1,1] = 400
print(df)

