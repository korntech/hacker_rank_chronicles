
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#
# https://www.hackerrank.com/challenges/two-arrays/problem?isFullScreen=true

def twoArrays(k, A, B):
    # Write your code here
    sorted_a = sorted(A)
    sorted_b = sorted(B, reverse=True)
    
    for tup in zip(sorted_a, sorted_b):
        if sum(tup) < k:
            return 'NO'
    
    return 'YES'

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)
        print(result)
       # fptr.write(result + '\n')

    #fptr.close()
