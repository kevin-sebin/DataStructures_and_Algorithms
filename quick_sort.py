def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        return quickSort(left) + [pivot] + quickSort(right)

arr = [21, 9, 3, 4, 1, 3, 7, 343]
print(quickSort(arr))