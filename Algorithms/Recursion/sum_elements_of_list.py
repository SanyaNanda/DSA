#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 22:32:36 2021

@author: tapli
"""

def sum_list_elements(l):
    # base case
    if len(l)==0:
        return 0
    # moving toward base case using recursion
    return l[0] + sum_list_elements(l[1:])

print(sum_list_elements([1,2,3,4]))