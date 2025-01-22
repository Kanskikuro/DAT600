def quicksort(arr):
    step_counter = [0]

    def quick_sort_recursive(arr):
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
            step_counter[0] += 1

        return quick_sort_recursive(left) + middle + quick_sort_recursive(right)

    sorted_arr = quick_sort_recursive(arr)
    return sorted_arr, step_counter[0]

arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr, step_count = quicksort(arr)
print("Step count:", step_count)
print("Sorted array:", sorted_arr)




