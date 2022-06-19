#Programme  to check Even or Odd
var1=int(input('Enter the number  to check if it\'s even or odd: ' ))
if var1%2 == 0:
    print ('The Number is even')
else:
    print ('The number is odd')

#Check whether the year is Leap Year or not
year=int(input('Enter the Year to check if it\'s leap year or not: '))

if ((year%400==0) or (year%100==0) and (year%4==0)):
    print ('Given Year is leap Year')
else:
    print('Not a Leap Year')

# Programme to Check Youngest Age
rage=int(input('Enter Age for Ram: '))
sage=int(input('Enter Age for Shyam: '))
aage=int(input('Enter Age for Ajay: '))

if ((rage<sage)  and (rage<aage)):
    print ('Ram is youngest')
elif ((sage<rage) and (sage<aage)):
    print ('Shyam is  the youngest one')
elif ((aage<rage) and (aage<sage)):
    print ('Ajay is the youngest one')
else:
    print ('Pass')