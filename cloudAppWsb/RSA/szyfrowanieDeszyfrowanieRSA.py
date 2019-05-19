
from ExCheckPy.cloudAppWsb.RSA.KeysPublicPrivate import genKeys, makeKeyFiles


# przyjety SŁOWNIK NA PODSTAWIE KTÓREGO BĘDZIEMY przeprowadzać szyfrowanie i odszyfrowanie danego tekstu 90 znaków/symboli

SYMBOLS='ABCDEFGHIJKLMNOPQRSTUWVYZabcdefghijklmnoprstuvwzy '

def main():

    filename='encrypted_file.txt' # nadanie nazwy pliku w którym będzie zapisany zaszyfrowany tekst
    filename2='decrypted_file.txt'
    mode='encrypt'  # moze byc 'decrypt'  WYBIERAMY TRYB

    # otiweramy tekst do szyfrowania

    with open(r'tekst.txt', 'r', encoding='utf-8') as r:
        message= r.read()

        # generujemy klucze publiczne i prywatne pobieramy klucz pod indeksem [0] a prywatny pod [1]
        pubiprivKey= genKeys()
        print(pubiprivKey)
        publKey=pubiprivKey[0]
        print(publKey)
        privKey=pubiprivKey[1]
        print(privKey)

        makeKeyFiles('klucz',pubiprivKey)

    if mode=='encrypt':

        mess=getIndexSYMFromText(message)
        print("message", mess)
        indexmess=encryptMessage(mess,publKey)
        print("indexmess",indexmess)
        indexy=toFIX(indexmess)
        encryptedText=toSYMBOLS(indexy)
        print(encryptedText)
        encrypted=WriteToFile(filename,encryptedText)
        print('Encrypting and writting to %s...' % (filename))

        print('Encrypted text:')


        print('DESZYFROWANIEReading from %s...' %(filename))

        encryptedText=ReadFromFile(filename)
        print("decryptedfile",encryptedText)
        indextekst=getIndexSYMFromText(encryptedText)
        indexrev=indexSlownik(indextekst)
        print("indextekst",indextekst)
        print("indexrev",indexrev)
        tekst=decryptMessage(indexrev,privKey)
        print('de tekst',tekst)
        decryptedText=toSYMBOLS(tekst)
        print(decryptedText)
        decrypted=WriteToFile(filename2,decryptedText)

        print('Decrypted text:to %s' % (filename2))


###############################

# zamiana symboli z naszego tekstu na indexy ze slownika SYMBOLS do szyfrowania


def getIndexSYMFromText(message):
    mess=[]
    for ch in message:
        if ch not in SYMBOLS:
            mess.append('')
        else:
            mess.append(SYMBOLS.index(ch))
    return mess

# szyfrowanie > każdemu znaku wg algorytmu C=t^e mod n jest nadany nowy indekst i symbol

def encryptMessage(message,key):
    encryptedText=[]
    n,e=key
    for index in message:
        encryptedText.append((pow(index,e,n)))
    return encryptedText

def decryptMessage(encryptedText,key):
    decrypted=[]
    n,d=key
    #plaintext = ciphertext ^d mod n
    for symbol in encryptedText:
        decrypted.append((pow(symbol,d,n)))

    return decrypted

'''def readFile(keyFilename):
    fo=open(keyFilename)
    content=fo.read()
    fo.close()
    keySize,n,EorD=content.split(',')
    return (int(keySize),int(n),int(EorD))'''

def toFIX(x):
    y=[]
    for i in x:
        y.append(i%49)
    return y

def toSYMBOLS(indexy):
    content = []
    for i in indexy:
        content.append(SYMBOLS[i])
    Contenttofile = ''.join(content)

    return Contenttofile

def indexSlownik(indexy):
    content=[]
    for i in indexy:
        content.append(i)
    return content



def WriteToFile(messageFilename, odszyfr):
    fo = open(messageFilename, 'w')
    fo.write(odszyfr)
    fo.close()




def ReadFromFile(messageFilename):

    fo=open(messageFilename)
    content=fo.read()
    fo.close()

    return content

if __name__=='__main__':
    main()


