import array

arr = array.array('i', [1,2,3,4,5,6])

for j in range(0,2):
    temp = arr[0]
    for i in range(0, 5):
        arr[i]= arr[i+1]
    arr[5]=temp

for i in range(0, 6):
    print(arr[i])