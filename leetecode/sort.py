#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/10/16'
"""

import json
import copy


class Solution:
    def sortArray(self, nums):
        # bubbling sort ,time complexity : O(n*n)
        # for i in range(0,len(nums)-1):
        #     flag=False
        #     for j in range(i+1,len(nums)):
        #         if nums[i]>nums[j]:
        #             temp=nums[j]
        #             nums[j]=nums[i]
        #             nums[i]=temp
        #             flag=True
        #     if flag==False:
        #         break
        # return nums

        # select sort
        # for i in range(0, len(nums) - 1):
        #     min = nums[i]
        #     minIndex = i
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] < min:
        #             min = nums[j]
        #             minIndex = j
        #     if minIndex == i:
        #         break
        #     temp = nums[minIndex]
        #     nums[minIndex] = nums[i]
        #     nums[i] = temp
        # return nums

        # insert sort
        # for i in range(1,nums.__len__()):
        #     value=nums[i]
        #     breakFlag=False
        #     for j in range(i-1,-1,-1):
        #         if value<nums[j]:
        #             nums[j+1]=nums[j]
        #         else:
        #             breakFlag=True
        #             break
        #     if breakFlag==True:
        #         nums[j+1]=value
        #     else:
        #         nums[j]=value
        # return nums

        # merge sort
        # merge_sort = self.merge_sort_c(nums, 0, nums.__len__() - 1)
        # return nums

        #quick sort
        self.quick_sort_c(nums,0,nums.__len__()-1)
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

    def quick_sort_c(self, nums, p, r):
        if p>=r:
            return

        q=self.partition(nums,p,r)
        self.quick_sort_c(nums,p,q-1)
        self.quick_sort_c(nums,q,r)

    def partition(self, nums, p, r):
        pivot=nums[r]
        i=p
        for j in range(p,r):
            if nums[j]<pivot:
                temp=nums[j]
                nums[j]=nums[i]
                nums[i]=temp
                i+=1
        temp = nums[i]
        nums[i] = nums[r]
        nums[r] = temp
        return i


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
