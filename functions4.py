# ومن الممكن اعطاء قيم افتراضية للدالة , بحيث يتم استخدامها اذا لم يتم تحديدها
def power(m,n=3):
    print(m**(n))
power(3,2)
# 9

# واذا لم يتم تحديدها تستخدم القيمة الافتراضية
def power(m,n=3):
    print(m**(n))
power(3,)
# 27

# وممكن اثناء استدعاء الدالة ان يتم عمل تحديد للارقام المعطاة 
def power(m,n):
    print(m**(n))
power(m=3,n=2)
# 9

# وممكن اثناءالاستدعاءان يتم كتابةالرموز دون ترتيب
def power(m,n):
    print(m**(n))
power(n=2,m=3)
# 9
# ويمكن استخدام امر return لاعطاء قيمة للدالة
def power(m,n):
    x=m**n
    return x
print(power(3,2))
# 9

# ويمكن عمل دوال متداخلة
def power(y,c) : 
    x = y**c
    return x
     
def times4(x) : 
    z = 4*x
    return z

def add7(z) : 
    w = z+7
    return w
    
d = int(input('first : '))
dd = int(input('second : '))

print (add7(times4(power(d,dd))))
# first : 1

# second : 1
# 11

# اللذي في الخارج لا يتعارض مع ما داخل الدالة حتى لو بنفس الاسم
xx = 5

def gg() : 
    xx = 14
    
gg()
print (xx)
# 5


# لطباعة ما داخل الدالة ويجب استدعاء الدالة والمتغير في الخارج وكتابة القيمة المرادة للمتغير داخل الدالة
xx = 5

def gg() : 
    global xx
    xx = 14
    
gg()
print (xx)


# lambda تستخدم لتعريف دالة قصيرة
powers = lambda x,y : x**y

print (powers(5,3))
# 125

# اكثر من لمدا داخل list ونقوم بتعبئة العناصر تباعا
powers=[lambda x:"df",lambda x:x ,lambda x:x**2 ,lambda x:x**3]
print(powers[0](5))  
print(powers[1](5))  
print(powers[2](5))  
print(powers[3](5))  
# df
# 5
# 25
# 125


# filter طريقة لاختيار ارقام معينة بناء على شرط باستخدام لمدا
mylist = (0,1,2,3,4,5,6,7,8,9)
two=tuple(filter(lambda x:x%2==0,mylist))
one=set(filter(lambda x:x%2==1,mylist))
print (two)
print (one)
# (0, 2, 4, 6, 8)
# {1, 3, 5, 7, 9}

# map تطبيق دالة معينة على جميع العناصر
mylist = {0,1,2,3,4,5,6,7,8,9}
print("square list",tuple(map(lambda x :x**2,mylist)))
# square list (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

# طريقة ثانية باستخدام دالة
list1=[1,2,3,4]
def powerlist(x):
    return x**3
print(list(map(lambda x:powerlist(x),list1)))
# [1, 8, 27, 64]


# return تسمح بتكرار ارقام معينة وتستخد في فور بدل yield 
def yie():
    for i in range(10):
        yield i
        
for g in yie():
       print(g)
0
1
2
3
4
5
6
7
8
9



a=[i for i in range(10)]
print(a)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# او عن طريق دالة next
def yie():
    for i in range(10):
        yield i
           
f = yie()
print (next(f))
print (next(f))
print (next(f))
0
1
2

# طريقة عمل قانون فيبوناتشي ويعطي فارغة مع الصفر والسالب
def fibon(v):
    a=b=1
    result=[]
    for i in range(v):
        result.append(a)
        a,b=b,a+b
    return result
print(fibon(4))
# [1, 1, 2, 3]


# طريقة ثانية باستخدام yield
def fibon(v):
    a=b=1
    for i in range(v):
        yield a
        a,b=b,a+b
for x in fibon(4):
    print(x)
1
1
2
3


# لحساب فاكتوريا ل
def fac(n):
    if n ==1 : 
        return 1
    else : 
        return n * fac(n-1)

print(fac(10))
# 24






































































































































































































































































































































































































