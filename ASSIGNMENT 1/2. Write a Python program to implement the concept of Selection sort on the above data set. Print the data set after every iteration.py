# 2. Write a Python program to implement the concept of Selection sort on the above data set. Printthe data set after every iteration.
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"After iteration {i+1}: {arr}")

data = [27, 15, 39, 21, 28, 70]
selection_sort(data)
