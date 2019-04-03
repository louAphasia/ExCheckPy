import time


def sumn2(n):
    start = time.time()

    sum = 0
    for i in range(1, n + 1):
        sum = sum+1
    end = time.time()
    return sum,end-start

for x in range(5):
    print("sum is %d reguired %10.7f sekunds" % sumn2(10000))


# jak obliczac bez umieszczenia w srodku tylko z return
def sumn3(n):
    start=time.time()
    return (n*(n+1))/2, time.time()-start

for x in range(5):
    print("sumn3 %d i sek %10.99f " % sumn3(10000))
