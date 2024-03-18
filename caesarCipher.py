#!/bin/python3
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem?isFullScreen=true
import math
import os
import random
import re
#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
import string
import sys

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

def caesarCipher(s, k):
    # Write your code here
    new_s = []
    for char in s:
        if char.isalpha():
            if char.isupper():
                new_char = uppercase[(uppercase.index(char) + k) % 26]
            else:
                new_char = lowercase[(lowercase.index(char) + k) % 26]
        else:
            new_char = char
        new_s.append(new_char)

    return ''.join(new_s)








if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)