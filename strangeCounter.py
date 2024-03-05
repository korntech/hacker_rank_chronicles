#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):  
    target = t
    time = 1
    value = 3
    init_value = value 
    while True:
        if target == time:
            return value
        elif value == 1:
            time += 1
            value = init_value * 2
            init_value = init_value * 2
        else:
            time += 1
            value -= 1


# so time icnrements by 3 to the power of x at each round
# value doubles each round    

    
def strangeCounter(t):
    time = 3 
    value = 3
    if t <= time:
        time_beginning = 1

    while time < t:
        value *= 2
        time += value
        time_beginning = time - value + 1
        
    if time_beginning != t:
        return value - (t - time_beginning)
       
    return value
    





            

if __name__ == '__main__':

    t = int(input().strip())

    result = strangeCounter(t)

    print(result)