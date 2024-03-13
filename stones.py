#!/bin/python3
# https://www.hackerrank.com/challenges/manasa-and-stones/problem?isFullScreen=true
import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
    # Write your code here
    
    if a == b:
        return [(n-1)*a]
    
    max_val = max(a,b) * (n-1)
    min_val = min(a,b) * (n-1)
    
    return sorted(list(range(min_val, max_val + abs(a-b), abs(a-b))))

if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)
        print(result)

    #     fptr.write(' '.join(map(str, result)))
    #     fptr.write('\n')

    # fptr.close()
