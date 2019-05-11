def fibon(n):
    if n>1:
        a=0
        b=1
        for x in range(n-1):
            a,b=b,a+b
        return b
    elif n==1:
        return 1
    else:
        return 0

print(fibon(10))

def fibbonaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbonaci(n-1)+fibbonaci(n-2)

print(fibbonaci(10))

