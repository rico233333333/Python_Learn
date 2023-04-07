# -*- coding: utf-8 -*-

# 数据清洗
import pandas as pd 
pd.set_option("display.unicode.east_asian_width", True)

# 数据导入
A = pd.read_excel(r"C:\Users\lichade\Desktop\数据统计.xlsx",sheet_name = 0 ,index_col = 0,header = 0)
A1 = A.head(5013)
print(A1)

print(A1.isnull())

print(A1.notnull())

A1.info()  # info()查看缺失值
A2 = A1.dropna()
print("#######################################################")
print(A1[A1["单价"] == False])
print(A2)
print(A1[A1.isnull() == False])  # 返回对象是一个Serise类型的数据
print(A1.notnull())
print(A1["单价"])
print(A1["单价"].notnull())
A3 = A1["单价"].notnull()
print(A1[A1["单价"].isnull()])
A4 = A1[A1["单价"].notnull()]
print(A4)
A1["单价"] = A1["单价"].fillna(0)  # fillna() 有三种填充方式None:指定一个数据填充 backfill/bfill:表示使用空数据后面的值填充 pad/Ffill:表示使用前一个数据填充
