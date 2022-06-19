#from unicodedata import decimal


#a=1+2j
#print(a.imag)
#print(a.conjugate())

#print( (bin(110000110)))
#print(bin(467))

#Converting Binary to Decimal
#def binarytodecimal():
binary1=input("Enter a binary number:" )
binary=int(binary1)
decimal,i,decy=0,0,0
temp=0
while (binary != 0):
    decy=binary%10
    temp=decy*pow(2, i)
    decimal=temp+decimal
    binary=binary//10
    i += 1
print("The decimal value for binary number {} is {}".format(binary1,decimal))

#binarytodecimal()

