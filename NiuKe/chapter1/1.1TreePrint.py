#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/9/5'
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class TreePrinter:
    def printTree(self, root):
        if root==None
            return
        last=None
        nlast=None
        res=[]
        temp=[]
        queue=[]
        queue.append(root)
        while queue.__len__()>0:
            curr=queue.pop(0)
            temp.append(curr.val)
            if(curr.left!=None):
                queue.append(curr.left)
                nlast=curr.left
            if(curr.right!=None):
                queue.append(curr.right)
                nlast=curr.right
            if curr==last:
                res.append(temp)
                last=nlast
                temp=[]

        return res
