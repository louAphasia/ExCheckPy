def shell(lista):
    sublist_count=len(lista)//2
    while sublist_count>0:
        for start_pos in range(sublist_count):
            gap_insert(lista,start_pos,sublist_count)

        print("size after increments", sublist_count, "the list", lista)

        sublist_count=sublist_count//2

def gap_insert(lista,start,gap):
    for i in range(start+gap,len(lista),gap):
        currval=lista[i]
        pos=i
        while pos>=gap and lista[pos-gap]> currval:
          lista[pos]=lista[pos-gap]
          pos=pos-gap

          lista[pos]=currval



array1=[23,4,3,2,12]

print(shell(array1))