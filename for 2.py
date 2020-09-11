w="hello python"
# تقسيم احرف الكلمة بدون الفراغ
for v in w:
    if v == " ":
       continue
    print(v)
# h
# e
# l
# l
# o
# p
# y
# t
# h
# o
# n

# طباعة الارقام ما عدا التي تقبل القسمة على 5
for c in range(21):
    if c %5==0 :
        continue
    print(c)
1
2
3
4
6
7
8
9
11
12
13
14
16
17
18
19


# طباعة الارقام ما عدا التي تقبل القسمة على 5 او 3
for z in range(21):
    if z % 5 ==0 or z%3==0:
        continue
    print(z)
1
2
4
7
8
11
13
14
16
17
19

# طباعة الارقام ما عدا التي تقبل القسمة على 
for x in range(11):
    if x%5==0 and x!=0:
        print("divided over is"+str(x))
        continue
    print("not divided over is"+str(x))
# not divided over is0
# not divided over is1
# not divided over is2
# not divided over is3
# not divided over is4
# divided over is5
# not divided over is6
# not divided over is7
# not divided over is8
# not divided over is9
# divided over is10
  
# فصفصة قائمة
students=['ahmad','omar','osman']
for a in students:
    print(a)
# ahmad
# omar
# osman

# فصفصة قاموس :فقط المفاتيح
grades={'ahmad':100,'omar':75,'osman':60}
for a in grades:
    print(a)
# ahmad
# omar
# osman

# فصفصة قاموس :فقط المفاتيح
grades={'ahmad':100,'omar':75,'osman':60}
for a in grades.keys():
    print(a)
# ahmad
# omar
# osman

# فصفصة قاموس :فقط القيم
grades={'ahmad':100,'omar':75,'osman':60}
for a in grades.values():
    print(a)
100
75
60

# فصفصة قاموس :الكل
grades={'ahmad':100,'omar':75,'osman':60}
for a in grades.items():
    print(a)
# ('ahmad', 100)
# ('omar', 75)
# ('osman', 60)

# فصفصة قاموس :الكل
grades={'ahmad':100,'omar':75,'osman':60}
for a,b in grades.items():
    print(a)
    print(b)
# ahmad
100
# omar
75
# osman
60

# فصفصة قاموس :الكل
grades={'ahmad':100,'omar':75,'osman':60}
for a,b in grades.items():
    print(a,b)
# ahmad 100
# omar 75
# osman 60

































