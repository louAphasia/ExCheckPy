import math

def do_slownika(wejscie):
     slowniktupleSort=sorted(wejscie)
     return ''.join(slowniktupleSort)

def dlugosc(wejscie):
    return len(wejscie)

def unikalne(slownik):
    y=len(slownik)
    return y

def liczbabitnaznak(y):
    b=math.ceil((math.log2(y)))
    return b

def nadmiarowe(liczbabitnaznak,dlugosc):
    dlugoscbit=math.ceil(((liczbabitnaznak*dlugosc)+3)/8)*8
    nadmiar=dlugoscbit-(3+liczbabitnaznak*dlugosc)
    return nadmiar
#nadmiarowe=(8-(3+dl*bitynaznak)%8)%8

def bytetab(wejsciowe):
    listwej=list(wejsciowe)
    listascii=[]
    for x in listwej:
        listascii.append(ord(x))

def znajdzkod(slownik,x):
    doind=list(slownik)
    return doind.index(x)




#ile jest liter nie powtarzajacych sie

#dlugosc input

#obliczenie ile bitow na znak 00 czy 000 czy 0000

# zamiana liter na bity
# ile nadmiarowych i ile ma byc dodane na poczatku



if __name__ == '__main__':



  #wejscie=input("Tekst do kompresji:")
  fh=open('plik','r')
  wejscie=fh.read()

  print("Tekst do kompresji %s" % (wejscie))
  print("Slownik:", do_slownika(wejscie))

  print("Dlugosc tekstu przed kompresja:",dlugosc(wejscie))
  print("Unikalnych liter:",unikalne(do_slownika(wejscie)))
  iloscunikalne=unikalne(do_slownika(wejscie))
  print("Liczba bitow na znak:", liczbabitnaznak(iloscunikalne))
  lb=liczbabitnaznak(iloscunikalne)
  print("Liczba nadmiarowych:", nadmiarowe(lb,dlugosc(wejscie)))

  dlugoscall=nadmiarowe(lb,dlugosc(wejscie))+lb*dlugosc(wejscie)+3

  bytetekst=bytearray()
  for x in range(int(dlugoscall/8)):
      bytetekst.append(0)

  print(bytetekst)


  print("Skompresowany tekst:" , skompresowany)
  print("Dlugosc tekstu po kompresji %d" % dlugoscpokomp)








  print(chr(97))
  print(ord('a'))

  print(ord('a'))
  print(chr(97))

  print(bool(None))

  def dec_to_bin(x):
    return int(bin(x)[2:])

  print(dec_to_bin(97))

