def mergesort(arr):
    len_arr = len(arr)
    if len_arr <= 1:
        return arr


    middle_index = len_arr // 2

    left = mergesort(arr[:middle_index])
    right = mergesort(arr[middle_index : len_arr])


    i = 0
    j = 0
    k = 0
        
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1

     # If there are remaining elements in left, copy them
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # If there are remaining elements in right, copy them
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = mergesort(arr)
print("Sorted array:", sorted_arr)
    

