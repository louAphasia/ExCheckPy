import  time

def ana(s1,s2):
    start=time.time()
    list1=list(s2)
    pos1=0
    still=True

    while pos1<len(s1) and still:
        pos2=0
        found=False
        while pos2<len(list1) and not found:
            if s1[pos1]==list1[pos2]:
                found=True
            else:
                pos2=pos2+1
        if found:
            list1[pos2]=None
        else:
            still=False
        pos1+=1

        end=time.time()

    return still, end-start




def ana2(s1,s2):
    start=time.time()
    alist=list(s1)
    blist=list(s2)

    alist.sort()
    blist.sort()

    pos=0
    match=True

    while pos<len(s1) and match:
        if alist[pos]==blist[pos]:
            pos+=1
        else:
            match=False
    end=time.time()
    return match, end-start



for x in range(10):
    print("%s is speeed %10.99f " % ana('qwertyuiopasdfghjklzxcvbnm'*100,'mnbvcxzlkjhgfdsapoiuytrewq'*100))
    #o wiele szybszy drugi algorytm z sort
    print("%s is speeed %10.999f " % ana2('qwertyuiopasdfghjklzxcvbnm'*100,'mnbvcxzlkjhgfdsapoiuytrewq'*100))