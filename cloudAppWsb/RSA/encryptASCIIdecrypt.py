from ExCheckPy.cloudAppWsb.RSA.KeysPublicPrivate import genKeys, makeKeyFiles


# przyjety SŁOWNIK NA PODSTAWIE KTÓREGO BĘDZIEMY przeprowadzać szyfrowanie i odszyfrowanie danego tekstu 90 znaków/symboli



def main():

    filename='encrypted_file.txt' # nadanie nazwy pliku w którym będzie zapisany zaszyfrowany tekst
    filename2='decrypted_file.txt'
    mode='encrypt'  # moze byc 'decrypt'  WYBIERAMY TRYB

    # otiweramy tekst do szyfrowania

    with open(r'tekst.txt', 'r', encoding='latin-1') as r:
        message= r.read()
        print(message)
        # generujemy klucze publiczne i prywatne pobieramy klucz pod indeksem [0] a prywatny pod [1]
        pubiprivKey= genKeys()
        print(pubiprivKey)
        publKey=pubiprivKey[0]
        privKey=pubiprivKey[1]

       #makeKeyFiles('klucze',pubiprivKey)


    if mode=='encrypt':

        x=TextIndexDec(message)
        print('ords',x)
        e= encrypted(x,publKey)
        print('encrypted',e)
        d=DecCharASCII(e)
        print(d)


        o=ChrnaOrds(d)
        print("ords",o)
        de=decrypted(o,privKey)
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
    for x in szyfr:
        print(x)
        content.append(pow(x,d,n))
    return content



if __name__=="__main__":

    main()
