import pandas as pd
# عمل مصفوفة من بعد واحد(الـ S كابيتال)
data=pd.Series([1,0.75,0.5,True])
print(data)
# 0       1
# 1    0.75
# 2     0.5
# 3    True

# القيم
data=pd.Series([1,0.75,0.5,True])
print(data.values)
# [1 0.75 0.5 True]
print(data.index)
# RangeIndex(start=0, stop=4, step=1)
print(data.keys)
# keys of 0       1
# 1    0.75
# 2     0.5
# 3    True

# معلومات عنها
data=pd.Series([1,0.75,0.5,True])
print(data.describe())
# count     4.0
# unique    3.0
# top       1.0
# freq      2.0
data=pd.Series([10,40,50,65,73,67,20,90])
print(data.describe())
# count     8.000000
# mean     51.875000
# std      27.294361
# min      10.000000
# 25%      35.000000
# 50%      57.500000
# 75%      68.500000
# max      90.000000

# معلومات محددة عنها
data=pd.Series([10,40,50,65,73,67,20,90])
print(data.agg(['min','max','std']))
# min    10.000000
# max    90.000000
# std    27.294361

# الاجتزاء
data=pd.Series([10,40,50,65,73,67,20,90])
print(data[2])
# 50
print(data[2:10])
# 2    50
# 3    65
# 4    73
# 5    67
# 6    20
# 7    90
print(data[0:8:2])
# 0    10
# 2    50
# 4    73
# 6    20

# كتابة ليست
galaxy=pd.Series(['note1','note2','note3','note4','note5','note7','note8','note9','note10','note20'],index=[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])
galaxy0=pd.Series({'note1':2011,'note2':2012,'note3':2013})
print(galaxy)
# 2011     note1
# 2012     note2
# 2013     note3
# 2014     note4
# 2015     note5
# 2016     note7
# 2017     note8
# 2018     note9
# 2019    note10
# 2020    note20
print(galaxy0)
# note1    2011
# note2    2012
# note3    2013


# قيمة محددة
print(galaxy[2014])
# note4

# عمل ليست
x = pd.Index([2,3,5,7,11])

print(x)
# Int64Index([2, 3, 5, 7, 11], dtype='int64')



# علاقات منطقية
a=pd.Index([0,2,4,6])
b=pd.Index([1,2,4,7])

print(a)
# Int64Index([0, 2, 4, 6],
print('-------------------------')
print(b)
# Int64Index([1, 2, 4, 7],
print('-------------------------')
print(a & b)
# Int64Index([2, 4], dtype='int64')
print('-------------------------')
print(a | b)
# Int64Index([0, 1, 2, 4, 6, 7],
print('-------------------------')
print(a ^ b)
# Int64Index([0, 1, 6, 7],





























































































































































































