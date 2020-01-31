arr = []
print("Enter the size of Array: ", end='')
n = int(input())

print("Enter the array element: ", end='')
for i in range(0, n):
    arr.append(input())

print("Array before sorting: ")
for i in range(0, n):
    print(arr[i] + " ", end='')

def minnumber(arrlist):
    for i in range(0, n-1):
        minindex = i
       
        for j in range(i+1, n):
            if(arrlist[minindex] > arrlist[j]):
                minindex = j
                print("\n miniindex: {0} ".format(minindex))
    
        # if(minindex != i):
        print("items swaped: " + arrlist[i] + " " + arrlist[minindex])
        temp = arrlist[i]
        arrlist[i] = arrlist[minindex]
        arrlist[minindex] = temp
            
        print("iteration: {0}".format(i+1))
        for j in range(0,n):
             print(arrlist[j] + " ", end='')
    # print ("After sortinng array elements are: ", end='')
    

   

# def selection_sort(arrlist1):
#     loc = minnumber(arrlist1)
#     print("Location: " + loc)
    # for i in range(0,n): 
    #     temp = loc
    #     arrlist1[]

minnumber(arr)

# selection_sort(arr)
