#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#
from time import sleep


def decentNumber(n):
    # Write your code here
    
    if n <= 2:
        print(-1)
    elif not n % 3:
        print(n * '5')
    elif n % 5 or n % 3:
        old = n
        val = 1
        while n > 0:
            n -= 1

            if not n % 3 and not val % 5:
                print(n * '5' + val * '3')
                return
            val += 1
    elif not n % 5: 
        print(n * '3')
    else:
        print(-1)
    





if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)

