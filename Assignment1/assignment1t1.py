# hello
calls = open("calls.txt","r")
calllist = []
for call in calls:
    calllist.append(call.split(';'))

customers = open("customers.txt", "r")
customerlist = []
for customer in customers:
    customerlist.append(customer.split(';'))


#for customer in customerlist:
    #print(customer)

#for call in calllist:
    #print(call)

def getNumber(number):
    ac= str(number)[0:3]
    middleDigits = str(number)[3:6]
    finalDigits = str(number)[6:]
    customerNumber = "(" + ac + ")" + " " + middleDigits + " " + finalDigits
    return customerNumber

def Numberofcalls(phoneNumber,calllist):
    count = 0
    for calls in calllist:
        if calls[1] == phoneNumber:
            count += 1
    return (count)


def getDuration(duration, calllist):
    callTime = 0
    for calls in calllist:
        if calls[]


def getDueammount(arg):
    pass

print(Numberofcalls("7801234567", calllist))
