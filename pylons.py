#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def pylons(k, arr):
    plants = 0
    i = 0

    while i < len(arr):
        pos = -1
        for j in range(min(n - 1, i + (k - 1)), max(i - (k - 1), -1), -1):
            if arr[j] == 1:
                pos = j
                break
        if pos == -1:
            return -1
        plants += 1
        i = pos + k

    return plants

       
        

if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    print(result)

   # fptr.write(str(result) + '\n')
#
  #  fptr.close()
