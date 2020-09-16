
# ممكن عمل كلاس جديدة عن طريق اكتب class بعدها اسمها بعدها نقطتين , ثم المتغيرات او الدوال
#ممكن استخدام اي بيانات في الكلاس 
class car:
    length=20
    width=10
    height=50
    color="white"
    volume=length*width*height
print(car.color)
# white


renault=car
print(renault.color)
# white

# ولو تم حفظ الكلاس في ملف بامتداد py  ممكن اعمله استدعاء واستخدام كافة الدوال و المتغيرات فيها
from myclasses import car

# او ممكن استدعاء كل الكلاسات المحفوظة فيه
from myclasses import *
























































