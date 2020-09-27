# 16 . Images


# قراءة الصور  imread 
import matplotlib.pyplot as plt 


a = plt.imread('D:\\1t\\tt.jpg')


print(a.shape)
# (1073, 1080, 3)
print(a)
# [[[255 255 255]
#   [255 255 255]
#   [255 255 255]
#   ...



# عدد البيانات
import matplotlib.pyplot as plt 
a = plt.imread('D:\\1t\\tt.jpg')

print(a.size)
# 3476520




# قراءة مصفوفة الصور و كتابتها في ملف   txt  
import matplotlib.pyplot as plt 
a = plt.imread('D:\\1t\\tt.jpg')

f= open("D:\\2.txt","w+")

b,c,d = a.shape

for x in range(b):
    for y in range(c):
        for z in range(3):
            f.write('\n' + str('Data for : ' +str(x) 
            +' & ' + str(y) +' & ' + str(z)) +' is :  '
            + str((a[x,y,z])))
f.close()



# Data for : 0 & 0 & 0 is :  255
# Data for : 0 & 0 & 1 is :  255
# Data for : 0 & 0 & 2 is :  255
# Data for : 0 & 1 & 0 is :  255
# Data for : 0 & 1 & 1 is :  255
# Data for : 0 & 1 & 2 is :  255
# Data for : 0 & 2 & 0 is :  255
# Data for : 0 & 2 & 1 is :  255
# Data for : 0 & 2 & 2 is :  255
# Data for : 0 & 3 & 0 is :  255





# اظهار الصورة
import matplotlib.pyplot as plt 

a = plt.imread('D:\\1t\\tt.jpg')

plt.imshow(a)


# اظهار الوان معينة في الصورة
import matplotlib.pyplot as plt 


a = plt.imread('D:\\1t\\tt.jpg')

plt.subplot(221)
plt.imshow(a)

x = a[:,:,0]
plt.subplot(222)
plt.imshow(x)

y = a[:,:,1]
plt.subplot(223)
plt.imshow(y)

z = a[:,:,2]
plt.subplot(224)
plt.imshow(z)




# اقتطاع جزء من الصورة
import matplotlib.pyplot as plt 


a = plt.imread('D:\\1t\\tt.jpg')

plt.subplot(221)
plt.imshow(a)

x = a[:200,:300,:]
plt.subplot(222)
plt.imshow(x)

y = a[120:470,220:550,:]
plt.subplot(223)
plt.imshow(y)

z = a[300:350,450:500,:]
plt.subplot(224)
plt.imshow(z)



# حفظ الصورة
import matplotlib.pyplot as plt 
a = plt.imread('D:\\1t\\tt.jpg')
plt.imsave('D:\\6.jpg', a)


# حفظ جزء من الصورة
import matplotlib.pyplot as plt 
a = plt.imread('D:\\1t\\tt.jpg')
plt.imsave('D:\\6.jpg', a[:,0:500])
b = plt.imread('D:\\6.jpg')
plt.imshow(b)



# ضغط الصورة
import matplotlib.pyplot as plt 


a = plt.imread('D:\\1t\\tt.jpg')

plt.imsave('D:\\6.jpg', a[::15,::15])


b = plt.imread('D:\\6.jpg')
plt.imshow(b)









































































































