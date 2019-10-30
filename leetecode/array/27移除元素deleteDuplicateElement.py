#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/10/29'
"""

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if nums.__len__() <1:
            return 0
        noDuplicateIndex=0
        current=nums[0]
        duplicateIndex=0
        for duplicateIndex in range(1,nums.__len__()):
            if nums[duplicateIndex] == current:
                continue
            else :
                current=nums[duplicateIndex]
                noDuplicateIndex+=1
                nums[noDuplicateIndex]=current
        i = 0
        while i < nums.__len__() - 1 - noDuplicateIndex:
            nums.pop()
            i += 1
        return noDuplicateIndex+1








