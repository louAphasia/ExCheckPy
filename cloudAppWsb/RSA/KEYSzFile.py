def readFile(keyFilename):
    fo=open(keyFilename)
    content=fo.read()
    fo.close()
    keySize,n,EorD=content.split(',')
    return (int(keySize),int(n),int(EorD))

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