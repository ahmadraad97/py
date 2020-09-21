# اكثر من دالة في نفس السطر
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10,0.5)

plt.plot(x,x,'r--',x,x**2,'bo',x,x**3,'g^')


# مثال
x = np.arange(0,10,0.05)
y = np.exp(-x/3)*np.sin(3*np.pi*x)
z = np.exp(x/2)*np.sin(3*np.pi*x)
w  = np.exp(x/2)**np.cos(4*np.pi*x)

plt.plot(x,y,'b',x,z,'g',x,w,'r')


# مثال
x = np.linspace(0, 10, 500)
y = np.cumsum(np.random.randn(500, 6), 0)

plt.plot(x, y)


# قيمة التفاوت 
x = np.linspace(0, 10, 50)
dy = 0.2
y = np.sin(x) + dy * np.random.randn(50)
plt.errorbar(x, y, yerr=dy, fmt='.b')


# مثال
x = np.linspace(0, 10, 50)
dy = 1.2
y = np.sin(x) + dy * np.random.randn(50)
plt.errorbar(x, y, yerr=dy, fmt='.r');


# مثال
x = np.linspace(0, 10, 50)
dy = 1.2
y = np.sin(x) + dy * np.random.randn(50)

plt.errorbar(x, y, yerr=dy, fmt='o',
             color='black', ecolor='lightgray',
             elinewidth=3, capsize=0)


# التفاوت الافقي
x = np.linspace(0, 10, 50)
dy = 1.2
y = np.sin(x) + dy * np.random.randn(50)
plt.errorbar(x, y, xerr=dy, fmt='.r')


# قراءة من ملف و رسم بيانات
def extract_data(filename):
    infile = open(filename, 'r')
    infile.readline() # skip the first line
    numbers = []
    for line in infile:
        words = line.split()
        number = float(words[1])
        numbers.append(number)
    infile.close()
    return numbers

values = extract_data('D:\\2.txt')
print(values)
month_indices = range(1, 13)
plt.plot(month_indices, values[:-1], '*r')

# =================================================
# Average rainfall (in mm) in Rome: 1188 months between 1782 and 1970
# Jan 81.2
# Feb 63.2
# Mar 70.3
# Apr 55.7
# May 53.0
# Jun 36.4
# Jul 17.5
# Aug 27.5
# Sep 60.9
# Oct 117.7
# Nov 111.0
# Dec 97.9
# Year 792.9
























































































