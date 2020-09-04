# یتم ذكر اسم المكتبة في كل دالة
import math
a=math.sqrt(16)

# یتم ذكر الاختصار في كل دالة
import math as m
a=m.sqrt(16)

# تصلح فقط لدالة واحد
from math import sqrt,cos
b=cos(10)
c=sqrt(4)
print(b)
# -0.8390715290764524
print(c)
# 2.0
# g=sin(60)
# print(g)
# name 'sin' is not defined

# یتم ذكر الدالة فقط دون مقدمة,لا ينصح بها لعدم معرفة نوع الدالة
from math import *
x=tan(90)

# مكتبة math
import math as m
print(m.factorial(3))
# 6,(3*2*1)

print(m.exp(3))
# 20.085536923187668,(e^3)

print(m.log(5))
# 1.6094379124341003

print(m.log10(5))
# 0.6989700043360189

print(m.log(2,3))
# 0.6309297535714574

print(m.sqrt(4))
# 2.0

print(m.radians(180))
# 3.141592653589793و(تحويل الى راديان)

print(m.degrees(1.5))
# 85.94366926962348,(تحويل الى درجة)

# الدوال المثلثية
print(m.cos(m.radians(90)))
# 6.123233995736766e-17
print(m.cos(m.radians(180)))
# -1.0
print(m.sin(m.radians(90)))
# 1
print(m.tan(m.radians(180)))
# -1.2246467991473532e-16

# الدوال المثلثیة العكسیة
# m.asin(x)      m.acos(x)      m.atan(x)

# الدوال المثلثیة للقطع الزائد
# m.sinh(x)      m.cosh(x)      m.tanh(x)


# الدوال المثلثیة العكسیة للقطع الزائد
# m.asinh(x)      m.acosh(x)      m.atanh(x)

# الثوابت الھامة
print(m.pi)
# 3.141592653589793

print(m.e)
# 2.718281828459045

print(m.tau)
# 6.283185307179586

print(m.inf)
# inf

# نسخ الاشارة
print(m.copysign(-7,3))
# 7.0

# التقریب للأعلي
print(m.ceil(5.1))
# 6

# التقریب للأقل
print(m.floor(5.9))
# 5

# دالة قیمة الخطأ
print(m.erf(1))
# 0.8427007929497149
print(m.erf(10))
# 1.0

# دالة الجاما
print(m.gamma(1))
# 1.0
print(m.gamma(x))
# 104.64151718539263





