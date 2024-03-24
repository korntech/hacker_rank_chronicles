#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import chain, combinations

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true

def closestNumbers(arr):
    # Write your code here
    arr = sorted(arr)
    min_diff = abs(arr[0] - arr[1])

    for i in range(1, len(arr) - 1):
        if abs(arr[i] - arr[i+1]) < min_diff:
            min_diff = abs(arr[i] - arr[i+1])
    answers = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i] - arr[j]) == min_diff:
                answers.append(arr[i])
                answers.append(arr[j])
            elif abs(arr[i] - arr[j]) > min_diff:
                break
            else:
                pass


    return answers


if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    print(result)
