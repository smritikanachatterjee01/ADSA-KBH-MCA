# Q1. Write a Python program to implement the concept of Bubble sort on the above data set. Print the data set after every iteration.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"After iteration {i+1}: {arr}")

data = [27, 15, 39, 21, 28, 70]
bubble_sort(data)
