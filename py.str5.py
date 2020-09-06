# نزول سطر
a='i \nlove python'
print(a)
# i 
# love python
# لتهميش عملها نضع r
c=r'C:\some\name'
print(c)
# C:\some\name

# يعمل فراغ ك تاب
b='i \tlove python'
print(b)
# i 	love python

# كتابة جمل في اسطر متعددة
d='''i
love
python'''
print(d)
# i
# love
# python

# لوصل الجمل
e,f='ahmad','rad'
print(e , end="" )
print(f)
# ahmadrad

g='ahmad'
i=20
h='my name is %s and my old is %d'%(g,i)
print(h)
# my name is ahmad and my old is 20

k="numbers %5d"%7
print(k)
# numbers     7

l="numbers %05d"%7
print(l)
# numbers 00007

m='%s has %03d qpute types'%("python",2)
print(m)
# python has 002 qpute types

# لجعل لاكوتيشن جزء من الكلام
print('doesn\'t')
# doesn't
print("doesn't")
# doesn't
print('"Yes," he said.')
# "Yes," he said.
print("\"Yes,\" he said.")
# "Yes," he said.
print('"Isn\'t," she said.')
# "Isn't," she said.

