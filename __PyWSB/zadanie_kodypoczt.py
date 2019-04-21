
print('''
#################################################
# ***Zadanie trudniejsze***
# Napisz funkcję o nazwie kody przyjmującą
# dwa parametry - kody pocztowe jako napisy
# w formacie XX-XXX, a zwracającą listę kodów
# pocztowych pomiędzy nimi. Nie rozważamy
# poprawności kodów pocztowych.
# Przykład:
# s = kody('01-000', '02-003')
# print(s)  # ['01-001', '01-002', ... , '02-001', '02-002']
#################################################
''')

import re

def kody(x,y):
    if re.match(r'[0-9]{2}-[0-9]{3}',x):
        print("ok")
    else: print("zle dane")
    if re.match(r'[0-9]{2}-[0-9]{3}',y):
        print("ok")
    else: print("zle dane")
    n=x.split('-')
    m=y.split('-')
    p=n[0]
    r=m[0]
    l=n[1]
    b=m[1]
    print(p)
    print(m)

# miejsce na rozwiązanie


kody('00-001','00-120')