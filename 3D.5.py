# جزء محدد
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
r = np.linspace(0, 6, 20)
theta = np.linspace(-0.9*np.pi,0.8*np.pi, 40)
r, theta = np.meshgrid(r, theta)
X = r * np.sin(theta)
Y = r * np.cos(theta)
Z = f(X, Y)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z,cmap='Reds')
# الباقي من العدد العشري السالب هو المقطوع
# الباقي من العدد العشري الموجب هو المقطوع
# 1 الموجب يمثل نصف الشكل و 1 السالب يمثل النصف الثاني(1,-1)




# أمر   trisurf
# يجعل الشكل مجعد
fig = plt.figure()

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
 
theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = r * np.sin(theta)
y = r * np.cos(theta)
z = f(x, y)

ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z,cmap='viridis')


# أمر contour3D   مشابه لأمر  3D  الي حد ما مع فارق انه يرسم خطوط كونتور وليس مجسم

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='Blues')


# زيادة الارقام

ax.contour3D(X, Y, Z, 500, cmap='Blues')


# تقليل الارقام
ax.contour3D(X, Y, Z, 10, cmap='Blues')


# تغيير الدالة
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()

def f(x, y):
    return np.cos(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 120, cmap='Blues')


# دالة اخري
def f(x, y):
    return -(x**(2))
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 180, cmap='Blues')


# أمر plot_wireframe    يقوم بعمل رسم شبيه بالشبكة
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()

def f(x, y):
    return np.cos(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-6, 6, 20)
y = np.linspace(-6, 6, 20)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_wireframe(X, Y, Z, cmap='Blues')


# أمر plot_surface بيعمل رسم للاسطح وليس اسلاك
ax.plot_surface(X, Y, Z)


# تغيير لون الخط
ax.plot_surface(X, Y, Z, edgecolor='w')


# أمر scatter   يقوم بعمل نقاط بدل الخطوط
ax.scatter(X, Y, Z)

