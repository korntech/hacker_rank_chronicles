#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
# https://www.hackerrank.com/challenges/flipping-bits/problem?isFullScreen=true
def flippingBits(n):
    return int(''.join(['1' if x == '0' else '0' for x in f"{n:032b}"]), 2)


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)
        print(result)

        