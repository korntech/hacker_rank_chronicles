#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'andProduct' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER a
#  2. LONG_INTEGER b
#



def andProduct(a, b):
    # Write your code here
    
    while a < b:

        b &= b - 1
    
    return b

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = andProduct(a, b)
        print(result)
       # fptr.write(str(result) + '\n')

   # fptr.close()
