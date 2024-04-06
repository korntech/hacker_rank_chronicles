#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    # Write your code here
    for index, order in enumerate(orders, start=1):
        order.append(sum(order))
        order.append(index)
    sorted_orders = sorted(orders, key=lambda x: (x[2], x[3]))
    
    return [x[-1] for x in sorted_orders]

if __name__ == '__main__':

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    print(result)