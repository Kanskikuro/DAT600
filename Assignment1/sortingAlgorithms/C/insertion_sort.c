#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void InsertionSort(int arr[], int len_arr) {
    for (int i = 1; i < len_arr; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && key < arr[j]) {
            arr[j + 1] = arr[j];
            j -= 1;
        }
        arr[j + 1] = key;
    }
}

void test_insertion_sort(int len_arr) {
    // Generate a random array of length len_arr
    int arr[len_arr];
    for (int i = 0; i < len_arr; i++) {
       arr[i] = rand() % 2001 - 1000;  // Random numbers between 0 and 999
    }

    // Measure the time to sort the array
    clock_t start_time = clock();
    InsertionSort(arr, len_arr);
    clock_t end_time = clock();

    // Calculate the time taken
    double time_taken = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    // Output the length of the array and the time taken
    printf("Array length: %d, Time taken: %lf seconds\n", len_arr, time_taken);
}

int main() {
    // Set a fixed seed for random number generation
    srand(42);

    // Test for different array lengths
    int lengths[] = {100, 1000, 5000, 10000, 20000};
    int num_tests = sizeof(lengths) / sizeof(lengths[0]);

    for (int i = 0; i < num_tests; i++) {
        test_insertion_sort(lengths[i]);
    }

    return 0;
}
