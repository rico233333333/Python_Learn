# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 15:29:29 2022

@author: lichade
"""

# 增加数据
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
data = [[110,120,119],[108,117,114]]
index = ["李科","冯涛"]
columns = ["语文","数学","英语"]

df = pd.DataFrame(data = data , index = index , columns = columns)
print(df)
# 直接为DataFrame对象赋值
df["物理"] = [80,70]
print(df)  
# 以loc属性增加数据
df.loc[:,"化学"] = [80,78]
print(df)
df.insert(0,"生物",[78,77])
print(df)