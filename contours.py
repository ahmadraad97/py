# 7 . Contour
# يعمل رسم كانه ثلاثي الابعاد , ويقوم بايثون برسم خطوط الحدود
# نعطيه قيم x وy , ثم z الارتفاع 
# ويجب z مصفوفة ثناية الابعاد,وتكون صفوفها نفس قيم x واعمدتها نفس قيم y , والذي يقوم علي اساسها برسم الحدود
plt.contour(X, Y, Z, colors='red')


import matplotlib.pyplot as plt
import numpy as np




# مثال بسيط
X = [1,2,3,4,5,6,7]
Y = [1,2,3,4,5,6,7]
Z = [[1,1,1,1,1,1,1],
     [1,2,2,2,2,2,1],
     [1,2,3,3,3,2,1],
     [1,2,3,4,3,2,1],
     [1,2,3,3,3,2,1],
     [1,2,2,2,2,2,1],
     [1,1,1,1,1,1,1]]
plt.contour(X, Y, Z, colors='red')


# قيم عشوائية
X = np.random.randint(1,10,6)
Y = np.random.randint(1,10,6)
Z = np.random.randint(1,10,36)
ZZ = np.reshape(Z,(6,6))

plt.contour(X, Y, ZZ, colors='red')


# تطبيق متداخل
def f(x, y):
    e = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
    return e

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contour(X, Y, Z, colors='red')


# كثافة الخطوط
plt.contour(X, Y, Z, 20, colors='b')

# تدريج الالوان
plt.contour(X, Y, Z, 20 , cmap='RdGy')


# الامر   contourf  يقوم بعمل ملئ fill   للخطوط البينية
plt.contourf(X, Y, Z, 20 , cmap='RdGy')


# عمود الالوان
plt.colorbar()


# تفاصيل هامة علي الرسم
contours = plt.contour(X, Y, Z, 3,colors='black')
plt.clabel(contours, inline=True, fontsize=8)
plt.imshow(Z, extent=[0, 5, 0, 5],cmap='RdGy',alpha=0.5)


# ألوان دون خطوط
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='jet')
#C = plt.contour(X,Y,f(X,Y),8,colors='b')


# خطوط دون ألوان
#pl.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='jet')
C = plt.contour(X,Y,f(X,Y),8,colors='b')


# ألوان و خطوط
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='jet')
C = plt.contour(X,Y,f(X,Y),8,colors='b')















































































































