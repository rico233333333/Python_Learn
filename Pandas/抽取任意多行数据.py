# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 21:58:18 2022

@author: lichade
"""

# 抽取任意多个数据
import pandas as pd
data = [[110, 120, 119], [120, 130, 145], [100, 98, 90], [120, 112, 123]]
index = ["冯涛", "李科", "桂家波", "考神"]
columns = ["语文", "数学", "英语"]
df1 = pd.DataFrame(data=data, index=index, columns=columns)
print(df1)
print("{:-^100}".format("抽取多行数据"))
print("{:-^100}".format("自定义标签索引DataFrame对象.loc[[]] 输出多行(采用嵌套，元素之间使用逗号间隔)"))
df2 = df1.loc[["李科", "冯涛"]]
print(df2)
print("{:-^100}".format("默认索引标签DataFrame对象.iloc[[]] 输出多行(采用嵌套，元素之间使用)"))
df3 = df1.iloc[[0, 2]]  # 取不到2
