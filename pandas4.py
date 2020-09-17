import pandas as pd
import numpy as np
# اظهار قيم بالشرط
a = pd.Series({2016:10 ,2017:20 ,2018:50 ,2019:60 ,2020:65})
b = pd.Series({2016:50 ,2017:50 ,2018:30 ,2019:20 ,2020:5})
c = pd.Series({2016:5,2017:20 ,2018:40 ,2019:40 ,2020:30})
d = pd.Series({2016:5 ,2017:20 ,2018:30 ,2019:50 ,2020:60})


sales = pd.DataFrame({'samsung':a,'htc':b,'huawei':c,'oneplus':d})

print(sales.loc[sales.htc>30] )
#       samsung  htc  huawei  oneplus
# 2016       10   50       5        5
# 2017       20   50      20       20

# اظهار اعمدة بشرط محدد
print(sales.loc[sales.htc>30,['samsung']] )
#       samsung
# 2016       10
# 2017       20

print(sales.loc[sales.htc>30,['samsung','htc']] )
#       samsung  htc
# 2016       10   50
# 2017       20   50

# اظهار اعمدة
print(sales.columns )
# Index(['samsung', 'htc', 'huawei', 'oneplus'], dtype='object')

# اظهار عمود محدد
print(sales['huawei'] )

# اظهار صفوف
print(sales.index)
# Int64Index([2016, 2017, 2018, 2019, 2020], dtype='int64')


# اظهار عمود محدد
print(sales['huawei'] )
# 2016     5
# 2017    20
# 2018    40
# 2019    40
# 2020    30
# Name: huawei, dtype: int64


# ترتيب صفوف
print(sales.sort_values(['huawei'] ))
#       samsung  htc  huawei  oneplus
# 2016       10   50       5        5
# 2017       20   50      20       20
# 2020       65    5      30       60
# 2018       50   30      40       30
# 2019       60   20      40       50

print(sales.sort_values(['oneplus'] ,ascending=False))
#       samsung  htc  huawei  oneplus
# 2020       65    5      30       60
# 2019       60   20      40       50
# 2018       50   30      40       30
# 2017       20   50      20       20
# 2016       10   50       5        5



# اظهار قيم احصائية
print(sales.max())
# samsung    65
# htc        50
# huawei     40
# oneplus    60
print(sales.min())
# samsung    10
# htc         5
# huawei      5
# oneplus     5
print(sales.mean())
# samsung    41.0
# htc        31.0
# huawei     27.0
# oneplus    33.0
print(sales.std())
# samsung    24.596748
# htc        19.493589
# huawei     14.832397
# oneplus    22.248595



# اظهار قيم احصائية لعمود محدد
print(sales['htc'].max())
# 50
print(sales['samsung'].min())
# 10
print(sales['oneplus'].mean())
# 33.0
print(sales['huawei'].std())
# 14.832396974191326


# معامل الارتباط
print(sales.corr())
#           samsung       htc    huawei   oneplus
# samsung  1.000000 -0.954161  0.866845  0.952502
# htc     -0.954161  1.000000 -0.678745 -0.959754
# huawei   0.866845 -0.678745  1.000000  0.734848
# oneplus  0.952502 -0.959754  0.734848  1.000000

df=pd.DataFrame(np.random.rand(4,3),columns=['a','b','c'])
print(df)
#           a         b         c
# 0  0.523277  0.997553  0.749156
# 1  0.136942  0.346841  0.164385
# 2  0.957239  0.946560  0.574280
# 3  0.759046  0.256133  0.238808
print(df.corr())
#           a         b         c
# a  1.000000  0.380306  0.408766
# b  0.380306  1.000000  0.957519
# c  0.408766  0.957519  1.000000


# قيمة الانحراف
print(df.skew())
# a    1.845568
# b    1.192371
# c   -1.584784

# كتابة جدول بدالة تربيعية
data = [{'square': i**2} for i in range(10)]
d = pd.DataFrame(data)

print(data)
# [{'square': 0}, {'square': 1}, {'square': 4}, {'square': 9}, {'square': 16}, {'square': 25}, {'square': 36}, {'square': 49}, {'square': 64}, {'square': 81}]
print(d)
# square
# 0       0
# 1       1
# 2       4
# 3       9
# 4      16
# 5      25
# 6      36
# 7      49
# 8      64
# 9      81





# عدد من الدوال
data = [{'square': i**2,'cube': i**3
         ,'root': i**0.5} for i in range(5)]

d = pd.DataFrame(data)
print(d)
#    square  cube      root
# 0       0     0  0.000000
# 1       1     1  1.000000
# 2       4     8  1.414214
# 3       9    27  1.732051
# 4      16    64  2.000000


# مزج القواميس

d = pd.DataFrame([{'htc':'one8','samsung':'s5'},{'htc':'one9','samsung':'s6'},{'htc':10,'samsung':'s7'}],index=[2015,2016,2017])
print(d)
#        htc samsung
# 2015  one8      s5
# 2016  one9      s6
# 2017    10      s7


# مزج القواميس مع وجود فراغات 
d = pd.DataFrame([{'htc':'one8','samsung':'s5'},{'htc':'one9','samsung':'s6'},{'htc':10,'samsung':'s7'},{'oppo':'findx','xiaomi':'alpha'}])
print(d)
#     htc samsung   oppo xiaomi
# 0  one8      s5    NaN    NaN
# 1  one9      s6    NaN    NaN
# 2    10      s7    NaN    NaN
# 3   NaN     NaN  findx  alpha























