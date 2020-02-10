arr = [2,4,6,8,10]
key = 8

def brecursearh(arr, low, high, key):
    if high >= low:
        mid = (low + high)//2

        if arr[mid] == key:
            return mid
        
        elif arr[mid] > key:
            return brecursearh(arr, low, mid-1, key)
        else:
            return brecursearh(arr, mid+1, high, key)

    else:
        return -1

index = brecursearh(arr, 0, len(arr)-1, key)
if (index == -1):
    print("Element is not present in array")
else:
    print("Element is present in array at index", index)