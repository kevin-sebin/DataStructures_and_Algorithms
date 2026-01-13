import math
from quick_sort import quickSort

def bucketSort(arr):
    if not arr:
        return
    div = math.ceil((max(arr)+1)/10)
    buckets = [[] for x in range(10)]
    for i in range(len(arr)):
        index = math.floor(arr[i]/div)
        buckets[index].append(arr[i])
    fin = []
    for j in range(len(buckets)):
        buckets[j] = quickSort(buckets[j])
        fin.extend(buckets[j])
    return fin


print(bucketSort([140, 100, 30, 120, 10, 5]))