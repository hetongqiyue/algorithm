#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/8/12'
"""
import numpy as np

#给定数组arr=[25,10,5,1],每种面值的货币能使用任意张数，再给定aim代表需要找的钱数，求换钱有多少种方法

#思路：
# 0张25，[10,5,1]组成剩下的1000
# 1张25，[10,5,1]组成剩下的995 ....

def violentSearch(arr,index,aim):
    res=0
    if(index == arr.__len__()):
        #return res=aim==0?1:0
        return  1 if aim==0 else 0
    else:
        count=0
        while arr[index]*count<=aim:
            res+=violentSearch(arr,index+1,aim-arr[index]*count)
            count+=1
        return res

def memorandumSearch(arr,index,aim,map):
    res=0
    if(index==len(arr)):
       return 1 if aim==0 else 1
    else:
        count = 0
        mapValue=0
        while arr[index] * count <= aim:
            mapValue=map[index+1,aim-arr[index]*count]
            if(mapValue!=0):
                res+= 0 if mapValue==-1 else mapValue
            else:
                res += violentSearch(arr, index + 1, aim - arr[index] * count)
            count += 1
        map[index,aim] = -1 if res==0 else res
        return res


if __name__=='__main__':
    arr=[25,10,5,1]
    aim=15
    print(violentSearch(arr,0,aim))
    map=np.zeros((arr.__len__()+1,aim+1))
    print(memorandumSearch(arr,0,aim,map))