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

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    if (head==None):
        return
    temp = head
    if(position == 0):
        head = temp.next
        temp = None
        return head
    for i in range(position -1 ):
        temp = temp.next
        if temp is None:
            break
    if temp is None: 
        return 
    if temp.next is None: 
        return
    next = temp.next.next
    temp.next = None
    temp.next = next
    return head
if __name__ == '__main__':