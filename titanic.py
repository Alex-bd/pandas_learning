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

good_ages = titanic_survival["Age"][age_is_null == False]   # 获取年龄不缺失的
correct_mean_age = sum(good_ages) / len(good_ages)
print(correct_mean_age) # 计算结果29.

# 求均值，但是不是个好方法，直接忽略缺失值
correct_mean_age = titanic_survival["Age"].mean()
print(correct_mean_age)
# 每个仓位等级的平均价格
passenger_classes = [1, 2, 3]
fares_by_class = {}
for this_class in passenger_classes:
    # pclass_rows先获取到Pclass为1的数据，然后pclass_fares获取到这些1仓的人的价格那一列，然后求平均值，之后在对2,3仓重复操作
    pclass_rows = titanic_survival[titanic_survival["Pclass"] == this_class]    # Pclass为不同等级的仓
    pclass_fares = pclass_rows["Fare"]  # Fare为价格
    fares_for_class = pclass_fares.mean()   # 平均值
    fares_by_class[this_class] =fares_for_class
print(fares_by_class)
# 上面的循环的过程可以通过pivot_table函数实现
passenger_fares = titanic_survival.pivot_table(index="Pclass", values="Fare", aggfunc=np.mean)
print(passenger_fares)
# Pclass
# 1       84.154687
# 2       20.662183
# 3       13.675550

# 求各舱年龄的最大值
passenger_age_max = titanic_survival.pivot_table(index = "Pclass" , values = "Age", aggfunc = np.max)
print(passenger_age_max)

# dropna 去掉有缺失值的样本
drop_na_columns = titanic_survival.dropna(axis=1)
new_titanic_survival = titanic_survival.dropna(axis =0,subset=["Age", "Sex"])

# 获取某一个值
row_index_83_age = titanic_survival.loc[83, "Age"]
print(row_index_83_age)

new_titanic_survival2 = titanic_survival.sort_values("Age", ascending=False)    # 新的数据按照Age升序排序
print(new_titanic_survival2[0:10])
titanic_reindexed = new_titanic_survival2.reset_index(drop=True)    # 重新建立索引值，drop=True的意思是原来的索引不要了
print('---------')
print(titanic_reindexed.loc[0:10])

# 年龄连续值离散化
def generate_age_label(row):
    age = row["Age"]
    if pd.isnull(age):
        return "unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"
age_labels = titanic_survival.apply(generate_age_label,axis=1)
print(age_labels)
# 想求得 成年人，未成年人获救的均值
titanic_survival['age_labels'] = age_labels     # 把minor,adult和unknown作为一个新的列加入到数据中
age_group_survial = titanic_survival.pivot_table(index="age_labels", values="Survived",aggfunc=np.mean)
print(age_group_survial)


