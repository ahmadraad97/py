a=[1,2,3,4,5,6,7,8,9]
print(a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[0]=2
print(a)
# [2, 2, 3, 4, 5, 6, 7, 8, 9]

a[2:5]=[]
print(a)
# [2, 2, 6, 7, 8, 9]

a[:]=[]
# يمسحها كلها

b=["a","b","c"]
c=[1,2,3]
d=[b,c]
print(d)
# [['a', 'b', 'c'], [1, 2, 3]]

print(b[0])
# a
print(d[0][1])
# b

del b[0]
print(b)
# ['b', 'c']

y=["s","e","r"]
print(y)
# ['s', 'e', 'r']

y.remove("e")
print(y)
# ['s', 'r']
del y
print(y)
# name 'y' is not defined






















