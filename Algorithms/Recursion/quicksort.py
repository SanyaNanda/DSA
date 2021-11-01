#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 19:59:07 2021

@author: tapli
"""

def quicksort(array):
    # base case
    if len(array)<=1:
        return array
    # moving toward base case 
    pivot = array[len(array)//2]
    smaller = [ x for x in array if x < pivot]
    equal = [ x for x in array if x == pivot]
    greater = [ x for x in array if x > pivot]
    # recursive call
    return quicksort(smaller) + equal + quicksort(greater)
    
print(quicksort([5,2,6,1]))