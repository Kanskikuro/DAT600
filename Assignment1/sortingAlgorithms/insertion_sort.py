def insert_sort(arr):
    step_counter = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            step_counter += 1
        arr[j + 1] = key
        step_counter += 1

    return arr, step_counter

arr = [3, 6, 8, 10, 1, 2, 9]
sorted_arr, step_count = insert_sort(arr)
print("Step count:", step_count)
print("Sorted array:", sorted_arr)


            


