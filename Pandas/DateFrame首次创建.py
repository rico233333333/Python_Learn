# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:34:48 2022

@author: lichade
"""

# DataFrame类型
import pandas as pd

# 创建DataFrame类型数据
data = [[110,105,99],[105,88,115],[109,120,130]]
index = [0,1,2]
columns = ["语文","数学","英语"]
# 创建DataFrame类型数据
df = pd.DataFrame(data = data , index = index , columns = columns)
print(df)
# 遍历DataFrame 数据的每一列
for cor in df.columns:
    print(df[cor])  # 得到一串Series对象
