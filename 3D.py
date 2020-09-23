# 8 . 3D
#  هي الاداة الاكثر اهمية لرسم رسوم ثلاثية الابعاد
#  غالبا  ما نستخدمها مع مكتبة numpy  او pandas  لرسم البيانات الناتجة منهما 

#  يتم استدعائها بالأمر :
# mpl_toolkits.mplot3d 
# لرسم الفراغ المجسم
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = plt.axes(projection='3d')


# أمر plot_surface 
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.25) # X Value
Y = np.arange(-4,4,0.25) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value

ax.plot_surface(X,Y,Z) # Draw them
plt.show()


# عمل اسماء للمحاور
ax.set_xlabel('Time')
ax.set_ylabel('Work')
ax.set_zlabel('Efficiency')
plt.show()



# باقات الألوان
ax.plot_surface(X,Y,Z,cmap ='hot') # Color





