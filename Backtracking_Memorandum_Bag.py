#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/7/30'
"""


import logging
import sys
sys.setrecursionlimit(10000000)
logging.basicConfig(level='INFO',datefmt='%m%d%Y %I:%M:%S %p',format='%(levelname)s %(asctime)s %(message)s')
maxWeight=0
import numpy as np

memorandum=np.zeros((5,11))
thresholdWeight=10
currentWeight=0
solution=[]
def backtrackingForBag(seq, items=[1,2,3,4,5],thresholdCount=5 ):
    global maxWeight,currentWeight # maxWeight有赋值语句maxWeight=currentWeight，因此必须声明为全局变量，thresholdWeight没有赋值语句，因此不用声明为全局变量
    if(currentWeight==thresholdWeight or seq==thresholdCount):
        if(currentWeight>maxWeight):
            maxWeight=currentWeight
            logging.info("the current max weights is : {0} ".format(maxWeight))
            logging.info("the current bag is :{0}".format(seq))
            #logging.info("memorandum record seq :{0},currentWeight: {1}".format(seq, currentWeight))
        return
    #判断第seq号，重量为currentWeight是否有记录
    if(memorandum[seq,currentWeight]==True):
        logging.info("状态已经记录，当前背包重量为{1},决策第{0}个是否装入背包memorandum has recorded seq :{0},currentWeight: {1}".format(seq, currentWeight))
        return
    memorandum[seq,currentWeight]=True
    logging.info("正在记录状态，当前背包重量为{1},决策第{0}个是否装入背包, memorandum record seq :{0},currentWeight: {1}".format(seq, currentWeight))

    backtrackingForBag(seq+1,items)
    if(currentWeight+items[seq]<=thresholdWeight):
        backtrackingForBag(seq+1,currentWeight+items[seq])

def backtrackingForBagRegularise(seq,items=[1,2,3,4,5],thresholdCount=5 ):
    global maxWeight,currentWeight # maxWeight有赋值语句maxWeight=currentWeight，因此必须声明为全局变量，thresholdWeight没有赋值语句，因此不用声明为全局变量
    if(currentWeight==thresholdWeight or seq==thresholdCount):
        if(currentWeight>maxWeight):
            maxWeight=currentWeight
            logging.info("the current max weights is : {0} ".format(maxWeight))
            logging.info("the current bag is :{0}".format(seq))
            #logging.info("memorandum record seq :{0},currentWeight: {1}".format(seq, currentWeight))
            logging.info("解决方案为：{}".format(solution))
        return
    #判断第seq号，重量为currentWeight是否有记录 此处备忘录的作用是不管以何种方式到达(seq,currentWeight)的状态，由这个中间状态最终得到的最大背包的结果已经计算过，被确定了，并肯定会曾经被赋值给maxWeight，不用再计算了
    #可画下图，==》末端状态，不放入备忘录，备忘录只放中间状态，
    # 状态，当前背包重量为{1}, 决策第{0}个是否装入背包 ===》中间状态==对应的方法 为从此中间状态到最后的目的地的方法 而不是当前背包重量为{1}, 将第{0}个装入或不装入背包的方法

    if(memorandum[seq,currentWeight]==True):
        logging.info("初始或中间状态已经记录，当前背包重量为{1},决策第{0}个是否装入背包memorandum has recorded seq :{0},currentWeight: {1}".format(seq, currentWeight))
        return
    memorandum[seq,currentWeight]=True
    logging.info("初始或中间正在记录状态，当前背包重量为{1},决策第{0}个是否装入背包, memorandum record seq :{0},currentWeight: {1}".format(seq, currentWeight))

    #遍历选择 放入和不放入，不放入限定条件条件为seq+1<n,放入条件则还包括重量小于阈值
    backtrackingForBagRegularise(seq+1,items)
    if(currentWeight+items[seq]<=thresholdWeight):
        currentWeight+=items[seq]
        solution.append(items[seq])
        backtrackingForBagRegularise(seq+1,items)
        currentWeight-=items[seq]
        solution.pop()


def HayForSale(maxVolumn,nums,list):
    memorandum=np.zero(maxVolumn)
    suffixSum=np.zeros(nums)
    for i in range(nums,0):
        suffixSum[i]=list[i]+suffixSum[i+1]

    for i in range(0,nums):
        toUpdate=max(list[i],maxVolumn-suffixSum[i])
        for v in range(maxVolumn,toUpdate-1):
            memorandum[v]=max(memorandum[v],memorandum[v-list[i]]+list[i])
            if memorandum[v]==maxVolumn:
                print(v)
                return
        print(memorandum[maxVolumn])

def HayForSale():
    input0=input()
    input02List=input0.split(' ')
    maxVolumn=int( input02List[0])
    nums=int(input02List[1])
    temp=0
    count =0
    list=[]
    while (count<nums):
        list.append(int(input()))
        count+=1
    memorandum=np.zeros(maxVolumn+1)
    suffixSum=np.zeros(nums+2)

    for i in range(nums-1,-1,-1):
        suffixSum[i]=list[i]+suffixSum[i+1]

    for i in range(0,nums):
        if(maxVolumn-suffixSum[i]>0):
            toUpdate=max(list[i],maxVolumn-suffixSum[i])
        else:
            toUpdate=list[i]
        for v in range(maxVolumn,int(toUpdate-1),-1):
            memorandum[v]=max(memorandum[v],memorandum[v-list[i]]+list[i])
            if memorandum[v]==maxVolumn:
                print(maxVolumn)
                return
    print(memorandum[maxVolumn])


if __name__=='__main__':
    #backtrackingForBag(seq=0,currentWeight=0,items=[1,2,3,4,5],thresholdCount=5)
    # backtrackingForBagRegularise(seq=0,items=[1, 2, 3, 4, 5], thresholdCount=5)
    matrix=np.array([[1,3,5,9],
                     [2,1,3,4],
                     [5,2,6,7],
                     [6,8,4,3]
                     ])
    #backtrackingForDiagonalMatrix(0,0,1,matrix,3)
    #backtrackingForDiagonalMatrixRegularization(0,0,1,matrix,3)
    # currDist=dpForDiagonalMatrixRegularization(3,3)
    # print(currDist)
    # print(memorandumForDpDiagonalMatrix)

    # finalNeedMoney=11
    # change=(1,6,5,9)
    # memorandumForChange = np.zeros(finalNeedMoney)
    # solution=[]
    # changeCount=dpForChange(11,*change)
    # print(changeCount)
    # print(solution)

    # coins = [1,3,5]
    # finalNeedMoney = 9
    # m = len(coins)
    # V = 11
    # coins = [9, 6, 5, 1]
    # m = len(coins)
    # V = 11
    # print("Minimum coins required is ",
    #       minCoins(coins, m, V))

    # minCount=sys.maxsize
    # res=backtrackingForChange(0,0,*coins)

    HayForSale()