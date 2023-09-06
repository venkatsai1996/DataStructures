from os import *
from sys import *
from collections import *
from math import *

def minimumParentheses(pattern):
    count = 0
    #li = list(pattern)
    while '()' in pattern:
        pattern = pattern.replace('()', '', 1)
    return len(pattern)
    
    # for i in li:
    #     if i == '(' and i + 1 == ')':
    #         li.pop(char)
    # for i in range(len(li)):
    #     j = i+1
    #     # if i == len(li) -1:
    #     #     count = count + 1
    #     #     return count
    #     # j = i+1
    #     # if i == len(li) - 2:
    #     #     if li[i] == '(' and li[j] == ')':
    #     #         return count
    #     #     else:
    #     #         count = count + 2
    #     #         return count
    #     if li[i] == '(' and li[j] == ')':
    #         li.pop(i)
    #         li.pop(i+1)
    #         continue
    #     print(li)
    #     return len(li)
  
    # Write your code here
    # Return the minimum number of parentheses required.
