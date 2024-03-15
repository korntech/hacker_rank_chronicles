#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#
sys.set_int_max_str_digits(1000000)
def bigSorting(unsorted):
    # Write your code here
    
    new = []
    for item in unsorted:
        new.append((item, len(item)))
    
    s = sorted(new, key=lambda x: (x[1], int(x[0])))

    s = map(lambda x: x[0], s)


    return list(s)

    
    

if __name__ == '__main__':

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    print(result)
