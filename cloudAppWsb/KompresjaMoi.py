import math

s="aabbccdd"

def slownik(t):
    s=sorted(set(t))
    slownik=list(s)
    return slownik

print(slownik(s))

def dlugosc(slownik):
    y=len(slownik)
    return y

print(dlugosc(slownik(s)))

def bitnaznak(dlugosc):
    b=math.ceil((math.log2(dlugosc)))
    return b

print(bitnaznak(dlugosc(slownik(s))))



def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)



def listabitow(dlugosc):
    lista=[]
    for i in range(dlugosc):
        lista.append("%02d" % (int(bin(i))))
    return lista

print(listabitow(dlugosc(slownik(s))))
d=1
p=3*0
print(f"%0{4}d" %(d))