#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/10/23'
"""
import json
import math

class Solution:
    def maximumGap(self, nums:list) -> int:
        # def maxGap(self,nums):
        if nums.__len__() < 2:
            return 0
        minNum = nums[0]
        maxNum = nums[0]
        for num in nums:
            if num < minNum:
                minNum = num
            if num > maxNum:
                maxNum = num

        if maxNum - minNum == 0:
            return 0
        # 分桶
        bucketSize = math.floor((maxNum - minNum) / (nums.__len__() - 1))
        if bucketSize < 1:
            bucketSize = 1
        bucketNums = math.ceil((maxNum + 1 - minNum) / bucketSize)
        buckets = [[] for _ in range(bucketNums)]
        infoBuckets = [[] for _ in range(bucketNums)]
        for num in nums:
            bucketIndex = math.floor((num - minNum) / bucketSize)
            buckets[bucketIndex].append(num)
        for bucketIndex in range(bucketNums):
            if buckets[bucketIndex].__len__() == 0:
                infoBuckets[bucketIndex].append(0)
            else:
                infoBuckets[bucketIndex].append(1)
                infoBuckets[bucketIndex].append(min(buckets[bucketIndex]))
                infoBuckets[bucketIndex].append(max(buckets[bucketIndex]))

        maxGap = 0
        lastMax = None
        currentMin = None
        index = 0
        while index < bucketNums:
            if infoBuckets[index][0] == 0:
                index += 1
                continue
            else:
                # if lastMax!=None and currentMin!=None
                #     maxGap=currentMin-lastMax if  currentMin - lastMax > maxGap else maxGap
                lastMax = infoBuckets[index][2]
                while index < bucketNums - 1:
                    if infoBuckets[index + 1][0] == 0:
                        index += 1
                        continue
                    currentMin = infoBuckets[index + 1][1]
                    maxGap = currentMin - lastMax if currentMin - lastMax > maxGap else maxGap
                    break
                index += 1
        return maxGap


def stringToIntegerList(input):
    return json.loads(input)


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
            nums = stringToIntegerList(line);

            ret = Solution().maximumGap(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()