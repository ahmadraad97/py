# 11 . Imshow

# تستخدم لرسم مربعات بالوان تعبر عن الارقام بها 
# وهو شبيه بالامر كونتور , مع الفارق انه لا يوجد قيم x,y , ولكن نعطيه مصفوفة من بعدين
# , ويقوم برسمها بناء علي قيمتها , فالقيم العليا غامقة  , والدنيا فاتحة 
# تستخدم الأمر
# plt.imshow()
# حسب الرقم , الاصغر للفاتح و الاكبر للغامق
import matplotlib.pyplot as plt
I=  [[1,1,1,1,1,1,1],
     [1,2,2,2,2,2,1],
     [1,2,3,3,3,2,1],
     [1,2,3,4,3,2,1],
     [1,2,3,3,3,2,1],
     [1,2,2,2,2,2,1],
     [1,1,1,1,1,1,1]]
plt.imshow(I)
plt.colorbar()


# يتم تغيير الباقة
import matplotlib.pyplot as plt
plt.style.use('classic')
I=  [[1,1,1,1,1,1,1],
     [1,2,2,2,2,2,1],
     [1,2,3,3,3,2,1],
     [1,2,3,4,3,2,1],
     [1,2,3,3,3,2,1],
     [1,2,2,2,2,2,1],
     [1,1,1,1,1,1,1]]
plt.imshow(I)
plt.colorbar()





# لو تم عكس الارقام
import matplotlib.pyplot as plt
plt.style.use('classic')
I=  [[4,4,4,4,4,4,4],
     [4,3,3,3,3,3,4],
     [4,3,2,2,2,3,4],
     [4,3,2,1,2,3,4],
     [4,3,2,2,2,3,4],
     [4,3,3,3,3,3,4],
     [4,4,4,4,4,4,4]]


plt.imshow(I)
plt.colorbar()




# تحديد باقة الالوان من داخل الامر
import matplotlib.pyplot as plt
I=  [[1,1,1,1,1,1,1],
     [1,2,2,2,2,2,1],
     [1,2,3,3,3,2,1],
     [1,2,3,4,3,2,1],
     [1,2,3,3,3,2,1],
     [1,2,2,2,2,2,1],
     [1,1,1,1,1,1,1]]
plt.imshow(I, cmap='gray');
plt.colorbar()






# ارقام معكوسة و باقة الازرق
import matplotlib.pyplot as plt
I=  [[4,4,4,4,4,4,4],
     [4,3,3,3,3,3,4],
     [4,3,2,2,2,3,4],
     [4,3,2,1,2,3,4],
     [4,3,2,2,2,3,4],
     [4,3,3,3,3,3,4],
     [4,4,4,4,4,4,4]]


plt.imshow(I, cmap='Blues')
plt.colorbar()




# دالة غريبة و باقة مختلفة
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 1000)
I = np.cos(x) * np.sin(x[:, np.newaxis])


plt.imshow(I, cmap='Accent')
plt.colorbar()




# تأثير النقاط علي الرسم
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 1000)
I = np.cos(x) * np.sin(x[:, np.newaxis])

speckles = (np.random.random(I.shape) < 0.01)

I[speckles] = np.random.normal(0, 3, 
             np.count_nonzero(speckles))

plt.figure(figsize=(10, 3.5))
plt.imshow(I, cmap='RdBu')
plt.colorbar()
plt.clim(-1, 1)







# دالة مختلفة
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np

x = np.linspace(0, 10, 1000)
I = np.sin(x) * np.cos(x[:, np.newaxis])
plt.imshow(I)
plt.colorbar()

