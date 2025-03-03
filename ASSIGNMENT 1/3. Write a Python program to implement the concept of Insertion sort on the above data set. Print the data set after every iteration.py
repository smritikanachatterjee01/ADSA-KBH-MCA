# 3. Write a Python program to implement the concept of Insertion sort on the above data set. Printthe data set after every iteration.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(f"After iteration {i}: {arr}")

data = [27, 15, 39, 21, 28, 70]
insertion_sort(data)
