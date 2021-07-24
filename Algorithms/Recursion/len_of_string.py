#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 22:59:40 2021

@author: tapli
"""

def len_string(s):
    # base case
    if s[0]==s:
        return 1
    # moving toward base case using recursion
    return 1 + len_string(s[1:])
print(len_string('hello'))