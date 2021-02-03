#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(d):
    maxval = None
    for j in range(4):
        for i in range(4):
            add = d[j][i]+d[j][i+1]+d[j][i+2]+d[j+1][i+1]+d[j+2][i]+d[j+2][i+1]+d[j+2][i+2]
            if(maxval ==None):
                maxval=add
            elif(add>maxval):
                maxval=add
    return maxval
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d = []

    for _ in range(6):
        d.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(d)

    fptr.write(str(result) + '\n')

    fptr.close()