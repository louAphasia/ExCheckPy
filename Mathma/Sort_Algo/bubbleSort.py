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