#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
# https://www.hackerrank.com/challenges/recursive-digit-sum/problem?isFullScreen=true
from time import sleep

first = False
def superDigit(n, k):
    # Write your code here
    global first
    if not first:
        x  = str(k)
        if x[0] == '1' and '0' in set(x[1:]) and len(set(x[1:])) == 1:
            n = n * 1
        else:

            n = n * k 
    if first:
        n = n * 1
        pass
    first = True

    if n in range(11):
        return n 
    else:


        return superDigit(sum(map(int, list(str(n)))), k)
        


if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print(result)

    #fptr.write(str(result) + '\n')

   # fptr.close()
#