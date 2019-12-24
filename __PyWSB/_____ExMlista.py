a=[1,2,3,4,5]
b=a
a.append(6)

print('a',a)
print('b',b)

def f():
    print("hello")


g=f
g()
print('g',g())
print('g bez', g)


def listaa(n):
    i=0
    nr=[]
    while i<n:
        nr.append(i)
        i=i+1
    return nr

for x in listaa(5):
    print('e',x)

lista=[2,3,4,5,5,7,2]

print(len(lista))
y=0
x=4
try:
    z=x/y
except Exception as e:
    print("ok" ,e)

print("lol ", (x+y))

e=2
if e not in lista:
    raise ValueError
i=lista.index(e)
print(i)

for w in range(len(lista[i+1:])):
  if lista[w]==e:
      print('yes')
      del lista[w]
'''
x=4
listaa=[2,3,4,3,4,5,4,4]

def usun(listaa,x):
    indices = [i for i, x in enumerate(listaa) if x == 4]
    print(indices)

    for x in indices[1:]:
        listaa[x]='del'
        print(listaa)
        newlist=[]
        for x in listaa:
            if x!='del':
                newlist.append(x)
    return newlist
==================================
def main():
    while True:
        capacity=int(input( " Podaj początkowy rozmiar listy " ))
        lista = MLista(capacity)
        if capacity>=0:
            break

        #else:
            #print("Pojemnosc listy musi byc >=0")

    #lista=MLista(capacity)

class InvalidCapacity(ValueError):
    def __init__(self, msg):   #msg napis opisujacy co sie stalo
        super().__init__(msg)
        
         def __init__(self, capacity):
            self.capacity = capacity
            self.elementy = []
            if capacity < 0 :
                raise InvalidCapacity("Capacity is negative {} ".format(self.capacity))
===============================
2 rozw 
def main():
    while True:
        capacity=int(input( " Podaj początkowy rozmiar listy " ))
        lista = MLista(capacity)
        if capacity>=0:
            break
        else:
            print("Pojemnosc listy musi byc >=0")
            =====================================
            
                def pisz(self):
        print("Rozmiar aktualny listy:", MLista.rozmiar(self))  # self.elementy.rozmiar(self) MLista.rozmiar(self)
        print("Pojemnosc listy : ", self.capacity)
        print("Elementy: ", self.elementy)
            
print(usun(listaa,x))'''

x=2
elementy=[2,3,2,2,2,5]
indices = [i for i, a in enumerate(elementy) if a == x]
print(indices)
for x in indices[1:]:
    elementy[x] = 'del'
print(elementy)
elementy=[x for x in elementy if x!='del']
print(elementy)














#print('alalal')
#print(lista.reverse())
#print(lista)