def liniowa(x):
    wynik=2*x+2
    return wynik

assert liniowa(0)==2,"funkcja powinna zwrocic 2"


lista=[]
moja_lista=[1,2,3,'ala']
moja_lista.append(99)

for n in moja_lista:
    print(n)

napis ="Ala ma kota"

wlkn=napis.upper()
print(wlkn,len(wlkn))

def prawda():
    return True
def concat(n,m):
   w=n+m
   return w
