import numpy as np
print("The value of pi is {}".format(np.pi))
# The value of pi is 3.141592653589793

print('{0} and {1}'.format('red', 'blue'))
# red and blue

print('{1} and {0}'.format('red', 'blue'))
# blue and red

print("First: {first}. Last: {last}.".format(last='Z', first='A'))
# First: A. Last: Z.

print("pi = {0:.3}".format(np.pi))
# pi = 3.142

print("pi = {0:.3}".format(np.pi))
# pi = 3.14

print('{:s} {:d} years old'.format('Im',20))
# Im 20 years old

print('|' + '{:^20}'.format('Hello') + '|')
# |       Hello        |

# الارقام تبدا من 1 ويمكن كتابة النص بدون s
print('{0:10} ==> {1:10d}'.format('name', 56322))
# name       ==>      56322

import re
email = re.compile('\w+@\w+\.[a-z]{3}')
text = "To email Guido, try guido@python.org or guido@google.com "
print(email.findall(text))

import re
text = "To email Guido, try guido@python.org or guido@google.com "
email3=re.compile(r'([\w]+)@(\w+)\.([a-z]{3})')
print(email3.findall(text))
# [('guido', 'python', 'org'), ('guido', 'google', 'com')]

import re
email4=re.compile(r'(?P<user>[\w.]+)@(?P<domain>\w+).(?P<suffix>[a-z]{3})')
match=email4.match('guido@python.org')
print(match.groupdict())
# {'user': 'guido', 'domain': 'python', 'suffix': 'org'}


































