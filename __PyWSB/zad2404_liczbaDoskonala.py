

def perfect(n):
    for num in range(1,n+1):
        res=0
        for i in range(1,num):
            if(num%i)==0:
                res=res+i
        if num==res:
            print(num)


print(perfect(30))
