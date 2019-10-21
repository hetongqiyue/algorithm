#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/10/18'
"""


class QuickSort:
    def __init__(self):
        return

    def quick_sort(self, nums):
        self.quick_sort_c(nums, 0, nums.__len__() - 1)
        return nums

    def quick_sort_c(self, nums, p, r):
        if p >= r:
            return

        q = self.partition(nums, p, r)
        self.quick_sort_c(nums, p, q - 1)
        self.quick_sort_c(nums, q + 1, r)


    def partition(self, nums, p, r):
        '''
        此为原地排序算法，空间复杂度为O(1)，若是为了思维简便可申请两个临时数组X,Y，将小于pivot的数组元素拷贝到X,大于pivot的数组元素拷贝到Y
        '''
        pivot = nums[r]
        i = p
        for j in range(p, r):
            if nums[j] < pivot:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i += 1
        temp = nums[i]
        nums[i] = nums[r]
        nums[r] = temp
        return i
