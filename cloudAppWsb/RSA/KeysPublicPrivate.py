import os,sys
import random
import math

# SITO algorytm wyznaczania liczb pierwszych z zadanego przedziału

def primeSieve(sieveSize):
    sieve=[True]*sieveSize
    sieve[0]=False
    sieve[1]=False

    for i in range(2, int(math.sqrt(sieveSize))+1):
        pointer=i*2
        while pointer<sieveSize:
            sieve[pointer]=False
            pointer+=i

    primes=[]
    for i in range(sieveSize):
        if sieve[i]==True:
            primes.append(i)

    return primes

# test RABIN -MILLERa=  algorytmem określającym czy dana liczba jest pierwsza. test probabilistycznym, wymagającym stosowania liczb losowych.

def rabinMiller(num):
    if num%2 ==0 or num<2:
        return False
    if num==3:
        return True

    s=num-1
    t=0
    while s%2==0:
        s=s//2
        t+=1
    for trials in range(5):
        a=random.randrange(2,num-1)
        v=pow(a,s,num)
        if v!=1:
            i=0
            while v!=(num-1):
                if i==t-1:
                    return False
                else:
                    i=i+1
                    v=(v**2)%num
    return True

# FUNKCJA CZY TO JEST LICZBA PIERWSZA > korzysta z SITA liczba pierwszych Z PRZEDZIAŁU DO 100 i testu rabin Millera

def isPrime(num):
    if(num <2):
        return False

    for prime in primeSieve(10):
        if(num%prime==0):
            return False

    return rabinMiller(num)

# WYGENERUJ DOŚĆ DUŻE LICZBY PIERWSZE > zależne od założonej wielkości klucza

def generatePrime():
    while True:
        num=random.randrange(2,50)
        if isPrime(num):
            return num


# ALGORYTYM NAJWIĘKSZEGO WSPÓLNEGO DZIELNIKA NWD dwóch liczba a i b

def gcd(a,b):
    while a!=0:
        a,b=b%a,a
    return b

# ALGORYTM ODWROTNOŚCI MODULARNEJ Odwrotnością modularną A (mod C) jest A^-1


def findModInverse(a,m):
    if gcd(a,m)!=1:
        return None
    u1,u2,u3=1,0,a
    e1,e2,e3=0,1,m

    while e3!=0:
        q=u3//e3
        e1,e2,e3,u1,u2,u3 = (u1-q*e1),(u2-q*e2),(u3-q*e3),e1,e2,e3
    return u1%m
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
        print(p,q)
    return (p,q)

# obliczanie liczby n

def generatorN(p,q):

    n = p * q
    return n

# obliczanie  e [ zależność od przyjętej wielkości klucza] i p i q

def generateE(p,q):

    print("generating e prime relative to p-1(q-1)")
    while True:
        e=random.randrange(2,1000)
        if gcd(e, (p - 1) * (q - 1))==1:
            break
    return e

# obliczanie d na podstawie Algorytmu odwrotności modulo

def generateD(p,q,e):
    print ("Generating d mod inverse of e" )
    d= findModInverse(e, (p - 1) * (q - 1))

    return d
# generowanie kluczy prywatnego [1] i publicznego [0] - zależność od przyjętej wielkości klucza

def genKeys():

    p,q=generatePQ()
    n=generatorN(p,q)
    e=generateE(p,q)
    d = generateD(p, q, e)
    if e==d:
        e = generateE(p, q)
        d = generateD(p, q, e)
    publicKey=(n,e)
    privateKey = (n, d)

    print("n,e",publicKey)
    print("n,d", privateKey)
    return (publicKey,privateKey)




# opcjonalny zapis wygenerowanych kluczy do pliku

def makeKeyFiles(name,Keys):

    if os.path.exists('%s_pubkey.txt'%(name)) or os.path.exists('%s_private.txt'%(name)):
            sys.exit('WARNING: THE FILE %s_pubkey.txt or %s_privatekey.txt already exists!use diffrent name or delete'% (name,name))

    publKey, privKey=Keys

    print()
    print('writing public key to file %s_publickey.txt...'%(name))
    fo=open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s'% (privKey[0], privKey[1]))
    fo.close()

    fo = open('%s_publkey.txt' % (name), 'w')
    fo.write('%s,%s' % (publKey[0], publKey[1]))
    fo.close()
