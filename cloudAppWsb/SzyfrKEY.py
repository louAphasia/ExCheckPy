key='dom'
for i in range(len(key)):
    print((ord(key[i])%26),end=',')

print()
tekst="Ala ma kota"
for x in range(len(tekst)):
    print(ord(tekst[x]),end=',')
print()

def Cezar(text,key):
    p=[(ord(key[x]) % 26)for x in range(len(key))]
    input=''
    for i in range(len(tekst)):
            if tekst[i].isalpha():
                if ord(tekst[i])<91:
                    input+=chr((ord(tekst[i])-65+p[i%(len(key))])%26+65)
                else:
                    input+=(chr((ord(tekst[i])-97+p[i%(len(key))])%26+97))
            else:
                input+=tekst[i]
    return input


print(Cezar(tekst,key))