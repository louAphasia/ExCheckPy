def bubbleSort(arr):
    def swap(i,j):
        arr[i],arr[j]=arr[j],arr[i]

    n=len(arr)
    swapped=True

    x=-1
    while swapped:
        swapped=False
        x+=1
        for i in range(1,n-x):
            if arr[i-1]>arr[i]:
                swap(i-1,i)
                swapped=True
    return arr

array1=[22,23,1,4,5,6,11,0]

print(bubbleSort(array1))

array2=[3,1,2,0,25,21]
def bubble2(lista):
    for num in range(len(lista)-1,0,-1):
        for i in range(num):
            if lista[i]>lista[i+1]:
                tmp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=tmp
    return lista

print(bubble2(array2))

def shbubble(lista):
    exch=True
    num=len(lista)-1
    while num>0 and exch:
        exch=False
        for i in range(num):
            if lista[i]>lista[i+1]:
                exch=True
                list[i],lista[i+1]=lista[i+1],lista[i]
    return lista

print(shbubble(array2))
