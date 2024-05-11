def merge_sort_recursive(arr: list, start: int, end: int) -> list:
    if start < end: 
        mid = (start + end) // 2
        # Sort left array
        merge_sort_recursive(arr, start, mid)
        # Sort right array
        merge_sort_recursive(arr, mid + 1, end)

        # Merge left and right
        merge(arr, start, mid, end)
        
    return arr
      
def merge(arr: list, start: int, mid: int, end: int) -> list:

    left = arr[start:mid + 1]
    right = arr[mid + 1:end+1]
        
    i = j = 0
    k = start
    
    # Compare one by one the earliest element in the left array (sorted) with the other in the right array (sorted)
    while i < len(left) and j < len(right): 
        if left[i] <= right[j]: 
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    # If the left array is not yet exhausted, put all remaining elements in the left array to the remaining slots
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        
    # If the right array is not yet exhausted, put all remaining elements in the right array to the remaining slots
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        
if __name__ == '__main__':
    merge_sort_recursive([8, 6, 2, 3, 5, 1, 1, 7], start=0, end=7)
    