#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/8/12'
"""

import logging
import sys
sys.setrecursionlimit(10000000)
logging.basicConfig(level='INFO',datefmt='%m%d%Y %I:%M:%S %p',format='%(levelname)s %(asctime)s %(message)s')
maxWeight=0
import numpy as np



def violentSearchForLIS(arr):
    maxCnt=0
    length=len(arr)
    for i in range(0,length):
        cnt=1
        p=i
        for j in range(i+1,length):
            if arr[p]<arr[j]:
                cnt+=1
                p=j
        maxCnt=max(cnt,maxCnt)
    return maxCnt

def backstrackingLIS(seq,cnt,items):
    global maxCnt,solution
    length = len(items)

    if seq == length:
        if cnt>maxCnt:
            maxCnt=cnt
            logging.info("解决方案为：{}".format(solution))
        return maxCnt
    else:
        # 遍历选择 放入和不放入，不放入限定条件条件为seq+1<n,放入条件则还包括重量小于阈值
        #不放入
        backstrackingLIS(seq + 1, cnt,items)
        #放入
        if(solution.__len__()==0 or solution[solution.__len__()-1]<items[seq]):
            solution.append(items[seq])
            backstrackingLIS(seq+1,cnt+1,items)
            solution.pop()
    return maxCnt

if __name__=='__main__':
    maxCnt=0
    arr=[2,4,3,7,8,1,2,3,4,5,6,4,5]
    print(violentSearchForLIS(arr))
    solution = []
    print(backstrackingLIS(0,0,arr))