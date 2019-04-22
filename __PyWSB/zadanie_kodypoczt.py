import re
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

"""def kod2numer(kod):
    czesci = kod.split('-')
    czesc1 = int(czesci[0])*1000# pierwsza czesc kodu to tysiace
    czesc2 = int(czesci[1])
    print(czesc1,czesc2)
    return czesc1 + czesc2

# konwertuje numer na kod pocztowy i formatuje do poprawnego stringa
def numer2kod(num):
    czesc1 = num / 1000 # czesci tysieczne
    czesc2 = num % 1000 # reszta
    kod = '%02d-%03d' % (czesc1,czesc2) # formatowanie z tzw leading zeros
    return kod

def kody(kod1, kod2):
    tablica = [] # tu damy wyjscie
    kod1_to_numer = kod2numer(kod1) # konwersja argumentow na numery
    kod2_to_numer = kod2numer(kod2)

    if kod1_to_numer > kod2_to_numer:
        print('Blad, pierwszy kod wiekszy niz drugi')
        return tablica # zwracamy pusta tablice

    for kod in range(kod1_to_numer + 1, kod2_to_numer): # petla nie zawiera kodu poczatkowego
        kod_napis = numer2kod(kod) # konwersja z powrotem na stringi
        tablica.append(kod_napis) # dodaj do tablicy
    return tablica # zwroc tablice


print(kody('01-000','02-003'))"""

# miejsce na rozwiązanie

def kody(kod1, kod2):
    tablica = []  # tu damy wyjscie



    # podzielmy po dywizie
    czesci1 = kod1.split('-')
    czesci2 = kod2.split('-')

    if len(czesci1) != 2:
        print('Zly format kodu kod1')
        return tablica  # zwracamy pusta tablice
    if len(czesci2) != 2:
        print('Zly format kodu kod2')
        return tablica  # zwracamy pusta tablice



    # konwersja argumentow na numery
    kod1_numer = int(czesci1[0]) * 1000 + int(czesci1[1])
    kod2_numer = int(czesci2[0]) * 1000 + int(czesci2[1])

    if kod1_numer > kod2_numer:
        print('Blad, pierwszy kod wiekszy niz drugi')
        return tablica  # zwracamy pusta tablice

    for kod in range(kod1_numer + 1, kod2_numer):  # petla nie zawiera kodu poczatkowego
        # konwertuje numer na kod pocztowy i formatuje do poprawnego stringa
        kod_tysiace = kod / 1000  # czesci tysieczne
        kod_reszta = kod % 1000
        # konwersja z powrotem na stringi
        kod_napis = '%02d-%03d' % (kod_tysiace, kod_reszta)  # formatowanie z tzw leading zeros
        tablica.append(kod_napis)  # dodaj do tablicy
    return tablica  # zwroc tablice


# testujmy
print(kody('01-000', '02-003'))


