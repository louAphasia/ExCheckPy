array1=[23,0,211,22,21,0,4]


array=[23,0,2,1]

#mergesort(array)


def mergeso(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left,right=mergeso(arr[:mid]),mergeso(arr[mid:])
    print('l,r',left,right)

    return merge(left,right,arr.copy())

def merge(left,right,merged):
    leftcur,rightcur=0,0
    print('lc',left[leftcur],len(left), 'rc', right[rightcur],len(right))
    while leftcur<len(left) and rightcur<len(right):
        if left[leftcur]<=right[rightcur]:
            merged[leftcur+rightcur]=left[leftcur]
            leftcur+=1
            print(leftcur,rightcur, 'len(right)')
        else:
            merged[leftcur+rightcur]=right[rightcur]
            rightcur+=1
            print(leftcur, rightcur, 'ellen(right)')

    for leftcur in range(leftcur,len(left)):
        print("leftc",leftcur,'rightc',rightcur,left[leftcur])
        merged[leftcur + rightcur] = left[leftcur]

    for rightcur in range(rightcur,len(right)):
        print("2leftc", leftcur, '2rightc', rightcur, right[rightcur])
        merged[leftcur + rightcur] = right[rightcur]
    return merged


print(mergeso(array))
