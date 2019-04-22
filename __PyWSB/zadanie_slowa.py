print('''
#####################################################
# Napisz funkcję o nazwie 'slowa' zwracającą liczbę
# różnych słów w podanym tekście przyjmowanym
# poprzez parametr funkcji.
# Przyjmujemy, że:
#   Słowo jest to zbiór głosek, który w zapisie
#   graficznym oddzielony jest od innych zbiorów
#   spacjami bądź znakami interpunkcyjnymi
# Przykładowo, dla napisu "Ala ma kota." wynikiem
# jest liczba 3 - w tekście znajdują się trzy różne słowa.
#   liczba_slow = slowa("Ala ma kota.")
#   print(liczba_slow)
# Wskazówki:
# * do rozdzielenia napisu na słowa użyj metody split()
#   przykład:
#     s = 'ala ma kota'
#     lista_slow = s.split()
# * do zamiany wielkich liter na małe lub odwrotnie
#   użyj metod lower() i upper()
#   przykład:
#     s = 'Ala Ma Kota'
#     male = s.lower()
# * użyj zbioru do rozróżnienia słów
# * liczbę elementów w zbiorze otrzymasz za pomocą
#   funkcji len()
#   przykład:
#     s = {1, 4, 2, 6}
#     liczba_elementow = len(s)
#####################################################
''')
import re

def slowa(x):
    if x=='':
        return 0
    n=x.lower()
    s = re.split(r'[\s\W\-\n\.\,)]+', n)
    if '' in s:
       s.remove('')

    z=set(s)
    count =len(z)

    return count





# miejsce na rozwiązanie

print('Sprawdzenie poprawności rozwiązania... Test 1/11...')
liczba_slow = slowa('')
assert liczba_slow == 0, 'Napis pusty nie zawiera żadnego słowa, Twoja funkcja zwróciła wartość {}.'.format(liczba_slow)
print('Sprawdzenie poprawności rozwiązania... Test 2/11...')
liczba_slow = slowa('Kot')
assert liczba_slow == 1, 'Napis "Kot", zawiera 1 słowo, Twoja funkcja zwróciła wartość {}.'.format(liczba_slow)
print('Sprawdzenie poprawności rozwiązania... Test 3/11...')
liczba_slow = slowa('Ala Ala')
assert liczba_slow == 1, 'Napis "Ala Ala", zawiera 1 słowo, Twoja funkcja zwróciła wartość {}.'.format(liczba_slow)
print('Sprawdzenie poprawności rozwiązania... Test 4/11...')
liczba_slow = slowa('Ala ala')
assert liczba_slow == 1, 'Napis "Ala Ala", zawiera 1 słowo, Twoja funkcja zwróciła wartość {}.'.format(liczba_slow)
print('Sprawdzenie poprawności rozwiązania... Test 5/11...')
liczba_slow = slowa('Ala ma kota.')
assert liczba_slow == 3, 'Napis "Ala ma kota." zawiera 3 słowa, Twoja funkcja zwróciła wartość {}.'.format(liczba_slow)
print('Sprawdzenie poprawności rozwiązania... Test 6/11...')
liczba_slow = slowa('Ala Ala.')
assert liczba_slow == 1, 'Napis "Ala Ala.", zawiera 1 słowo, Twoja funkcja zwróciła wartość {}.'.format(liczba_slow)
print('Sprawdzenie poprawności rozwiązania... Test 7/11...')
liczba_slow = slowa('Ala    Ala.   ')
assert liczba_slow == 1, 'Napis "Ala    Ala.   ", zawiera 1 słowo, Twoja funkcja zwróciła wartość {}.'.format(liczba_slow)
print('Sprawdzenie poprawności rozwiązania... Test 8/11...')
liczba_slow = slowa('Ala\nAla.')
assert liczba_slow == 1, 'Napis "Ala\nAla.", zawiera 1 słowo, Twoja funkcja zwróciła wartość {}.'.format(liczba_slow)
print('Sprawdzenie poprawności rozwiązania... Test 9/11...')
liczba_slow = slowa('Ala ma kota.Ala ma kota.')
assert liczba_slow == 3, 'Napis "Ala ma kota.Ala ma kota.", zawiera 3 różne słowa, Twoja funkcja zwróciła wartość {}.'.format(liczba_slow)
print('Sprawdzenie poprawności rozwiązania... Test 10/11...')
liczba_slow = slowa('Wojewodztwo kujawsko-pomorskie.')
assert liczba_slow == 3, 'Napis "Wojewodztwo kujawsko-pomorskie.", zawiera 3 różne słowa, Twoja funkcja zwróciła wartość {}.'.format(liczba_slow)
print('Sprawdzenie poprawności rozwiązania... Test 11/11...')
tekst = '''
Biała dziura - hipotetyczne przeciwieństwo czarnej dziury. Według teorii biała dziura
miałaby być obszarem, gdzie zarówno energia, jak i materia wypływają z osobliwości.
Dotychczasowe badania nie potwierdziły istnienia białych dziur.'''
''''''
liczba_slow = slowa(tekst)
assert liczba_slow == 27, 'Napis "{}", zawiera 27 różnych słów, Twoja funkcja zwróciła wartość {}.'.format(tekst, liczba_slow)
print("Rozwiązanie poprawne.")

