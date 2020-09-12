def star():
    for h in range(10):
        print("*")
star()       


# لابد ان يتم تعريف الدالة قبل استخدامها 
# ah()
def ah() : 
    for h in range(10) : 
        print ('**')


def ar():
    for h in range(5):
        print(3)
s=ar
s()

# لتعريف دالة من متغيرين
def find_avg(a,b):
    average=(a+b)/2
    print("average is",average)
find_avg(3,3)    
# average is 3.0


# لتعريف دالة من اكثر من متغير
def find_avg(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    print("average is",sum/(len(numbers)))
    print(numbers)
find_avg(2,3,4,5)    
# average is 3.5
# (2, 3, 4, 5)


# طريقة ثانية
def avg_two(a,b):
    print((a+b)/2)
def avg_three(a,b,c):
    print((a+b+c)/3)
var1=(1,2)
avg_two(*var1)
# 1.5

var2=(4,5,6)
avg_three(*var2)
# 5.0

# تعريف دالة من متغير ودالة من اكثر من متغير مع بعضها
def test_args(f_arg,*argv):
    print("first normal arg",f_arg)
    for f_arg in argv:
        print("another arg",f_arg)
test_args('ahmad','mahmoud','omar')
# first normal arg ahmad
# another arg mahmoud
# another arg omar














































