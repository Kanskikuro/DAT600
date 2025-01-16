def quicksort(arr):

    len_arr = len(arr)
    if len_arr <= 1:
        return arr

    pivot_index = len_arr // 2

    pivot = arr[pivot_index]

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    sorted_arr = quicksort(left) + middle + quicksort(right)

    return sorted_arr
        


arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)




