from ExCheckPy.cloudAppWsb.RSA.KeysPublicPrivate import genKeys, makeKeyFiles


# przyjety SŁOWNIK NA PODSTAWIE KTÓREGO BĘDZIEMY przeprowadzać szyfrowanie i odszyfrowanie danego tekstu 90 znaków/symboli



def main():

    filename='encrypted_file.txt' # nadanie nazwy pliku w którym będzie zapisany zaszyfrowany tekst
    filename2='decrypted_file.txt'
    mode='encrypt'  # moze byc 'decrypt'  WYBIERAMY TRYB

    # otwieramy tekst do szyfrowania

    if mode == 'encrypt':
        with open(r'tekst.txt', 'r', encoding='utf-8') as r:
            message= r.read()
            print(message)
        # generujemy klucze publiczne i prywatne pobieramy klucz pod indeksem [0] a prywatny pod [1]
        pubiprivKey= genKeys()
        print(pubiprivKey)
        publKey=pubiprivKey[0]
        #privKey=pubiprivKey[1]

        makeKeyFiles('klucze',pubiprivKey)






        x=TextIndexDec(message)
        print('ords',x)
        e= encrypted(x,publKey)
        print('encrypted',e)
        dch=DecCharASCII(e)
        print(dch)
        WriteToFile(filename,dch)

    #if mode == 'decrypt':

        m = readFileKey('klucze_privkey.txt')
        print(m)
        re=ReadFromFile(filename)
        print(re)
        o=ChrnaOrds(re)
        print("ords",o)
        de=decrypted(o,m)
        print("decrypted",de)
        dee=DecCharASCII(de)
        print(dee)






def TextIndexDec(message):
    content=[]
    for x in message:
        content.append(ord(x))
    return content

def encrypted(message,keyPubl):
    content=[]
    n,e=keyPubl
    for x in message:
        content.append((pow(x,e,n)))
    return content

def DecCharASCII(ords):
    content=[]
    for x in ords:
        content.append(chr(x))
    stringi=''.join(content)
    return stringi

##########################


def ChrnaOrds(szyfr):
    content=[]
    for x in szyfr:
        content.append(ord(x))
    return content


def decrypted(szyfr,keyPriv):
    content=[]
    n,d=keyPriv
    print("n",n)
    print("d",d)
    for x in szyfr:
        content.append(pow(x,d,n))
    return content

#######
def readFileKey(keyFilename):
    fo=open(keyFilename)
    content=fo.read()
    fo.close()
    d,n,=content.split(',')
    return (int(d),int(n))


def WriteToFile(messageFilename, odszyfr):
    fo = open(messageFilename, 'w', encoding="utf-8")
    fo.write(odszyfr)
    fo.close()



def ReadFromFile(messageFilename):

    fo=open(messageFilename,'r',encoding='utf-8')
    content=fo.read()
    fo.close()

    return content


if __name__=="__main__":

    main()
