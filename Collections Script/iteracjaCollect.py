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

z=False
m=5
while m>3 and not z:
   print("nooo")
   m-=1
   z=bool(m<3)

#### Dictionery and for

for v in {"ta":23,"ert":2344}:  # default keys
    print(v)

for tuple in (2,'345', True):
    print(tuple)

### for many append for *2

li=["cat", 'dog', 'bird']
a=[]

for m in li:
    for xx  in m:
        a.append(xx)
print(a)

#### for range


for e in range(-1,10,3):
    print(e)


sss=[ch.upper() for ch in 'comph' if ch not in 'aeiou']
print(sss)