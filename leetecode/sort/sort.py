#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/10/16'
"""

import json
import copy

from mergesort import MergeSort
from quicksort import QuickSort


class Solution:
    def sortArray(self, nums):
        # bubbling sort ,time complexity : O(n*n)
        # return self.bubble_sort(nums)
        #
        # # select sort
        # return self.select_sort()
        #
        # # insert sort
        # return self.insert_sort(nums)

        # merge sort
        # merge_sort=MergeSort()
        # return merge_sort.merge_sort(nums)

        #quick sort
        # quick_sort=QuickSort()
        # return quick_sort.quick_sort(nums)

        #heap sort
        return self.heap_sort(nums)

    def heap_sort(self,lists):
        size = len(lists)
        self.build_heap(lists, size)
        for i in range(0, size)[::-1]:
            lists[0], lists[i] = lists[i], lists[0]
            self.adjust_heap(lists, 0, i)
        return lists

    #build heap
    def build_heap(self,list,size):
        for i in range(0,size>>1)[::-1]:
            self.adjust_heap(list,i,size)

    def adjust_heap(self, nums, i, size):
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        max = i
        if i < size / 2:
            if lchild < size and nums[lchild] > nums[max]:
                max = lchild
            if rchild < size and nums[rchild] > nums[max]:
                max = rchild
            if max != i:
                nums[max], nums[i] = nums[i], nums[max]
                self.adjust_heap(nums, max, size)



    def select_sort(self,nums):
        for i in range(0, len(nums) - 1):
            min = nums[i]
            minIndex = i
            for j in range(i + 1, len(nums)):
                if nums[j] < min:
                    min = nums[j]
                    minIndex = j
            if minIndex == i:
                continue
            temp = nums[minIndex]
            nums[minIndex] = nums[i]
            nums[i] = temp
        return nums

    def bubble_sort(self, nums):
        for i in range(0, len(nums) - 1):
            flag = False
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                    flag = True
            if flag == False:
                break
        return nums


    def insert_sort(self, nums):
        for i in range(1, nums.__len__()):
            value = nums[i]
            breakFlag = False
            for j in range(i - 1, -1, -1):
                '''
                nums[j]>value时才移动数据，保证了后面出现的元素不会插入到前面出现过的相同元素的后面
                '''
                if  nums[j]>value :
                    nums[j + 1] = nums[j]
                else:
                    breakFlag = True
                    break
            if breakFlag == True:
                nums[j + 1] = value
            else:
                nums[j] = value
        return nums




def stringToIntegerList(input):
    return json.loads(input)


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

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)
            ret = Solution().sortArray(nums)
            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
