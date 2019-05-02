def mergesort(arr):
    print("splitting", arr)
    if len(arr)>1:
        mid=len(arr)//2
        lefthalf=arr[:mid]
        righthalf=arr[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[i]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1

        print("mergin",arr)

array=[23,0,3,22,111,12,21]

mergesort(array)