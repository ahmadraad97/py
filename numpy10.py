# التعامل مع Polynomials
from numpy import *
import numpy as np
# الدرجة الأولي
poly= np.polynomial.Polynomial

x=np.array([0,-20,30,40,50,60,70,80,90])
y=np.array([10,9,8,7,6,5,4,3,2])

point,a=poly.fit(x,y,1,full=True)
print(point)
# poly([ 6.36129032 -4.18064516])


# كتابة الـ Poly
a=np.poly1d((-5))
print(a)
# -5

b=poly1d((4,2))
print(b)
# 4 x + 2

print(poly1d((9,2,-5)))
#    2
# 9 x + 2 x - 5
print(poly1d((9,2,-5,0)))
   # 3     2
# 9 x + 2 x - 5 x


# التعويض
a=poly1d((9,2,-5))
#    2
# 9 x + 2 x - 5

print(a(2))
# 35

print(a(0))
# -5

# معادلة مع قيمتها
a = polyval((1,2),2)
b = polyval((1,2,3),7)
c = polyval((1,2,3,5),-3)
d = polyval((1,2,3,5,-6),12.6)

print(a)
# 4
print('-------------------------')
print(b)
# 66
print('-------------------------')
print(c)
# -13
print('-------------------------')
print(d)
# 29738.769599999992


# اشتقاق المعادلة
a =polyder(poly1d((1,2,3)))
b =polyder(poly1d((1,2,3)),2)
c =polyder(poly1d((1,2,3)),3)

print(a)
# 2 x + 2
print('-------------------------')
print(b)
# 2
print('-------------------------')
print(c)
# 0

# التعويض في الاشتقاق
a =polyder(poly1d((1,2,3)))
b =polyder(poly1d((1,2,3)),2)
c =polyder(poly1d((1,2,3)),3)

print(a(3))
# 8
print('-------------------------')
print(b(0))
# 2
print('-------------------------')
print(c(-1))
# 0.0



# التكامل
a =polyint(poly1d((1,2,3)))
b =polyint(poly1d((1,2,3)),2)
c =polyint(poly1d((1,2,3)),3)

print(a)
#         3     2
# 0.3333 x + 1 x + 3 x
print('-------------------------')
print(b)
#          4          3       2
# 0.08333 x + 0.3333 x + 1.5 x
print('-------------------------')
print(c)
#          5           4       3
# 0.01667 x + 0.08333 x + 0.5 x
print('-------------------------')

# التعويض في التكامل
a =polyint(poly1d((1,2,3)))
b =polyint(poly1d((1,2,3)),2)
c =polyint(poly1d((1,2,3)),3)

print(a(2))
# 12.666666666666666
print('-------------------------')
print(b(0))
# 0.0
print('-------------------------')
print(c(3))
# 24.300000000000004
print('-------------------------')


# جذور المعادلة (حلها)
a =roots(poly1d((1,2)))
b =roots(poly1d((1,2,3)))
c =roots(poly1d((1,2,3,5)))
d =roots(poly1d((1,2,3,5,12)))

print(a)
# [-2.]
print('-------------------------')
print(b)
# [-1.+1.41421356j -1.-1.41421356j]
print('-------------------------')
print(c)
# [-1.84373428+0.j         -0.07813286+1.64492638j -0.07813286-1.64492638j]
print('-------------------------')
print(d)
# [-1.61635728+1.15083694j -1.61635728-1.15083694j  0.61635728+1.63342631j
#   0.61635728-1.63342631j]
print('-------------------------')



# توافق النقاط
x = array([3,6,2,5,4])
y = array([2,3,-9,6,2.5])
z = polyfit(x, y, 2)

print(x)
# [3 6 2 5 4]
print('-------------------------')
print(y)
# [ 2.   3.  -9.   6.   2.5]
print('-------------------------')
print(z)
# [ -1.78571429  17.08571429 -35.3       ]
print('-------------------------')
























































