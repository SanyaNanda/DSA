#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 22:42:22 2021

@author: tapli
"""

def gcd(a,b):
    # base case
    if a%b==0:
        return b
    # moving toward base case using recursion
    return gcd(b,a%b)
print(gcd(32,12))