# 14 . Limits

# ابعاد الشكل  وهي تقوم بتعيين ابعاد المربع الذي يظهر فيه الشكل و تكون بالامر :  

# set_xlim
# set_ylim 

# قبل التحديد
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10) 
ax = plt.axes()
plt.plot(x,-x**2  )


# بعد التحديد
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10) 
ax = plt.axes()
ax.set_xlim(-20,20)
ax.set_ylim(-20,20)
plt.plot(x,-x**2  )



# امر اخر
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10) 

plt.axis([-20,10,-10,20])
#X start , X end , Y start , Y end
plt.plot(x,-x**2  )


# أمر اخر
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10) 
ax = plt.axes()
ax.set(xlim=(-5, 10), ylim=(-20, 20) )
plt.plot(x,-x**2  )



# لجعل الخطوة في xو y متساوية
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10) 

plt.axis('equal')
plt.plot(x,-x**2  )


# بالأمر set_visible  يتم تحديد اذا ما كانت المحاور مرئية او مختفية
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10) 

ax = plt.axes()

ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

plt.plot(x,-x**2  )
