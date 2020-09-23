
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# تغيير الخطوة  0.25=>0.01
fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.01) # X Value
Y = np.arange(-4,4,0.01) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value

ax.plot_surface(X,Y,Z, cmap ='hot') # Color
               
plt.show()



# تغيير الخطوة  0.25=>1 
# max=1
fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,1) # X Value
Y = np.arange(-4,4,1) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value

ax.plot_surface(X,Y,Z, cmap ='hot') # Color
plt.show()


# تغيير ابعاد x  عن  y 
fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-10,10,0.1) # X Value
Y = np.arange(-5,5,0.1) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value

ax.plot_surface(X,Y,Z, cmap ='Blues') # Color
          
plt.show()


# لون الحواف 

fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-10,10,0.1) # X Value
Y = np.arange(-5,5,0.1) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value

ax.plot_surface(X,Y,Z, cmap ='Reds',edgecolor='Gray',alpha=0.8) # Color
