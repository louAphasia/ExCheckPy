set={False,3,4.5,'cat'}

setdwa={5,6,7,'dog'}

newset=set.union(setdwa)

print(newset)

print(setdwa.pop())
setok=("false", 2,4.5)
setokdwa=("t", True,3)

print({3}.issubset(setok))

#------------------------

myDi={"lu":1234,"ka":345,"jan":345}

print(myDi.keys())
print(myDi.values())
print(myDi.items())

print(myDi.get('lu',"ka"))

print(myDi.get('k',"nie ma"))

print("my cat nr is %2.4f"%(myDi["ka"]))