

import random

import math

def isPrimeTrial(num):
    if num<2:
        return False

    for i in range(2,int(math.sqrt(num))+1):
        if num%1==0:
            return False
    return True

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

def isPrimeFactor(num):

    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return (i,num/i)
    return None

def isPrime(num):
    if(num <2):
        return False

    for prime in primeSieve(100):
        if(num%prime==0):
            return False

    return rabinMiller(num)

def generateLargePrime(keySize=16):
    while True:
        num=random.randrange(2**(keySize-1),2**keySize)
        if isPrime(num):
            return num




def gcd(a,b):
    while a!=0:
        a,b=b%a,a
    return b

print(primeSieve(100))




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
def main():

    print('Make KEYS')
    print(genKeys(16))
    print("Key  made.")


def generatePQ(keySize):
    p = 0
    q = 0
    # Step 1 PRIMES p i q
    while p == q:
        p = generateLargePrime(keySize)
        q = generateLargePrime(keySize)
        print(p,q)
    return (p,q)


def generatorN(p,q):

    n = p * q
    return n


def generateE(keySize,p,q):
    #step 2 create e

    print("generating e prime relative to p-1(q-1)")
    while True:
        e=random.randrange(2**(keySize-1),2**(keySize))
        if gcd(e, (p - 1) * (q - 1))==1:
            break
    return e

def generateD(p,q,e):
    # step 3 the mod inverse of e
    print ("Generating d mod inverse of e" )
    d= findModInverse(e, (p - 1) * (q - 1))

    return d

def genKeys(keySize):

    p,q=generatePQ(keySize)
    n=generatorN(p,q)
    e=generateE(keySize,p,q)
    d = generateD(p, q, e)
    publicKey=(n,e)
    privateKey = (n, d)

    print("n,e",publicKey)
    print("n,d", privateKey)
    return (publicKey,privateKey)






'''def makeKeyFiles(name,keySize):

    if os.path.exists('%s_pubkey.txt'%(name)) or os.path.exists('%s_private.txt'%(name)):
            sys.exit('WARNING: THE FILE %s_pubkey.txt or %s_privatekey.txt already exists!use diffrent name or delete'% (name,name))

    publicKey, privateKey=generatorKey(keySize)

    print()
    print('thr public key is a %s and a %s digit nr' % (len(str(publicKey[0])),(len(str(publicKey[1])))))
    print('writing public key to file %s_publickey.txt...'%(name))
    fo=open('%s_publickey.txt' % (name), 'w')
    fo.write('%s,%s,%s'% (keySize,privateKey[0], publicKey[1]))
    fo.close()'''


if __name__=='__main__':
        main()



