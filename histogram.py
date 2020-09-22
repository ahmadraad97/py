# 6. Histogram
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# وهو امر خاص بالتكتلات , سواء اعمدة او نقاط مثال بسيط
data = np.random.randn(5000)
plt.hist(data)


# خصائص
data = np.random.randn(5000)

plt.hist(data, bins=50, normed=True,
         alpha=0.5,histtype='step',color='blue')
plt.hist(data, bins=50, normed=True,
         alpha=0.5,histtype='bar',color='r')




# جرافين معا
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
for col in 'xy':
    plt.hist(data[col], normed=True, alpha=1)


# اكثر من واحد 
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

plt.hist(x1,histtype='bar',
         alpha=0.3, normed=True, bins=100)
plt.hist(x2,histtype='step',
         alpha=0.7, normed=True, bins=100)
plt.hist(x3,histtype='stepfilled',
         alpha=1, normed=True, bins=100)




