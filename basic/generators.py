
#yield

def gen():
    for i in range(10):
        X=yield i
        print("for",X)

G=gen()
print("n1",next(G))
print("n2",next(G))
print("__next",G.__next__())

print("send",G.send(77))
print("send",G.send(88))
print("send",G.send(120))
print("n1",next(G))
print("n1",next(G))
print("n1",next(G))

#generator składany

gs=(x**2 for x in range(4))
print('z gs',gs.__next__())

i1=iter(gs)
print(next(i1))
print(next(i1))
g2=(x**2 for x in range(4))

i2=iter(g2)
print(next(i1))
print('i2',next(i2))


#mechanizm dzialania reduce

"""def fu(x,y):
    return x*y
def myred(fu,seq):
    t=seq[0]
    print("t",t)
    for next in seq[1:]:
        print(t,next)
        t=fu(t,next)
        print("tpo",t)
    return t

print(myred(fu,[1,2,3,4]))"""

def mymap(fu,*seq):
    res=[]
    for args in zip(*seq):
        res.append(fu(*args))
    return res

def mymapy(fu,*seq):
    res=[]
    for args in zip(*seq):
        yield fu(*args)

print(mymap(abs,[1,-2,3,-4]))

print(list(mymapy(abs,[1,-2,-3,5])))

print(next(mymapy(abs,[1,-2,3,-4])))
print(next(mymapy(abs,[1,-2,3,-4])))
print(next(mymapy(abs,[2,-2,3,-4])))
print(next(mymapy(abs,[1,-2,3,-4])))

def mymapr(fu,*seq):
    return (fu(*args) for args in zip(*seq))

print('return',next(mymapr(abs,[1,2])))
print('return',next(mymapr(abs,[1,2])))
print('return',next(mymapr(abs,[1,2])))
#print('return',mymapr(abs,[2,3,-3]).send(100))
