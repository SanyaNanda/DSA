#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:22:17 2021

@author: tapli
"""

class root:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inorder(root, path=''):
    if root:
        path = inorder(root.left, path)
        path += str(root.data)
        path = inorder(root.right,path)
    return path
    
def preorder(root, path=''):
    # base case
    if root.left==None and root.right==None:
        return
    # moving toward base case via recursive calls
    path += str(root.data)
    path = inorder(root.left, path)
    path = inorder(root.right,path)
    return path

def postorder(root, path=''):
    if root.left==None and root.right==None:
        return
    path += str(root.data)
    path = inorder(root.left, path)
    path = inorder(root.right,path)
    return path

a = root('a')
b = root('b')
c = root('c')
a.left=b
a.right=c

print('inorder: ', end=' ')
print(inorder(a), end='\n')
print('preorder: ', end=' ')
print(preorder(a), end='\n')
print('postorder: ', end=' ')
print(postorder(a), end='\n')
    