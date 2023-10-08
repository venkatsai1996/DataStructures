from os import *
from sys import *
from collections import *
from math import *



def firstNonRepeatingCharacter(str):
    character_list = []
    remove_list = []
    for char in str:
        if char in character_list:
            remove_list.append(char)
            character_list.remove(char)
            continue
        if char in remove_list:
            continue
        character_list.append(char)
    if len(character_list) > 0:
        return character_list[0]
    else:
        return str[0]
    # Write your Code here.
