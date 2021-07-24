#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 22:22:35 2021

@author: tapli
"""

def fibonacci(n):
    # base case
    if n<2:
        return n
    # moving toward base case using recursion
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))