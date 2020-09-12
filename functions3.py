def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue') :
    print ( "(-- This parrot wouldn't", action)
    print ("if you put", voltage, "volts through it.")
    print ("-- Lovely plumage, the", type)
    print ("-- It's", state, "!")
parrot(100)
# if you put 100 volts through it.
parrot(voltage=100)
# if you put 100 volts through it.
parrot(voltage=10,action=8)
# (-- This parrot wouldn't 8
# if you put 10 volts through it.


parrot(action=4,voltage=20)
# (-- This parrot wouldn't 4
# if you put 20 volts through it.


parrot('million','thousand','jump')
# (-- This parrot wouldn't jump
# if you put million volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's thousand !




def parrot(voltage, state='a stiff', action='voom'):
    print ("-- This parrot wouldn't", action),
    print ("if you put", voltage, "volts through it."),
    print ("E's", state, "!")

d = { "state": "bleedin' demised","voltage": "four million", "action": "VOOM"}
parrot(**d)
# -- This parrot wouldn't VOOM
# if you put four million volts through it.
# E's bleedin' demised !





def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue') :
    print ( "-- This parrot wouldn't", action)
    print ("if you put", voltage, "volts through it.")
    print ("-- Lovely plumage, the", type)
    print ("-- It's", state, "!")

parrot()
# يجب تعريف قيمة على الاقل
parrot(voltage=5.0, 'dead') 
# لا يمكن تعريف قيمة بمفتاح وترك الاخرى بدون مفتاح
parrot(110, voltage=220)
# تم تعريف القيمة الاولى التي هي نفسها voltage
parrot(actor='John Cleese')
# المفتاح غير موجود اساسا 

# يمكن البدء بتعريف قيمة بدون مفتاح والباقي بمفتاح اما العكس لا
parrot(110, action=220)
# -- This parrot wouldn't 220
# if you put 110 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !





































