#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#


def extraLongFactorials(n):

    return reduce(lambda a,b : a*b, list(range(1, n+1)))



# import math

# def extraLongFactorials(n):

#     if n == 0:
#         return 1
#     else:
#         return n * extraLongFactorials(n-1)
        
        
if __name__ == '__main__':

    n = int(input().strip())

    print(extraLongFactorials(n))
