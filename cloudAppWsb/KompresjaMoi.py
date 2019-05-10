import math

s="aabbccddee"

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


def lentext(wejscie):
    return len(wejscie)

def nadmiarowe(liczbabitnaznak,lentext):
    dlugoscbit=math.ceil(((liczbabitnaznak*lentext)+3)/8)*8
    nadmiar=dlugoscbit-(3+liczbabitnaznak*lentext)
    return nadmiar

print(nadmiarowe(bitnaznak(dlugosc(slownik(s))),lentext(s)))

def listabitow(dlugosc,b):
    lista=[]
    for i in range(dlugosc):
        lista.append(f"%0{b}d" % (int(bin(i))))
    return lista

#lista z bitami
lsb=listabitow(dlugosc(slownik(s)),bitnaznak(dlugosc(slownik(s))))
slo=list(slownik(s))
#slownik znak : bity
Dict=dict(zip(slo,lsb))
print(Dict)
d=1
p=3*0
print(f"%0{4}d" %(d))

def ilebitend(nadmiarowe):
    end=''
    for i in range(nadmiarowe):
         end+='1'
    return end

print(ilebitend(nadmiarowe(bitnaznak(dlugosc(slownik(s))),lentext(s))))

def ilebitFirst(nadmiarowe):
    dicto={0:'000',1:'001',2:'010',3:'011',4:'100',5:'101',6:'110',7:'111'}
    return dicto.get(nadmiarowe)

print(ilebitFirst(nadmiarowe(bitnaznak(dlugosc(slownik(s))),lentext(s))))