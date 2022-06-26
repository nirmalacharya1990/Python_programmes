##this programme is to check if a point is in the circle or not using function
##reference Stackoverflow
##create a cicrcle unit
##the detail contains cordinates of  Origin and Radius
import math
mycircle=((0,0),2)
##create Points 
mypoint1=(2,3)
mypoint2=(4,5)

#write function to find distance between points 
def distance(point1,point2):
   return math.sqrt((pow((point1[0]-point2[0]),2))+(pow((point1[1]-point2[1]),2)))

#write function to check point in  circle or not
def incircle(point,circle):
    origin,radius=circle
    return radius >= distance(point,origin) ##Returns True if the radius is greater that distance between 2 points.This means  the given point is inside in circle

print(incircle(mypoint1,mycircle)) ##Returns False if Point doesn't fall in Circle

print(incircle(mypoint2,mycircle))



