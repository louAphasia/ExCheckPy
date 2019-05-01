def inserSort(arr):
    for i in range(len(arr)):
        cursor=arr[i]
        pos=i

        while pos>0 and arr[pos-1]>cursor:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=cursor
    return arr

array3=[22,45,2,3,0,1]

print(inserSort(array3))

def insert2(lista):
    for index in range(1,len(lista)):
        current=lista[index]
        pos=index

        while pos>0 and lista[pos-1]>current:
            lista[pos]=lista[pos-1]
            pos=pos-1

        lista[pos]=current

    return lista

print(insert2(array3))