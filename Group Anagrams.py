from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def getGroupedAnagrams(inputStr):
    # Write your code here.
    finalDict = {}
    for i in inputStr:
        temp = ''.join(sorted(i))
        if temp in finalDict.keys():
            finalDict[temp].append(i)
        else:
            finalDict[temp] = [i]
    #print(finalDict)   
    for i in finalDict.keys():
        temp = ''
        for k in finalDict[i]:
            temp = temp + k +' '
        print(temp)
    

def sortString(str):
    return ''.join(sorted(str))

def takeInput():

    n = stdin.readline().strip()
    inputStr = list(stdin.readline().strip().split(" "))

    return inputStr, n


def printAnswer(groupedAnagram):
    for group in groupedAnagram:
        group.sort()

    groupedAnagram.sort()

    print('\n'.join(map(' '.join, groupedAnagram)))


T = int(stdin.readline().strip())
for i in range(T):
    inputStr, n = takeInput()
    groupedAnagram = getGroupedAnagrams(inputStr)
    #print(groupedAnagram)
