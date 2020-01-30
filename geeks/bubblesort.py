arr = []
print("Enter the size of array: ", end='')
n = int(input())
print("Enter array elements are: ")
for i in range(0,n):
    arr.append(input())

print("Before sorting arrary elements are: ", end='')
for i in range(0, n):
    print(arr[i] + " ", end='')

for i in range (0,n-1):
    if (arr[i] > arr[i+1]):
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp

print("After sorting array elements are: ", end='')
for i in range(0, n):
    print(arr[i] + " ", end='')
    
