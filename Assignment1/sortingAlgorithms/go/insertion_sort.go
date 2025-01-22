package main

import (
	"fmt"
	"math/rand"
	"time"
)

func InsertionSort(arr []int) {
	for i := 1; i < len(arr); i++ {
		key := arr[i]
		j := i - 1

		for j >= 0 && key < arr[j] {
			arr[j+1] = arr[j]
			j--
		}
		arr[j+1] = key
	}
}

func testInsertionSort(lenArr int) {
	// Generate a random array of length lenArr with values between -1000 and 1000
	arr := make([]int, lenArr)
	for i := 0; i < lenArr; i++ {
		arr[i] = rand.Intn(2001) - 1000 // Random numbers between -1000 and 1000
	}

	// Measure the time to sort the array
	startTime := time.Now()
	InsertionSort(arr)
	duration := time.Since(startTime)

	// Output the length of the array and the time taken in seconds
	fmt.Printf("Array length: %d, Time taken: %f seconds\n", lenArr, duration.Seconds())
}

func main() {
	// Set a fixed seed for random number generation
	rand.Seed(42)

	// Test for different array lengths
	lengths := []int{100, 1000, 5000, 10000, 20000}
	for _, lenArr := range lengths {
		testInsertionSort(lenArr)
	}
}
