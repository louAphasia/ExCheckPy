sss=[1,2,3,4,5]

for x in sss:
    print("yes"+str(x))
    if x>2:
        print("no"+str(x))
        break

for x in sss:
    print("di"+str(x))
    if x>2:
        continue
    print("look"+str(x))