# 15 . Shapes


# رسوم هندسية بالأمر      matplotlib.patches
# وهي تشتمل علي عدد من الاشكال : 

# Rectangle , Circle  , Polygon  , Ellipse  , Arc

# أمر Circle
import matplotlib.patches as pat
import matplotlib.pyplot as plt 

c = pat.Circle((0.5, 0.5),radius=0.1)

ax = plt.axes()
ax.add_patch(c)



# خصائص
c = pat.Circle((0.5, 0.5),radius=0.1
               ,edgecolor='red',facecolor='g',alpha=0.5)

ax = plt.axes()
 
ax.add_patch(c)



# انتظام شكل الدائرة , عبر الحدود
ax = plt.axes()
ax.set_xlim(-1,2)
ax.set_ylim(-0.5,1.5)



# تطبيق اخر
c = pat.Circle((-2,5),radius=4
               ,color='b', alpha=1)

 
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-2,12)

ax.add_patch(c)



# الشكل البيضاوي
import matplotlib.patches as pat
import matplotlib.pyplot as plt 

c = pat.Ellipse((-2,5),2,3,20,color='r')
#center , width , height , angle , color
 
ax = plt.axes()
ax.set_xlim(-5,5)
ax.set_ylim(0,8)

ax.add_patch(c)



# مربع او مستطيل
import matplotlib.patches as pat
import matplotlib.pyplot as plt 

c = pat.Rectangle((0.2, 0.2), 1, 1.2, color='r',angle =20 )
 #location of southwest ,width ,hight ,color , angle
ax = plt.axes()
ax.set_xlim(-1,2)
ax.set_ylim(-0.5,1.5)

ax.add_patch(c)



# مثلث
import matplotlib.patches as pat
import matplotlib.pyplot as plt 

c = pat.Polygon(((-7,-7), (5,-2), (-5,5)) ,color='b')
# vertices , color
 
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

ax.add_patch(c)



# مضلع باربع اضلاع
import matplotlib.patches as pat
import matplotlib.pyplot as plt 

c = pat.Polygon(((-7,-7),(5,-2),(2,7),(-5,5)) ,color='b')
# vertices , color
 
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

ax.add_patch(c)



# النقاط تكون بالترتيب
import matplotlib.patches as pat
import matplotlib.pyplot as plt 

c = pat.Polygon(((-7,-7),(5,-2),(-5,5),(2,7)) ,color='b')
# vertices , color
 
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

ax.add_patch(c)



# اي عدد من  من الاضلاع , النقاط بالترتيب
import matplotlib.patches as pat
import matplotlib.pyplot as plt 

c = pat.Polygon(((-7,-7),(0,-8),(5,-7),(8,0),
                 (0,-3),(3,8),(0,10),(-10,5)),
                color='b')
# vertices , color
 
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

ax.add_patch(c)



# القوس
import matplotlib.patches as pat
import matplotlib.pyplot as plt 

c = pat.Arc((3,2),7,10,theta1=0,theta2=80  )
# center , width , height ,start angle , end angle
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.add_patch(c)


# تغيير الخصائص + اللون
c = pat.Arc((3,2),7,10,theta1=80,theta2=300,color='r' )
# center , width , height ,start angle , end angle,color
 
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

ax.add_patch(c)



# مثال
c = pat.Arc((3,2),7,10,theta1=180,theta2=90,color='b')
# center , width , height ,start angle , end angle,color
 
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

ax.add_patch(c)


