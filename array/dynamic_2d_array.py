!/bin/python3

import math 
import os 
import random 
import re 
import sys

#Complete the 'dynamicArray' function below.

#The function is expected to return an INTEGER_ARRAY. The function accepts following parameters:1. INTEGER n 2. 2D_INTEGER_ARRAY queries

#

def dynamicArray(n, queries):
	 # Write your code here 
	 l = [] lastAnswer=0 
	 x = [[],[]] 
	 for i in range(len(queries)): 
		if(queries[i][0]==1): 
			lastAnswer=0 
			x[(queries[i][1]^lastAnswer)%n].append(queries[i][2]) 
		elif(queries[i][0]==2): 
			idx = (queries[i][1]^lastAnswer)%n #print(idx) 
			#print(len(x[idx])) 
			lastAnswer=x[idx][queries[i][2]%len(x[idx])] 
			l.append(lastAnswer) 
	return l

if name == 'main': 
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	first_multiple_input = input().rstrip().split()

	n = int(first_multiple_input[0])

	q = int(first_multiple_input[1])

	queries = []

	for _ in range(q):
	    queries.append(list(map(int, input().rstrip().split())))

	result = dynamicArray(n, queries)


	fptr.write('\n'.join(map(str, result)))
	fptr.write('\n')

	fptr.close()

