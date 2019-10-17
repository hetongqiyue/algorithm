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
def backtrackingForDiagonalMatrix(row,col,dist,matrix,finalDistDiagonalSeq):
    global minDist
    if(row==finalDistDiagonalSeq and col == finalDistDiagonalSeq):#走到最后一步了
        if(dist < minDist ):
            minDist=dist
            logging.info('以当前方式到达目的地的最小距离为{}'.format(minDist))
        return
    if (row<finalDistDiagonalSeq): #行数小于目标对角点的序号，还可以往下走
        backtrackingForDiagonalMatrix(row+1,col,dist+matrix[row,col],matrix,finalDistDiagonalSeq)
    if(col<finalDistDiagonalSeq):   #列数小于目标对角点的序号，还可以往右走
        backtrackingForDiagonalMatrix(row,col+1,dist+matrix[row,col],matrix,finalDistDiagonalSeq)


def backtrackingForDiagonalMatrix1(row,col,dist,matrix,finalDistDiagonalSeq):
    global minDist
    if(row==finalDistDiagonalSeq and col == finalDistDiagonalSeq):#走到最后一步了
        if(dist < minDist ):
            minDist=dist
            logging.info('以当前方式到达目的地的最小距离为{}'.format(minDist))
        return
    if (row<finalDistDiagonalSeq): #行数小于目标对角点的序号，还可以往下走
        backtrackingForDiagonalMatrix(row+1,col,dist+matrix[row,col],matrix,finalDistDiagonalSeq)
    if(col<finalDistDiagonalSeq):   #列数小于目标对角点的序号，还可以往右走
        backtrackingForDiagonalMatrix(row,col+1,dist+matrix[row,col],matrix,finalDistDiagonalSeq)


def backtrackingForDiagonalMatrixRegularization(row,col,matrix,finalDistDiagonalSeq): ##从格子(0,0)走到对角线(n,n)
    global minDist,solution,result,distance
    if(row==finalDistDiagonalSeq and col == finalDistDiagonalSeq):#走到最后一步了
        if(distance < minDist ):
            minDist=distance
            logging.info('以当前方式到达目的地的最小距离为{}'.format(minDist))
            logging.info('路线：{}'.format(solution))
            logging.info('路线组成：{}'.format(result))
        return

    #枚举所有可能的路径
    if (row<finalDistDiagonalSeq): #行数小于目标对角点的序号，还可以往下走--满足衔接函数和约束条件
        solution.append('down')
        result.append(matrix[row+1,col])
        distance=distance+matrix[row+1,col]
        backtrackingForDiagonalMatrixRegularization(row+1,col,matrix,finalDistDiagonalSeq)##从格子(row+1,0)走到对角线(n,n)
        #  solution.pop()
        result.pop()
        distance=distance-matrix[row+1,col]

    if(col<finalDistDiagonalSeq):   #列数小于目标对角点的序号，还可以往右走
        solution.append('right')
        result.append(matrix[row, col+1])
        distance = distance + matrix[row, col+1]
        backtrackingForDiagonalMatrixRegularization(row,col+1,matrix,finalDistDiagonalSeq)
        solution.pop()
        result.pop()
        distance = distance - matrix[row, col+1]



#回溯法，是自顶向下分解
def backtrackingAndMemorandumForDiagonalMatrixRegularization(row,col,currentDistance,matrix,finalDistDiagonalSeq): ##从格子(0,0)走到对角线(n,n)
    global minDist,solution,result,distance
    if(row==finalDistDiagonalSeq and col == finalDistDiagonalSeq):#走到最后一步了
        if(distance < minDist ):
            minDist=distance
            logging.info('以当前方式到达目的地的最小距离为{}'.format(minDist))
            logging.info('路线：{}'.format(solution))
            logging.info('路线组成：{}'.format(result))
        return

    if (matrixMemorandum[row,col]!=0):
        if(matrixMemorandum[row,col]<currentDistance): #表示状态(row,col,currentDistance)这种状态不如(row,col,matrixMemorandum[row,col])，且由(row,col,matrixMemorandum[row,col])，这种状态走到末端的方法已经计算过，不许再计算
            logging.info('到达格子({0},{1})的路线已经记录过，同时现在到达此格子的路径大小{3}不如曾经记录过的路径大小{2}'.format(row,col,matrixMemorandum[row,col],currentDistance))
            return
    matrixMemorandum[row,col]=currentDistance
    logging.info('记录到达格子({0},{1})的路线的路径大小{2}'.format(row, col, matrixMemorandum[row, col],
                                                                                 currentDistance))
    #枚举所有可能的路径
    if (row<finalDistDiagonalSeq): #行数小于目标对角点的序号，还可以往下走--满足衔接函数和约束条件
        solution.append('down')
        result.append(matrix[row+1,col])
        distance=distance+matrix[row+1,col]
        backtrackingAndMemorandumForDiagonalMatrixRegularization(row+1,col,currentDistance+matrix[row+1,col],matrix,finalDistDiagonalSeq)##从格子(row+1,0)走到对角线(n,n)
        #  solution.pop()
        result.pop()
        distance=distance-matrix[row+1,col]

    if(col<finalDistDiagonalSeq):   #列数小于目标对角点的序号，还可以往右走
        solution.append('right')
        result.append(matrix[row, col+1])
        distance = distance + matrix[row, col+1]
        backtrackingAndMemorandumForDiagonalMatrixRegularization(row,col+1,currentDistance+matrix[row,col+1],matrix,finalDistDiagonalSeq)
        solution.pop()
        result.pop()
        distance = distance - matrix[row, col+1]

#动态规划是自底向上分解
def dpForDiagonalMatrixRegularization(row,col):
    if(row==0 and col ==0):
        return matrix[0,0]
    if memorandumForDpDiagonalMatrix[row,col] >0:
        return memorandumForDpDiagonalMatrix[row,col]
    minLeft=sys.maxsize
    minUp=sys.maxsize
    if(col-1>=0):
        minLeft=dpForDiagonalMatrixRegularization(row,col-1)
    if(row-1>=0):
        minUp=dpForDiagonalMatrixRegularization(row-1,col)
    currMinDist=matrix[row,col]+min(minLeft,minUp)
    memorandumForDpDiagonalMatrix[row,col]=currMinDist
    return currMinDist

def dpOfStateTable(matrix,row,col):
    map=np.ones((row,col))
    map=map*sys.maxsize
    map[0,0]=matrix[0,0]
    for i in range(0,row):
        for j in range(0,col):
            if i<row-1:
                map[i+1,j]=min(map[i+1,j],map[i,j]+matrix[i+1,j])
            if j<col-1:
                map[i,j+1]=min(map[i,j+1],map[i,j]+matrix[i,j+1])
    return map[row-1,col-1]




if __name__=='__main__':
    #backtrackingForBag(seq=0,currentWeight=0,items=[1,2,3,4,5],thresholdCount=5)
    # backtrackingForBagRegularise(seq=0,items=[1, 2, 3, 4, 5], thresholdCount=5)
    solution = []
    result = []
    distance = 1
    minDist = sys.maxsize
    matrix=np.array([[1,3,5,9],
                     [2,1,3,4],
                     [5,2,6,7],
                     [6,8,4,3]
                     ])

    matrixMemorandum = np.zeros(matrix.shape)
    backtrackingAndMemorandumForDiagonalMatrixRegularization(0,0,1,matrix,3)
    # backtrackingForDiagonalMatrixRegularization(0,0,matrix,3)
    matrix = np.array([[1, 3, 5, 9],
                       [2, 1, 3, 4],
                       [5, 2, 6, 7],
                       [6, 8, 4, 3]])
    memorandumForDpDiagonalMatrix = np.zeros(matrix.shape)
    currDist=dpForDiagonalMatrixRegularization(3,3)
    print(currDist)
    print(memorandumForDpDiagonalMatrix)

    print(dpOfStateTable(matrix,matrix.shape[0],matrix.shape[1]))