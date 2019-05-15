import sys,math

SYMBOLS='ABCDEFGHIJKLMNOPQRSTUWVYZabcdefghijklmnoprstuvwzy1234567890_ !?.,'

def main():
    filename='encrypted_file.txt'
    mode='encrypt'  # moze byc decrypt

    if mode=='encrypt':
        message='Residents can get parcels sent to a depot then receive a notification once they arrive. They can then get the items delivered  app subscription will get you an unlimited number of deliveries. The service will launch in the San Francisco Bay Area by the end of the year.'
        pubKeyFilename='nadisnowdi_publickey.txt'
        print('Encrypting and writting to %s...'% (filename))
        encryptedText=encryptAndWriteToFile(filename,pubKeyFilename,message)

        print('Enncrypted text:')
        print(encryptedText)

    elif mode=='decrypt':
        privKeyFilename='ul_privatekey.txt'
        print('Reading from %s...' %(filename))

        decryptedText=readFromFileAndDecrypt(filename,privKeyFilename)

        print('Decrpted text:')
        print(decryptedText)

#BLOCK ZAMIANA

def getBlockFromText(message,blockSize):
    for ch in message:
        if ch not in SYMBOLS:
            print('ERROR don have literka %s' % (ch))
            sys.exit()

    blockInts=[]
    for blockStart in range(0,len(message),blockSize):
        blockInt=0
        for i in range(blockStart,min(blockStart+blockSize,len(message))):
            blockInt+=(SYMBOLS.index(message[i]))*(len(SYMBOLS)**(i%blockSize))
            blockInts.append(blockInt)
    return blockInts

def getTextFromBlock(blockInts,messageLen,blockSize):
    message=[]
    for blockInt in blockInts:
        blockMessage=[]
        for i in range(blockSize-1,-1,-1):
            if len(message)+i<messageLen:
                charIndex=blockInt//(len(SYMBOLS)**i)
                blockInt=blockInt%(len(SYMBOLS)**i)
                blockMessage.insert(0,SYMBOLS[charIndex])
        message.extend(blockMessage)
    return''.join(message)

def encryptMessage(message,key,blockSize):
    encryptedBlocks=[]
    n,e=key

    for block in getBlockFromText(message,blockSize):
        encryptedBlocks.append(pow(block,e,n))
    return encryptedBlocks

def decryptMessage(encryptedBlocks, messageLen,key,blockSize):
    decryptedBlocks=[]
    n,d=key
    #plaintext = ciphertext ^d mod n
    for block in encryptedBlocks:
        decryptedBlocks.append(pow(block,d,n))

    return getTextFromBlock(decryptedBlocks,messageLen,blockSize)

def readFile(keyFilename):
    fo=open(keyFilename)
    content=fo.read()
    fo.close()
    keySize,n,EorD=content.split(',')
    return (int(keySize),int(n),int(EorD))

def encryptAndWriteToFile(messageFilename, keyFilename,message,blockSize=None):
    keySize,n,e=readFile(keyFilename)
    if blockSize==None:
        blockSize=int(math.log(2**keySize,len(SYMBOLS)))
        print('blocksize',blockSize)

    if not(math.log(2**keySize,len(SYMBOLS))>=blockSize):
        sys.exit('ERROR: BlockSize is too large specencrpyfy correct key file ')

    encryptedBlocks=encryptMessage(message,(n,e),blockSize)

    for i in range(len(encryptedBlocks)):
        encryptedBlocks[i]=str(encryptedBlocks[i])
    encryptedContent=','.join(encryptedBlocks)

    encryptedContent='%s_%s_%s'%(len(message),blockSize,encryptedContent)
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


