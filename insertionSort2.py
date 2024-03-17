#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/insertionsort2/problem
#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here

    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            smaller_value = arr[i]
            for j, val in enumerate(arr[:i]):
                if smaller_value < val:
                    arr.insert(j, smaller_value)
                    arr.pop(i+1)
                    break
        if not i == 1:
            print(*arr, sep=" ")
        
        
     
        
        



            
            
            
        


        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
