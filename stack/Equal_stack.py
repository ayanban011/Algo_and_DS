#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    a = sum(h1)
    b = sum(h2)
    c = sum(h3)
    print(a,b,c)
    tp1, tp2, tp3 = 0, 0, 0
    ans = 0
    while (1):
        # If any stack is empty
        if (tp1 == len(h1) or tp2 == len(h2) or tp3 == len(h3)):
            return 0
        # If sum of all three stack are equal
        if (a == b and b == c):
            return a
        # Finding the stack with maximum sum and
        # removing its top element
        if (a >= b and a >= c):
            a -= h1[tp1]
            tp1=tp1+1
        
        elif (b >= a and b >= c):
            b -= h2[tp2]
            tp2=tp2+1
        elif (c >= b and c >= a):
            c -= h3[tp3]
            tp3=tp3+1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
