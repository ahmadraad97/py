# الدوال المثلثية مشكلتها انها تتعامل بالـ radians  و ليس الـ degree
from numpy import *
a=sin(30)
b=cos(30)
c=tan(30)
print(a)
print(b)
print(c)
# -0.9880316240928618
# 0.15425144988758405
# -6.405331196646276


# ولعلاج الامر , اما يم يتم ضرب الرقم في (باي  / 180) 

a=sin(30*pi/180)
b=cos(30*pi/180)
c=tan(30*pi/180)
print(a)
print(b)
print(c)
# 0.49999999999999994
# 0.8660254037844387
# 0.5773502691896257


# او يتم استخدام الدالة  deg2rad

a=sin(deg2rad(30))
b=cos(deg2rad(30))
c=tan(deg2rad(30))
print(a)
print(b)
print(c)
# 0.49999999999999994
# 0.8660254037844387
# 0.5773502691896257


# التقريب أمر round  
a=round(3.5674)
b=round(3.5674,1)
c=round(3.5654,2)
d=round(3.5676,3)
print(a)
print(b)
print(c)
print(d)
# 4
# 3.6
# 3.57
# 3.568

# أمر ceil , floor  للتقريب الاعلي و الاقل  
a=floor(3.425)
b=ceil(3.99)
print(a)
print(b)
# 3.0
# 4.0


# أمري mod , power  
a=mod(20,7)
b=power(2,3)
print(a)
print(b)
# 6
# 8












