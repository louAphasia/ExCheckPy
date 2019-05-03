S=[ord(c) for c in 'spam']
print(S)

l=[x + y for x in 'abc' for y in 'lmn']
print(l)

#slownik
def f(x):
    return x*2
items=['aaa','bbb','ccc']
keys=[1,2,3,4]
vals=['a','b','c','d']
D={key : val for (key,val) in zip(keys,vals) }
D1=dict(zip(keys,vals))
D2={x:f(x) for x in items}
D3=dict((x, f(x))for x in items) #wyrazenie generatora
#set
S=[2,4,6,7]
ss={f(x) for x in S}
s2=set(f(x) for x in S)

print('iter',type(s2))



tu=()
print(type(tu))

###lista a generujace funkcje map filter

reslist= [ x**2 for x in range(10) if x%2==0 ]

resfm=list(map((lambda x:x**2),filter((lambda x:x%2==0),range(10))))

print(reslist)
print(resfm)

#skladne permutacje

per=[(x,y) for x in range(10)if x%2==0 for y in range(10) if y%3==1]
print(per)

# MACIERZE
B=[[1,2,3],
   [2,3,3],
   [5,6,7]]

print([B[i][i]for i in range(len(B))])

# macierze mnozenie

N=[[1,2],
   [2,2]]
M=[[4,5],
   [1,3]]
print("lista ma1",[M[row][col]*N[row][col] for row in range(2)for col in range(2)])

def ma(M,N):
    resp=[]
    for row in range(2):
        for col in range(2):
            resp.append(M[row][col]*N[row][col])
    return resp

print("ma",ma(M,N))

print("lista ma",[[M[row][col]*N[row][col] for row in range(2)]for col in range(2)])

def ress(M,N):
    res=[]
    for row in range(2):
        tmp=[]
        for col in range(2):
            tmp.append(M[row][col]*N[col][row])
        res.append(tmp)
    return res

print("ma z tmp for",ress(M,N))