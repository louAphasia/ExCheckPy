#error


"""def mergesort(arr):
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

        print("mergin",arr)"""

array=[23,0,3,12,1,6,20]

#mergesort(array)


def mergeso(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left,right=mergeso(arr[:mid]),mergeso(arr[mid:])

    return merge(left,right,arr.copy())

def merge(left,right,merged):
    leftcur,rightcur=0,0
    while leftcur<len(left) and rightcur<len(right):
        if left[leftcur]<=right[rightcur]:
            merged[leftcur+rightcur]=left[leftcur]
            leftcur+=1
        else:
            merged[leftcur+rightcur]=right[rightcur]
            rightcur+=1

    for leftcur in range(leftcur,len(left)):
        merged[leftcur + rightcur] = left[leftcur]

    for rightcur in range(rightcur,len(right)):
        merged[leftcur + rightcur] = right[rightcur]
    return merged


print(mergeso(array))
