from bisect import bisect_left

def fibonaccisearch(arr, key, n):

    fibmm2 = 0
    fibmm1 = 1
    fibmm = fibmm2 + fibmm1

    while(fibmm<n):
        fibmm2 = fibmm1
        fibmm1 = fibmm
        fibmm = fibmm2 + fibmm1

    offset = -1

    while(fibmm>1):
        i = min(offset + fibmm2, n-1)
        if(arr[i]<key):
            fibmm = fibmm1
            fibmm1 = fibmm2
            fibmm2 = fibmm - fibmm1
            offset = i
        elif(arr[i]>key):
            fibmm = fibmm2
            fibmm1 =  fibmm1 - fibmm2
            fibmm2 = fibmm - fibmm1
        else:
            return i
        
    if(fibmm1 and arr[offset+1] == key):
        return offset+1

    return -1

arr = [10, 22, 35, 40, 45, 50, 
       80, 82, 85, 90, 100] 
n = len(arr) 
key = 85
print("Found at index:", 
      fibonaccisearch(arr, key, n))
