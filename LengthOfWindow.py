from math import *
from collections import *
from sys import *
from os import *

def LongestSubsetWithZeroSum(arr):

    # Write your Code here.
    # Return an integer denoting the answer.
    lengthOfWindow = len(arr) 
    while lengthOfWindow != 0:
        i = 0 
        j = lengthOfWindow - 1
        while j< len(arr):
            if sum(arr[i:j+1]) == 0 :
                return lengthOfWindow 
            else:
                i = i + 1
                j = j + 1
        lengthOfWindow = lengthOfWindow - 1
    return 0
    pass


