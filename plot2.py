# 2 . Plot
import matplotlib.pyplot as plt
# يستخدم للرسم البياني , للخطوط والمنحنيات , علي ان تكون من بعدين 

# رسم بياني تقليدي
a = ( 1,2,3,6,5,8,7,4)
plt.plot(a)


# لو اخدت 2 ليست , فسيتم رسمها اكس و واي لا تعمل مع set
import matplotlib.pyplot as plt
a = [1,2,3,4,5,6]
b =  [1,2,3,4,5,6]
plt.plot(a,b)



# تغيير الستايل
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
plt.plot(a,b)



# دالة الـ   sin 
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
plt.style.use ('ggplot')

x = np.linspace(0, 360) 
y = np.sin(x*pi/180)
plt.plot(x, y)



# دالة الـ cos  
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
plt.style.use ('ggplot')

x = np.linspace(0, 360) 
y = np.cos(x*pi/180)
plt.plot(x, y)


# تحديد اسماء المحاور
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
plt.ylabel(0)
plt.xlabel(1)
plt.plot(a,b)


# بطريقة اخري
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
ax = plt.axes()
ax.set_xlabel('Time')
ax.set_ylabel('Work')

plt.plot(a,b)


# بطريقة اخري
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
ax = plt.axes()

ax.set(xlabel='Time', ylabel='Work' )

plt.plot(a,b)


# تحديد شكل التقاء النقاط
# لا يعمل مع جميع الاحرف والارقام
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
ax = plt.axes()

ax.set(xlabel='Time', ylabel='Work' )
plt.plot(a,b,marker='o')

plt.plot(a,b,marker=1)





































































































































