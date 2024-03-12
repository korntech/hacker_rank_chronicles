#!/bin/python3
# https://www.hackerrank.com/challenges/fair-rations/problem?isFullScreen=true
import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

# firt case - at index 0 we have odd number and then even, there is no way to fix it, 

def fairRations(B):
    # Write your code here
    c = 0
    if len(B) == 1 or sum(B) % 2:
        return 'NO'
    else:
        for i in range(len(B)- 1):
            if B[i] % 2:
                B[i] += 1
                B[i+1] += 1
                c += 2
    
    return str(c)
                
    
    
    

if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    print(result)