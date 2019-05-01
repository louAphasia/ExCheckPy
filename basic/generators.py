#reduce

#mechanizm dzialania reduce


def fu(x,y):
    return x*y
def myred(fu,seq):
    t=seq[0]
    print("t",t)
    for next in seq[1:]:
        print(t,next)
        t=fu(t,next)
        print("tpo",t)
    return t

print(myred(fu,[1,2,3,4]))
#map

#filter

