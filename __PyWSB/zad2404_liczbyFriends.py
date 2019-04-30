
def sumv(n):
    sum=0
    for x in range(1,n//2+1):
        print(n)
        if n%x==0:
            sum+=x
            print("sum",sum)
    return sum

def ami(n):
    for x in range(1,n):
        print("sumv",sumv(x))
        if sumv(sumv(x))==x and sumv(x)!=x and sumv(x)>x:
            print(x, "and", sumv(x))

print(sumv(30))