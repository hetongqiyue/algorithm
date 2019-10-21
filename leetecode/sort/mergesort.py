#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/10/18'
"""
import copy
class MergeSort:
    def __init__(self):
        return
    def merge_sort(self,nums):
        merge_sort = self.merge_sort_c(nums, 0, nums.__len__() - 1)
        return nums

    def merge_sort_c(self, nums, p, r):
        if p >= r:
            return

        q = (p + r) // 2
        self.merge_sort_c(nums, p, q)
        self.merge_sort_c(nums, q + 1, r)
        self.merge(nums, p, r, q)

    def merge(self, nums, p, r, q):
        temp = copy.deepcopy(nums[p:r + 1])
        i = p
        j = q + 1
        k = 0
        while i <= q and j <= r:
            if nums[i] < nums[j]:
                temp[k] = nums[i]
                i += 1
                k += 1
            else:
                temp[k] = nums[j]
                j += 1
                k += 1

        start = i
        end = q
        if j <= r:
            start = j
            end = r
        while start <= end:
            temp[k] = nums[start]
            k += 1
            start += 1

        for i in range(0, r + 1 - p):
            nums[p + i] = temp[i]


    def merge_with_guard(self,dataArray,startIndex,endIndex,delimiterIndex):
        '''
            利用哨兵的归并函数
            例如 data_list[p:q] = [...,1,4,2,3,...]
            part_left = [1,4]
            part_right = [2,3]
            归并后 data_list[p:q] = [...,1,2,3,4,...]
        '''
        part_left=[dataArray[index] for index in range(startIndex,delimiterIndex+1)]
        part_right=copy.deepcopy(dataArray[delimiterIndex+1:endIndex+1])

        import sys
        maxValue=sys.maxsize
        part_left.append(maxValue)
        part_right.append(maxValue)
        i=0;j=0;k=0
        while i!=delimiterIndex+1-startIndex:
            if part_left[i]<=part_right[j]:
                dataArray[k]=part_left[i]
                i+=1
            else:
                dataArray[k]=part_right[j]
                j+=1
            k+=1

