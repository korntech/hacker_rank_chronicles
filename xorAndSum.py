#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'xorAndSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def xorAndSum(a, b):
    # Write your code here
    a = int(a, 2)
    b = int(b, 2)
    start=  0
    end = 314159 
    total_sum = 0 
    MOD = (10 ** 9) + 7
    for i in range(start,  end+1):

        total_sum += a ^ (b << i )
      

    total_sum %= MOD   


    return total_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = xorAndSum(a, b)

    print(result)
