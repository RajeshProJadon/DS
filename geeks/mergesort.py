arr = []
print("Enter the size of array: ")
n = int(input())
print("Enter the array elements: ", end='')
for i in range(0,n):
    arr.append(input())

# Merge Sort
def mergelist(al1, al2, arrlist):
    i = j = k=0
    while(i < len(al1) and j < len(al2)):
        if(al1[i] < al2[j]):
            arrlist[k] = al1[i]
            i += 1
        else:
            arrlist[k] = al2[j]
            j +=1
        k = k+1

    while(i< len(al1) or j<len(al2)):
        arrlist[k] =al1[i]
        arrlist[k] =al2[j]

        i = i+1
        j = j+1
        k = k+1

def mergeSort(arrlist):
    size = len(arrlist)
    print("size: {0}".format(size))
    if(size < 1):
        print("List is already sorted")
        return size
    else:
        mid = size // 2
        print(mid)
        arrlist1 = arrlist[0:mid]
        arrlist2 = arrlist[mid:]
        mergeSort(arrlist1)
        mergeSort(arrlist2)
        mergelist(arrlist1,arrlist2,arrlist)
    
    print("\nArray after sort: ")
    for i in range(0,n):
        print(arrlist[i] + " ", end='')


mergeSort(arr)