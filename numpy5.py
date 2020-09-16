from numpy import *
# مجموع قيم المصفوفة
a=arange(5)
print(a)
# [0 1 2 3 4]
print(add.reduce(a))
# 10


# حاصل ضرب قيم المصفوفة
a=arange(1,5)
print(a)
# [1 2 3 4]
print(multiply.reduce(a))
# 24


# عملية ضرب متبادلة
a=arange(1,5)
print(a)
# [1 2 3 4]
print(multiply.outer(a,a))
# [[ 1  2  3  4]
 # [ 2  4  6  8]
 # [ 3  6  9 12]
 # [ 4  8 12 16]]

# جمع كل الارقام السابقة غير فينوباتشي
a=arange(5)
print(a)
# [0 1 2 3 4]
print(add.accumulate(a))
# [ 0  1  3  6 10]


# ضرب الارقام السابقة
a=arange(1,5)
print(a)
# [1 2 3 4]
print(multiply.accumulate(a))
# [ 1  2  6 24]

# لمعرفة عدد عناصر المصفوفة , او عدد صفوفها لو اكتر من بعد
a=arange(6)
print(a)
# [0 1 2 3 4 5]
print(len(a))
# 6


c=a.reshape(2,3)
print(c)
# [[0 1 2]
 # [3 4 5]]
print(len(c))
# 2

# لمعرفة كل عدد عناصرها
a=arange(6)
print(a)
# [0 1 2 3 4 5]
print(a.size)
# 6

c=a.reshape(2,3)
print(c)
# [[0 1 2]
 # [3 4 5]]
print(a.size)
# 6

# و هنا الابعاد بالتفصيل
c=a.reshape(2,3)
print(c)
# [[0 1 2]
 # [3 4 5]]
print(c.shape)
# (2, 3)

# عدد ابعادها
a=arange(6)
print(a.ndim)
# 1

c=a.reshape(2,3)
print(c.ndim)
# 2

# نوع البيانات في المصفوفة
a=array(['dsa','hfr',5,15,89])
print(a.dtype)
# <U3

b=arange(8)
print(b.dtype)
# int32






























































