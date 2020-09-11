# تقوم بحذف المتشابه والترتيب فقط للارقام
d={1,1,2,2,6,8,4,6,9}
print(d)
# {1, 2, 4, 6, 8, 9}

# هنا لا يقوم بالترتيب
print({n**2 for n in range(12)})
# {0, 1, 64, 121, 4, 36, 100, 9, 16, 49, 81, 25}

# لا يقوم بترتيب النصوص
a={'homs','idlib','aleppo'}
b={'homs','tartos','hama','horan'}

# يطبع الاقل
print(a or b)
# {'homs', 'aleppo', 'idlib'}
# يطبع الاكثر
print(a and b)
# {'tartos', 'homs', 'hama', 'horan'}

# جميع العناصر هنا وهنا
print(a|b)
# {'homs', 'horan', 'idlib', 'tartos', 'hama', 'aleppo'}
# طريقة ثانية
print(a.union(b))
# {'homs', 'horan', 'idlib', 'tartos', 'hama', 'aleppo'}
print(b.union(a))
# {'homs', 'horan', 'idlib', 'tartos', 'hama', 'aleppo'}

# العناصر المشتركة فقط
print(a&b)
# {'homs'}
print(a.intersection(b))
# {'homs'}

# جميع العناصر عدا المشتركة
print(a^b)
# {'horan', 'hama', 'idlib', 'tartos', 'aleppo'}
print(a.symmetric_difference(b))
# {'horan', 'hama', 'idlib', 'tartos', 'aleppo'}
print(b.symmetric_difference(a))
# {'horan', 'hama', 'idlib', 'tartos', 'aleppo'}

# عناصر a بعد حذف العناصر المشتركة مع b
print(a-b)
# {'aleppo', 'idlib'}
print(a.difference(b))
# {'aleppo', 'idlib'}
# عناصر b بعد حذف العناصر المشتركة مع a 
print(b.difference(a))
# {'tartos', 'hama', 'horan'}













