#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 19:44:57 2021

@author: tapli
"""

import turtle

max_length = 300
increment = 10

def spiral(turtle1, line_length):
    # Base case
    if line_length > max_length:
        return
    # Moving toward it
    turtle1.forward(line_length)
    turtle1.right(90)
    # function calling itself recursively
    spiral(turtle1, line_length+increment) 
    
T = turtle.Turtle(shape="turtle")
T.pensize(5)
T.color("purple")
spiral(T, 10)
T.done()