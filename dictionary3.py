tel={'syria':'00963' ,'turkey':'0090','ksa':'00966' }
# طباعة قائمة بالمفاتيح فقط
a=list(tel.keys())
print(a)
# ['syria', 'turkey', 'ksa']
# طباعة قائمة بالقيم فقط
b=list(tel.values())
print(b)
# ['00963', '0090', '00966']
# طباعة قائمة بجميع القيم
c=list(tel.items())
print(c)
# [('syria', '00963'), ('turkey', '0090'), ('ksa', '00966')]
# يمكن وضع اكثر من قيمة لنفس المفتاح
point={'names':(1,2,3),'adress':(4,5,6)}
print(point)
# {'name': (1, 2, 3), 'adress': (4, 5, 6)}
# طباعة قيم المفتاح
print(point['names'])
# (1, 2, 3)

# طباعة قيمة محددة من مجموع قيم المفتاح
print(point['names'][2])
# 3
# حذف قيمة من القاموس
del(point['names'])
print(point)
# {'adress': (4, 5, 6)}
# لا يمكن حذف قيم مفتاح لانها tuple
# del(point['names'][2])
print(point)
# 'tuple' object doesn't support item deletion



















































