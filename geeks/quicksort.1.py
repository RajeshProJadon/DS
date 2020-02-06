arr=[]
print("Enter the size of array: ", end='')
n=int(input())
print("Enter the array element: " )
for i in range(0,n):
    arr.append(input())

print("Array Before sorting: ", end='')
for i in range(0,n):
    print(arr[i] + " ", end='')

print("\n========= Quick Sort ===============")
def partition(arrlist,low,high):
    idx = (low-1)
    pivot = arrlist[high]

    for j in range(low,high):
        if arrlist[j] <= pivot:
            idx = idx+1
            arrlist[idx], arrlist[j] = arrlist[j], arrlist[idx]

    arrlist[idx + 1], arrlist[high] = arrlist[high], arrlist[idx+1]
    return(idx+1)

def quicksort(arrlist, low, high):
    if low < high:
        pi = partition(arrlist, low, high)

        quicksort(arrlist, low, pi-1)
        quicksort(arrlist, pi+1, high)


quicksort(arr, 0, n-1)            
print("\nArray After sorting: ", end='')
for i in range(0,n):
    print(arr[i] + " ", end='')