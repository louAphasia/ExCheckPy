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
