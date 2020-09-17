from numpy import *
# فتح الملفات 

fname = 'D:\\2t\\ab'
dtype1 = dtype([('gen', '|S4'), ('heig', 'f8')])
a = loadtxt(fname, dtype=dtype1, skiprows=10, usecols=(0,3))

print(a)
print('-------------------------')

a,b,c= loadtxt('D:\\3t\\00', unpack=True,skiprows=3)
print(a)
print(b)
print(c)
print('-------------------------')

data = genfromtxt('D:\\1t\\11.txt', skip_header=1,
                  dtype=[('student','u8'),
                         ('gender','S1'),('black','f8'),
                         ('colour','f8')],delimiter=',',
                         missing_values='X')
print(data)



























































































