def heapify(arr, n, i, step_counter):
    largest = i  # Initialize the largest as root
    while True:
        left = 2 * largest + 1  # Left child index
        right = 2 * largest + 2  # Right child index
        current = largest

        # Check if the left child exists and is greater than the root
        if left < n and arr[left] > arr[largest]:
            largest = left
        step_counter[0] += 1

        # Check if the right child exists and is greater than the largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right
        step_counter[0] += 1

        # If no change, heap property is satisfied
        if largest == current:
            break

        # Swap and move down the tree
        arr[current], arr[largest] = arr[largest], arr[current]
        step_counter[0] += 1

def heapsort(arr):
    step_counter = [0]
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, step_counter)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to the end
        step_counter[0] += 1
        heapify(arr, i, 0, step_counter)  # Call heapify on the reduced heap

    return arr, step_counter[0]

arr = [12, 11, 13, 5, 6, 7, 10]
print("Original array:", arr)
arr, step_count = heapsort(arr)
print("Step Count:", step_count)
print("Sorted array:", arr)