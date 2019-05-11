import math
import binascii

s="aaaaaaaaaaaaabbbbbbbbbfffffddddddddddd"

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
end=ilebitend(nadmiarowe(bitnaznak(dlugosc(slownik(s))),lentext(s)))

def ilebitFirst(nadmiarowe):
    dicto={0:'000',1:'001',2:'010',3:'011',4:'100',5:'101',6:'110',7:'111'}
    return dicto.get(nadmiarowe)

print(ilebitFirst(nadmiarowe(bitnaznak(dlugosc(slownik(s))),lentext(s))))

first=ilebitFirst(nadmiarowe(bitnaznak(dlugosc(slownik(s))),lentext(s)))


def ciagbity(input,dict):
    ciag=''
    for i in input:
        if i in dict.keys():
            ciag+=dict.get(i)
        else:
            ciag+=i
    return ciag
print(ciagbity(s,Dict))

ciag=ciagbity(s,Dict)


def calyciagbity(ciag,first,end):
    caly=first+ciag+end
    return caly

print(calyciagbity(ciag,first,end))

def bajtpodzial(calyciag):
    bajty=[]
    for i in range(0,len(calyciag),8):
        bajty.append(calyciag[:8])
        calyciag=calyciag[8:len(calyciag)]
    return bajty


print(bajtpodzial(calyciagbity(ciag,first,end)))


def binaryToDecimal(n):
    num = n;
    dec_value = 0;

    # Initializing base
    # value to 1, i.e 2 ^ 0
    base1 = 1;

    len1 = len(num);
    for i in range(len1 - 1, -1, -1):
        if (num[i] == '1'):
            dec_value += base1;
        base1 = base1 * 2;

    return dec_value;

def listaDecimalAscii(bajtylista):
    output=[]
    for i in range(len(bajtylista)):
        decimal=binaryToDecimal(bajtylista[i])
        asciiznak=chr(decimal)
        output.append(asciiznak)
    return output

print(listaDecimalAscii(bajtpodzial(calyciagbity(ciag,first,end))))
asciikod=listaDecimalAscii(bajtpodzial(calyciagbity(ciag,first,end)))

def skompresowany(asciikod,slownik,dlugosc):
    asciistr=''.join(asciikod)
    strslownik=''.join(slownik)
    output=chr(dlugosc)+strslownik+asciistr
    return output

print(skompresowany(asciikod,slownik(s),dlugosc(slownik(s))))


def Dekompresja(skompresowany):