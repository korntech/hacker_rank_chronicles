#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter
from collections import deque

def superReducedString(s):
    ind = 0
    s_list = list(s)
    while True and len(s_list) > 1:
        if s_list[ind] == s_list[ind+1]:
            del s_list[ind:ind+2]
            ind = 0
        else:
            ind += 1
        if ind + 1 == len(s_list) or not s_list:
            break
 
    return "".join(s_list) if s_list else "Empty String"
    

        


if __name__ == '__main__':

    s = input()

    result = superReducedString(s)

    print(result)
