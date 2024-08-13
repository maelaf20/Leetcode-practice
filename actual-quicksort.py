case_1 = [5,4,3,8,9,1,6,7,2]
def Quicksort(array):
    if len(array)<=1:
        return array
    pivot = array[len(array)//2]
    left = []
    right = []
    for i in array:
        if i<pivot:
            left.append(i)
        else:
            right.append(i)
    left.append(pivot)
    return Quicksort(left)+Quicksort(right)
print(Quicksort(case_1))