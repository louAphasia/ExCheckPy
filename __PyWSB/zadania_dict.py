def ship(s):
  dict={'b': "BattleShip", 'B':"Battleship", 'c':"Cruiser", 'C':"Cruiser"}
  for  i in dict.keys():     #for i in dict.keys():
    if i == s:                            # if i ==s:
      return dict[i]                      # return dict[i]  / dict.get(i)



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