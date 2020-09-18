# أداة MultiIndex
import pandas as pd
import numpy as np

company = [('samsung', 2011),('samsung', 2020),
         ('htc', 2011),('htc', 2020),
         ('huawei', 2011),('huawei', 2020)]

model = ['s2','s20',
               'Incredible S','u12plus',
               'Ascend','p40']

company = pd.MultiIndex.from_tuples(company)
pop = pd.Series(model, index=company)
pop = pop.reindex(company)
print(pop)
# samsung  2011              s2
#          2020             s20
# htc      2011    Incredible S
#          2020         u12plus
# huawei   2011          Ascend
#          2020             p40
print('------------------------------')



# سنة محددة
print(pop[:,2011])
# samsung              s2
# htc        Incredible S
# huawei           Ascend
print('------------------------------')

# تدوير البيانات
print(pop.unstack())
#                  2011     2020
# htc      Incredible S  u12plus
# huawei         Ascend      p40
# samsung            s2      s20
print('------------------------------')


# زيادة عمود
pop_df = pd.DataFrame({'model': pop,
                       'sales':[10, 50,5,
                                  15,2, 30]})

print(pop)
# samsung  2011              s2
#          2020             s20
# htc      2011    Incredible S
#          2020         u12plus
# huawei   2011          Ascend
#          2020             p40

print('------------------------------')


print(pop_df)
#                      model  sales
# samsung 2011            s2     10
#         2020           s20     50
# htc     2011  Incredible S      5
#         2020       u12plus     15
# huawei  2011        Ascend      2
#         2020           p40     30
print('------------------------------')

# نفس النتيجة باستخدام dataframe
myarray = np.array([[6,9],[6,9],[6,9],[6,9]])
y = [['a', 'a','b','b'],[1,2,1,2]]
x= ['x','y']
df = pd.DataFrame(myarray, index=y, columns=x)
print(df)
#      x  y
# a 1  6  9
#   2  6  9
# b 1  6  9
#   2  6  9
print('------------------------------')

# نفس الامر 
data = {('samsung', 2011): 's2',('samsung', 2020):'s20',
        ('htc', 2011): 'Incredible S',('htc', 2020): 'u12plus',
        ('huawei', 2011): 'Ascend',('huawei', 2020): 'p40'}
df = pd.Series(data)

print(df)
# samsung  2011              s2
#          2020             s20
# htc      2011    Incredible S
#          2020         u12plus
# huawei   2011          Ascend
#          2020             p40
print('------------------------------')





































































