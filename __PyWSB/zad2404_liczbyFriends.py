
def sumv(n):
    sum=0
    for x in range(1,n//2+1):
        if n%x==0:
            sum+=x
    return sum

def ami(n):
    for x in range(1,n):
        if sumv(sumv(x))==x and sumv(x)!=x and sumv(x)>x:
            print(x, "and", sumv(x))

print(ami(3000))