import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
#y = json.loads(x)

# the result is a Python dictionary:
#print(y["age"]) 
Str= ['sample1','sample2','sample3']

fileObject = open(r"C:\Users\hp\Downloads\sample2.json")
jsonContent = fileObject.read()
aList = json.loads(jsonContent)
print(aList)
print(aList['phoneNumbers'])
print(aList['address']['streetAddress'],aList['address']['city'])
var=input('Please pass a string to match:  ')
if aList['d']['key1']['nestkey']['subnestkey']== var :
 print(aList['d']['key1']['nestkey']['subnestkey'])
 print('bucketname')

new_var = 'firstName'
#print(aList[new_var])
def new_func():
    return 'address'
#print(aList[new_func()])
#print(aList['color'])