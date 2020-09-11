for m in range(1,10,2):
    print(m)
# 1
# 3
# 5
# 7
# 9

# لا يجب وضع نقطتين او مسافة بادئة للطباعة
g=[(x,y)for x in [1,2,3] for y in[1,2,3] if x != y]
print(g)
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

y='hello python'
for n in range(len(y)):print(n)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11

for n in range(len(y)):print(y[n])
# h
# e
# l
# l
# o
# 
# p
# y
# t
# h
# o
# n

s=''
d="hello python"
for n in range(len(d)):
    s=s+d[(len(d)-n-1)]
print(s)
# nohtyp olleh















































