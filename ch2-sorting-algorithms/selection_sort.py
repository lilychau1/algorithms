def selection_sort(arr: list) -> list:
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        min = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = min
    return arr
            