import random as rn
# رقم عشوائي بين 0و1
a=rn.random()
print(a)
# 0.48248994619933416

# رقم عشوائي بين 1 و 20
a=rn.randint(1,20)
print(a)
# 2

# رقم كسري
b=rn.uniform(1,20)
print(b)
# 13.320965085295143

# رقم عشوائي ضمن حد معين
a=rn.randrange(10)
print(a)
# 1

# رقم عشوائي بين 1 و 10
a=rn.randrange(1,10)
print(a)
# 3

# رقم عشوائي بين حدين ويمشي خطوتين
a=rn.randrange(0,10,2)
print(a)
# 4
# يختار قيمة عشوائية ولا يعمل مع set 
a=rn.choice((1,2,3))
print(a)
# 1
a=rn.choice(['a','b','c'])
print(a)
# b

# يختار عشر قيم من ضمن الحدين
a=rn.sample(range(20,50),10)
print(a)
# [34, 41, 22, 27, 20, 48, 33, 31, 26, 43]

a=rn.choice("hello python")
print(a)
# h

# يرتب ترتيب عشوائي ولا يعمل مع tuple , set
items=[1,2,3,4,5]
rn.shuffle(items)
print(items)
# [3, 5, 4, 1, 2]

items=("ahmad")
rn.shuffle(items)
print(items)
# 'str' object does not support item assignment











































