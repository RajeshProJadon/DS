arr = [2,4,6,8,10]
key = 6

def binarysearch(arr, low, high, key):
    while high >= low:
        mid = (low+high)//2

        if arr[mid] == key:
            return mid
        elif arr[mid]>key:
            high = mid -1
        else:
            low = mid +1

    return -1

index = binarysearch(arr, 0, len(arr) - 1, key )
if (index == -1):
    print("Element is not present in array")
else:
    print("Element is present in array at index", index)