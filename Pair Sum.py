from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, n, target):
    el = target
    count = 0
    for i in arr:
        el = target - i
        if i >= target / 2:
            break
        if el in arr and el != i :
            count +=  1
              
    if count == 0:
        return -1
    else:
        return count 
    # Write your code here.
    pass
