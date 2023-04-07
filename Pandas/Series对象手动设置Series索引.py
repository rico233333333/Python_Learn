# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:28:12 2022

@author: lichade
"""

# 手动设置Series索引

import pandas as pd

s1 = pd.Series([88,99,110],index = ["物理","化学","地理"])
print(s1)

# Series 位置索引
x = pd.Series([0,1,2,3],index=["英文","德文","日文","法文"])
print(x)

# Series 位置索引
print(x[0]) # series位置索引是[0] 控制台输出第一个元素 以此类推 第n个元素是n-1
# Series 标签索引
"""
Series对象["数据标签1"] 只能输出一个
如果想要引用多个 需要使用Series对象[["数据标签1","数据标签2","以此类推……"]] 
"""
print("Series标签索引1\n",x["日文"])
print("Series标签索引2\n",x[["法文","日文"]])
'''
Series使用标签做切片索引（此方法包头包尾）
Series对象["德文":"法文"]  # 输出"德文","法文"之间的所有 
Series使用位置做切片索引（此方法包头露尾）
Series对象[0,3] 不包含索引3位置的数据
'''
print(x["德文":"法文"])
print(x[0:3])
"""
获取Series对象的索引和值
Series对象.index 输出所有的数据标签  # 返回值为元组(前面是列表，后买是一个类型表达式)
Series对象.value 输出所有的数值  # 返回值为列表
"""
print("所有的数据标签:\n",x.index)
print("所有的值:\n",x.values)



# 创建Series对象
# 使用字典创建Series对象
DICT1 = dict(
    a = 5 ,
    b = 10
    )
S1 = pd.Series(data=DICT1)
print(S1)
# 广播创建Series 标量创建Series对象
S2 = pd.Series(90,index=["a","b","c"])
S3 = pd.Series(67)
print(S2,S3)
# 修改index 的
S1.index = ["D","E"]
print(S1)
# 为Series 和 index 添加对应的name属性
S1.name = "这是给Series添加的属性"
print(S1)
S1.index.name = "这是给index添加的属性"
print(S1)
print(S1.shape)
