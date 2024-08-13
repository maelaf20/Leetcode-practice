def quicksort(array,low,high):
    if low<high:
        pivot_index = partition(array,low,high)
        quicksort(array,low,pivot_index-1)
        quicksort(array,pivot_index+1,high)
def partition(array,low,high):
    pivot = array[high]
    i = low-1
    for j in range(low,high):
        if array[j]<pivot:
            i+=1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[high] = array[high],array[i+1]
    return i+1
arr = [22,11,66,33,44,55,77,99,88]
quicksort(arr,0,len(arr)-1)
print(arr)