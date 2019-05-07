
# zamiast *args moga byc inn slowa umowne
def fu(*ul):
    print(*ul, "hey")


fu("los","bos","wols")

#SITO
"""def sito(n):
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
print("sito",sito(30))"""

def pierwsza_funk(n):
    pierwsze=[]
    for x in range(2,n):
        for k in pierwsze:
            print(pierwsze)
            print(x,k)
            if x%k==0: break
        else:
            #yield x
            pierwsze.append(x)
    return pierwsze

print("pf",list(pierwsza_funk(25)))

# stringi metody

st="oo-nadi-oooosnowdi-ooo"
print(st.lstrip("o"))

print(st.rjust(100))
print(st.zfill(50))

print(st.isalnum())

sss='SpamSpamEggsSpamSpam'
print(sss.strip('Spam'))