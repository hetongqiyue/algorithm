#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/10/29'
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dictNums=dict()

        for index in range(0,nums.__len__()):
            complement=target-nums[index]
            if(dictNums.get(complement)!=None):
                return [index,dictNums.get(complement)]
            dictNums[nums[index]]=index
