# مكتبة سيبورن  Seaborn


# وهي مشابهة لماتبلوتليب  , خاصة في الرسوم
import seaborn as sns

# أمر kdeplot  لو اخد الـ data  كلها يرسمها كونتور
import pandas as pd
import numpy as np
import seaborn as sns

data =np.random.multivariate_normal([0,0],[[5,2],[2,2]],size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

sns.kdeplot(data)


# ولو أخذ الـ data  علي مرحلتين يرسمها كالتوزيع الطبيعي
import pandas as pd
import numpy as np
import seaborn as sns

data =np.random.multivariate_normal([0,0],[[5,2],[2,2]],size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

for col in 'xy':
    sns.kdeplot(data[col], shade=True)
 
# نفس الأمر لكن مع إلغاء الـ shade
for col in 'xy':
    sns.kdeplot(data[col], shade=False)



# أمر distplot  لعمل خطوط رأسية في الرسم
data =np.random.multivariate_normal([0,0],[[5,2],[2,2]],size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

for col in 'xy':
    sns.kdeplot(data[col], shade=True)

sns.distplot(data['x'])
sns.distplot(data['y'])



# أمر joinplot
data =np.random.multivariate_normal([0,0],[[5,2],[2,2]],size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='kde')



# ولو تم تحويل الـ kind  لنوعية : hex   
with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='hex')


