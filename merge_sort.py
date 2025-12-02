def mergeSort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr)//2
        sub = []
        left_half = mergeSort(arr[:mid])
        right_half = mergeSort(arr[mid:])
        p1 = 0
        p2 = 0
        while p1 < len(left_half) and p2 < len(right_half):
            if left_half[p1] < right_half[p2]:
                sub.append(left_half[p1])
                p1 += 1
            else:
                sub.append(right_half[p2])
                p2 += 1
        sub.extend(left_half[p1:])
        sub.extend(right_half[p2:])
        return sub

arr = [21, 9, 3, 4, 1, 3, 7, 343]
print(mergeSort(arr))