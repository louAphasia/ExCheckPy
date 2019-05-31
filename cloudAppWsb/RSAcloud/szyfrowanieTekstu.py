import math
import os
import random
import sys


# przyjety SŁOWNIK NA PODSTAWIE KTÓREGO BĘDZIEMY przeprowadzać szyfrowanie i odszyfrowanie danego tekstu 90 znaków/symboli


def main():
    filename = 'encrypted_file.txt'  # nadanie nazwy pliku w którym będzie zapisany zaszyfrowany tekst

    mode = 'encrypt'  # moze byc 'decrypt'  WYBIERAMY TRYB

    # otwieramy testowy tekst do szyfrowania
    if mode == 'encrypt':
        with open(r'rekordy.txt', 'r', encoding='utf-8') as r:
            message = r.read()
            print(message)

        # generujemy klucze publiczne i prywatne pobieramy klucz pod indeksem [0] a prywatny pod [1]
        pubiprivKey = genKeys()
        print(pubiprivKey)
        publKey = pubiprivKey[0]   # pobieramy wartości n i e i przekazujemy do funkcji szyfrowania

        # opcjonalne
        # zapisanie do pliku [ wygenerowane klucze publiczne i prywatne
        makeKeyFiles('klucz', pubiprivKey)

        # odczytujemy znaki z text.txt w oparciu o ASCII  extended characters +1
        x = TextIndexDec(message)

        # szyfrujemy kluczemu publicznym
        e = encrypted(x, publKey)
        print('encrypted', e)
        dch = DecCharASCII(e)
        print(dch)
        WriteToFile(filename, dch)

    # if mode == 'decrypt':...
    # m = readFileKey('klucze_privkey.txt')
    # re=ReadFromFile(filename)

######### FUNCKJE SZYFRUJĄCA I zamieniające

#zamiana znaków na liczebną reprezentację
def TextIndexDec(message):  #  ord() string representing one Unicode character, return an integer representing the Unicode
    content = []
    for x in message:
        content.append(ord(x))
    return content

#szyfrowanie znaków reprezentowanych przez liczbę dziesiętną znaku za pomocą algorytmu RSA  x^e mod n
def encrypted(message, keyPubl):
    content = []
    n, e = keyPubl
    for x in message:
        content.append((pow(x, e, n))+1)    # w deszyfrowaniu musi byc pow(x-1,d,n)
    return content

#zamiana liczby dzisiętnej -kodu ASCII expended na znak chr()
#For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. This is the inverse of ord()
def DecCharASCII(ords):
    content = []
    for x in ords:
        content.append(chr(x))
    stringi = ''.join(content)
    return stringi


######################FUNCKJE ODCZYTU ZAPISU Z PLIKÓW

# opcjonalne czytanie klucza  z pliku txt
def readFileKey(keyFilename):
    fo = open(keyFilename)
    content = fo.read()
    fo.close()
    e, n, = content.split(',')
    return (int(e), int(n))


def WriteToFile(messageFilename, odszyfr):
    fo = open(messageFilename, 'w', encoding="utf-8")
    fo.write(odszyfr)
    fo.close()


def ReadFromFile(messageFilename):
    fo = open(messageFilename, 'r', encoding='utf-8')
    content = fo.read()
    fo.close()

    return content


########## FUNKCJE POTRZEBNE DO WYGENEROWANIA KLUCZY


# SITO algorytm wyznaczania liczb pierwszych z zadanego przedziału

def primeSieve(sieveSize):
    sieve = [True] * sieveSize
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i

    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)

    return primes


# test RABIN -MILLERa=  algorytmem określającym czy dana liczba jest pierwsza. test probabilistycznym, wymagającym stosowania liczb losowych.

def rabinMiller(num):
    if num % 2 == 0 or num < 2:
        return False
    if num == 3:
        return True

    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


# funkcja CZY TO JEST LICZBA PIERWSZA > korzysta z SITA liczba pierwszych Z PRZEDZIAŁU DO 100 i testu rabin Millera

def isPrime(num):
    if (num < 2):
        return False

    for prime in primeSieve(10):
        if (num % prime == 0):
            return False

    return rabinMiller(num)


# WYGENERUJ  LICZBY PIERWSZE > zależne od zalozonego przedzialu random

def generatePrime():
    while True:
        num = random.randrange(2, 50)
        if isPrime(num):
            return num


# ALGORYTYM NAJWIĘKSZEGO WSPÓLNEGO DZIELNIKA NWD dwóch liczba a i b

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


# ALGORYTM ODWROTNOŚCI MODULARNEJ Odwrotnością modularną A (mod C) jest A^-1


def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    e1, e2, e3 = 0, 1, m

    while e3 != 0:
        q = u3 // e3
        e1, e2, e3, u1, u2, u3 = (u1 - q * e1), (u2 - q * e2), (u3 - q * e3), e1, e2, e3
    return u1 % m


########################################################################

# tworzenie KLUCZY PUBLICZNEGO [N,E] jawnego  - do szyfrowania  I PRYWATNEGO [N,D]niejawnego - do odszyfrowania


# generowanie licz pierwszych p i q
def generatePQ():
    p = 0
    q = 0
    # Step 1 PRIMES p i q
    while p == q:
        p = generatePrime()
        q = generatePrime()
        print(p, q)
    return (p, q)


# obliczanie liczby n

def generatorN(p, q):
    n = p * q
    return n


# obliczanie  e [ zależność od przyjętej wielkości klucza] i p i q

def generateE(p, q):
    while True:
        e = random.randrange(2, 1000)
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break
    return e


# obliczanie d na podstawie Algorytmu odwrotności modulo

def generateD(p, q, e):
    d = findModInverse(e, (p - 1) * (q - 1))

    return d


# generowanie kluczy prywatnego [1] i publicznego [0] - zależność od przyjętej wielkości klucza

def genKeys():
    p, q = generatePQ()
    n = generatorN(p, q)
    e = generateE(p, q)
    d = generateD(p, q, e)
    if e == d:
        e = generateE(p, q)
        d = generateD(p, q, e)
    publicKey = (n, e)
    privateKey = (n, d)

    print("n,e", publicKey)
    print("n,d", privateKey)
    return (publicKey, privateKey)


# zapis wygenerowanych kluczy do pliku

def makeKeyFiles(name, Keys):
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_private.txt' % (name)):
        sys.exit('WARNING: THE FILE %s_pubkey.txt or %s_privatekey.txt already exists!use diffrent name or delete' % (
        name, name))

    publKey, privKey = Keys

    print()
    print('writing public key to file %s_publickey.txt...' % (name))
    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s' % (privKey[0], privKey[1]))
    fo.close()

    fo = open('%s_publkey.txt' % (name), 'w')
    fo.write('%s,%s' % (publKey[0], publKey[1]))
    fo.close()


if __name__ == "__main__":
    main()
