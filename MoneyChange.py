#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/8/12'
"""
import sys
import numpy as np
import logging
logging.basicConfig(level='INFO',datefmt='%m%d%Y %I:%M:%S %p',format='%(levelname)s %(asctime)s %(message)s')
#minDist=1

def dpForChange1(needMoney, *change):
    if needMoney == 5:
        solution.append(5)
        return 1
    if needMoney == 3:
        solution.append(3)
        return 1
    if needMoney == 1:
        solution.append(1)
        return 1

    minSubstract5 = sys.maxsize
    minSubstract3 = sys.maxsize
    minSubstract1 = sys.maxsize

    if needMoney > 5:
        minSubstract5 = dpForChange(needMoney - 5, *change)
    # solution.pop()
    if needMoney > 3:
        minSubstract3 = dpForChange(needMoney - 3, *change)
    # solution.pop()
    if needMoney > 1:
        minSubstract1 = dpForChange(needMoney - 1, *change)
    # solution.pop()

    currentCount = min(minSubstract1, minSubstract3, minSubstract5) + 1
    if (min(minSubstract1, minSubstract3, minSubstract5) == minSubstract5):
        solution.append(5)
    if (min(minSubstract1, minSubstract3, minSubstract5) == minSubstract3):
        solution.append(3)
    if (min(minSubstract1, minSubstract3, minSubstract5) == minSubstract1):
        solution.append(1)

    return currentCount

    # A Dynamic Programming based Python3 program to
    # find minimum of coins to make a given change V

    # m is size of coins array (number of
    # different coins)


def dpForChange(needMoney):
    if needMoney == 5:
        solution.append(5)
        return 1
    if needMoney == 3:
        solution.append(3)
        return 1
    if needMoney == 1:
        solution.append(1)
        return 1

    minSubstract5 = sys.maxsize
    minSubstract3 = sys.maxsize
    minSubstract1 = sys.maxsize
    minCount = sys.maxsize
    if needMoney > 5:
        minSubstract5 = dpForChange(needMoney - 5)
        minSubstract3 = dpForChange(needMoney - 3)
        minSubstract1 = dpForChange(needMoney - 1)
        currentCount = min(minSubstract5, minSubstract3, minSubstract1) + 1
        if (currentCount < minCount):
            minCount = currentCount
    # solution.pop()
    if needMoney > 3:
        minSubstract3 = dpForChange(needMoney - 3)
        minSubstract1 = dpForChange(needMoney - 1)
        currentCount = min(minSubstract3, minSubstract1) + 1
        if (currentCount < minCount):
            minCount = currentCount
    # solution.pop()
    if needMoney > 1:
        currentCount = dpForChange(needMoney - 1) + 1
        if (currentCount < minCount):
            minCount = currentCount
    # solution.pop()

    return minCount

    # A Dynamic Programming based Python3 program to
    # find minimum of coins to make a given change V

    # m is size of coins array (number of
    # different coins)


# m is size of coins array (number of different coins)
def minCoins(coins, m, V):
    # base case
    if (V == 0):
        return 0

    # Initialize result
    res = sys.maxsize

    # Try every coin that has smaller value than V
    for i in range(0, m):
        if (coins[i] <= V):
            sub_res = minCoins(coins, m, V - coins[i])

            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if (sub_res + 1 < res):
                res = sub_res + 1

    return res


# def minCoins(coins, m, V):
#
#     # table[i] will be storing the minimum
#     # number of coins required for i value.
#     # So table[V] will have result
#     table = [0 for i in range(V + 1)]
#
#     # Base case (If given value V is 0)
#     table[0] = 0
#
#     # Initialize all table values as Infinite
#     for i in range(1, V + 1):
#         table[i] = sys.maxsize
#
#     # Compute minimum coins required
#     # for all values from 1 to V
#     for i in range(1, V + 1):
#
#         # Go through all coins smaller than i
#         for j in range(m):
#             if (coins[j] <= i):
#                 sub_res = table[i - coins[j]]
#                 if (sub_res != sys.maxsize and
#                         sub_res + 1 < table[i]):
#                     table[i] = sub_res + 1
#     return table[V]
#
#     # Driver Code

# if __name__ == "__main__":
#     coins = [9, 6, 5, 1]
#     m = len(coins)
#     V = 11
#     print("Minimum coins required is ",
#           minCoins(coins, m, V))

# This code is contributed by ita_c



def backtrackingForChange(currentNeedMoney, currentCount, *changes):

    # 终止条件
    global minCount, finalNeedMoney, solution
    if currentNeedMoney == finalNeedMoney:
        if (currentCount < minCount):
            minCount = currentCount
            logging.info('找零{0}的最小个数为{1}'.format(currentNeedMoney, minCount))
            logging.info('路线：{}'.format(solution))
        return

    if (changeMemorandum[currentNeedMoney] != 0):
        if (changeMemorandum[currentNeedMoney] < currentCount):
            logging.info("找零{0}的路线已经记录过，同时现在到达找零状态的找零硬币个数{1}不如曾经记录过的{2}".format(currentNeedMoney, currentCount,
                                                                                changeMemorandum[currentNeedMoney]))
            return

    changeMemorandum[currentNeedMoney] = currentCount
    logging.info('记录到达找零{0}的零钱个数{1}'.format(currentNeedMoney, currentCount))

    # 枚举所有可能的路径
    for change in changes:
        if (currentNeedMoney + change <= finalNeedMoney):
            solution.append(change)
            currentCount += 1
            backtrackingForChange(currentNeedMoney + change, currentCount, *changes)
            currentCount -= 1
            solution.pop()

    return minCount


if __name__ == '__main__':

    finalNeedMoney = 6
    solution = []
    memorandumForChange = np.zeros(finalNeedMoney)
    changeCount = dpForChange1(finalNeedMoney )
    print(changeCount)
    print(solution)

    # coins = [1,3,5]
    # m = len(coins)
    # V = 11
    # coins = [9, 6, 5, 1]
    # m = len(coins)
    # V = 11
    # solution = []
    # res=minCoins(coins,m,V)
    # print('找零{0}的最小硬币个数为{1}'.format(V, res))

    # finalNeedMoney = 11
    # changeMemorandum = np.zeros(finalNeedMoney+1)
    # minCount=sys.maxsize
    # res=backtrackingForChange(0,0,*coins)
    # print('找零{0}的最小硬币个数为{1}'.format(finalNeedMoney,res))
