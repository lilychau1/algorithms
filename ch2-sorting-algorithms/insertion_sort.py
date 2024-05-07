def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = key
    return arr

def insertion_sort_recursive(arr: list, n: int) -> list:
    if n <= 0:
        return arr
    insertion_sort_recursive(arr, n - 1)
    key = arr[n]
    i = n - 1
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        arr[i] = key
        i -= 1
    return arr