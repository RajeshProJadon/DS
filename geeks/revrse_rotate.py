
def  reverseArray(arr, start, end):
    while(start<end):
        temp = arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start += 1
        end -=1

def leftRotate(arr, d):
    if d==0:
        return
    n = len(arr)
    reverseArray(arr,0,n-1)
    reverseArray(arr,d,n-1)
    reverseArray(arr,0,n-1)

def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i])

print("Enter arrar element:")
n=int(input())
arr = []
for i in range(0, n):
    arr.append(input())
print("enter divide:")
d=int(input())
# d = d%n
leftRotate(arr,d)
print("array after rotation:")
printArray(arr)

