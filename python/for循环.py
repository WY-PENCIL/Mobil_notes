aList={"a":1, "b":2, "c":3, "d":4}
for user,status in aList.copy().items():
    if status == 1:
        del aList[user]
print(aList)


a = []
b = a+[5]
print(b)

def testList(a,b={'sum':0}):
    b['sum'] = a+b['sum']
    return b
print(testList(1))
print(testList(2))
print(testList(3))