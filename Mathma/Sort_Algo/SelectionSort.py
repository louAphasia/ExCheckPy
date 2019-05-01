def selectSort(arr):
    for i in range(len(arr)):
        min=i

        for j in range(i+1,len(arr)):
        #the smallest
            if arr[j]<arr[min]:
                min=j

        #place in front of sorted end of array
        arr[min],arr[i]=arr[i],arr[min]
    return arr

array1=[23,1,0,33,20]

print(selectSort(array1))