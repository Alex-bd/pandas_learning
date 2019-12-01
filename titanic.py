import pandas as pd
import numpy as np
titanic_survival = pd.read_csv("titanic_train.csv")
titanic_survival.head()
# print(titanic_survival)
# NaN在pandas是缺失值
age = titanic_survival["Age"]
print(age.loc[0:10])    # 打印前十个年龄
age_is_null = pd.isnull(age) # 判断是否是缺失值
print(age_is_null)
age_null_true = age[age_is_null]# 把判断为缺失的索引为True的值保留出来
age_null_count =len(age_null_true)
print(age_null_count)   # 打印数量  共177个
# 计算年龄均值
mean_age =sum(titanic_survival["Age"]) / len(titanic_survival["Age"])
print(mean_age)  # 因为有缺失值，所以无法计算