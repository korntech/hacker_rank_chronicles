#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#
from collections import deque


def equalStacks(h1, h2, h3):
    # Write your code here
    h1, h2, h3 = [deque(v) for v in [h1, h2, h3]]
    s1, s2, s3 =  [sum(v) for v in [h1, h2, h3]]


    while s1 != s2 or s1 != s3:

        if s1 > s2 or s1 > s3:
            s1 -= h1.popleft()
            continue
        
        if s2 > s1 or s2 > s3:
            s2 -= h2.popleft()
            continue
        
        if s3 > s1 or s3 > s2:
            s3 -= h3.popleft()
            continue

        
            
      

    
    return s1
    

            





    
    


if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    print(result)
   # fptr.write(str(result) + '\n')

   # fptr.close()
