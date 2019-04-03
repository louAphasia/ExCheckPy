sss=[1,2,3,4,5]

for x in sss:
    print("y"+str(x))
    if x>2:
        print("no"+str(x))
        break
    print("brrrr"+ str(x))

for x in sss:
    print("yes"+str(x))
    if x>2:
        print("c1___" + str(x))
        continue
    print("c"+str(x))
    print("56666666")

while True:
    name=input("name")
    if name=='joe':
        continue
    print("hey")
    password=input("pass?")
    if password=='ppp':
        break
    else:
        print("ok")
print("break rile")