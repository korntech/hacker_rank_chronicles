#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr.sort()
    min_unfairness = arr[-1] - arr[0]
    for i in range(len(arr) - k + 1):
        
        slice = arr[i:i+k]
        if slice[-1] - slice[0] < min_unfairness:
            min_unfairness = slice[-1] - slice[0]


    return min_unfairness
if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)

   # fptr.write(str(result) + '\n')

  #  fptr.close()
