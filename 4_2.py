bs=int(input("Enter Basic Salary for the Employee: "))
if bs >= 1500:
    hra=500
    da=bs*98/100
else:
    hra=bs*10/100
    da=bs*90/100
gs=bs+hra+da
print("Gross salary is: {}".format(gs))