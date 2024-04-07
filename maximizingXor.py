#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#
# https://www.hackerrank.com/challenges/maximizing-xor/editorial
from operator import xor


def maximizingXor(l, r):
    # Write your code here
    arr = list(range(l, r+1))
    max_val = 0
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if xor(arr[i], arr[j]) > max_val:
                max_val = xor(arr[i], arr[j])
    
    return max_val  

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    print(result)


