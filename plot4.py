# سمك الخط
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10,0.005)

plt.plot(x,x+0,'b-',linewidth = 1)
plt.plot(x,x+3,'b-',linewidth = 5)
plt.plot(x,x+6,'b-',linewidth = 11)
plt.plot(x,x+9,'b-',linewidth = 20)


# الوان الخطوط

x=np.arange(0,10,0.005)

plt.plot(x, x + 0, color = 'b')
plt.plot(x, x + 2, color = 'g')
plt.plot(x, x + 4, color = 'y')
plt.plot(x, x + 6, color = 'r')
plt.plot(x, x + 8, color = 'c')
plt.plot(x, x + 10, color = 'm')
plt.plot(x, x + 12, color = 'k')
plt.plot(x, x + 14, color = 'w')


# خطوط و نقاط

x=np.arange(0,10,0.5)

plt.plot(x, x + 10, '-o')


# شكل النقاط


x=np.arange(0,10,0.5)


plt.plot(x,x+6,'^')
plt.plot(x,x+9,'>')
plt.plot(x,x+12,'<')

plt.plot(x,x,',')
plt.plot(x,x+9,'.')

plt.plot(x,x+12,'*')
plt.plot(x,x+3,'+')

plt.plot(x,x+9,'|')
plt.plot(x,x+6,'_')

plt.plot(x,x+6,'o')
plt.plot(x,x+6,'v')
plt.plot(x,x+9,'s')
plt.plot(x,x+6,'P')
plt.plot(x,x+3,'p')
plt.plot(x,x+9,'h')
plt.plot(x,x+6,'x')
plt.plot(x,x+12,'d')


plt.plot(x,x+9,'1')
plt.plot(x,x+6,'2')
plt.plot(x,x+3,'3')
plt.plot(x,x,'4')
plt.plot(x,x+12,'8')



# الالوان مع شكل المارك
# ويمكن عكسها
x=np.arange(0,10,0.5)

plt.plot(x,x+12,'r*')
plt.plot(x,x+9,'gh')
plt.plot(x,x+6,'bx')
plt.plot(x,x+3,'y+')





























































































































































































