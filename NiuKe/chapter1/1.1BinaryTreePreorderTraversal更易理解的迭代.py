#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/9/6'
"""


# Definition for a binary tree node.
import json


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #         if root ==None:
    #             return []
    #         return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]

    #     def postorderTraversal(self, root: TreeNode) -> List[int]:
    #         if root ==None:
    #             return
    #         #return [self.postorderTraversal(root.left)]+[self.postorderTraversal(root.right)]+[root]
    #         # tempNodeLeftSubNode
    #         # tempNodeRightSubNode
    #         list=[]
    #         stack=[root]
    #         while stack:
    #             currNode=stack.pop()
    #             list.insert(0,currNode.val)
    #             if currNode.left:
    #                 stack.append(currNode.left)
    #             if currNode.right:
    #                 stack.append(currNode.right)

    #         return list

    def postorderTraversal(self, root: TreeNode):
        if root == None:
            return
        # return [self.postorderTraversal(root.left)]+[self.postorderTraversal(root.right)]+[root]
        # tempNodeLeftSubNode
        # tempNodeRightSubNode
        list = []
        stack = [root]
        pre = None
        while stack:
            currNode = stack[-1]
            if (currNode.left == None and currNode.right == None) or (pre!=None and (pre == currNode.left or pre == currNode.right)):
                list.append(currNode.val)
                pre = currNode
                stack.pop()
            else:
                if currNode.right:
                    stack.append(currNode.right)
                if currNode.left:
                    stack.append(currNode.left)

        return list


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    root = stringToTreeNode("[1,null,2,3]");

    ret = Solution().postorderTraversal(root)

    out = integerListToString(ret);
    print(out)

    # lines = readlines()
    # while True:
    #     try:
    #         line = next(lines)
    #         root = stringToTreeNode(line);
    #
    #         ret = Solution().postorderTraversal(root)
    #
    #         out = integerListToString(ret);
    #         print(out)
    #     except StopIteration:
    #         break


if __name__ == '__main__':
    main()