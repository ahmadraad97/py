# 1 . webbrowser



# لفتح أي موقع   
import webbrowser as w
w.open('www.fb.com') 

# لفتح ملف أونلاين كبيانات  
from pandas import read_csv
url='https://github.com/cs109/2014_data/blob/master/countries.csv'
data = read_csv(url, names=[2])
print(data.shape)

# 2 . glob
import glob as gb


# للبحث عن الملفات   هنا يأتي بكل الملفات
a = gb.glob(pathname= 'D:\\3.sinif\\ILETISIM\\*.*')

print(a)
# ['D:\\3.sinif\\ILETISIM\\anadol.pdf', 'D:\\3.sinif\\ILETISIM\\ataturk.pdf', 'D:\\3.sinif\\ILETISIM\\İletişim ve teknoloji1 Tanım ve tarihsel gelişimi (1).pptx']



# أمر glob1  يأتي بالاسم فقط من غير المسار كامل 
a = gb.glob1('D:\\3.sinif\\ILETISIM\\' , '*.*')

print(a)
# ['anadol.pdf', 'ataturk.pdf', 'İletişim ve teknoloji1 Tanım ve tarihsel gelişimi (1).pptx']



# للبحث عن ملف معين  ,بالاسم و المسار 
a = gb.glob(pathname= 'D:\\3.sinif\\ILETISIM\\*.pdf')

print(a)
# ['D:\\3.sinif\\ILETISIM\\anadol.pdf', 'D:\\3.sinif\\ILETISIM\\ataturk.pdf']



# أمر glob1  للبحث عن ملف معين , بالاسم فقط  
a = gb.glob1( 'D:\\3.sinif\\ILETISIM\\','*.pdf')

print(a)
# ['anadol.pdf', 'ataturk.pdf']

