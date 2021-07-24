#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 22:52:45 2021

@author: tapli
"""
from multiply import multiply 
def exponent(m,n):
    # base case
    if n==1:
        return m
    # moving toward base case using recursion
    #return m*exponent(m,n-1)
    return multiply(m, exponent(m,n-1))
print(exponent(3,3))