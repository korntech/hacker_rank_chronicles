#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
from operator import xor


#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def sansaXor(arr):
    # Write your code here
    result = 0
    for i in range(len(arr)):
        
        left = i + 1
        right = n - i
        
        total = left * right 
        
        if total % 2 == 1:
            result ^= arr[i]
    
    return result




if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))


        result = sansaXor(arr)

        print(result)