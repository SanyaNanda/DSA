#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:22:43 2021

@author: tapli
"""

class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def traverse(head):
    # base case
    if head is None:
        return
    # moving toward base case via recursive call
    print(head.data)
    traverse(head.next)
    
a = node('a', node('b', node('c')))
traverse(a)