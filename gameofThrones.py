#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import defaultdict


def gameOfThrones(s):
    # Write your code here
    count = defaultdict(int)

    for char in s:
        count[char] += 1

    even = [num for num in count.values() if not num % 2 ]
    odd = [num for num in count.values() if num % 2 ]

    if len(s) % 2:
        if len(odd) != 1 and even:
            return 'NO'
        else:
            return 'YES'
    else:
        if not odd and even:
            return 'YES'
        # check if all values but 1 are even when counting them 
    return 'NO'



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)
    print(result)

   # fptr.write(result + '\n')

   # fptr.close()
