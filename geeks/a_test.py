import sys
import array
#print("enter the array size : ")
t = int(input())
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(input())
    #print("enter rotate time: ")

while(t>0):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    # #print("enter rotate time: ")
    d = int(input())
    
    #print("enter the array element arr : ")
    
    
    # print("before rotation array:")
    # for i in range(0, n):
    #     print(arr[i], end='')
    
    # if d <= n:
    for i in range(0,d):
        temp = arr[0]
        for j in range(0, n-1):
            arr[j]= arr[j+1]
        arr[n-1]=temp
   
# print("after rotation array:")
    for i in range(0, int(n)):
        print(arr[i], end='')
    t -= 1