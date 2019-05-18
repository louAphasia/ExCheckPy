x=pow(19,5,119)
# c=t^e mod n
print(x)

SYMBOLS='ABCDEFGHIJKLMNOPQRSTUWVYZabcdefghijklmnoprstuvwzy1234567890_ !?.,'

message='Ala ma koty i lubi 123'
key=119,5


def encryptMessage(message,key):
    encryptedBlocks=[]
    n,e=key

    for block in message:
        print(ord(block),end=',')
        encryptedBlocks.append(chr(pow(ord(block),e,n)))
    return ''.join(encryptedBlocks)


print(encryptMessage(message,key))


def getindexSYMBOLSFromText(message):
    mess=[]
    for ch in message:
        if ch not in SYMBOLS:
            print('ERROR don have literka %s' % (ch))
        else:
            mess.append(SYMBOLS.index(ch))
    return mess

print(getindexSYMBOLSFromText(message))