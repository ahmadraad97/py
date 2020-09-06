# هل الكل ارقام
a="123"
print(a.isdigit())
# True

# هل الاحرف كلها كبيرة
b="AH"
print(b.isupper())
# True

# هل الاحرف كلها صغيرة
c="ah"
print(c.islower())
# True

# هل اول حرف كبير
d="Ahmad"
print(d.istitle())
# True

# هل تنتهي ب
e="i'm ahmad"
print(e.endswith("ad"))
# True 

# هل تبدا ب
f="i'm ahmad"
print(f.startswith("i'"))
# True

# لضم ما قبلها بما بعدها
g=','.join(('one','tow','three'))
print(g)
# one,tow,three

h="ahmad"
print(' '.join((h)))
# a h m a d

import numpy as np
print(' '.join([str(i) for i in np.random.randint(10,size=100)]))
# 8 4 8 0 7 6 0 3 5 5 0 9 7 8 9 9 7 7 7 9 9 5 2 2 6 8 3 2 7 6 7 8 7 2 1 2 2 0 1 8 8 2 4 3 1 6 6 5 8 8 4 0 3 8 2 7 1 1 7 7 4 6 3 3 7 9 3 8 1 9 4 2 2 7 3 5 8 0 6 3 7 7 3 7 1 4 0 0 2 9 5 7 4 2 7 5 8 3 0 3
































