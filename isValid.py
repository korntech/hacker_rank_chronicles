#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter


def isValid(s):
    # Write your code here
    c = Counter(s)
    if len(set(c.values())) == 1:
        return 'YES'
    elif len(set(c.values())) > 2:
        return 'NO'
    elif len(set(c.values())) == 2:
        c = Counter(c.values())
        if (c[min(Counter(c))] == 1 and min(Counter(c)) == 1) or abs(sub(*c.keys())) == 1 and 1 in c.values():
            return 'YES'
        else:
            return 'NO'
        
   
    
if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    print(result)