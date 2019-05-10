tekst="Ala ma kota"

print(chr(90))
print(ord(tekst[0]))
print(ord('C'))

def Cezar(text):
    input=''
    for i in range(len(tekst)):
        if tekst[i].isalpha():
            if ord(tekst[i])<91:
                input+=chr((ord(tekst[i])-65+3)%26+65)
            else:
                input+=(chr((ord(tekst[i])-97+3)%26+97))
        else:
            input+=tekst[i]
    return input


print(Cezar(tekst))


def revCezar(szyfr):
    text=''
    for i in range(len(szyfr)):
        if szyfr[i].isalpha():
            if ord(szyfr[i])<91:
                text+=chr(90-(90-ord(szyfr[i])+3)%26)
            else:
                text+=chr(122-(122-ord(szyfr[i])+3)%26)
        else:
            text+=szyfr[i]
    return text


print(revCezar(Cezar(tekst)))

