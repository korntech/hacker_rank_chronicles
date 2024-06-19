#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#
from collections import Counter, defaultdict


def countSort(arr):
    c = defaultdict(int)
    first_half = arr[:len(arr)//2]
    for i, item in enumerate(first_half):
        c[''.join(item)] += 1


    

    
    max_val = max(list(map(lambda x: int(x[0]), arr)))
  #  print(f"max val is {max_val}")
    table = (max_val+1) * [0]

    for num in arr:
        table[int(num[0])] +=1

    for i in range(1, len(table)):
        table[i] += table[i-1]

    
    output = len(arr) * [0]

    for num in reversed(arr):
        output[table[int(num[0])] - 1] = num 
        table[int(num[0])] -= 1

    for item in output:
      #  print(f" to jest to{''.join(item)}")
        if ''.join(item) in c and c[''.join(item)] > 0:
            print("-", end=" ")
            c[''.join(item)] -= 1
        else:
            print(item[1], end=" ") 

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
