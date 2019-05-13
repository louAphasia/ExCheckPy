import math




def slownik(t):
    s=sorted(set(t))
    slownik=list(s)
    return slownik



def dlugosc(slownik):
    y=len(slownik)
    return y



def bitnaznak(dlugosc):
    b=math.ceil((math.log2(dlugosc)))
    return b





def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)


def lentext(wejscie):
    return len(wejscie)

def nadmiarowe(liczbabitnaznak,lentext):
    dlugoscbit=math.ceil(((liczbabitnaznak*lentext)+3)/8)*8
    nadmiar=dlugoscbit-(3+liczbabitnaznak*lentext)
    return nadmiar



def listabitow(dlugosc,b):
    lista=[]
    for i in range(dlugosc):
        lista.append(f"%0{b}d" % (int(bin(i))))
    return lista



def ilebitend(nadmiarowe):
    end=''
    for i in range(nadmiarowe):
         end+='1'
    return end



def ilebitFirst(nadmiarowe):
    dicto={0:'000',1:'001',2:'010',3:'011',4:'100',5:'101',6:'110',7:'111'}
    return dicto.get(nadmiarowe)




def ciagbity(input,dict):
    ciag=''
    for i in input:
        if i in dict.keys():
            ciag+=dict.get(i)
        else:
            ciag+=i
    return ciag



def calyciagbity(ciag,first,end):
    caly=first+ciag+end
    return caly



def bajtpodzial(calyciag):
    bajty=[]
    for i in range(0,len(calyciag),8):
        bajty.append(calyciag[:8])
        calyciag=calyciag[8:len(calyciag)]
    return bajty





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



def skompresowany(asciikod,slownik,dlugosc):
    asciistr=''.join(asciikod)
    strslownik=''.join(slownik)
    output=chr(dlugosc)+strslownik+asciistr
    return output



def kompread(skomp):
    return skomp


def dekompresja(skompresowany):
    def odczytslownik(skompresowany):
        znak=ord(skompresowany[0])
        slownik=skompresowany[1:(znak+1)]
        return slownik

    print(odczytslownik(skompresowany))

    slownikde=odczytslownik(skompresowany)
    dlugoscslo=len(odczytslownik(skompresowany))

    def bitnaznak(dlugosc):
        b = math.ceil((math.log2(dlugosc)))
        return b

    bitnazn=bitnaznak(dlugoscslo)
    print(bitnaznak)

    def listabitow(dlugosc, b):
        lista = []
        for i in range(dlugosc):
            lista.append(f"%0{b}d" % (int(bin(i))))
        return lista

    lsb=listabitow(dlugoscslo,bitnazn)

    slo = list(slownikde)
    # slownik znak : bity
    Dict = dict(zip(slo, lsb))
    print(Dict)

    def dec_to_bin(n):
        return bin(n)

    def odczytdecimalascii(skompresowany,dlugoscslownik):
        listadecimal=[]
        for i in range((dlugoscslownik+1),len(skompresowany)):
            listadecimal.append(ord(skompresowany[i]))
        return listadecimal

    print(odczytdecimalascii(skompresowany,dlugoscslo))

    listaodczytde=odczytdecimalascii(skompresowany,dlugoscslo)

    def decnabinlista(listaodczytdec):
        listabit=[]
        for i in range(len(listaodczytde)):
            listabit.append((dec_to_bin(listaodczytde[i])))
        return listabit

    listabity=decnabinlista(listaodczytde)
    print(listabity)

    def stringzBitow(listybity):
        ciagstr=''
        for i in range(len(listybity)):
            stbity = str(listybity[i])
            if len(listybity[i])<8:
                str8=stbity.zfill(8)
                ciagstr=ciagstr+''.join(str8)
            else:
                ciagstr=ciagstr+''.join(stbity)

        return ciagstr

    print(stringzBitow(listabity))

    ciagstr=stringzBitow(listabity)

    def ilenadmiarowe(ciagstr):
        ile=ciagstr[:3]
        dict={'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
        return dict.get(ile)

    print(ilenadmiarowe(stringzBitow(listabity)))

    endjedynki=ilenadmiarowe(stringzBitow(listabity))

    def bezendfirstjedynek(ciagstr,endjedynki):
        ciagodszyfr=ciagstr[3:]
        ciagodszyfr=ciagodszyfr[:len(ciagodszyfr)-endjedynki]
        return ciagodszyfr

    print(bezendfirstjedynek(ciagstr,endjedynki))

    ciagdoodszyfr=bezendfirstjedynek(ciagstr,endjedynki)

    def odszyfrowanie(Dict,ciagdoodszyfr):
        revdict={Dict[v]: v for v in Dict.keys()}
        print(revdict)
        ile=len(revdict)
        print(ile)
        ilezer=bitnaznak(ile)
        print(ilezer)

        ciagdoodszyfrowanie= [ciagdoodszyfr[x:x+ilezer] for x in range(0,len(ciagdoodszyfr),ilezer)]
        print(ciagdoodszyfrowanie)
        odszyfr = ''
        for i in range(len(ciagdoodszyfrowanie)):
           print(ciagdoodszyfrowanie[i])
           if ciagdoodszyfrowanie[i] in revdict.keys():
              odszyfr=odszyfr +''.join(revdict.get(ciagdoodszyfrowanie[i]))
        return odszyfr




    print(odszyfrowanie(Dict,ciagdoodszyfr))











if __name__ == '__main__':



  #wejscie=input("Tekst do kompresji:")
  fh=open('plik','r')
  s=fh.read()

  print(slownik(s))

  print(dlugosc(slownik(s)))

  print(bitnaznak(dlugosc(slownik(s))))

  print(nadmiarowe(bitnaznak(dlugosc(slownik(s))), lentext(s)))

  # lista z bitami
  lsb = listabitow(dlugosc(slownik(s)), bitnaznak(dlugosc(slownik(s))))
  slo = list(slownik(s))
  # slownik znak : bity
  Dict = dict(zip(slo, lsb))
  print(Dict)
  d = 1
  p = 3 * 0
  print(f"%0{4}d" % (d))

  print(ilebitend(nadmiarowe(bitnaznak(dlugosc(slownik(s))), lentext(s))))
  end = ilebitend(nadmiarowe(bitnaznak(dlugosc(slownik(s))), lentext(s)))

  print(ilebitFirst(nadmiarowe(bitnaznak(dlugosc(slownik(s))), lentext(s))))

  first = ilebitFirst(nadmiarowe(bitnaznak(dlugosc(slownik(s))), lentext(s)))

  print(ciagbity(s, Dict))

  ciag = ciagbity(s, Dict)

  print(calyciagbity(ciag, first, end))

  print(bajtpodzial(calyciagbity(ciag, first, end)))

  print(listaDecimalAscii(bajtpodzial(calyciagbity(ciag, first, end))))
  asciikod = listaDecimalAscii(bajtpodzial(calyciagbity(ciag, first, end)))

  print(skompresowany(asciikod, slownik(s), dlugosc(slownik(s))))



  print(len(skompresowany(asciikod, slownik(s), dlugosc(slownik(s)))))


  print(len(s))

  with open(r'D:\Pliki\skompresowany.txt', 'w+', encoding='utf-8') as w:
          w.write(skompresowany(asciikod, slownik(s), dlugosc(slownik(s))))

  with open(r'D:\Pliki\skompresowany.txt', 'r', encoding='utf-8') as r:
      komp=r.read()

  dekompresja(komp)
     # '''''with open(r'D:\Pliki\dekompresja.txt', 'w+') as w:
      #    for i in dekompresja(r.read()):
      #        w.write(i)'''