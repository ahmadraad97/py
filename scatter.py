
import matplotlib.pyplot as plt
import numpy as np

x=np.random.rand(500)
y=np.random.rand(500) 
plt.scatter(x,y)


# التوزيع الطبيعي
x=np.random.normal(0,1,1000)
y=np.random.normal(0,1,1000)
plt.scatter(x,y)


# اللون : بنفس عدد العناصر
x=np.random.normal(0,1,1000)
y=np.random.normal(0,1,1000)
z=np.random.normal(0,1,1000) 
plt.scatter(x,y,c=z)


# الحجم
x=np.random.normal(0,1,1000)
y=np.random.normal(0,1,1000)
z=np.random.normal(0,1,1000)
w=50*np.random.normal(0,1,1000) 

plt.scatter(x,y,s=w,c=z)


# مثال 
x=[1,2,3,4,5,6,7,8,9,10]
y=[4,7,8,3,0,5,9,4,1,9]
w=[600,900,800,700,400,200,300,100,600,300]
z=[7,5,6,9,8,5,6,3,2,1]
plt.scatter(x,y,s=w,c=z)
plt.show()


# الشفافية
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
cl = rng.rand(100)
sz = 1000 * rng.rand(100)
plt.scatter(x, y,c=cl,s=sz,alpha=0.3)

plt.show()


# عمود الالوان
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
cl = rng.rand(100)
sz = 1000 * rng.rand(100)
plt.scatter(x, y,c=cl,s=sz,alpha=0.3)
plt.colorbar()
plt.show()

 
    
       
    
  

























































































