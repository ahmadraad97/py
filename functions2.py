def t_values(**val):
    print(val)
t_values(ahmad=90,omar=60)
# {'ahmad': 90, 'omar': 60}

# يجب {} هذا النوع من الاقواس
def t_values(**val):
    for key,value in val.items():
        print("{}={}".format(key,value))
        
t_values(ahmad=90,omar=60,osman=75)
# ahmad=90
# omar=60
# osman=75


def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print ("%s = %s" %(key,value))
 
greet_me(name1='python',name2=1)
# name1 = python
# name2 = js





def avg_of_two(a,b):
  print ((a+b)/2)
def avg_of_three(a,b,c):
  print ((a+b+c)/3)
var1 = {'a':1,'b':2}
avg_of_two(**var1)
# 1.5
var2 = {'a':1,'b':2,'c':3}
avg_of_three(**var2)
# 2



def details(a,b,*arg,**kw):
    print("a is",a)
    print("b is",b)
    print("arg is",arg)
    print("kw args is",kw)
details(1,2,3,"adf",6,True)    
# a is 1
# b is 2
# arg is (3, 'adf', 6, True)
# kw args is {}


# الkw يجب كتابتها كما في الاسفل بدون تغيير
def details(a,b,*arg,**kw):
    print("a is",a)
    print("b is",b)
    print("arg is",arg)
    print("kw args is",kw)
details(1,2,3,"adf",6,True,ahmad=90,omar=100) 
# a is 1
# b is 2
# arg is (3, 'adf', 6, True)
# kw args is {'ahmad': 90, 'omar': 100}


def test(arg1,arg2,arg3):
    print("arg1 is",arg1)
    print("arg2 is",arg2)
    print("arg3 is",arg3)
args=('two',2,False)
test(*args)
# arg1 is two
# arg2 is 2
# arg3 is False
# هنا يجب تعريفه ك قاموس وبنفس القيم المعرفة في الاعلى
kw={"arg3":1,"arg2":2,"arg1":3}
test(**kw)
# arg1 is 3
# arg2 is 2
# arg3 is 1




































