import math, random

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

def generateLargePrime(keySize=1024):
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