# Vlines, Hlines

# خط رأسي

import matplotlib.pyplot as plt
plt.vlines(0,-1,1,lw=5, color='r')
# value of X then Y start then Y end




# خصائص
plt.vlines(-2,-5,5,lw=5, color='r')
plt.vlines(-1,-4,4,lw=10, color='g')
plt.vlines(0,-3,3,lw=15, color='b')
plt.vlines(1,-2,2,lw=20, color='y')
plt.vlines(2,-1,1,lw=25, color='black')




# العديد منهم
w =[-1.5,-1,-.5,0,.5,1,1.5]
plt.vlines(w,-1,1,lw=10, color='r')
# X as list

# ----------------------------------------------

w =[-1.5,-1,-.5,0,.5,1,1.5]
plt.hlines(w,-1,1,lw=10, color='b')






# مثال
import matplotlib.pyplot as plt

plt.hlines(-3,-1,1,lw=10, color='w')
plt.hlines(-2,-1,1,lw=10, color='b')
plt.hlines(-1,0,1,lw=10, color='b')
plt.hlines(1,0,1,lw=10, color='b')
plt.hlines(2,-1,1,lw=10, color='b')
plt.hlines(3,-1,1,lw=10, color='w')


plt.vlines(-2.5,-1,1,lw=10, color='w')
plt.vlines(-1,-2,2,lw=10, color='r')
plt.vlines(0,-1,1,lw=10, color='r')
plt.vlines(1,1,2,lw=10, color='r')
plt.vlines(1,-2,-1,lw=10, color='r')
plt.vlines(2.5,-1,1,lw=10, color='w')

