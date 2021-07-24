#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 22:49:31 2021

@author: tapli
"""

def multiply(n,a):
    # base case
    if n==1:
        return a
    # moving toward base case using recursion
    return a + multiply(n-1,a)

#print(multiply(5,-4))
#print(multiply(2,3))