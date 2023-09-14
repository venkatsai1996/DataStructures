from os import *
from sys import *
from collections import *
from math import *

def isMatrixSymmetric(matrix):
    # Write your code here.  
    rows = len(matrix)
    cols = len(matrix[0])
    boo = False
    for i in range(0,rows):
        for j in range(0,cols):
            if i == j:
                continue
            if matrix[i][j] ==  matrix[j][i]:
                continue
            else:
                return False
    return True
