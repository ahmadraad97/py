telefon={'syria':'00963' ,'turkey':'0090','ksa':'00966' }
# يجلب قيمة المفتاح
print(telefon.get('syria'))
# 00963

# يجلب قيمة المفتاح ولو مو موجودة يطبع القيمة المعطاة
print(telefon.get('lebanon','0012'))
# 0012

# تضتفة مفتاح مع قيمته
telefon['lebanon']='0012'
print(telefon)
# {'syria': '00963', 'turkey': '0090', 'ksa': '00966', 'lebanon': '0012'}

# يمسح المفتاح مع قيمته يعمل فقط بوضع المفتاح
del(telefon['syria'])
print(telefon)
# {'turkey': '0090', 'ksa': '00966', 'lebanon': '0012'}

# يعطي طول القاموس
print(len(telefon))
# 3

# يقوم بتفريغ القاموس
telefon.clear()
print(telefon)
# {}


# يقوم بحذف القاموس نهائيا
# del(telefon)
print(telefon)
# name 'telefon' is not defined



tel={'syria':'00963' ,'turkey':'0090','ksa':'00966' }
# يقوم بنسخ المصفوفة
a=tel.copy()
print(a)
# {'syria': '00963', 'turkey': '0090', 'ksa': '00966'}

# يقوم بعمل قاموس مشتق من الset
set1={"d","a","b"}
dic1=dict.fromkeys(set1)
print(dic1)
# {'d': None, 'a': None, 'b': None}

# نعطي قيم لمفاتيح القاموس
dic1['d']=1
dic1['a']=2
dic1['b']=3
print(dic1)
# {'d': 1, 'a': 2, 'b': 3}
















