
print('''
#####################################################
# Pociąg z miejscowości A do B jedzie z prędkością v1,
# a wraca z miejscowości B do A z prędkością v2.
# Napisz funkcję o nazwie 'szybkosc_srednia' przyjmującą
# dwie liczby - v1 oraz v2, a zwróci średnią szybkość
# na całej trasie.
#
# Przykład:
#   vs = pociag(60, 40)
#   print(vs)
# Na ekranie powinna pojawić się liczba 48.
#####################################################
''')

def szybkosc_srednia(x,y):
    wynik=(2*x*y)/(x+y)
    return wynik

# miejsce na rozwiązanie

print('Sprawdzenie poprawności rozwiązania... Test 1/3...')
otrzymana_szybkosc = szybkosc_srednia(50, 50)
assert otrzymana_szybkosc == 50, 'Średnia prędkość dla 50 i 50 to 50, Twoja funkcja zwróciła {}'.format(otrzymana_szybkosc)
print('Sprawdzenie poprawności rozwiązania... Test 2/3...')
otrzymana_szybkosc = szybkosc_srednia(60, 40)
assert otrzymana_szybkosc == 48, 'Średnia prędkość dla 60 i 40 to 48, Twoja funkcja zwróciła {}'.format(otrzymana_szybkosc)
print('Sprawdzenie poprawności rozwiązania... Test 3/3...')
otrzymana_szybkosc = szybkosc_srednia(60, 12)
assert otrzymana_szybkosc == 20, 'Średnia prędkość dla 60 i 12 to 20, Twoja funkcja zwróciła {}'.format(otrzymana_szybkosc)
print("Rozwiązanie poprawne.")

