#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/8/13'
"""

import logging
import sys
sys.setrecursionlimit(10000000)
logging.basicConfig(level='INFO',datefmt='%m%d%Y %I:%M:%S %p',format='%(levelname)s %(asctime)s %(message)s')


def findLCS( A, n, B, m):
    # write code here
    import numpy as np
    redundancyTable = np.zeros((n + 1, m + 1))
    mnTable=np.zeros((n,m))
    ret=0
    for i in range(0, n):
        for j in range(0, m):
            if (A[i] != B[j]):
                mnTable[i, j]=redundancyTable[i+1, j + 1] = max(redundancyTable[i, j + 1], redundancyTable[i + 1, j])

            if (A[i] == B[j]):
                mnTable[i, j]=redundancyTable[i + 1, j + 1] = max(redundancyTable[i+1,j+1],redundancyTable[i, j] + 1)
            if (redundancyTable[i + 1, j + 1] > ret):
                ret = redundancyTable[i + 1, j + 1]
    return ret,mnTable



if __name__=='__main__':
    print(findLCS("1A2C3D4B56",10,"B1D23CA45B6A",12)[0])
    print(findLCS("1A2C3D4B56",10,"B1D23CA45B6A",12)[1])