def fibon(n):
    if n>1:
        m,d=0,1
        for x in range(n-1):
            m,d=d,d+m
        return d
    elif n==1:
        return 0
    else:
        return 1

print(fibon(8))