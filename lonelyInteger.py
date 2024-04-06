#!/bin/python3

import math
import os
import random
import re
import sys
# https://www.hackerrank.com/challenges/lonely-integer/problem?isFullScreen=true
#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
from collections import defaultdict


def lonelyinteger(a):
    # Write your code here
    count = defaultdict(int)

    for item in a:
        count[item] += 1
    
    sorted_dict = sorted(count.items(), key=lambda item: item[1])

    return sorted_dict[0][0]

if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

   
    print(result)