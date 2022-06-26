x1,y1=map(int,input('Enter the Cordinates of first Point  separated by space= ').split())
x2,y2=map(int,input('Enter the Co-ordinates of 2nd Pointseparated by space= ').split())
x3,y3=map(int,input('Enter the cordinates of 3rd pointseparated by space=').split())

print ( 'The First Cordinates are %s,%s' %(x1,y1))
print ('The second Cordinates are {},{}'.format(x2,y2))
print (f'The 3rd Cordinates are {x3,y3}')

areaofpts=x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)

if(areaofpts==0):
    print('The points (',x1,',', y1, ') , (',x2,',',y2,') , (',x3,',',y3,')' ' are  Collinear')
else:
    print('The points (',x1,',', y1, ') , (',x2,',',y2,') , (',x3,',',y3,')' ' are not  Collinear')
    
