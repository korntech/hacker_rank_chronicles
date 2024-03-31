#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):

    important_count = sum(1 if x[1] else 0 for x in contests)

    if important_count == k or important_count < k:
        return sum(x[0] for x in contests)
    else:
        diff = important_count - k 
        important_only = sorted([x[0] for x in contests if x[1] == 1])

        return sum(x[0] for x in contests) - 2 * sum(important_only[:diff])



    # Write your code here

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(result)
   
