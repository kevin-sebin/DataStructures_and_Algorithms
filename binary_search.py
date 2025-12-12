def binarySearch(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1
    
arr = [3, 5, 9, 10, 13, 19, 22, 25, 27, 30]
print(binarySearch(arr, 12))
