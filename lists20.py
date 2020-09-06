y=[1,2,3,4,5,6]
# ترتيب عكسي
print(sorted(y,reverse=True))
# [6, 5, 4, 3, 2, 1]


y=[("at",85),("br",30),("er",40),('zs',90)]
# بناء على العنصر الثاني ترتيب عكسي 
print(sorted(y,reverse=True,key=lambda e:e[1]))
# [('zs', 90), ('at', 85), ('er', 40), ('br', 30)]


# يفصل بناء على حد
a='5,6,8,7,9,1,4,2,3'
print(a.split(sep=",",maxsplit=4))
# ['5', '6', '8', '7', '9,1,4,2,3']


# هل القيمة موجودة
x=[2,6,4,9]
print(6 in x)
# True

v=["a","g","r"]
print("a" in v)
# True

# يدمج مع تغيير الاصل
x.extend(v)
print(x)
# [2, 6, 4, 9, 'a', 'g', 'r']





























