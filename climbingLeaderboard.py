#!/bin/python3

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true


import bisect
import math
import os
import random
import re
import sys


def climbingLeaderboard(ranked, player):
    # Write your code here
    set_diff = set(player) - set(ranked)
    
    merged = set(ranked) | set(player)

    merged = {v:k for k, v in dict(enumerate(sorted(merged, reverse=True), start=1)).items()}

    results = [] 

    for index, p in enumerate(player, start=1):
        if p in set_diff:
            set_diff.remove(p)

        results.append(merged[p]-len(set_diff))
    
    
    return results


   


if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(result)
