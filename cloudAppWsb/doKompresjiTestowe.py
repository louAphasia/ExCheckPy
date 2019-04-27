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




def bit_l(self):
    s = bin(self)
    print(s)# binary representation:  bin(-37) --> '-0b100101'
    s = s[2:]
    return s




#wczytanie zawartosci do lancucha znakow

file=open('test.txt')
s=file.read()

#wczytanie znak po znaku

while True:
    char=file.read(1)
    if not char: break
    print(char)
for char in open('test.txt').read():
    print(char)

# wczytywanie po wierszu
while True:
    line=file.readline()
    if not line: break
    print(line, end='')

# wczytywanie BAJTOWYCH fragmentów do 10

file=open('test.txt','rb')
while True:
    chunk=file.read(10)
    if not chunk: break
    print(chunk)



print(bit_l(0))





