def liniowa(x):
    wynik=2*x+2
    return wynik

assert liniowa(0)==2,"funkcja powinna zwrocic 2"


lista=[1,2,3,4,5,6]
print(lista[0:])

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

#LISTY SKŁADANE

list1=[1,2,3,4,5,6,7,8]

nowa=[]

for i in list1:
    if i%2==0:
        nowa.append(i)

nowa2=[x for x in list1 if x%2==0]

inne3=[2*x for x in list1 if x%2==0]

print(nowa2)

#ZBIORY SKŁADANE

zbior={x for x in list1 if x%2==0}

#generator

generator=(x for x in list1)

for x in generator:
    print(x)
#NIE PRZECHOWUJEMY CALEJ TUPLI W PAMIECI - tylko moc obliczeniowa

#funkcje wbudowane FILTER

liczby=[1,2,3,4,5,6,7,8]

def czy_pa(x):
    return x%2==0
cos=filter(czy_pa,liczby)
listaa=list(cos)
print("filter", listaa)

#musi byc w petli for
for i in cos:
    print("i", i)

#map funkcja  iter cos po czym mozna przechodzi lista generator filter object
def plus(x):
    return x+1
cos1=map(plus,liczby)

print("map", cos1)
for i in cos1:
    print("mapz for",i)

import functools

####reduce  functtools  reduce wykonuje funkcje na 2 argumentach

s=0
for i in liczby:
    s=s+1

def suma(x,y):
    return x+y

ss=functools.reduce(suma,liczby)

# reduce 2

liczba2=[1,2,3,4,5]

suma=1
for i in liczba2:
    suma=suma*i # suma=f(suma,i)

print("suma", suma)

def f(x,y):

    return x*y

wynik=functools.reduce(f,liczba2)

wynikbezf=functools.reduce(lambda x,y:x*y,liczba2)

print("zlambda",wynikbezf)

print(wynik)

