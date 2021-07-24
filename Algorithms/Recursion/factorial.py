#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 20:08:59 2021

@author: tapli
"""

def factorial(n):
    # base case
    if n<=1:
        return 1
    # move toward it using recursion
    return n*factorial(n-1)
print(factorial(5))