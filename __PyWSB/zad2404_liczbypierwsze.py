limit=100
pierwsze_skl=[num for num in range(1,limit) if 0 not in [num%i for i in range(2,int(num/2)+1)]]
print(pierwsze_skl)

#z filter

n=100
primesf=filter(lambda x:all(x%y!=0 for y in range(2,x)), range(1,n))

for x in primesf:
    print(x,end="\t")


def pierwsza_funk(n):
    pierwsze=[]
    for x in range(2,n):
        for k in pierwsze:
            if x%k==0: break
        else:
            yield x
            pierwsze.append(x)
    return pierwsze

print("pf",pierwsza_funk(25))

for x in pierwsza_funk(13):
   print(x,end="\t")

#trivial dev ZWRACA LICZBY PIERWSZE DZIELONE DANA LICZBE

'''def trialD(n):
    a=[]
    f=2
    while n>1:
        if n%f==0:
            a.append(f)
            n/=f
        else:
            f+=1
    return a
print("trial ",trialD(30), end="\t")'''

#SITO
def sito(n):
  L=[0]+n*[1]
  for p in range(2,n):
      q=p*p
      if q>n:
          break
      if L[p]==1:
         for i in range(q,n+1,p):
            L[i]=0
  return [i for i in range(1,n+1) if L[i]==1]

print("")
print("sito",sito(30))