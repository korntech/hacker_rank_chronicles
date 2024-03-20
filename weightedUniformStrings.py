#!/bin/python3

import math
import os
import random
import re
import string
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
    #
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem


def weightedUniformStrings(s, queries):
    unique_chars = set(s)
    lower_chars = {letter: index for index, letter in enumerate(string.ascii_lowercase, start=1) if letter in unique_chars}

    max_lengths = {}
    answers = []
    current_char = s[0]
    current_length = 1

    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == current_char:
            current_length += 1
        else:
            if current_char not in max_lengths or current_length > max_lengths[current_char]:
                max_lengths[current_char] = current_length
            if i < len(s):
                current_char = s[i]
            current_length = 1

    for key, value in max_lengths.items():
        max_lengths[key] = value * lower_chars[key]
        

    for query in queries:
        for char, maxi in max_lengths.items():
            if not query % lower_chars[char] and query // lower_chars[char] <=  maxi:
                answers.append("Yes")
                break
        else:
            answers.append("No") 
    


    return answers


    






        




if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    print(result)