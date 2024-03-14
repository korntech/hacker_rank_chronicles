#!/bin/python3

# https://www.hackerrank.com/challenges/happy-ladybugs/problem?isFullScreen=true
import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    
    if b.count('_') == len(b):
        return 'YES'
    elif '_' not in b and 1 in [b.count(x) for x in set(b) if x != "_"]:
        return 'NO'
    elif 1 in [b.count(x) for x in set(b) if x != "_"]:
        return 'NO'
    elif '_' not in b:
        for i in range(1, len(b) - 1):
            if b[i] != b[i-1] and b[i] != b[i+1]:
                return 'NO'
        return 'YES'
    else:
        return 'YES'

if __name__ == '__main__':
 #   fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)
        print(result)

     #   fptr.write(result + '\n')

  #  fptr.close()
