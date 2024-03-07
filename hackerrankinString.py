#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def hackerrankInString(s):
    pat = list('hackerrank')
    for char in s:
        if char == pat[0]:
            del pat[0]
        if not len(pat):
            break
        
    if not pat:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':


    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        print(result)