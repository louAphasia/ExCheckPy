def tabliczka(x1,x2,y1,y2):
    for wiersz in (1,x1,y2,x2):
        for kolumna in (1,y1,x1,y2):
            print(wiersz*kolumna,end="\t")
        print("")


print(tabliczka(3,5,2,4))