#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here

    last = arr[-1]
    copy = arr
    for i, num in enumerate(reversed(arr[:-1]), 1):
        if num > last:
            copy[-i] = num
            print(*copy)
        else:
            copy[-i] = last
            print(*copy)
            break

    if last not in copy:
        copy[0] = last
        print(*copy)
            
            
            
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
