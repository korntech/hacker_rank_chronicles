#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/priyanka-and-toys/problem?isFullScreen=true

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w):
    # Write your code here
    count = 1
    w.sort()

    current_min = w[0]

    for i in range(len(w)):
        
        if not w[i] - current_min <= 4:
          #  print(f"value: '{w[i]}' is not withing range to current_min {current_min}")
            count+=1
            current_min = w[i]
    
    return count
            





if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)
    print(result)
   # fptr.write(str(result) + '\n')

   # fptr.close()
