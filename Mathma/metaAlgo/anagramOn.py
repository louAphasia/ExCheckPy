
import time
def anag3(s1,s2):
    start=time.time()
    c1=[0]*26
    c2=[0]*26

    for i in range(len(s1)):
        pos=ord(s1[1])-ord('a')  #ord integer z UNICODE
        c1[pos]+=1

    print(pos , c1[pos])

    for i in range(len(s2)):
        pos=ord(s2[i])-ord('a')
        c2[pos]+=1

    print(pos , c2[pos])

    j=0
    still=True
    while j<26 and still:   #26 characters alfabet
        print(c1)
        print(c2)
        if c1[j]==c2[j]:
            j+=1
        else:
            still=False

    end=time.time()
    return still,end-start


print(" odp %s but the time %10.99f" % anag3('asdfg', 'sdfag'))