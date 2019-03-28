lista= ["zero", 3,"cat", "dog"]

for item in lista:
    print(item)

di={"name": 'Ann',"age":22,'pet':"cat"}

for key,va in di.items():
    print("%s --->>> %s " %(key,va))


########
x=0
y=True
while x<=5 and y:  # and false or true warunek
    print("yesss")
    x+=1
    y=bool(x<4)

#### Dictionery and for

for v in di:  # default keys
    print(v)