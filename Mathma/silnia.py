#iteracyjnie
from functools import reduce


def silnia(n):
    result=1
    for n in range(2,n+1):
        result*=n
    return result

def silnia1(k):
    if k<0:
        return False
    elif k==0:
        return 1
    else:
        r=1
        while k>0:
            r*=k
            k-=1
        return r

#rekurencyjnie

def silniar(n):
    if n<0:
        return False
    elif n==0:
        return 1
    else:
        return n*silniar(n-1)

#z lambda

silnialr=lambda n:1 if n<1 else n*silnialr(n-1)

silniali=lambda n:1 if n<1 else \
    reduce(lambda x,y: x*y, range(1,n+1))

x=5
print(silniali(5))