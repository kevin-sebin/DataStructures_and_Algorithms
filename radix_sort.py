def radixSort(arr):
    if not arr:
        return
    dig = -len(str(max(arr)))
    for i in range(-1, dig-1, -1):
        buckets = [[] for x in range(10)]
        for j in range(len(arr)):
            if len(str(arr[j]))+i < 0:
                buckets[0].append(arr[j])
            else:
                buckets[int(str(arr[j])[i])].append(arr[j])
        arr = []
        for k in buckets:
            arr.extend(k)
    return arr
    

print(radixSort([140, 100, 30, 120, 10, 5]))