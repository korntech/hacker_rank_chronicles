#!/bin/python3
#https://www.hackerrank.com/challenges/marcs-cakewalk/problem?isFullScreen=true
import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):

    calorie.sort(reverse=True)
    return sum(cal * 2 ** i for i, cal in enumerate(calorie))

if __name__ == '__main__':

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    print(result)
