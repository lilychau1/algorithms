from typing import Tuple
def merge_sort_with_inversion_count(arr: list, start: int, end: int) -> Tuple[list, int]:
    inversion_count = 0
    if start < end:
        mid = (start + end) // 2
        # Sort left array
        arr, inversion_count_left = merge_sort_with_inversion_count(arr, start, mid)
        # Sort right array
        arr, inversion_count_right = merge_sort_with_inversion_count(arr, mid + 1, end)
        
        arr, inversion_count_merge = merge(arr, start, mid, end)
        inversion_count = inversion_count + inversion_count_merge + inversion_count_left + inversion_count_right
    
    return arr, inversion_count

def merge(arr: list, start: int, mid: int, end: int) -> int:
    inversion_count = 0

    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]
    
    i = j = 0
    k = start
    
    # Compare one by one the earliest element in the left array (sorted) with the other in the right array (sorted)
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else: 
            arr[k] = right[j]
            inversion_count += (len(left) - i)
            j += 1
        k += 1
        
    # If the left array is not yet exhausted, put all remaining elements in the left array to the remaining slots
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
            
    # If the left array is not yet exhausted, put all remaining elements in the right array to the remaining slots
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        
    return arr, inversion_count

if __name__ == '__main__':
    merge_sort_with_inversion_count([8, 6, 2, 3, 5, 1, 1, 7], start=0, end=7)
    