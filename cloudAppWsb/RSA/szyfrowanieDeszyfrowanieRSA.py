import sys,math
from ExCheckPy.cloudAppWsb.RSA.KeysPublicPrivate import genKeys

SYMBOLS='ABCDEFGHIJKLMNOPQRSTUWVYZabcdefghijklmnoprstuvwzy1234567890_ !?.,'

def main():
    filename='encrypted_file.txt'
    mode='encrypt'  # moze byc decrypt
    with open(r'tekst.txt', 'r', encoding='utf-8') as r:
        komp = r.read()
    if mode=='encrypt':
        message=komp
        pubKeyFilename=genKeys(16)[0]

        print('Encrypting and writting to %s...'% (pubKeyFilename))
        encryptedText=encryptAndWriteToFile(filename,pubKeyFilename,komp)

        print('Enncrypted text:')
        print(encryptedText)

    elif mode=='decrypt':
        privKeyFilename=genKeys(16)[1]
        print('Reading from %s...' %(filename))

        decryptedText=readFromFileAndDecrypt(filename,privKeyFilename)

        print('Decrpted text:')
        print(decryptedText)



def getIndexSYMFromText(message):
    mess=[]
    for ch in message:
        if ch not in SYMBOLS:
            print('ERROR don have literka %s' % (ch))
        else:
            mess.append(SYMBOLS.index(ch))
    return mess



def encryptMessage(message,key):
    encryptedText=[]
    n,e=key

    for index in getIndexSYMFromText(message):
        encryptedText.append(pow(index,e,n))
    return encryptedText

def decryptMessage(encryptedText,key):
    decrypted=[]
    n,d=key
    #plaintext = ciphertext ^d mod n
    for symbol in encryptedText:
        decrypted.append(pow(symbol,d,n))

    return decrypted

'''def readFile(keyFilename):
    fo=open(keyFilename)
    content=fo.read()
    fo.close()
    keySize,n,EorD=content.split(',')
    return (int(keySize),int(n),int(EorD))'''

def encryptAndWriteToFile(messageFilename,message,key):
    content= encryptMessage(message,key)
    for i in range(content):
        content[i]=str(content[i])
    encryptedContent=','.join(content)

    fo=open(messageFilename,'w')
    fo.write(encryptedContent)
    fo.close()

    return encryptedContent

def readFromFileAndDecrypt(messageFilename,keyFilename):
    keySize,n,d=readFile(keyFilename)

    fo=open(messageFilename)
    content=fo.read()
    messageLen,blockSize,encryptedMessage=content.split('_')
    messageLen=int(messageLen)
    blockSize=int(blockSize)

    if not (math.log(2**keySize,len(SYMBOLS))>=blockSize):
        sys.exit('ERROR block size is too large fo the key and symbol set size correct key file')

    encryptedBlocks=[]
    for block in encryptedMessage.split(','):
        encryptedBlocks.append(int(block))

    return decryptMessage(encryptedBlocks,messageLen,(n,d),blockSize)

if __name__=='__main__':
    main()


