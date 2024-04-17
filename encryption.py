#!/bin/python3

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
import math
import os
import random
import re
import sys


def encryption(s):
    # Write your code here

    s = s.replace(" ","")

    row = math.floor(len(s)**0.5)
    col = math.ceil(len(s)**0.5)
   # print(f"Floor is {row} and ceil is {col}.")
    
    if row * col < len(s):
        row += 1
    matrix = []
    for i in range(0,len(s) , col):
        matrix.append(s[i:i+col])


   # print(f"matrix is {matrix}")
    decoded_msg = ""
    for i in range(len(matrix[0])):
        for word in matrix:
            decoded_msg += word[i:i+1]
        decoded_msg += " "


    return decoded_msg

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)
    print(result)