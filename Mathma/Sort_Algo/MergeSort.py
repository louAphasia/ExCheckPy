array1=[23,0,211,22,21,0,4]


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
