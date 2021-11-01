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

# Memoization
def fib(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n<2:
        return n
    result = fib(n-1, cache) + fib(n-2, cache)
    cache[n] = result
    return result
print(fib(600))