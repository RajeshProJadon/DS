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
def quick(arrlist,size,beg,end,loc):
    left = beg
    right = end - 1
    loc = beg
    #print("left:{0},Right:{1}, loc:{2}\n ".format(left, right, loc))
    while (arrlist[loc] <= arrlist[right]) and (loc != right):
        right = right - 1
        if loc == right:
            print("same1")
            return
            
        if arrlist[loc] > arrlist[right] :
            temp = arrlist[loc]
            arrlist[loc] = arrlist[right]
            arrlist[right] = temp

            loc=right
    

    # print("loc:{0}, left:{1}".format(loc,left))
    while (arrlist[left] <= arrlist[loc]) and (left != loc):
        left = left + 1

        if loc == left:
            print("same")
            return

        if (arrlist[left] > arrlist[loc]):
            temp = arrlist[loc]
            arrlist[loc] = arrlist[left]
            arrlist[left] = temp

            loc =left
   

def quicksort(arrlist1):
    top = -1
    size = len(arrlist1)
    lower = [0] * size
    upper = [0] * size
    loc1 = 0
    
    if size > 0:
        top = top +1
        lower[top] = 0
        top = top + 1
        upper[top] = size
        print("lower: {0}".format(lower[top]))
        print("upper: {0}".format(upper[top]))

    while top >= 0:
        beg = lower[top]
        end = upper[top]
        top = top -1

        quick(arrlist1,size,beg,end,loc1)

        if (beg < loc1-1):
            top = top +1
            lower[top] = beg
            upper[top] = loc1-1

        if (loc1+1 < end):
            top = top+1
            lower[top] = loc1 + 1
            upper[top] = end


quicksort(arr)

