

cipher = {'a': 'y', 'e': 'i', 'i': 'o', 'o': 'a', 'y': 'e'}


def encode(plaintext, cipher=cipher):
    szyfr = []
    for ch in plaintext:
        if ch in cipher.keys():
            szyfr.append(cipher.get(ch))
        else:
            szyfr.append(ch)
    return ''.join(szyfr)


cipherdev = {cipher[v]: v for v in cipher.keys()}


def decode(encoded, cipherdev=cipherdev):

    return encode(encoded, cipherdev)







def main():
    while True:
        odp = input("Wybierz operacje (szyfrowanie, deszyfrowanie, wyjscie): ")
        if odp == "szyfrowanie":
            text = input("Podaj tekst ")
            print("Wynik: ",encode(text))

        elif odp == "deszyfrowanie":
            szyfr = input("Podaj tekst ")
            print("Wynik: ", decode(szyfr))

        elif odp == "wyjscie":
            break
        else:
            print("Bledna operacja ")


if __name__ == "__main__":
    main()
