import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# زاوية الرؤية بشكل مفصل :
    
fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.1) # X Value
Y = np.arange(-4,4,0.1) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value

ax.plot_surface(X,Y,Z,cmap ='hot')
ax.view_init(30, 30)

# view_init عبارة عن شقين 


# الشق الاول elev :
# عبارة عن هيلوكبتر يطير بشكل دائري فوق الشكل 


#     الشق الثاني  azim :
# عبارة عن شخص يدور حول الشكل على الارض (سيارة حول الدوار)










