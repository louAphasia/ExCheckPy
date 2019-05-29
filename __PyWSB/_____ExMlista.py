lista=[2,3,4,5,5,7,2]

print(len(lista))

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


while True:
    print('ok')
    if 2>1:
       False











#print('alalal')
#print(lista.reverse())
#print(lista)