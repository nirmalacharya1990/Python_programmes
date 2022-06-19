#PGm to calculate salary
from telnetlib import GA


a=4000
bs=int(a);
print ("Ramesh's Base salary is {}".format(a))
DA=int(4000*0.4)
print  ("The DA for Ramesh is: " +str(DA))

HRA=4000*0.2
print("The HRA  for Ramesh is: {}" .format(HRA))
GA=bs+DA+HRA

#print ("The gross Salary for  Ramesh is Basic Salary:{BS}+DA:{DA}+HRA:{HRA}={GA}".format(BS=bs,DA=DA,HRA=HRA,GA=GA))

print ("Total salary is {}" .format(bs+DA+HRA))
#########################################
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)