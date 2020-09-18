import pandas as pd
# مزج الجداول
df1 = pd.DataFrame({'marka': ['htc', 'samsung', 'sony', 'huawei'],
                    'mobile': ['one8', 'note9',
                              'z3', 'mate30']})

df2 = pd.DataFrame({'marka': ['htc', 'samsung', 'sony', 'huawei'],
                    'date': [2015, 2018, 2016, 2020]})
print(df1)
#      marka  mobile
# 0      htc    one8
# 1  samsung   note9
# 2     sony      z3
# 3   huawei  mate30
print('--------------------------')
print(df2)
#      marka  date
# 0      htc  2015
# 1  samsung  2018
# 2     sony  2016
# 3   huawei  2020
print('--------------------------')

df3 = pd.merge(df1, df2)
print(df3)
#      marka  mobile  date
# 0      htc    one8  2015
# 1  samsung   note9  2018
# 2     sony      z3  2016
# 3   huawei  mate30  2020
print('--------------------------')
df4 = pd.DataFrame({'marka': ['htc', 'samsung', 'sony', 'huawei'],
                    'mobile2': ['one8eye', 's9plus',
                              'z3plus', 'p30pro']})
df5=pd.merge(df3,df4)
print(df5)
#      marka  mobile  date  mobile2
# 0      htc    one8  2015  one8eye
# 1  samsung   note9  2018   s9plus
# 2     sony      z3  2016   z3plus
# 3   huawei  mate30  2020   p30pro
print('--------------------------')

a = pd.DataFrame({'marka': ['htc', 'samsung', 'sony', 'huawei'],
                    'mobile2': ['one8eye', 's9plus',
                              'z3plus', 'p30pro']})

b = pd.DataFrame({'name': ['htc', 'samsung', 'sony', 'huawei'],
                    'date': [2015, 2018, 2016, 2020]})

print(pd.merge(a,b,left_on='marka',right_on='name'))
#      marka  mobile2     name  date
# 0      htc  one8eye      htc  2015
# 1  samsung   s9plus  samsung  2018
# 2     sony   z3plus     sony  2016
# 3   huawei   p30pro   huawei  2020
print('--------------------------')


# حذف اعمدة
print(pd.merge(a,b,left_on='marka',right_on='name').drop('name',axis=1))
#      marka  mobile2  date
# 0      htc  one8eye  2015
# 1  samsung   s9plus  2018
# 2     sony   z3plus  2016
# 3   huawei   p30pro  2020
print('--------------------------')


# تغيير المفتاح
a = pd.DataFrame({'marka': ['htc', 'samsung', 'sony', 'huawei'],
                    'mobile2': ['one8eye', 's9plus',
                              'z3plus', 'p30pro']})
a=a.set_index('marka')
print(a)
#          mobile2
# marka           
# htc      one8eye
# samsung   s9plus
# sony      z3plus
# huawei    p30pro
print('--------------------------')


# تقاطع البيانات
y=pd.DataFrame({'name': ['asus', 'htc', 'nokia'],
                    'mobile': ['ROG', 'u11', '8.1']},
                    columns=['name', 'mobile'])

x=pd.DataFrame({'name': ['lenovo', 'asus'],
                    'laptop': ['thinkpad', 'zenbook']},
                    columns=['name', 'laptop'])

df = pd.merge(y, x)
print(df)
#    name mobile   laptop
# 0  asus    ROG  zenbook
print('--------------------------')
df = pd.merge(y, x,how='inner')
print(df)
#    name mobile   laptop
# 0  asus    ROG  zenbook
print('--------------------------')

# جميع الصفوف
df = pd.merge(y, x,how='outer')
print(df)
#      name mobile    laptop
# 0    asus    ROG   zenbook
# 1     htc    u11       NaN
# 2   nokia    8.1       NaN
# 3  lenovo    NaN  thinkpad
print('--------------------------')

# الجدول الايمن كامل
df = pd.merge(y, x,how='right')
print(df)
#      name mobile    laptop
# 0  lenovo    NaN  thinkpad
# 1    asus    ROG   zenbook
print('--------------------------')

# الجدول الايسر كامل
df = pd.merge(y, x,how='left')
print(df)
#     name mobile   laptop
# 0   asus    ROG  zenbook
# 1    htc    u11      NaN
# 2  nokia    8.1      NaN
print('--------------------------')



# بيانات احصائية
import numpy as np
df = pd.DataFrame({'A': np.random.rand(5),'B': np.random.rand(5)})
print(df)
#           A         B
# 0  0.692655  0.110046
# 1  0.803382  0.082373
# 2  0.643961  0.958995
# 3  0.212085  0.467393
# 4  0.130715  0.901826
print('------------------------------')
print(df.sum())
# A    2.482798
# B    2.520633
print('------------------------------')
print(df.prod())
# A    0.009934
# B    0.003664
print('------------------------------')
print(df.mean())
# A    0.496560
# B    0.504127
print('------------------------------')

# بيانات احصائية لعمود معين
df = pd.DataFrame({'A': np.random.rand(5),'B': np.random.rand(5)})
print(df)
#           A         B
# 0  0.389761  0.970258
# 1  0.599605  0.799224
# 2  0.509164  0.841637
# 3  0.935683  0.001344
# 4  0.603871  0.362601
print('------------------------------')
print(df['A'].sum())
# 3.03808364310572
print('------------------------------')
print(df['A'].prod())
# 0.0672347500743544
print('------------------------------')
print(df['B'].mean())
# 0.5950127664754483
print('------------------------------')


# بيانات إحصائية للصفوف
df = pd.DataFrame({'A': np.random.rand(5),'B': np.random.rand(5)})
print(df)
#           A         B
# 0  0.558331  0.674797
# 1  0.629246  0.889954
# 2  0.550782  0.817899
# 3  0.085006  0.724003
# 4  0.420916  0.814145
print('------------------------------')
print(df.mean(axis='rows'))
# A    0.448856
# B    0.784160
print('------------------------------')
print(df.count(axis='rows'))
# A    5
# B    5
print('------------------------------')
print(df.min(axis='rows'))
# A    0.085006
# B    0.674797
print('------------------------------')
print(df.max(axis='rows'))
# A    0.629246
# B    0.889954
print('------------------------------')
print(df.std(axis='rows'))
# A    0.216842
# B    0.084866
print('------------------------------')
print(df.sum('rows'))
# A    2.244281
# B    3.920799
print('------------------------------')


# بيانات احصائية
df = pd.DataFrame({'key':['A','B','C','A','B','C'],
                   'data': range(6)},columns=['key', 'data'])

print(df)
#   key  data
# 0   A     0
# 1   B     1
# 2   C     2
# 3   A     3
# 4   B     4
# 5   C     5
print(df.describe())
#            data
# count  6.000000
# mean   2.500000
# std    1.870829
# min    0.000000
# 25%    1.250000
# 50%    2.500000
# 75%    3.750000
# max    5.000000
print('------------------------------')

# مجموع قيم متشابهة
df = pd.DataFrame({'key':['A','B','C','A','B','C'],
                   'data': range(6)},columns=['key', 'data'])

print(df)
#   key  data
# 0   A     0
# 1   B     1
# 2   C     2
# 3   A     3
# 4   B     4
# 5   C     5
print(df.groupby('key').sum())
#      data
# key      
# A       3
# B       5
# C       7
print('------------------------------')

# بيانات احصائية لقيم متشابهة
df = pd.DataFrame({'key':['A','B','C','A','B','C'],
                   'data': range(6)},columns=['key', 'data'])

print(df)
#   key  data
# 0   A     0
# 1   B     1
# 2   C     2
# 3   A     3
# 4   B     4
# 5   C     5
print('------------------------------')

print(df.groupby('key').describe())
#      data                                         
#     count mean      std  min   25%  50%   75%  max
# key                                               
# A     2.0  1.5  2.12132  0.0  0.75  1.5  2.25  3.0
# B     2.0  2.5  2.12132  1.0  1.75  2.5  3.25  4.0
# C     2.0  3.5  2.12132  2.0  2.75  3.5  4.25  5.0
print('------------------------------')

# فك القيم الاحصائية
df = pd.DataFrame({'key':['A','B','C','A','B','C'],
                   'data': range(6)},columns=['key', 'data'])

print(df)
#   key  data
# 0   A     0
# 1   B     1
# 2   C     2
# 3   A     3
# 4   B     4
# 5   C     5
print('------------------------------')
print(df.groupby('key').describe().unstack())
#              key
# data  count  A      2.00000
#              B      2.00000
#              C      2.00000
#       mean   A      1.50000
#              B      2.50000
#              C      3.50000
#       std    A      2.12132
#              B      2.12132
#              C      2.12132
#       min    A      0.00000
#              B      1.00000
#              C      2.00000
#       25%    A      0.75000
#              B      1.75000
#              C      2.75000
#       50%    A      1.50000
#              B      2.50000
#              C      3.50000
#       75%    A      2.25000
#              B      3.25000
#              C      4.25000
#       max    A      3.00000
#              B      4.00000
#              C      5.00000
print('------------------------------')


# المجموعات
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': np.random.randint(0, 10, 6)},
                    columns = ['key', 'data1', 'data2'])

print(df)
#   key  data1  data2
# 0   A      0      3
# 1   B      1      0
# 2   C      2      3
# 3   A      3      7
# 4   B      4      2
# 5   C      5      9
df2 = df.groupby('key').aggregate({'data1': 'min','data2': 'max'})
print(df2)
#      data1  data2
# key              
# A        0      7
# B        1      2
# C        2      9


# الفلتر
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': np.random.randint(0, 10, 6)},
                    columns = ['key', 'data1', 'data2'])

print(df)
#   key  data1  data2
# 0   A      0      1
# 1   B      1      8
# 2   C      2      9
# 3   A      3      4
# 4   B      4      7
# 5   C      5      0
def filter_func(x):
    return x['data2'].sum() <= 5

df2 = df.groupby('key').filter(filter_func)
print(df2)
#   key  data1  data2
# 0   A      0      1
# 3   A      3      4


# تطبيق لمدا
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': np.random.randint(0, 10, 6)},
                    columns = ['key', 'data1', 'data2'])

print(df)
#   key  data1  data2
# 0   A      0      7
# 1   B      1      7
# 2   C      2      8
# 3   A      3      9
# 4   B      4      4
# 5   C      5      0

df2 = df.groupby('key').transform(lambda x: x**2)

print(df2)
#    data1  data2
# 0      0     49
# 1      1     49
# 2      4     64
# 3      9     81
# 4     16     16
# 5     25      0
























































































































































































































































