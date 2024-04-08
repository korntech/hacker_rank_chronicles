#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

# https://www.hackerrank.com/challenges/sum-vs-xor/problem?isFullScreen=true
def sumXor(n):
    # Write your code here

    k = bin(n).count('0') - 1 
            
    return  2** k if n !=0 else 1

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for i in range(10000):
        print(f"Testing for {i} | result: {sumXor(i)}")

  

