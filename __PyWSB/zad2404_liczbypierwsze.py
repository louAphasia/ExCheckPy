pierwsze_skl=[]

def pierwsze_opcja(n):
    for x in range(n+1):
        if x>1:
            for i in range(2,x):
                if(x%i)==0:
                    break
            else:
                print(x,end="\t")

pierwsze_opcja(29)

def pierwsza_funk(n):
    pierwsze=[]
    for x in range(2,n):
        for k in pierwsze:
            if x%k==0: break
        else:
            yield x
            pierwsze.append(x)
    return pierwsze

print(pierwsza_funk(25))

for x in pierwsza_funk(13):
   print(x)

