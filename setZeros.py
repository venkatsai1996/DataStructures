from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    #print(matrix)
    temp_matrix = matrix
    rows = len(matrix)
    cols = len(matrix[0])
    result_list = []
    for i in range(0,rows):
        for j in range(0,cols):
            li = []
            if matrix[i][j] == 0:
                li = [i,j]
            if len(li) != 0:
                result_list.append(li)
    for i in result_list:

        for row in range(0,rows):
            matrix[row][i[1]] = 0
        for col in range(0,cols):
            matrix[i[0]][col] = 0
            
                            
   

