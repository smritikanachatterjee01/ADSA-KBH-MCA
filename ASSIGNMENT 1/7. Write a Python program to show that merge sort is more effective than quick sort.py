# 7. Write a Python program to show that merge sort is more effective than quick sort.
import time

# Merge Sort Algorithm
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort Algorithm (same as above)
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

# Measure Quick Sort Time
start_time = time.time()
quick_sort(data.copy())
quick_time = time.time() - start_time

# Measure Merge Sort Time
start_time = time.time()
merge_sort(data.copy())
merge_time = time.time() - start_time

# Output Results
print(f"Quick Sort Time: {quick_time:.6f} seconds")
print(f"Merge Sort Time: {merge_time:.6f} seconds")

if merge_time < quick_time:
    print("Merge Sort is faster than Quick Sort.")
else:
    print("Quick Sort is faster than Merge Sort.")