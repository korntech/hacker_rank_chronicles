#!/bin/python3
#https://www.hackerrank.com/challenges/pangrams/problem?isFullScreen=true
import math
import os
import random
import re
#
import string
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#



def pangrams(s):
    
    return "pangram" if len(set(s.lower().replace(' ',''))) == 26 else "not pangram"
            

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    print(result)
