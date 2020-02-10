arr = [12,8,15,11,14]
n = len(arr)
key = 10

def lsearch(arr,n,key):
    for i in range(n):
        if (arr[i] == key):
            return i
    return -1

index = lsearch(arr,n,key)
if (index == -1):
    print("Element is not present in array")
else:
    print("Element is present in array at index", index)