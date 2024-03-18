#!/bin/python3
# https://www.hackerrank.com/challenges/quicksort1/problem?isFullScreen=true#
import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    pivot = arr[0]
    left = []
    right = []
    equal = []
    out = []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    
    return out

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    print(result)