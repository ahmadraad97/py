a = 'hello python'
b="3659"
c="    ahmad   "
e="***ahmad***"
# مسافات على اليسار
print(a.rjust(20))
        # hello python
# مسافات على اليمين
print(a.ljust(20))
# hello python        

# فقط مع الارقام بصيغة نص ؛يملا اصفار قبل
print(b.zfill(6))
# 003659

# يعتبر المسافة والرموز ليست احرف
print(a.isalpha())
# False

# حذف المسافات
print(c.strip())
# ahmad
# حذف المسافات من اليمين
print(c.rstrip())
    # ahmad
# حذف المسافات من اليسار
print(c.lstrip())
# ahmad   
# حذف الرموز
print(e.strip("*"))
# ahmad
















