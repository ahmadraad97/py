# أداة DataFrame
import pandas as pd
import numpy as np

myarray = np.array([6,9,8,5,4])
y = ['a', 'b','c','d','e']
x= ['one']
df = pd.DataFrame(myarray, index=y, columns=x)
print(df)
#    one
# a    6
# b    9
# c    8
# d    5
# e    4

myarray = np.array([[6,9,8,5,4],[6,9,8,5,4]])
y = ['a', 'b']
x= ['one','two','three','four','five']
df = pd.DataFrame(myarray, index=y, columns=x)
print(df)
#    one  two  three  four  five
# a    6    9      8     5     4
# b    6    9      8     5     4


# باستخدام القاموس

a = pd.Series({2016:10 ,2017:20 ,2018:50 ,2019:60 ,2020:65})
b = pd.Series({2016:50 ,2017:50 ,2018:30 ,2019:20 ,2020:5})
c = pd.Series({2016:5,2017:20 ,2018:40 ,2019:40 ,2020:30})
d = pd.Series({2016:5 ,2017:20 ,2018:30 ,2019:50 ,2020:60})


sales = pd.DataFrame({'samsung':a,'htc':b,'huawei':c,'oneplus':d})

print(sales )
#       samsung  htc  huawei  oneplus
# 2016       10   50       5        5
# 2017       20   50      20       20
# 2018       50   30      40       30
# 2019       60   20      40       50
# 2020       65    5      30       60

# اظهار عمود محدد
print(sales['htc'])
# 2016    50
# 2017    50
# 2018    30
# 2019    20
# 2020     5



# اظهارها بالعكس (مقلوب المصفوفة)
print(sales.T )
#          2016  2017  2018  2019  2020
# samsung    10    20    50    60    65
# htc        50    50    30    20     5
# huawei      5    20    40    40    30
# oneplus     5    20    30    50    60



# اظهار القيم والمفاتيح
print(sales.keys())
# Index(['samsung', 'htc', 'huawei', 'oneplus']

print(sales.values)
# [[10 50  5  5]
#  [20 50 20 20]
#  [50 30 40 30]
#  [60 20 40 50]
#  [65  5 30 60]]



# معرفة هل القيمة كذا موجودة او لا
print('Htc'in sales.keys())
# False
print('htc'in sales.keys())
# True
print('a'in sales.keys())
# False


print(65 in sales.values)
# True
print(2016 in sales.values)
False

# فك القيم
print(sales.stack())
# 2016  samsung    10
#       htc        50
#       huawei      5
#       oneplus     5
# 2017  samsung    20
#       htc        50
#       huawei     20
#       oneplus    20
# 2018  samsung    50
#       htc        30
#       huawei     40
#       oneplus    30
# 2019  samsung    60
#       htc        20
#       huawei     40
#       oneplus    50
# 2020  samsung    65
#       htc         5
#       huawei     30
#       oneplus    60



# اظهار قيم محددة بالرقم
print(sales.iloc[:2,1:3])
#       htc  huawei
# 2016   50       5
# 2017   50      20

print(sales.iloc[:2,:-3])
#       samsung
# 2016       10
# 2017       20

print(sales.iloc[:-2,])
#       samsung  htc  huawei  oneplus
# 2016       10   50       5        5
# 2017       20   50      20       20
# 2018       50   30      40       30

# اظهار قيم بالاسم
print(sales.loc[2016:2019,'htc'])
# 2016    50
# 2017    50
# 2018    30
# 2019    20
















