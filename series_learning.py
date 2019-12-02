###
# 上面的用的都是DataFrame类型的数据，通过读取csv文件
# 另一个结构：Series  : 就是DataFrame的一行或者一列
import pandas as pd
fandango = pd.read_csv("fandango_score_comparison.csv") # 读取
series_film = fandango['FILM']  # 第一列
print(type(series_film))
print(series_film[0:5])
series_rt = fandango['RottenTomatoes']          # 其中一列
print(series_rt[0:5])
                                                    
from pandas import Series

film_names = series_film.values # 第一列的值 ,电影名
print(type(film_names)) # ndarray   说明DataFrame下是有Series组成，而Series是由ndarray组成
rt_scores = series_rt.values    # RottenTomatoes这一列的值
series_custom = Series(rt_scores, index=film_names)    # 相当于拿得分和电影名建立一个Key-value
series_custom[['Minions (2015)','Leviathan (2014)']]
fiveten = series_custom[5:10]
print(fiveten)

rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])       # 在Seires中，先值，后索引
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean = (rt_critics +rt_users)/2  # 把‘FILM’的两个列的值求平均
print(rt_mean)
