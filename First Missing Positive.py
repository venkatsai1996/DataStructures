from os import *
from sys import *
from collections import *
from math import *

def firstMissing(arr, n):
    # Write your function here.
    arr.sort()
    #print(arr)
    counter = 0
    bool_val = True
    final_val = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            if i == len(arr) - 1:
                return 1
            continue
        if arr[i] > 0:
            if counter == 0 and arr[i] == 1:
                counter = arr[i]
                continue
            elif counter == 0 and arr[i] != 1:
                return 1
            else:
                if arr[i] == counter + 1:
                    counter = arr[i]
                    if i == len(arr) - 1:
                        return counter + 1
                    continue
                else:
                    bool_val = False
                    final_val = counter + 1
                    return final_val
    pass



    

# Main Code
t=int(input())

for j in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    ans = firstMissing(arr,n)
    print(ans)
