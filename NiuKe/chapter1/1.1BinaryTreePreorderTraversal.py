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

class Solution:
    def __init__(self):
        self.list =[]
    #前序遍历+recursive
    # def preorderTraversal(self, root):
    #     if root == None:
    #         return []
    #     return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    #preorderTraversal+iterative  递归转迭代，+的运算顺序为从右往左，所以转换后顺序为：右，左，中
    def preorderTraversal(self, root):
        if root == None:
            return
        cur=root
        stack=[root]
        res=[]
        # while stack!=None:
        while stack:
            cur=stack.pop()
            res.append(cur.val)
            if cur.right!=None:
                stack.append(cur.right)
            if cur.left!=None:
                stack.append(cur.left)

        return res

    #递归法
    # def postorderTraversal(self, root):
    #     if root ==None:
    #         return
    #     return [self.postorderTraversal(root.left)]+[self.postorderTraversal(root.right)]+[root]

    #迭代法iterative
    def postorderTraversal(self, root):
        if root ==None:
            return
        #return [self.postorderTraversal(root.left)]+[self.postorderTraversal(root.right)]+[root]
        # tempNodeLeftSubNode
        # tempNodeRightSubNode
        list=[]
        stack=[root]
        while stack:
            currNode=stack.pop()
            if currNode.right:
                stack.append(currNode.right)
            if currNode.left:
                stack.append(currNode.left)
            list.append(currNode.val)
        return list