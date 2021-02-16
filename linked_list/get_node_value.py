#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    if(head.next==None):
        return head.data
    c=0
    temp = SinglyLinkedList();
    dum = SinglyLinkedList();
    temp=head
    dum=head
    while(temp!=None):
        temp=temp.next
        c+=1
    x=c-positionFromTail
    for i in range(1,x):
        dum=dum.next
    return dum.data

if __name__ == '__main__':
