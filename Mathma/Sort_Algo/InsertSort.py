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