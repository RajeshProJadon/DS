arr = []
print("Enter the size of array: ", end='')
n = int(input())

print("Enter the array element: ")
for i in range(0, n):
    arr.append(input())

print("Before sorting array elements are: ", end='')
for i in range(0, n):
    print(arr[i] + " ", end='')

print("Applying insertion sort for sorting on array elements: ")

def insertion_sort(arrList):
    for i in range(1, n):
        j = i - 1
        next_element = arrList[i]
    
    # Compare the current element with the next element

    while (arrList[j] > next_element) and (j >= 0):
        arrList[j+1] =arrList[j]
        j = j -1
    arrList[j+1] = next_element

    print ("After sortinng array elements are: ", end='')
    for j in range(0,n):
        print(arrList[j] + " ", end='')
# def printArray(arrList):
#     print ("After sortinng array elements are: ", end='')
#     for i in range(0,n):
#         print(arrList[i] + " ", end='')

insertion_sort(arr)
# printArray(arr)