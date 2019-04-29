
# zamiast *args moga byc inn slowa umowne
def fu(*ul):
    print(*ul, "hey")


fu("los","bos","wols")

#SITO
def sito(n):
  L=[0]+n*[1]
  print(L)
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


