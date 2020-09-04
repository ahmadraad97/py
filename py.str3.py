a=("i love python and i love AL")
print(a.partition('love'))
# ('i ', 'love', ' python and i love AL')

print(a.rpartition("love"))
# ('i love python and i ', 'love', ' AL')

print(a.find("i"))
# 0
print(a.rfind("i"))
# 18

print(a.index("i"))
# 0
# والفارق بینھم ان لو الكلمة او الحرف مش موجود , ف find ھتجیب سالب واحد بینما index ھتجیبerror 

print(a.replace("i","he"))
# he love python and he love AL
# المتغير الاساسي لا يتغير
print(a)
# i love python and i love AL

print(a.count("i"))
# 2

# یجعل اول حرف في الجملة كابیتال والباقي سمول
print(a.capitalize())
# I love python and i love al

# یجعل اول حرف في كل كلمة كابیتال
print(a.title())
# I Love Python And I Love Al

# یجعل كل الحروف كابیتال
print(a.upper())
# I LOVE PYTHON AND I LOVE AL

# يحول الكبير الى صغير والعكس
print(a.swapcase())
# I LOVE PYTHON AND I LOVE al

# يجعل فراغات يمين ويسار 
print(a.center(30))
 # i love python and i love AL  


