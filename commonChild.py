#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    

    if len(s1) < len(s2):
        short = s1
        long = s2 
    else:
        short = s2 
        long = s1 


    current = [0] * (len(long) + 1)
    previous = [0] * (len(long) + 1)


    for i in range(1, len(long)+1):
        for j in range(1, len(short)+1):
            if long[i-1] == short[j-1]:
                current[j] = previous[j-1] + 1
            else:
                current[j] = max(previous[j], current[j-1])

        previous, current = current, previous

    return previous[len(short)]






if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(result)

   # fptr.write(str(result) + '\n')

  #  fptr.close()
