#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    
    reversed_s = list(reversed(s))
   # print(f'reversedstring is {reversed_s}')
    for i in range(len(s) - 1):
        
        #print(f"Ordinal value for {s[i]} is {ord(s[i])} and for {s[i+1]} is {ord(s[i+1])}")

        if abs(ord(s[i]) - ord(s[i+1])) != abs(ord(reversed_s[i]) - ord(reversed_s[i+1])):
            print("Not Funny")
            break
    else:
        print("Funny")


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        print(result)
