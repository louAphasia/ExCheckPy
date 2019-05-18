from ExCheckPy.cloudAppWsb.RSA.KeysPublicPrivate import genKeys

SYMBOLS='ABCDEFGHIJKLMNOPQRSTUWVYZabcdefghijklmnoprstuvwzy1234567890_ !?.,'

x=pow(19,5,119)
# c=t^e mod n
#print(x)



message='Ala ma koty i lubi 123'
key=119,5


def encryptMessage(message,key):
    encryptedBlocks=[]
    n,e=key

    for block in message:
        #print(block,end=',')
        encryptedBlocks.append((pow(block,e,n))%66)
    return encryptedBlocks


#print(encryptMessage(message,key))

def encryptedDopliku(message):
    content=[]
    for x in message:
        content.append(SYMBOLS[x])
    return ''.join(content)



def getindexSYMBOLSFromText(message):
    mess=[]
    for ch in message:
        if ch not in SYMBOLS:
            print('ERROR don have literka %s' % (ch))
        else:
            mess.append(SYMBOLS.index(ch))
    return mess

#print(getindexSYMBOLSFromText(message))

def main():
    filename='encrypted_file.txt'
    mode='encrypt'  # moze byc decrypt
    with open(r'tekst.txt', 'r', encoding='utf-8') as r:
        komp = r.read()

        print("z pliku",komp)
    if mode=='encrypt':
        message=komp
        pubKeyFilename=genKeys(16)[0]

        ind=getindexSYMBOLSFromText(message)
        print("indexy",ind)
        doplik=encryptMessage(ind,pubKeyFilename)

        plik=encryptedDopliku(doplik)
        print(plik)

        #encryptAndWriteToFile(filename,doplik)

        print('Enncrypted text:')
        with open(r'D:\_COMPUTER Science\Python\ExCheckPy\ExCheckPy\cloudAppWsb\RSA\encrypted.txt', 'w', encoding='utf-8') as w:
            w.write(plik)

if __name__=='__main__':
    main()