def mergesort(arr):
    step_counter = [0]  # Use a list to allow modification inside recursive calls

    def merge_sort_recursive(arr):
        len_arr = len(arr)
        if len_arr <= 1:
            return arr

        middle_index = len_arr // 2

        left = merge_sort_recursive(arr[:middle_index])
        right = merge_sort_recursive(arr[middle_index:len_arr])

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            step_counter[0] += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            step_counter[0] += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            step_counter[0] += 1

        return arr

    sorted_arr = merge_sort_recursive(arr)
    return sorted_arr, step_counter[0]


arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr, step_count = mergesort(arr)
print("Step count:", step_count)
print("Sorted array:", sorted_arr)
    

