import sys

i = 1

while i < len(sys.argv):
    file_name = sys.argv[i]

    with open(file_name) as f:
        content = f.read()
        print(content)

    i += 1

### listy

             #-5,-4,-3,-2,-1  <---
             #0, 1, 2, 3, 4    -->
moja_lista = [1, 2, 3, 4, 5]

nowa_lista = moja_lista[1:4]

print("nowa lista:", nowa_lista)

print("moja_lista[1:] = ", moja_lista[1:])

print("moja_lista[:] = ", moja_lista[:])

print("moja_lista[:-1] = ", moja_lista[:-1])

# program cat - pętla for

import sys

for file_name in sys.argv[1:]:
    with open(file_name) as f:
        content = f.read()
        print(content)


# funkcje
def na_slowo_z_wielkiej_litery(slowo):
    return slowo[0].upper() + slowo[1:]


moja_lista = ["ala", "ma", "kota"]

nowa_lista = [ na_slowo_z_wielkiej_litery(moja_lista[0]) ] + moja_lista[1:]

print("Pierwsze slowo z wielkiej litery:", nowa_lista)

nowa_lista = []
for element in moja_lista:
    nowe_slowo = na_slowo_z_wielkiej_litery(element)
    nowa_lista.append(nowe_slowo)

print(nowa_lista)

# listy składane (list comprehension)

nowa_lista = [ x for x in moja_lista ]
print("lista składana:", nowa_lista)

nowa_lista = [ na_slowo_z_wielkiej_litery(slowo) for slowo in moja_lista ]
print("slowa z wielkiej litery (lista skladana):", nowa_lista)

# funkcja range

def zakres(i):
    lista = []
    x = 0
    while x < i:
        lista.append(x)
        x += 1
    return lista

for element in range(1000):
    print(element)


print('''
########################################
# program dir
########################################
''')

from sys import argv
from os import listdir
import os.path

names = listdir( argv[1] )

for name in names:
    if os.path.isdir(name):
        print('<DIR>', name)
    else:
        print('     ', name)


## kolejna wersja

from sys import argv
from os import listdir
import os.path

names = listdir( argv[1] )

dirs = [x for x in names if os.path.isdir(x)]
files = [x for x in names if os.path.isfile(x)]

for dir in dirs:
    print("<DIR>", dir)

for file in files:
    print('     ', file)


## kolejna wersja


from sys import argv
from os import listdir
import os.path
import itertools

names = listdir( argv[1] )

dirs = [x for x in names if os.path.isdir(x)]
files = [x for x in names if os.path.isfile(x)]

for name in itertools.chain(dirs, files):
    print(name)

