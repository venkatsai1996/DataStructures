from os import *
from sys import *
from collections import *
from math import *

def coverageOfMatrix(mat):
    # Write your code here.
    rows = len(mat)

    colums  =len(mat[0])
    total_sum = 0
    for i in range(0,rows):
        for j in range(0,colums):
            if mat[i][j] == 0:
                if i-1 >= 0:
                    total_sum = total_sum + mat[i-1][j]
                if i+1 <= rows -1:
                    total_sum = total_sum + mat[i+1][j]
                if j - 1 >= 0 :
                    total_sum = total_sum + mat[i][j-1]
                if j + 1 <= colums - 1 :
                    total_sum = total_sum + mat[i][j+1]

    return total_sum

    
    pass
