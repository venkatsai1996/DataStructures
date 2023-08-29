from os import *
from sys import *
from collections import *
from math import *



#Your code goes here.

name = input()
arr = input()
k = input()

k = int(k)
number_strings = arr.split()

# Convert the number strings to integers and create a list of integers
integer_list = [int(num) for num in number_strings]



for i in range(len(integer_list)):
    if k == 0:
        break
    initial_number = integer_list.pop(0)
    integer_list.append(initial_number)
    k = k - 1

for i in integer_list:
    print(str(i) + " ", end="") 






















