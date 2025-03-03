# 4. Write a Python program to implement the concept of Quick sort on the above data set. Print thedata set after every iteration.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    result = quick_sort(left) + middle + quick_sort(right)
    print(f"Quick sort iteration result: {result}")
    return result

data = [27, 15, 39, 21, 28, 70]
quick_sort(data)
