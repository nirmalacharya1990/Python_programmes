ci_x1,ci_y1=map(int,input('Enter Cordinates for center of the circle separated by Space: ').split())
radius=float(input('Enter value for radius of the  circle: '))
x2,y2=map(int,input('Enter the c-ordinates of points to be checked if they are inside circle or not: ').split())

import math
#def isInside(ci_x1,ci_y1,x2,y2,radius):
if ((pow((x2-ci_x1),2)+pow((y2-ci_y1),2)) >= pow(radius,2) ):
        print ('Outside')
else:
        print('Inside')