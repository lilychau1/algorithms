def bubble_sort(arr: list) -> list:
    for i in range(0, len(arr)):
        for j in range(len(arr) - 1, i, -1): 
            if arr[j] < arr[i]:
                min = arr[j]
                arr[j] = arr[i]
                arr[i] = min
    return arr