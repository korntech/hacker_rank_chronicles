#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    # Write your code here
    sym_diff = set(s1) ^ set(s2) 
    ops = 0
    for char in sym_diff:
        ops += (s1+s2).count(char)
    intersect = set(s1) & set(s2)
    
    for char in intersect:
        ops += abs(s1.count(char) - s2.count(char))
    
    return ops


if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    print(result)