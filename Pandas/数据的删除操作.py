# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 00:15:16 2022

@author: lichade
"""

# 删除数据 .drop()方法

import pandas as pd

pd.set_option("display.unicode.east_asian_width",True)
data = [[13,45],[65,87]]
index = ['老张','老李']
columns = ["Python","Java"]
df = pd.DataFrame(data = data , index = index , columns = columns)
# 增加数据
# 增加行(loc)
df.loc["小李子",:] = [56,12]
# 删除行index
df.drop(index = "小李子",inplace = True)
print(df)
# 增加行append()
df1 = df.append(pd.DataFrame(data = [[45,76],[34,24]],index = ["小李子","倒数第一"],columns = ["Python","Java"]))
print(df1)
# 增加列
df.loc[:,"R"] = [43,42]
print(df)
# 增加列
df.insert(1,"C",[34,21])  # 在指定的索引处添加元素
print(df)
# 修改标签（行）.index = []
df.index = ["王老虎","李老四"]
print(df)
# 修改标签（行）.rename({"原数据":"被修改后的数据"},inplace = True ,asix = 0)
df.rename({"王老虎":"王老五"},axis = 0,inplace = True)
print(df)
# 修改标签（列）.columns
df.columns = ["C#","JavaScript","Html","SQL"]
print(df)
# 修改标签（行）.rename(colunms = {},inplace = )
df.rename(columns = {"C#":"张拉三","Html":"去你妹"},inplace = True)
print(df)
# 删除某列
df.drop(["张拉三"],axis = 1,inplace = True)
print(df)
# 删除列 columns
df.drop(columns = "去你妹" ,inplace = True)
print(df)
# lable 删除列
df.drop(labels = "JavaScript",axis = 1 ,inplace = True)
print(df)
# 删除某行
df.drop(["王老五"],inplace = True)
print(df)
# 删除某行
df1.drop(["倒数第一"],axis = 0 ,inplace = True)
print(df1)
# labels
df1.drop(labels = "小李子",axis = 0 ,inplace = True)
print(df1)
a = df1.iat(1,1)
print(a)