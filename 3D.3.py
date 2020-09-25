import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# تحديد ابعاد   z   الاقصي و الادني
# عند التغيير الى عدد كسري يمط والى عدد صحيح يصغر 

fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.1) # X Value
Y = np.arange(-4,4,0.1) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value

ax.plot_surface(X,Y,Z,cmap ='hot')

ax.set_zlim(-0.5,0.5)
plt.show()


# زاوية الرؤية
ax.view_init(-50, 26)
plt.show()


# أمر   plot3d 
fig = plt.figure()
 
ax = plt.axes(projection='3d')
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'b')


# أمر scatter3D  
fig = plt.figure()
ax = plt.axes(projection='3d')
z = 15 * np.random.random(500)
x =np.sin(z)+0.1*np.random.randn(500)
y =np.cos(z)+0.1*np.random.randn(500)
ax.scatter3D(x,y,z,c=z,cmap='Reds')


# الاثنين معا
fig = plt.figure()

ax = plt.axes(projection='3d')
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'b')

z= 15 * np.random.random(100)
x= np.sin(z) + 0.1 * np.random.randn(100)
y= np.cos(z) + 0.1 * np.random.randn(100)
ax.scatter3D(x,y,z,c=z,cmap='Reds')




