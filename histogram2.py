# بطريقة اخرى
import numpy as np
import matplotlib.pyplot as plt


x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)


kwargs = dict(histtype='stepfilled',
              alpha=0.6, normed=True,
              bins=40)
 
plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs);


# الأمر  hist2d  خاص بمدي ترابط النقاط المتقاطعة(كلما كان العددين قريبين من بعض كان اللون اغمق)
x = np.random.rand(20)
y = np.random.rand(20)

print(x)
print('===================')
print(y)

plt.hist2d(x, y)


# اعداد اكبر
x = np.random.rand(200)
y = np.random.rand(200)
plt.hist2d(x, y)


# الالوان
x = np.random.rand(200)
y = np.random.rand(200)

plt.hist2d(x, y, cmap='Reds')


# عدد النقاط(عدد المربعات بالطول والعرض)
x = np.random.rand(200)
y = np.random.rand(200)

plt.hist2d(x, y, cmap='Blues', bins=30)


# قائمة الالوان
x = np.random.rand(200)
y = np.random.rand(200)

plt.hist2d(x, y, cmap='Blues', bins=30)
plt.colorbar()


# اسم قائمة الالوان 
x = np.random.rand(200)
y = np.random.rand(200)

plt.hist2d(x, y, cmap='Blues', bins=30)
a = plt.colorbar()
a.set_label('counts in bin')


# أمر  hexbin    مشابه لكن بخلايا مسدسة 
x = np.random.rand(200)
y = np.random.rand(200)

plt.hexbin(x, y, gridsize=30, cmap='Blues')
a = plt.colorbar()
a.set_label('counts in bin')


# معادلة
x = np.random.rand(200)
y= x**(1/3)

plt.hist2d(x, y, bins=30, cmap='Blues')
plt.colorbar()


# التوزيع الطبيعي
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T

plt.hist2d(x, y, bins=30, cmap='Blues')
plt.colorbar()


# باستخدام امر hexbin
plt.style.use('seaborn-white') 

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T

plt.hexbin(x, y, gridsize=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')























