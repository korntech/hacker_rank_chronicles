#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"


def minimumNumber(n, password):

    num = low = up = spec =  0
    for char in set(password):
        if char in numbers:
            num+=1
        elif char in lower_case:
            low+=1
        elif char in upper_case:
            up+=1
        elif char in special_characters:
            spec += 1

    missing = [num, low, up, spec].count(0)

    if 6 - n > missing:
        return 6 - n
    else:
        return missing


if __name__ == "__main__":

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    print(answer)
