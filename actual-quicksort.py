def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = []
    middle = []
    right = []
    for i in arr:
        if i<pivot:
            left.append(i)
        elif i>pivot:
            right.append(i)
        else:
            middle.append(i)
    return quicksort(left)+middle+quicksort(right)