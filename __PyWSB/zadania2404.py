def slownienr(n):
    D={0:'zero',1:'jeden',2:'dwa',3:'trzy',4:'cztery',5:'pięć',6:'sześć',7:'siedem',8:"osiem",\
       9:'dziewięć',10:"dziesięć", 11:"jedynaście",12:"dwanaście",\
       13:"trzynaście",14:"czternaście",15:"pietnaście",16:"szesnaście",17:"siedemnaście",\
       18:"osiemnaście",19:"dziewiętnąscie",20:"dwadzieścia",30:"trzydzieści",40:"czterdzieści",\
       50:"piędziesiąt",60:"sześcdziesiąt", 70:"siedemdziesiąt",80:"osiemdziesiąt",\
       90:"dziewiędziesiąt",100:"sto",200:"dwieście",300:"trzysta",400:"czterdziesci",500:"pięcset",\
       600:"sześćset",700:"siedemset",800:"osiemset",900:"dziewięćset",1000:"tysiąc"}
    if n<=20:
        for x in D.keys():
            if x==n:
                napis=D[x]
    if n>20:
        m=n%10




    return napis


print(slownienr(20))



import numToWord

def slownie(n):
    s=numToWord.numToWord(n)
    return s


print(slownie(50))

def tabliczka(x1,x2,y1,y2):
    print(x1,x2,x)
     for wiersz in (x1,x2,y1,y2):
         print(wiersz,end="\t")

         for kolumna in (x1,x2,y1,y2):
            print(kolumna,end="\t")
            print(wiersz*kolumna,end="\t")


print(tabliczka(3,5,2,4))