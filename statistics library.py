import statistics as st
# متوسط حساي
a=[1,2,3,4]
print(st.mean(a))
# 2,5

# متوسط متجانس
b=st.harmonic_mean((1,2,3,4))
print(b)
# 1,95

# الوسيط
c={1,2,3,4,5}
print(st.median(c))
# 3

# الوسيط لمجموع زوجي
c={1,2,3,4,5,6}
print(st.median(c))
# 3,5

# الوسيط الادنى
c={1,2,3,4,5,6}
print(st.median_low(c))
# 3

# الوسيط الاعلى
c={1,2,3,4,5,6}
print(st.median_high(c))
# 4

# اذا لم يكن هناك وسيط اعلى او ادنى يضع الوسيط المعتاد
c={1,2,3,4,5}
print(st.median_low(c))
# 3

# المنوال
e=[1,1,2,2,2,3,4,4,5]
print(st.mode(e))
# 2

# اذا كان هناك منوالين سيظهر خطا
e=[1,1,2,2,2,3,4,4,4,5]
# print(st.mode(e))
# no unique mode; found 2 equally common values

# الانحراف المعياري
f=[7,8.5,-9,20,100]
print(st.stdev(f))
# 43.016857160885195

# التباين
print(st.variance(f))
# 1850.45
















