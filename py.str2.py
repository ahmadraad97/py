a = "hello python"
print(a[0:6:2])
# hlo(يتجاهل حرف )
print(a[:12:3])
# hlph
print(a[0::4])
# hot
print(a[::2])
# hlopto
print(a[-1:5:1])
# hlopto
print(a[-1:5:-1])
# nohtyp
print(a[::-1])
# nohtyp olleh

print(list(a))
# ['h', 'e', 'l', 'l', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n']
print(sorted(list(a)))
# يرتبها ترتيب تصلعدي
# [' ', 'e', 'h', 'h', 'l', 'l', 'n', 'o', 'o', 'p', 't', 'y']

print(set(a))
# بدون ترتيب وبدون تكرار
# {'n', 'l', 'y', 't', 'p', 'e', 'o', ' ', 'h'}

print(a.split())
# سيفصل بناء على الكلمات
# ['hello', 'python']

x="1234567891233456789"
print(x.split("3"))
# عندما يتكرر الرقم مرتين يضع فراغ
# ['12', '45678912', '', '456789']

y="hhh""fgfh""fdvdth"
print(y.splitlines())
# ['hhhfgfhfdvdth']
b="hhh \nfgfh \nfdvdth"
print(b.splitlines())
# ['hhh ', 'fgfh ', 'fdvdth']































