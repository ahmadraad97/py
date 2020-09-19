# التعامل مع التواريخ
import pandas as pd

x = pd.to_datetime("4th of July, 2018")
 
print(x)

print('-------------------------')


# زيادة ايام
import pandas as pd
import numpy as np
x = pd.to_datetime("4th of July, 2018")
 
y = x + pd.to_timedelta(np.arange(20),'D')

print(x)
# 2018-07-04 00:00:00
print('-------------------------')
print(y)
# DatetimeIndex(['2018-07-04', '2018-07-05', '2018-07-06', '2018-07-07',
#                '2018-07-08', '2018-07-09', '2018-07-10', '2018-07-11',
#                '2018-07-12', '2018-07-13', '2018-07-14', '2018-07-15',
#                '2018-07-16', '2018-07-17', '2018-07-18', '2018-07-19',
#                '2018-07-20', '2018-07-21', '2018-07-22', '2018-07-23'],
print('-------------------------')


# نقص ايام
import numpy as np
x = pd.to_datetime("4th of July, 2018")
 
y = x - pd.to_timedelta(np.arange(20),'D')

print(x)
# 2018-07-04 00:00:00
print('-------------------------')
print(y)
# DatetimeIndex(['2018-07-04', '2018-07-03', '2018-07-02', '2018-07-01',
#                '2018-06-30', '2018-06-29', '2018-06-28', '2018-06-27',
#                '2018-06-26', '2018-06-25', '2018-06-24', '2018-06-23',
#                '2018-06-22', '2018-06-21', '2018-06-20', '2018-06-19',
#                '2018-06-18', '2018-06-17', '2018-06-16', '2018-06-15'],
print('-------------------------')


# سلسلة ايام
import pandas as pd


index = pd.DatetimeIndex(['2020-08-05', '2019-08-07',
                          '2018-08-18','2017-08-23'])

data = pd.Series(['note20', 'note10', 'note9', 'note8'], index=index)

print(data)
# 2020-08-05    note20
# 2019-08-07    note10
# 2018-08-18     note9
# 2017-08-23     note8
print('-------------------------')


# ايام محددة
print(data['2020-12-31':'2019-01-01'])
# 2020-08-05    note20
# 2019-08-07    note10

print('-------------------------')


# سنة محددة  
print(data['2020'])
# 2020-08-05    note20
print('-------------------------')


# شهر محدد  
print(data['2018-08'])
# 2018-08-18    note9
print('-------------------------')


# من كذا لكذا  
data = pd.date_range('2020-08-05', '2018-08-18')
print(data)
# 2020-08-05    note20
# 2019-08-07    note10

print('-------------------------')


# عدد من الايام  
data = pd.date_range('2011-12-25', periods=10)
print(data)
# DatetimeIndex(['2011-12-25', '2011-12-26', '2011-12-27', '2011-12-28',
#                '2011-12-29', '2011-12-30', '2011-12-31', '2012-01-01',
#                '2012-01-02', '2012-01-03'],
#               dtype='datetime64[ns]', freq='D')
print('-------------------------')


# عدد من الساعات  
data = pd.date_range('2011-12-25', periods=3, freq='S')
print(data)
# DatetimeIndex(['2011-12-25 00:00:00', '2011-12-25 00:00:01',
#                '2011-12-25 00:00:02'],
#               dtype='datetime64[ns]', freq='S')
print('-------------------------')
data = pd.date_range('2011-12-25', periods=3, freq='H')
print(data)
# DatetimeIndex(['2011-12-25 00:00:00', '2011-12-25 01:00:00',
#                '2011-12-25 02:00:00'],
#               dtype='datetime64[ns]', freq='H')
print('-------------------------')
data = pd.date_range('2011-12-25', periods=3, freq='M')
print(data)
# DatetimeIndex(['2011-12-31', '2012-01-31', '2012-02-29'], dtype='datetime64[ns]', freq='M')
print('-------------------------')


# اربع ساعات  
data = pd.timedelta_range(0, periods=4, freq='H')
print(data)
# TimedeltaIndex(['0 days 00:00:00', '0 days 01:00:00', '0 days 02:00:00',
#                 '0 days 03:00:00'],

print('-------------------------')


# خطوات بالساعة و الدقيقة والثانية  
data = pd.timedelta_range(0, periods=4, freq="2H30T40S")
print(data)
# TimedeltaIndex(['0 days 00:00:00', '0 days 02:30:40', '0 days 05:01:20',
#                 '0 days 07:32:00'],

print('-------------------------')


# أيام العمل Business Days  
from pandas.tseries.offsets import BDay

data = pd.date_range('2020-09-19', periods=5, freq=BDay())
print(data)
# DatetimeIndex(['2020-09-21', '2020-09-22', '2020-09-23', '2020-09-24',
#                '2020-09-25'],
#               dtype='datetime64[ns]', freq='B')
print('-------------------------')






























































































































