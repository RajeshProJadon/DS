import array

arr = array.array('i', [1, 2, 3])
for i in range(0, 3):
    print(arr[i])
print("\r")

arr.append(4)
for i in range(0,4):
    print(arr[i])

arr.insert(2, 5)
for i in range(0,4):
    print(arr[i])
print("\r")

arr.reverse()
for i in range(0,5):
    print(arr[i])
print("\r")

arr.remove(5)
for i in range(0,4):
    print(arr[i])
print("\r")