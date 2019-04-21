s="abbbcccsss"

print(chr(97))
print(ord('a'))


def dec_to_bin(x):
    return int(bin(x)[2:])

print(dec_to_bin(97))

'''Tekst do kompresji: aabbcc

Slownik: abc

Dlugosc tekstu przed kompresja: 6
Unikalnych liter: 3
Liczba bitow na znak: 2
Liczba nadmiarowych 1: 1

z 8 podzielone ile 
8-(3+dlugosc tekstu*N)%8)%8
00100000 10110101

32 181 --->asci jaki znak


Skompresowany tekst: abc Á
Dlugosc tekstu po kompresji: 2


Press any key to continue . . .'''