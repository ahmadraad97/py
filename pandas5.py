
import pandas as pd
import numpy as np



# كتابة جدول
a=pd.DataFrame(np.random.rand(3,4),columns=['laptop','mobile','tablet','E_reader'],index=['feb','mar','sep'])
print(a)
#        laptop    mobile    tablet  E_reader
# feb  0.862949  0.492020  0.315512  0.054492
# mar  0.757622  0.957805  0.432374  0.157055
# sep  0.912239  0.051822  0.121270  0.698241
print('-------------------------')
# عمليات حسابية مع اعمدة
a['total']=(a['laptop']+a['mobile']+a['tablet']+a['E_reader'])
print(a)
#        laptop    mobile    tablet  E_reader     total
# feb  0.862949  0.492020  0.315512  0.054492  1.724973
# mar  0.757622  0.957805  0.432374  0.157055  2.304856
# sep  0.912239  0.051822  0.121270  0.698241  1.783572
print('-------------------------')
b=(a['laptop']+a['mobile']+a['tablet']+a['E_reader'])
print(b)
# feb    1.724973
# mar    2.304856
# sep    1.783572
print('-------------------------')
total=(pd.eval('a.laptop+a.mobile+a.tablet+a.E_reader'))
print(total)
# feb    1.724973
# mar    2.304856
# sep    1.783572
print('-------------------------')


# اظهار صفوف بشروط محددة
print(a)
#        laptop    mobile    tablet  E_reader     total
# feb  0.124076  0.518070  0.091397  0.494942  1.228485
# mar  0.569775  0.211564  0.140963  0.418694  1.340996
# sep  0.767093  0.853031  0.373227  0.461816  2.455167
print('-------------------------')

result = a.query('mobile <= 0.5 and tablet <= 0.5')
print(result)
#        laptop    mobile    tablet  E_reader     total
# mar  0.569775  0.211564  0.140963  0.418694  1.340996
print('-------------------------')

tmp1 = a.mobile <= 0.5
tmp2 = a.tablet <= 0.5
tmp3 = tmp1 & tmp2
result = a[tmp3]
print(result)
#        laptop    mobile    tablet  E_reader     total
# mar  0.569775  0.211564  0.140963  0.418694  1.340996
print('-------------------------')

result = a[(a.mobile <= 0.5) & (a.tablet <= 0.5)]
print(result)
#        laptop    mobile    tablet  E_reader     total
# mar  0.569775  0.211564  0.140963  0.418694  1.340996
print('-------------------------')

result = a[(a.mobile <= 0.5) | (a.tablet <= 0.5)]
print(result)
#        laptop    mobile    tablet  E_reader     total
# feb  0.124076  0.518070  0.091397  0.494942  1.228485
# mar  0.569775  0.211564  0.140963  0.418694  1.340996
# sep  0.767093  0.853031  0.373227  0.461816  2.455167




# باستخدام دالة

def make_df(cols, ind):
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data,)

print(make_df('ABC', range(3)))
#     A   B   C
# 0  A0  B0  C0
# 1  A1  B1  C1
# 2  A2  B2  C2

















































































































































































































