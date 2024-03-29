#!/bin/python3

# https://www.hackerrank.com/challenges/countingsort1/problem?isFullScreen=true
import math
import os
import random
import re
import sys
import time

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    int_array = [0] * 100
    for n in arr:
        int_array[n] += 1

    return int_array

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(result)