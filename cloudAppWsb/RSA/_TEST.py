from ExCheckPy.cloudAppWsb.RSA.KeysPublicPrivate import genKeys



SYMBOLS='ABCDEFGHIJKLMNOPQRSTUWVYZabcdefghijklmnoprstuvwzy'



def encryptMessage(message,key):
    encryptedText=[]
    n,e=key
    for index in message:
        encryptedText.append((pow(index,e,n))+49%49)
    return encryptedText

def decryptMessage(encryptedText,key):
    decrypted=[]
    n,d=key
    #plaintext = ciphertext ^d mod n
    for symbol in encryptedText:
        print(symbol)
        decrypted.append((pow(symbol,d,n))+49%49)

    return decrypted

x=pow(36,29,713)
# c=t^e mod n
print(x)

k=(-5)%3
print('k',k)
y=pow(676,569,713)
print(y)
print('---------------------------------------------')
#[0, 36, 25, 60, 37, 25, 60, 35, 39, 43, 25, 60, 36, 39, 41, 44, 37, 60, 42, 39, 41, 44, 37, 60, 49, 50, 51, 52, 53]

#message=Ala ma kota lorum sorum 12345
keypubl=713,29
keypriv=713,569
szyfr=[0, 6, 36, 49, 21, 36,44, 36, 6, 7]
en=encryptMessage(szyfr,keypubl)
print(en)
de=decryptMessage(en,keypriv)
print(de)
