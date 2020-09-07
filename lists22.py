# من 0 الى 12 للتكعيب
y = [ x**3 for x in range(12)]
print(y)
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331]

# نفس الاعلى بطريقة ثانية
y = list(map(lambda x : x**3 , range(12)))
print(y)
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331]

# -5 +0.5 عشرين رقم
ss = [-5 + i*0.5 for i in range(20)]
print(ss)
# [-5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]

# طريقة ثانية للقائمة
f = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(f)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# عدد الصفوف 7 و عدد العواميد 5
L = [[0 for i in range(5)] for j in range(7)]
print(L)
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# عندما اكتب next يعطي العنصر اللي بعده
I = iter([2, 4, 6, 8, 10])
print(next(I))
# 2
print(next(I))
# 4

I = iter(range(20))
print(next(I))
# 0
print(next(I))
# 1

# تصبح القائمتين نفس القيمة
x = [1,2]
y = x
print(x)
# [1, 2]
print(y)
# [1, 2]

# بطريقة التعديل هذه تتغير الاثنتين
x = [1,2]
y = x
x[0] = 5
x[1] = 15
print(x)
# [5, 15]
print(y)
# [5, 15]

# بطريقة التعديل هذه تتغير الاصلية
x = [1,2]
y = x
print(x)
# [1, 2]
print(y)
# [1, 2]
x = [6,9]
print(x)
# [6, 9]
print(y)
# [1, 2]

# يعطي القيمة مع رقم
my_list = ['apple', 'banana', 'grapes', 'pear']
for a, value in enumerate(my_list, 4):
    print(a, value)
# 4 apple
# 5 banana
# 6 grapes
# 7 pear

# يقوم بجمع قائمتين (العنصر الاول مع الاول والثاني مع الثاني)
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print (a, b)
# a1 b1
# a2 b2
# a3 b3

# يقوم بالترتيب التصاعدي بحسب رقم العنصر
from operator import itemgetter,methodcaller
student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10),]
print(sorted(student_tuples, key=itemgetter(2)))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# يقوم بترتيب تصاعدي بحسب العنصر التاني ولو تساوى يرتب بحسب العنصر الثالث
print(sorted(student_tuples, key=itemgetter(1,2)))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

# يرتب الكلمات بناء على عدد حرف a
messages = ['critical!!!', 'hurry!', 'bla bla', 'alabama']
print (sorted(messages, key=methodcaller( 'count', 'a')))









