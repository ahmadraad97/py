from numpy import *
# ممكن حساب الارقام التي ليست صفر
a=random.randint(0,10,(3,3))
b=count_nonzero(a)
print(a)
# [[2 4 2]
 # [6 3 7]
 # [3 2 2]]
print(b)
# 9

# او تحديد عدد الارقام اكبر او اصغر من كذا
a=random.randint(0,10,(3,3))
b=count_nonzero(a>5)
c=count_nonzero(a<5)
print(a)
# [[0 4 1]
 # [4 9 4]
 # [5 0 9]]
print(b)
# 2
print(c)
# 6

# وممكن حساب الارقام يكون بالصف اوالعمود كله
a=random.randint(0,10,(3,3))
b=count_nonzero(a>5,axis=0)
c=count_nonzero(a<5,axis=1)
print(a)
# [[4 9 7]
 # [0 0 4]
 # [1 8 9]]
print(b)
# [0 2 2]
print(c)
# [1 3 1]

# لمعرفة هل فيه رقم اكبر او اصغر
a=random.randint(0,10,(3,3))
b=any(a>7)

print(a)
# [[8 6 4]
 # [5 8 9]
 # [6 6 6]]
print(b)
# True

# ويمكن عملها في كل عمود
a=random.randint(0,10,(3,3))
b=any(a>7,axis=0)
print(a)
# [[3 2 5]
 # [9 9 0]
 # [4 0 5]]
print(b)
# [ True  True False]
# او صف
a=random.randint(0,10,(3,3))
b=any(a>7,axis=1)
print(a)
# [[7 2 9]
 # [3 4 2]
 # [6 6 9]]
print(b)
# [ True False  True]


# ويمكن معرفة هل كل العناصر شرط معين
a=random.randint(0,10,(3,3))
b=all(a>7,axis=1)
print(a)
# [[0 3 4]
 # [9 0 4]
 # [3 7 5]]
print(b)
# [False False False]

# ويمكن معرفة هل العناصر اكبر من او اصغر من رقم معين
a=random.randint(0,10,size=6).reshape(2,3)
b=a>5
c=a<5
print(a)
# [[4 5 0]
 # [8 8 1]]
print(b)
# [[False False False]
 # [ True  True False]]
print(c)
# [[ True False  True]
 # [False False  True]]


a=arange(6).reshape(2,3)
b=arange(6).reshape(2,3)
c=a**2
d=isclose(a,b,rtol=0.2)
e=isclose(a,c,rtol=0.2)
print(a)
# [[0 1 2]
 # [3 4 5]]
print('------------------')
print(b)
# [[0 1 2]
 # [3 4 5]]
print('------------------')
print(c)
# [[ 0  1  4]
 # [ 9 16 25]]
print('------------------')
print(d)
# [[ True  True  True]
 # [ True  True  True]]
print('------------------')
print(e)
# [[ True  True False]
 # [False False False]]

# يمكن ضرب قيم المصفوفة في بعضها
a=arange(3)
print(a)
# [0 1 2]
print(multiply(a,10))
# [ 0 10 20]

# لرفع كل العناصر للأس الرابع
a=arange(3)
print(a)
# [0 1 2]
print(power(a,4))
# [ 0  1 16]




































































































































