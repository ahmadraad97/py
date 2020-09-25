# المسافات الراسية
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
                    ,wspace=0.5,hspace=0)


# المسافات الافقية
plt.subplots_adjust(left=0,right=1.5
                    ,bottom=0,top=1.5
                    ,wspace=0,hspace=0.9)




# المسافتين 
plt.subplots_adjust(left=0,right=1.5
                    ,bottom=0,top=1.5
                    ,wspace=0.3,hspace=0.9)


# كتابة نص في المربعات
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i))
    ,fontsize=18, ha='center')



# محور x مشترك
fig, ax = plt.subplots(2, 3, sharex='col')



# محور y مشترك
import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 3, sharey='row')


# المحورين مشتركين
import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 3, sharex ='col' ,sharey='row')


# تحديد اكثر من جراف و تعيين الاماكن
import matplotlib.pyplot as plt

grid = plt.GridSpec(2, 3)
plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1:])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2])




# قيم مختلفة
grid = plt.GridSpec(3, 5)
plt.subplot(grid[0, :1])
plt.subplot(grid[0, 1])
plt.subplot(grid[0, 2:])
plt.subplot(grid[1, :])
plt.subplot(grid[2, :4])
plt.subplot(grid[2, 4])


# محاور دائرية
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
r = np.arange(0,1,0.001)
theta = np.pi*r*4
line, = ax.plot(theta, r, color='r', lw=3)



# مثال

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
r = np.arange(0,1,0.001)
theta = np.pi*r*25
line, = ax.plot(theta, r, color='r', lw=3)


# مثال

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
r = np.arange(0,1,0.001)
theta = np.tan(r*2)
line, = ax.plot(theta, r, color='r', lw=3)


