from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

def findSecondLargest(sequenceOfNumbers):
    # Write your code here.

    if len(sequenceOfNumbers) > 0:
        sequenceOfNumbers.sort()
        #print(sequenceOfNumbers[len(sequenceOfNumbers) - 2])
        secondLargest = sequenceOfNumbers[len(sequenceOfNumbers) - 2]
        if secondLargest == sequenceOfNumbers[len(sequenceOfNumbers) - 1]:
            secondLargest = sequenceOfNumbers[len(sequenceOfNumbers) - 3]
        if len(set(sequenceOfNumbers)) == 1:
            return -1
        return secondLargest
 

# Taking input using fast I/O.
def takeInput():
    n = int(input())

    sequenceOfNumbers = list(map(int, input().strip().split(" ")))

    return sequenceOfNumbers, n

# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t-1
