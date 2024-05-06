import math
def merge_sort_recursive(arr: list, start: int, end: int) -> list:
    if start < end: 
        mid = start + math.floor((end - start) / 2)
        # Sort left array
        arr = merge_sort_recursive(arr, start, mid)
        # Sort right array
        arr = merge_sort_recursive(arr, mid + 1, end)

        # Merge left and right
        arr = merge(arr, start, mid, end)
    
    return arr
    
    
        
def merge(arr: list, start: int, mid: int, end: int) -> list:
    n_left = mid + 1 - start
    n_right = end - mid
    
    arr_left = []
    arr_right = []
    
    # Copy all elements from arr to arr_left and arr_right
    for i in range(0, n_left): 
        arr_left.append(arr[start + i])
    
    for j in range(0, n_right):
        arr_right.append(arr[mid + 1 + j])
    
    i = 0
    j = 0
    k = start
    
    # Compare one by one the earliest element in the left array (sorted) with the other in the right array (sorted)
    while i < n_left and j < n_right: 
        if arr_left[i] <= arr_right[j]: 
            arr[k] = arr_left[i]
            i += 1
        else:
            arr[k] = arr_right[j]
            j += 1
        k += 1
    
    # If the left array is exhausted, put all elements in the right array to the remaining slots
    if i == n_left:
        while j < n_right:
            arr[k] = arr_right[j]
            j += 1
            k += 1
    if j == n_right:
        while i < n_left:
            arr[k] = arr_left[i]
            i += 1
            k += 1
    return arr
    
if __name__ == '__main__':
    merge_sort_recursive([8, 6, 2, 3, 5, 1, 1, 7], start=0, end=7)
    