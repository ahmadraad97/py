# اذا بدء بصفر يجب تحويله الى نص
telefon={'syria':'00963' ,'turkey':'0090','ksa':'00966' }
print(telefon)
# {'syria': '00963', 'turkey': '0090', 'ksa': '00966'}

# تعديل القيم والمفاتيح
telefon['syria']='0011'
print(telefon)
# {'syria': '0011', 'turkey': '0090', 'ksa': '00966'}

# هل هذا المفتاح موجود
print('syria'in telefon)
# True
# يعطي ليس موجود لانه قيمة وليس مفتاح
print('0090'in telefon)
# False
# لايجاد القيمة
print('0090'in telefon.values())
# True

# طريقة ثانية لكتابة القاموس
print({n:n**2 for n in range(3)})
# {0: 0, 1: 1, 2: 4}
































