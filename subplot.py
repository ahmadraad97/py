# 9 . Subplot
# وهي الأداة التي تسمح لنا بعمل اكثر من شكل في نفس الرسم 

# وتكون عبر اعطاء امر plt.subplot  ثلاث قيم:
# الاولى والثانية , هي صفوف و اعمدة مصفوفة الرسومات الثالث هو ترتيب الرسم
# plt.subplot(2,2,4)
# يليها كتابة plt.plot  و تفاصيل الدالة


# مثال
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,100)
y = 3*x
plt.subplot(1,2,1)
plt.plot(x,y,c='r')


# رسم الشكل الثاني
x = np.linspace(0,100)

plt.subplot(1,2,1)
y = 3*x
plt.plot(x,y,c='r')

plt.subplot(1,2,2)
y = -3*x
plt.plot(x,y,c='g')


# مثال خطأ لن يتم استخدامه
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,100)

plt.subplot(1,2,1)
y = 3*x
plt.plot(x,y,c='r')

plt.subplot(1,2,2)
y = -3*x
plt.plot(x,y,c='g')

plt.subplot(1,2,3)
y = 12*x
plt.plot(x,y)


# مثال
x = np.linspace(0,100)

plt.subplot(2,1,1)
y = 3*x
plt.plot(x,y,c='r')

plt.subplot(2,1,2)
y = -3*x
plt.plot(x,y,c='g')


# مثال
x = np.linspace(0,100)

plt.subplot(2,2,1)
y = 3*x
plt.plot(x,y,c='r')

plt.subplot(2,2,2)
y = -3*x
plt.plot(x,y,c='g')

plt.subplot(2,2,3)
y = x**2
plt.plot(x,y,c='b')

plt.subplot(2,2,4)
y =  x**0.5
plt.plot(x,y,c='r')


# يمكن كتابة الرقم بفواصل او بدون
x = np.linspace(0,100)

plt.subplot(221)
y = 3*x
plt.plot(x,y,c='r')

plt.subplot(222)
y = -3*x
plt.plot(x,y,c='g')

plt.subplot(2,2,3)
y = x**2
plt.plot(x,y,c='b')

plt.subplot(2,2,4)
y =  x**0.5
plt.plot(x,y,c='r')


# شكل مختلف للامر
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,100)

fig, ax = plt.subplots(5)
ax[0].plot(x,3*x)
ax[1].plot(x,-x/400)
ax[2].plot(x,300*(0.002*x+3))
ax[3].plot(x,np.sin(x))
ax[4].plot(x,x**0.1)


# الابعاد و المسافات بين الجرافات
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,100)

plt.subplot(221)
y = 3*x
plt.plot(x,y,c='r')
plt.subplot(222)
y = -3*x
plt.plot(x,y,c='g')
plt.subplot(2,2,3)
y = x**2
plt.plot(x,y,c='b')
plt.subplot(2,2,4)
y =  x**0.5
plt.plot(x,y,c='r')

plt.subplots_adjust(left=0,right=1.5
                    ,bottom=0,top=1.5
                    ,wspace=0,hspace=0)


# تغيير الابعاد
x = np.linspace(0,100)

plt.subplot(221)
y = 3*x
plt.plot(x,y,c='r')
plt.subplot(222)
y = -3*x
plt.plot(x,y,c='g')
plt.subplot(2,2,3)
y = x**2
plt.plot(x,y,c='b')
plt.subplot(2,2,4)
y =  x**0.5
plt.plot(x,y,c='r')

plt.subplots_adjust(left=1,right=1.5
                    ,bottom=0,top=1.8
                    ,wspace=0,hspace=0)


# العكس
x = np.linspace(0,100)

plt.subplot(221)
y = 3*x
plt.plot(x,y,c='r')
plt.subplot(222)
y = -3*x
plt.plot(x,y,c='g')
plt.subplot(2,2,3)
y = x**2
plt.plot(x,y,c='b')
plt.subplot(2,2,4)
y =  x**0.5
plt.plot(x,y,c='r')

plt.subplots_adjust(left=0,right=1.5
                    ,bottom=1,top=1.5
                    ,wspace=0,hspace=0)


