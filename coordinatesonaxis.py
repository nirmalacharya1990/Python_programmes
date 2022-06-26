x,y=map(int,input('Enter the Cordinates  of point separated by space: ').split())
print(x,',',y)
if (x==0 and y!=0):
    print ('The coordinates are on Y axis')
elif (y==0  and x!=0):
    print('The corordinatea are on X axis')
elif (x==0 and y==0):
    print('The point is origin')
else:
    print('The Point neither lies on X axis nor Y axis')



