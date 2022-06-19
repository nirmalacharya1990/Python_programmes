qty=int(input('Enter the value for number of quantities purchased: '))
price=float(input('enter the price of  single item: '))
if qty >=1000:
   dis =10
else:
   dis=0
totalexp=qty*price-qty*price*dis/1000
print('Total Expense is: {}'.format(totalexp))

