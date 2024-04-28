#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    min_loss = 0
    price_dict = dict(enumerate(price, start=1))
    price_dict = {v:k for k,v in price_dict.items()}
    price = sorted(price, reverse=True)

    min_loss = price[0] - price[1]

    for i in range(len(price)-1):
        if price[i] - price[i+1] < min_loss and price_dict[price[i]] < price_dict[price[i+1]]:
            min_loss = price[i] - price[i+1]
    
    return min_loss




if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    print(result)
