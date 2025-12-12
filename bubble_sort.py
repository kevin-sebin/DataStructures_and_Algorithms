def bubbleSort(arr):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [5, 10, 3, 7, 2, 1, 6, 7, 4, 10, 11, 8, 15]
print(bubbleSort(arr))