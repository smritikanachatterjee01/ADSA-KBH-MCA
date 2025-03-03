# 6. Write a Python program to show that Quick sort is better than Bubble sort.
import time

# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Quick Sort Algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Dataset
data = [27, 15, 39, 21, 28, 706]

# Measure Bubble Sort Time
start_time = time.time()
bubble_sort(data.copy())
bubble_time = time.time() - start_time

# Measure Quick Sort Time
start_time = time.time()
quick_sort(data.copy())
quick_time = time.time() - start_time

# Output Results
print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
print(f"Quick Sort Time: {quick_time:.6f} seconds")

if quick_time < bubble_time:
    print("Quick Sort is faster than Bubble Sort.")
else:
    print("Bubble Sort is faster than Quick Sort.")