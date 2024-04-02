#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#
from collections import defaultdict


def beautifulPairs(A, B):
    # Write your code here


    count = 0
    for item in A:
        if item in B:
            B.remove(item)
            if len(B) != 0:
                count+=1
    
    if len(B) == 0:
        return len(A) - 1

    return count+1 if count else count
    

if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)
    print(result)

  #  fptr.write(str(result) + '\n')

  #  fptr.close()
