#####################################################
# UWAGA!                                            #
# ------------------------------------------------- #
# Przy próbie edycji tego pliku zostanie utworzona  #
# jego kopia. W pasku adresu przeglądarki pojawi    #
# się nowy URL wskazujący na zmieniony plik.        #
# Zapisz go sobie, jeśli chcesz mieć dostęp         #
# do swoich zmian.                                  #
#####################################################


print('''
#################################################
# Napisz funkcję o nazwie prawda zwracającą
# wartość True.
#################################################
''')

def prawda():
  return True

print('Sprawdzenie poprawności rozwiązania... Test 1/1...')
assert prawda() is True, "Funkcja powinna zwracać wartość True"
print("Rozwiązanie poprawne.")


print('''
#################################################
# Napisz funkcję o nazwie concat, która:
# * ma dwa parametry (przyjmuje dwa napisy)
# * łączy pierwszy napis z drugim
# * zwraca wynik operacji
#################################################
''')

def concat(m,n):
  w=m+n
  return w# miejsce na rozwiązanie

print('Sprawdzenie poprawności rozwiązania... Test 1/3...')
assert concat("ala", " ma kota") == "ala ma kota", "Funkcja powinna zwracać połączone napisy"
print('Sprawdzenie poprawności rozwiązania... Test 2/3...')
assert concat("jakis ", "napis") == "jakis napis", "Funkcja powinna zwracać połączone napisy"
print('Sprawdzenie poprawności rozwiązania... Test 3/3...')
assert concat("tekst", "bezspacji") == "tekstbezspacji", "Funkcja powinna zwracać połączone napisy"
print("Rozwiązanie poprawne.")


print('''
#################################################
# Napisz funkcję o nazwie parzysta,
# która sprawdza czy liczba jest parzysta
# i zwraca True, w przeciwnym prypadku False.
# Wskazówki:
# * wykorzystaj resztę z dzielenia
#   np. 3 % 2
#   % w jezyku Python oznacza resztę z dzielenia
#   Reszta z dzielenia 3 przez 2 wynosi 1,
#   więc 3 nie dzieli się przez 3 bez reszty.
#   Takie wyrażenie można umieścić w instrukcji if
# Przykład:
# * parzysta(2) = True
# * parzysta(5) = False
#################################################
''')

def parzysta(x):
  if x%2==0:
    return True
  else:
    return False

print('Sprawdzenie poprawności rozwiązania... Test 1/15...')
assert parzysta(0) is True, "Sprawdź poprawność wykonywanych obliczeń, liczba 2 jest parzysta"
print('Sprawdzenie poprawności rozwiązania... Test 2/15...')
assert parzysta(2) is True, "Sprawdź poprawność wykonywanych obliczeń, liczba 2 jest parzysta"
print('Sprawdzenie poprawności rozwiązania... Test 3/15...')
assert parzysta(4) is True, "Sprawdź poprawność wykonywanych obliczeń, liczba 4 jest parzysta"
print('Sprawdzenie poprawności rozwiązania... Test 4/15...')
assert parzysta(10) is True, "Sprawdź poprawność wykonywanych obliczeń, liczba 10 jest parzysta"
print('Sprawdzenie poprawności rozwiązania... Test 5/15...')
assert parzysta(12) is True, "Sprawdź poprawność wykonywanych obliczeń, liczba 12 jest parzysta"
print('Sprawdzenie poprawności rozwiązania... Test 6/15...')
assert parzysta(16) is True, "Sprawdź poprawność wykonywanych obliczeń, liczba 16 jest parzysta"
print('Sprawdzenie poprawności rozwiązania... Test 7/15...')
assert parzysta(18) is True, "Sprawdź poprawność wykonywanych obliczeń, liczba 18 jest parzysta"
print('Sprawdzenie poprawności rozwiązania... Test 8/15...')
assert parzysta(20) is True, "Sprawdź poprawność wykonywanych obliczeń, liczba 20 jest parzysta"
print('Sprawdzenie poprawności rozwiązania... Test 9/15...')
assert parzysta(1) is False, "Sprawdź poprawność wykonywanych obliczeń, liczba 1 jest NIEparzysta"
print('Sprawdzenie poprawności rozwiązania... Test 10/15...')
assert parzysta(3) is False, "Sprawdź poprawność wykonywanych obliczeń, liczba 3 jest NIEparzysta"
print('Sprawdzenie poprawności rozwiązania... Test 11/15...')
assert parzysta(7) is False, "Sprawdź poprawność wykonywanych obliczeń, liczba 7 jest NIEparzysta"
print('Sprawdzenie poprawności rozwiązania... Test 12/15...')
assert parzysta(9) is False, "Sprawdź poprawność wykonywanych obliczeń, liczba 9 jest NIEparzysta"
print('Sprawdzenie poprawności rozwiązania... Test 13/15...')
assert parzysta(11) is False, "Sprawdź poprawność wykonywanych obliczeń, liczba 11 jest NIEparzysta"
print('Sprawdzenie poprawności rozwiązania... Test 14/15...')
assert parzysta(13) is False, "Sprawdź poprawność wykonywanych obliczeń, liczba 13 jest NIEparzysta"
print('Sprawdzenie poprawności rozwiązania... Test 15/15...')
assert parzysta(15) is False, "Sprawdź poprawność wykonywanych obliczeń, liczba 15 jest NIEparzysta"
print("Rozwiązanie poprawne.")


print('''
#################################################
# Napisz funkcję o nazwie ostatnie zwracającą
# jako napis dwie ostatnie cyfry podanej liczby.
# Jeśli podana liczba jest jednocyfrowa,
# wynik na początku powinien zawierać dodatkowe 0.
# Przykład:
# * ostatnie(1) = "01"
# * ostatnie(9) = "09"
# * ostatnie(11) = "11"
# Wskazówki:
# * funkcja przyjmuje tylko jeden parametr
# * do zamiany liczby na napis użyj funkcji str()
#################################################
''')

def ostatnie(x):
  t=str(x)
  if len(t)>1:
    return t[-2:]
  elif len(t)==1:
    w="0"+t
    return w



print('Sprawdzenie poprawności rozwiązania... Test 1/9...')
assert ostatnie(0) == "00", "Sprawdź poprawność wykonywanych obliczeń"
print('Sprawdzenie poprawności rozwiązania... Test 2/9...')
assert ostatnie(1) == "01", "Sprawdź poprawność wykonywanych obliczeń"
print('Sprawdzenie poprawności rozwiązania... Test 3/9...')
assert ostatnie(9) == "09", "Sprawdź poprawność wykonywanych obliczeń"
print('Sprawdzenie poprawności rozwiązania... Test 4/9...')
assert ostatnie(10) == "10", "Sprawdź poprawność wykonywanych obliczeń"
print('Sprawdzenie poprawności rozwiązania... Test 5/9...')
assert ostatnie(11) == "11", "Sprawdź poprawność wykonywanych obliczeń"
print('Sprawdzenie poprawności rozwiązania... Test 6/9...')
assert ostatnie(21) == "21", "Sprawdź poprawność wykonywanych obliczeń"
print('Sprawdzenie poprawności rozwiązania... Test 7/9...')
assert ostatnie(100) == "00", "Sprawdź poprawność wykonywanych obliczeń"
print('Sprawdzenie poprawności rozwiązania... Test 8/9...')
assert ostatnie(132) == "32", "Sprawdź poprawność wykonywanych obliczeń"
print('Sprawdzenie poprawności rozwiązania... Test 9/9...')
assert ostatnie(523452) == "52", "Sprawdź poprawność wykonywanych obliczeń"
print("Rozwiązanie poprawne.")


print('''
#####################################################
# Napisz funkcję o nazwie unikalne zwracającą
# posortowaną listę niepowtarzających się elementów
# listy przekazanej do tej funkcji.
# Uwaga:
#   Do rozwiązania tego zadania wykorzystaj zbiory.
#   Funkcja sorted() zwraca posortowaną listę.
#####################################################
''')


def unikalne(list):
  s=set(list)
  z=sorted(s)
  return z


print('Sprawdzenie poprawności rozwiązania... Test 1/3...')
r = unikalne([1, 2, 2, 3, 4, 4, 5])
assert len(r) == 5, "Sprawdź liczbę elementów zwracanej listy"
assert r[0] == 1, "Sprawdź poprawność wykonywanych obliczeń"
assert r[1] == 2, "Sprawdź poprawność wykonywanych obliczeń"
assert r[2] == 3, "Sprawdź poprawność wykonywanych obliczeń"
assert r[3] == 4, "Sprawdź poprawność wykonywanych obliczeń"
assert r[4] == 5, "Sprawdź poprawność wykonywanych obliczeń"

print('Sprawdzenie poprawności rozwiązania... Test 2/3...')
r = unikalne([3, 4, 4, 5, 8, 8, 8, 8])
assert len(r) == 4, "Sprawdź liczbę elementów zwracanej listy"
assert r[0] == 3, "Sprawdź poprawność wykonywanych obliczeń"
assert r[1] == 4, "Sprawdź poprawność wykonywanych obliczeń"
assert r[2] == 5, "Sprawdź poprawność wykonywanych obliczeń"
assert r[3] == 8, "Sprawdź poprawność wykonywanych obliczeń"

print('Sprawdzenie poprawności rozwiązania... Test 3/3...')
r = unikalne([3, 99, 8, 8])
assert len(r) == 3, "Sprawdź liczbę elementów zwracanej listy"
assert r[0] == 3, "Sprawdź poprawność wykonywanych obliczeń"
assert r[1] == 8, "Sprawdź poprawność wykonywanych obliczeń"
assert r[2] == 99, "Sprawdź poprawność wykonywanych obliczeń"
print("Rozwiązanie poprawne.")


print('''
#####################################################
# Napisz funkcję zamieniającą jednoliterowy
# symbol statku na jego pełną nazwę.
# Funkcja ship powinna przyjmować jeden parametr
# (symbol statku) w formie napisu i zwracać
# pełną nazwę w formie napisu.
# Rodzaje statków (przyjmowany argument -->  nazwa statku):
#  B -->  BattleShip
#  b -->  BattleShip
#  C -->  Cruiser
#  c -->  Cruiser
#####################################################
''')


def ship(s):
  if s=="B":
    return "BattleShip"
  elif s=="b":
    return "BattleShip"
  elif s=="C" or s=="c":
    return "Cruiser"

# miejsce na rozwiązanie

print('Sprawdzenie poprawności rozwiązania... Test 1/4...')
assert ship('b') == 'BattleShip'
print('Sprawdzenie poprawności rozwiązania... Test 2/4...')
assert ship('c') == 'Cruiser'
print('Sprawdzenie poprawności rozwiązania... Test 3/4...')
assert ship('B') == 'BattleShip'
print('Sprawdzenie poprawności rozwiązania... Test 4/4...')
assert ship('C') == 'Cruiser'
print("Rozwiązanie poprawne.")


print('''
#####################################################
# Napisz funkcję o nazwie 'powtarzalne', która jako argument
# przyjuje listę, a zwraca listę wartości True/False.
# Każdemu elementowi z listy wejściowej powinna odpowiadać
# wartość True na liście wyjściowej, jeśli ten element wystąpił
# wcześniej na liście wejściowej. False w przeciwnym wypadku.
#
# Przykład:
#   lista_wejsciowa = [1, 2, 3, 2, 3, 4]
#   lista_wyjsciowa = powtarzalne(lista_wejsciowa)
#   print(lista_wyjsciowa)
#
#   Oczekiwany napis na ekranie: [False, False, False, True, True, False]
#
# Wskazówki:
# * aby dodać element do zbioru użyj funkcji add()
#   przykład:
#     s = {}
#     s.add(5)
# * aby sprawdzić, czy element znajduje się w zbiorze
#   użyj słowa kluczowego in
#   przykład:
#     if 5 in x:
#####################################################
''')

def powtarzalne(lista):
  if lista==[]:
    return []
  listw=[]
  s=set()
  for i in lista:
      if i in s:
          listw.append(True)
      else:
          listw.append(False)
      s.add(i)
  return listw






# miejsce na rozwiązanie

print('Sprawdzenie poprawności rozwiązania... Test 1/4...')
assert powtarzalne([]) == []
print('Sprawdzenie poprawności rozwiązania... Test 2/4...')
assert powtarzalne([1, 2, 3, 2, 3, 4]) == [False, False, False, True, True, False]
print('Sprawdzenie poprawności rozwiązania... Test 3/4...')
assert powtarzalne([1, 1, 1, 1]) == [False, True, True, True]
print('Sprawdzenie poprawności rozwiązania... Test 4/4...')
assert powtarzalne([1, 2, 3, 4]) == [False, False, False, False]
print("Rozwiązanie poprawne.")


print('''
#####################################################
# Szyfr Cezara to rodzaj szyfru podstawieniowego,
# w którym każda litera tekstu jawnego (niezaszyfrowanego)
# zastępowana jest inną, oddaloną od niej o stałą liczbę
# pozycji w alfabecie, literą (szyfr monoalfabetyczny),
# przy czym kierunek zamiany musi być zachowany.
# Nie rozróżnia się przy tym liter dużych i małych.
# Nazwa szyfru pochodzi od Juliusza Cezara, który
# prawdopodobnie używał tej techniki do komunikacji
# ze swymi przyjaciółmi.
#
# Współcześnie szyfru Cezara używa się z przesunięciem 13 (ROT13),
# będącego prostym i szybkim sposobem na ukrycie treści.
# Obecnie szyfr Cezara, jak każda technika podmieniająca
# pojedyncze litery alfabetu na inne, nie oferuje żadnego
# bezpieczeństwa komunikacji.
#
# Amerykański historyk wojskowy, David Kahn opisał w 1967 roku
# przypadki kochanków potajemnie komunikujących się zakodowanymi
# szyfrem Cezara wiadomościami na łamach The Times. Z kodu Cezara
# korzystano nawet w 1915 roku. Armia Imperium Rosyjskiego
# posługiwała się nim jako zamiennikiem dla jej bardziej
# skomplikowanych szyfrów, które były zbyt trudne do opanowania
# dla rosyjskiego wojska, dzięki czemu niemieccy i austriaccy
# kryptoanalitycy nie mieli większych problemów z odczytaniem
# tych wiadomości.
#
#
# Napisz funkcję o nazwie cezar przyjmującą napis,
# a zwracającą zaszyfrowany tekst. Przyjmujemy, że przesunięcie
# powinno wynosić 13 liter.
#
# Przykład:
#   zaszyfrowane = cezar("ala")
#   print(zaszyfrowane)
#  Na ekranie zobaczymy: kwk
#
# Wskazówki:
# * do zamiany liter tekstu jawnego na litery tekstu
#   zaszyfrowanego możesz (ale nie musisz) użyć słownika
# * metoda index() zwraca pozycję danej litery w tekście
#   przykład:
#     s = "ala"
#     x = s.index('l')
#     print(x)
#   Na ekranie zobaczymy: 1
#
# Informacje na temat szyfru Cezara:
#    https://pl.wikipedia.org/wiki/Szyfr_Cezara
#####################################################
''')




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
Dotychczasowe badania nie potwierdziły istnienia białych dziur.
'''
liczba_slow = slowa(tekst)
assert liczba_slow == 27, 'Napis "{}", zawiera 27 różnych słów, Twoja funkcja zwróciła wartość {}.'.format(tekst, liczba_slow)
print("Rozwiązanie poprawne.")


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

# miejsce na rozwiązanie
