#!/bin/python3

import math
import os
import random
import re
import string
import sys

alpha = string.ascii_lowercase



first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


matrix = [list(row) for row in matrix]

zipped = list(zip(*matrix))

joined = [''.join(tup) for tup in (zipped)]

s = ''.join(joined)
pat = r'(?<=\w)[^\w]+(?=\w)'

print(re.sub(pat, " ", s))