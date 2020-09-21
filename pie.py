

# لعمل الاشكال البيانية علي هيئة قرص 
import matplotlib.pyplot as plt
plt.pie([15,30,45,10])
plt.show()


# لجعل الدائرة متساوية الابعاد
plt.pie([15,30,45,10])
plt.axis('equal')
plt.show()


# تسمية القطع
plt.pie([15,30,45,10],labels=('xiaomi','huawei','samsung','htc'))
plt.axis('equal')
plt.show()


# ابعاد الاجزاء
plt.pie([15,30,45,10],labels=('xiaomi','huawei','samsung','htc'),explode = [0.1,0.1,0.1,0.3])
plt.axis('equal')
plt.show()
          


# النسبة المئوية
plt.pie([15,30,45,10],labels=('xiaomi','huawei','samsung','htc'),explode = [0.1,0.1,0.1,0.3],
        autopct ='%1.1f%%')
plt.axis('equal')
plt.show()



# عمل ظل
plt.pie([15,30,45,10],labels=('xiaomi','huawei','samsung','htc'),
        explode = [0.1,0.1,0.1,0.3],autopct ='%1.1f%%',shadow=True)
plt.axis('equal')
plt.show()


# زاوية البداية
plt.pie([15,30,45,10],labels=('xiaomi','huawei','samsung','htc'),explode = [0.1,0.1,0.1,0.3],
        autopct ='%1.1f%%',shadow=True,startangle=45)
plt.axis('equal')
plt.show()




# مسافة الكلام عن الشرائح
plt.pie([15,30,45,10],labels=('xiaomi','huawei','samsung','htc'),explode = [0.1,0.1,0.1,0.3],
        autopct ='%1.1f%%',shadow=True,
        startangle=-45,labeldistance=1.3)
plt.axis('equal')
plt.show()




# مسافة النسبة المئوية

plt.pie([15,30,45,10],labels=('xiaomi','huawei','samsung','htc'),explode = [0.1,0.1,0.1,0.3],
        autopct ='%1.1f%%',shadow=True,
        startangle=45,labeldistance=1.3,pctdistance=0.555)
plt.axis('equal')
plt.show()










