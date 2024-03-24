#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/gem-stones/problem?isFullScreen=true
#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    # Write your code here
    minerals = set(''.join(arr))
    count = 0
    found = False
    for mineral in minerals:
        for stone in arr:
            if mineral not in stone:
                found = False
                break
            else:
                found = True
        
        if found:
            count += 1
        
    
    print(count)

if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

