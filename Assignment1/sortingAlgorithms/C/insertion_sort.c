#include <stdio.h>

void InsertionSort(int arr[], int len_arr) {

    for(int i = 1; i < len_arr;i++) {
        int key = arr[i];
        int j = i -1;

        while(j >= 0 && key < arr[j]) {
            arr[j+1] = arr[j];
            j -= 1;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int arr[] = {3, 6, 8, 10, 1, 2, 1};
    int len_arr = sizeof(arr) / sizeof(arr[0]);
    InsertionSort(arr,len_arr);

    for(int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
        printf("%d, ",arr[i]);
    }
    printf("\n");

    return 0;
}