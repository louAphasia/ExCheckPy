def znajdzkod(slownik,x):
    doind=list(slownik)
    return doind.index(x)

slownik="abcd"

print(znajdzkod(slownik,'d'))


wejsciowe="aaabbbccc"
bitynaznak=2
x=len(wejsciowe)

bitlab=[]
for n in range(x):
    bitlab.append(0)

file = open('plik')
while True:
    char = file.read(1) # Wczytanie znak po znaku
    if not char: break
print(char)
for char in open('plik').read():
    print(char)

file = open('plik')
while True:
    line = file.readline() # Wczytanie wiersz po wierszu
    if not line: break
print(line, end='')

file = open('plik', 'rb')
while True:
    chunk = file.read(10) # Wczytanie bajtowych fragmentów — do 10 bajtów
    if not chunk: break
print(chunk)


def bit_l(self):
    s = bin(self)
    print(s)# binary representation:  bin(-37) --> '-0b100101'
    s = s[2:]
    return s


#powielanie liczb
s='nadi'
x=':'.join(":02:".format(ord(c))for c in s)

#wczytanie zawartosci do lancucha znakow

file=open('plik')
s=file.read()

#wczytanie znak po znaku

while True:
    char=file.read(1)
    if not char: break
    print(char)
for char in open('plik').read():
    print(char)

# wczytywanie po wierszu
while True:
    line=file.readline()
    if not line: break
    print(line, end='')

# wczytywanie BAJTOWYCH fragmentów do 10

file=open('plik','rb')
while True:
    chunk=file.read(10)
    if not chunk: break
    print(chunk)



print(bit_l(0))


bin()


