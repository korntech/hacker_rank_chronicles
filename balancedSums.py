#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    total = sum(arr)
    sum_count = 0
    if len(arr) > 2 and (len(set(arr[1:])) == 1 or len(set(arr[:len(arr)-1]))) == 1:
        return 'YES'
    else:
        for i in range(0, len(arr)):
            sum_count += arr[i]
        
            if sum_count == total:
                return 'YES'
            total -= arr[i]
    return 'NO'

        

if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result)
