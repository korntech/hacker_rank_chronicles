#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
from time import sleep


def largestPermutation(k, arr):
    # Write your code here
    sorted_arr = sorted(arr, reverse=True)
    if k > len(arr):
        return sorted_arr
    c = 0
    
    my_dict = {item: index for index, item in enumerate(arr)}
    
    for i, tup in enumerate(zip(sorted_arr, arr)):
        if c < k:
            if tup[0] > tup[1]:
                ind = my_dict[tup[0]]
    
                arr[i], arr[ind] = tup[0], tup[1]
                c += 1
                my_dict[tup[0]], my_dict[tup[1]] = i, ind
            
        else:
            break

    return arr
            

        




if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    print(result)