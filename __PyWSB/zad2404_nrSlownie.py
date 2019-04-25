def slownienr(n):
    D={0:'zero',1:'jeden',2:'dwa',3:'trzy',4:'cztery',5:'pięć',6:'sześć',7:'siedem',8:"osiem",\
       9:'dziewięć',10:"dziesięć", 11:"jedynaście",12:"dwanaście",\
       13:"trzynaście",14:"czternaście",15:"pietnaście",16:"szesnaście",17:"siedemnaście",\
       18:"osiemnaście",19:"dziewiętnąscie",20:"dwadzieścia",30:"trzydzieści",40:"czterdzieści",\
       50:"piędziesiąt",60:"sześcdziesiąt", 70:"siedemdziesiąt",80:"osiemdziesiąt",\
       90:"dziewiędziesiąt",100:"sto",200:"dwieście",300:"trzysta",400:"czterdziesci",500:"pięcset",\
       600:"sześćset",700:"siedemset",800:"osiemset",900:"dziewięćset",1000:"tysiąc"}
    napis=''
    if n>=1000:
        napis=napis+D[1000]
        n=n-1000
    if 1000>n>=100:
        k=(n//100)*100
        for x in D.keys():
            if k==x:
                napis=napis+D[x]
        n=n-k
    if  100>n>20:
        m = (n//10)*10
        for x in D.keys():
            if x == m:
                napis=napis+D[x]
        n=n-m
    if n<20:
        for x in D.keys():
            if n == x:
                napis =napis+D[x]



    return napis


print(slownienr(1322))





