# بيانات متداخلة

import pandas as pd
import numpy  as np

date = pd.MultiIndex.from_product([[2020, 2019,2018],["des", "mar"]],
                                   names=['year', 'mounth'])

company = pd.MultiIndex.from_product([['Samsung', 'LG', 'Xiaomi'],
                                      ['Mombile', 'Laptop','TV']],
                                    names=['company', 'type'])
data = np.array([[3,9,8,5,4,6,9,7,5],[6,9,8,5,4,6,9,7,5],[4,9,8,5,4,6,9,7,5],[6,9,8,5,4,6,9,7,5],[6,9,8,5,4,6,9,7,5],[6,9,8,5,4,6,9,7,5]])
salse_data = pd.DataFrame(data, index=date, columns=company)
print(salse_data)
# company     Samsung                LG            Xiaomi          
# type        Mombile Laptop TV Mombile Laptop TV Mombile Laptop TV
# year mounth                                                      
# 2020 des          3      9  8       5      4  6       9      7  5
#      mar          6      9  8       5      4  6       9      7  5
# 2019 des          4      9  8       5      4  6       9      7  5
#      mar          6      9  8       5      4  6       9      7  5
# 2018 des          6      9  8       5      4  6       9      7  5
#      mar          6      9  8       5      4  6       9      7  5

# اختيارات محددة
print(salse_data['Samsung', 'Mombile'])
# year  mounth
# 2020  des       6
#       mar       6
# 2019  des       6
#       mar       6
# 2018  des       6
#       mar       6


# تحديد بيانات
print(salse_data.loc[:, ('Samsung', 'Mombile')])
# year  mounth
# 2020  des       3
#       mar       6
# 2019  des       4
#       mar       6
# 2018  des       6
#       mar       6
print(salse_data.loc[2020, ('Samsung', 'Mombile')])
# mounth
# des    3
# mar    6



# اقتطاع شريحة
idx = pd.IndexSlice
print(salse_data.loc[idx[:, "des"], idx[:, 'Mombile']])
# Samsung  Mombile    4
# LG       Mombile    5
# Xiaomi   Mombile    9
# Name: (2019, des), dtype: int32

print(salse_data.loc[idx[2019, "des"], idx['Samsung', 'Mombile']])
# 4


print(salse_data.loc[idx[2019, "des"], idx['Samsung']])
# type
# Mombile    4
# Laptop     9
# TV         8

