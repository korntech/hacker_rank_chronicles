#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
# k is the divisor
from itertools import combinations


def nonDivisibleSubset(k, s):
    table = defaultdict(int)
    for num in s:
        table[num % k] += 1
    
    res = 0
    
    if 0 in table:
        res += 1
    
    if k % 2 == 0:
        val = k // 2
        if val in table:
            res += 1
    
    for i in range(1, (k // 2) + 1):
        if i != k - i:
            res += max(table[i], table[k - i])
    
    return res

    






if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(result)
