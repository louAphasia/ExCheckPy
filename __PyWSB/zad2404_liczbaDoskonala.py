

def perfect(n):
    for i in range(n+1):
        sum1=0
    for x in range(1,i):
        if(i%x==0):
            sum1=sum1+x
            if (sum1==i):
                print(i)


print(perfect(300))
