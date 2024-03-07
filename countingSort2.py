#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    sorted_array = []
    int_array = [0] * 100
    for n in arr:
        int_array[n] += 1

    for i, n in enumerate(int_array):
        sorted_array.extend(n * [i])
            
   
    return sorted_array

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    
