# حجم المارك
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('dark_background')
ax = plt.axes()

ax.set(xlabel='Time', ylabel='Work' )
plt.plot(a,b,marker='o',markersize=20)


# تحديد لون الخط
plt.plot(a,b,color='blue',marker='o',markersize=11)


# طرق كتابة اللون

plt.plot(a,b,color='blue',marker='o',markersize=11) #color name
plt.plot(a,b,color='g',marker='o',markersize=11) #color litter
plt.plot(a,b,color='0.75',marker='o',markersize=11) # its degree from B&W
plt.plot(a,b,color='#FFDD44',marker='o',markersize=11) # its code
plt.plot(a,b,color=(1.0,0.2,0.3),marker='o',markersize=11) #its RGB degrees
plt.plot(a,b,color='chartreuse',marker='o',markersize=11) #its name in html



# عنوانه
# 1
plt.title('time/work consumption')
# 2
ax.set_title('time/work consumption')
# 3
ax.set(title='time/work consumption')




# دالة مركبة
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10,0.005)
y = np.exp(-x/2) * np.sin(2*np.pi*x)
plt.plot (x,y)


# رسم دالتين معا
import matplotlib.pyplot as plt
import numpy as np

def p1(x):  return x**4 - 4*x**2 + 3*x
def p2(x):  return np.sin(10*x)*10
x = np.linspace(-3,3,1000)
plt.plot(x,p1(x),x,p2(x))


# نوع الخط المستخدم
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10,0.005)

plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='-')

plt.plot(x, x + 4, linestyle='dashed')
plt.plot(x, x + 5, linestyle='--')

plt.plot(x, x + 8, linestyle='dashdot')
plt.plot(x, x + 9, linestyle='-.')

plt.plot(x, x + 12, linestyle='dotted')
plt.plot(x, x + 13, linestyle=':')


# لون و ستايل الخط
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10,0.005)

plt.plot(x,x+0,'b--')
plt.plot(x,x+3,'g-')
plt.plot(x,x+6,'r-.')
plt.plot(x,x+9,'y:')


