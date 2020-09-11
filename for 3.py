students=['ahmad','omar','osman']
# لترقيم العناصر
for l,a in enumerate(students):
    print(l,a)
# 0 ahmad
# 1 omar
# 2 osman

# للجمع بين العناصر
students=['ahmad','omar','osman']
grades=[90,70,60]
for i,a in zip(students,grades):
    print('student' +" "+ i + " "+'got' +" "+ str(a) +" "+ 'degree')
# student ahmad got 90 degree
# student omar got 70 degree
# student osman got 60 degree

# تكرار الاعداد من0الى 19
a=[i for i in range(20)]
print(a)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


# الاعداد التي تقبل القسمة على 3 من 0الى 19
a=[i for i in range(20) if i%3==0]
print(a)
# [0, 3, 6, 9, 12, 15, 18]


# الاعداد التي تقبل القسمة على 3 و 2 في نفس الوقت من 0الى 19
a=[i for i in range(20) if i%3==0 and i%2==0]
print(a)
# [0, 6, 12, 18]


# الاعداد من 0الى 10 للترببيع
a=[i**2 for i in range(10)]
print(a)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# مصفوفة ثنائية
a=[(i,j)for i in range(3)for j in range(2)]
print(a)
# [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]


# مصفوفة ثنائية
a=[(i*2,j+1)for i in range(3)for j in range(2)]
print(a)
# [(0, 1), (0, 2), (2, 1), (2, 2), (4, 1), (4, 2)]

# بعد الانتهاء اطبع else
for x in range(10):
    print(x)
else:
    print("done")
0
1
2
3
4
5
6
7
8
9
# done

# جمع الارقام من 0 الى 9
print(sum([k for k in range (10)]))
# 45

# جمع من 1/1 ال 1/9
print(sum([1/k for k in range (1,10)]))
# 2.8289682539682537

# عمليات متداخلة
print(sum([3*(k**2) for k in range (1,4)]))
# 42

a=[3*x for x in[y**2 for y in range(1,4)]]
print(a)
# [3, 12, 27]

print([3*(k**2) for k in range (1,4)])
# [3, 12, 27]




