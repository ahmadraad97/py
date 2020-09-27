# 12 . Legend

# وهو الخاص بكتابة تفاصيل الرسم في مربع منفصل ولا بد ان يتم تحديد label   كل دالة اثناء عمل الـ plot
# يتم كتابة اسم الـ label  لكل دالة , ومنها يتم عمل الصندوق الخاص بها
import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(0, 20, 1000)
fig, ax = plt.subplots()
plt.axis('equal')
ax.plot(x, np.sin(x),  label='Sin')
ax.plot(x, np.cos(x), label='Cos')
leg = ax.legend()

# مكان الصندوق , وهل بخط ام لا
ax.legend(loc='upper left', frameon=False)



# تغيير المكان , وجعلها عمودين
ax.legend(frameon=False,
          loc='lower center', ncol=2)


# خصائص الصندوق
ax.legend(fancybox=True, # curvy or not
          framealpha=1, #1 for white,0 for black
          shadow=True, # shadow or not
          borderpad=1) #how big of box



# تحديد حجم الخط
ax.legend(fontsize=30)




# عمل صندوق لخطوط معينة
import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(0, 20, 1000)
fig, ax = plt.subplots()
plt.axis('equal')
 
y = np.sin(x[:, np.newaxis] + np.pi *
           np.arange(0, 2, 0.5))

lines = plt.plot(x, y)

# lines is a list of plt.Line2D instances
plt.legend(lines[:2], ['Cost', 'Time'])


