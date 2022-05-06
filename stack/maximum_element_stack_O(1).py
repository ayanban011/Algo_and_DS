#!/bin/python3

import math
import os
import random
import re
import sys
# Class to make a Node
class Node:
    #Constructor which assign argument to node's value
    def __init__(self, value):
        self.value = value
        self.next = None

    # This method returns the string representation of the object.
    def __str__(self):
        return "Node({})".format(self.value)
    
    # __repr__ is same as __str__
    __repr__ = __str__


class Stack:
    # Stack Constructor initialise top of stack and counter.
    def __init__(self):
        self.top = None
        self.count = 0
        self.maximum = None
        
    #This method returns the string representation of the object (stack).
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top {} \n\nStack :\n{}'.format(self.top,out))
        
    # __repr__ is same as __str__
    __repr__=__str__
    
    #This method is used to get minimum element of stack
    def getMax(self):
        if self.top is None:
            return "Stack is empty"
        else:
            return self.maximum


    # Method to check if Stack is Empty or not
    def isEmpty(self):
        # If top equals to None then stack is empty
        if self.top == None:
            return True
        else:
        # If top not equal to None then stack is empty
            return False

    # This method returns length of stack    
    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count+=1
        return self.count

    # This method returns top of stack    
    def peek(self):
        if self.top is None:
            print ("Stack is empty")
        else:
            if self.top.value > self.maximum:
                print("Top Most Element is: {}" .format(self.maximum))
            else:
                print("Top Most Element is: {}" .format(self.top.value))

    #This method is used to add node to stack
    def push(self,value):
        if self.top is None:
            self.top = Node(value)
            self.maximum = value
            
        elif value > self.maximum :
            temp = (2 * value) - self.maximum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.maximum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}" .format(value))

    #This method is used to pop top of stack
    def pop(self):
        if self.top is None:
            print( "Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode > self.maximum:
                print ("Top Most Element Removed :{} " .format(self.maximum))
                self.maximum = ( ( 2 * self.maximum ) - removedNode )
            else:
                print ("Top Most Element Removed : {}" .format(removedNode))
#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    stack = Stack()
    m=[]
    for i in range(len(operations)):
        if(len(operations[i])==1):
            if(int(operations[i])==2):
                stack.pop()
            else:
                r = stack.getMax()
                m.append(r)
        else:
            a =operations[i]
            v = int(a[2:])
            stack.push(v)
            #print(stack)
    return m
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
