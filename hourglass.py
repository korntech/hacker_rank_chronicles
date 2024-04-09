#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    max_sum = -54
    for j in range(4):
        for i in range(3, 7):   
            start = i - 3
            first_row = arr[j][start:i]
            second_row = arr[j+1][i-2]
            last_row = arr[j+2][start:i]

            res = sum(first_row) + sum(last_row)+ second_row
            if res > max_sum:
                max_sum = res
            
    
    return max_sum

       

                
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)


