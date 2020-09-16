
# الـ Class Variable
class car() : 
    color = 'blue'
    
volvo = car
renault = car
volvo.color='white'
renault.color="green"

print(volvo.color)
# green
print(renault.color)
# green


# الـ instance variable 

class car() : 
   def __init__(self,color):
       self.color=color
    
volvo = car("white")
renault = car("green")


print(volvo.color)
# white
print(renault.color)
# green

# و ممكن اعمل قيم مفترضة للمعاملات
class car() : 
   def __init__(self,color1="white",color2="green"):
       self.color1=color1*2
       self.color2=color2*2
a=car()
print(a.color2)
print(a.color1)
# greengreen
# whitewhite

class d : 
    def __init__(self,p2 = 2 ,p3 = 3) : 
        self.power2 = p2**2
        self.power3 = p3**3
a = d()
print(a.power2)
print(a.power3)
# 4
# 27
# وممكن اقوم انا بتعيينها و الغاء القيم المفترضة 
# (1)
class car() : 
   def __init__(self,color1="white",color2="green"):
       self.color1=color1*2
       self.color2=color2*2
a=car(1,2)
print(a.color2)
print(a.color1)
# 4
# 2
# (2)
class car() : 
   def __init__(self,color1="white",color2="green"):
       self.color1=color1*2
       self.color2=color2*2
a=car(color2=2,color1=1)
print(a.color2)
print(a.color1)
# 4
# 2



# تعريف دالة بداخلها
# (1)
class car() : 
   def __init__(self,nn,color1="white",color2="green"):
       self.color1=color1*2
       self.color2=color2*2
       self.color3=nn
   def newcolor(self):
       print(self.color3*3)
a=car("blue")
a.newcolor()
# blueblueblue

# (2)
class d :  
    def __init__(self,nn,p2 = 10 ,p3 = 100) : 
        
        self.power2 = p2**2
        self.power3 = p3**3
        self.roots = nn
        
    def root(self ) : 
        print (self.roots**0.5)
    
a = d(25)
a.root()
# 5

class d :  
    def square(n) : 
        print (n**2)
    
    def summ(a,b,c,d,e,f) : 
        return ((a+b-c+e)*(d+f))

a = d    
a.square(0)
print (a.summ(0,2,3,4,5,7))
# 0
# 44











































































