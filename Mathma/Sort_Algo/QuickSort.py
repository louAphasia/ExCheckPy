def quick(lista):
    quickhelp(lista,0,len(lista)-1)

def quickhelp(lista,first,last):
    if first<last:

        split_point=partition(lista,first,last)
        quickhelp(lista,first,split_point-1)
        quickhelp(lista,split_point+1,last)

def partition(lista,first,last):
    pivot_value=lista[first]

    left_mark=first+1
    right_mark=last

    done=False
    while not done:
        while left_mark<=right_mark and lista[left_mark]<=pivot_value:
            left_mark=left_mark+1
        while lista[right_mark]>=pivot_value and right_mark>=left_mark:
            right_mark=right_mark-1

        if right_mark<left_mark:
            done=True
        else:
            temp=lista[left_mark]
            lista[left_mark]=lista[right_mark]
            lista[right_mark]=temp

    temp=lista[first]
    lista[first]=lista[right_mark]
    lista[right_mark]=temp

    return right_mark

array=[23,0,2,1,12,22,10]

quick(array)
print(array)

##################### II KOD

def part(arr,begin,end):
    print('beg1',begin)
    pivot_idx=begin
    for i in range(begin+1,end+1):
        if arr[i]<=arr[begin]:
            pivot_idx+=1
            arr[i],arr[pivot_idx]=arr[pivot_idx],arr[i]
    arr[pivot_idx],arr[begin]=arr[begin],arr[pivot_idx]
    print('pivot',pivot_idx)
    print(arr)
    return pivot_idx

def quick_recursion(arr,begin,end):
    if begin>=end:
        print('BEG2',begin)
        return
    pivot_idx=part(arr,begin,end)
    quick_recursion(arr,begin,pivot_idx-1)
    quick_recursion(arr,pivot_idx+1,end)

def quick_merge(arr,begin=0,end=None):
    if end is None:
        end=len(arr)-1
        print('BEG3',begin)
    return quick_recursion(arr,begin,end)

array2=[23,0,1,3]
quick_merge(array2)
print(array2)
