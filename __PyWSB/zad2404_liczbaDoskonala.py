import functools

def perfect(n):
    for num in range(1,n+1):
        res=0
        for i in range(1,num):
            if(num%i)==0:
                res=res+i
        if num==res:
            print(num)


print(perfect(30))

def perf(n):
    perf=[]
    for x in range(2,n):
        a=2**(x-1)*((2**x)-1)
        if a>n:
            break
        else:
            perf.append(a)

    return perf

print(perf(10))

n=30

f=[ (2**(x-1)*((2**x)-1) for x in range(2,n))]

print(f)