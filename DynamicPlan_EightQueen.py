#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/7/26'
"""

def calcQueen(size):
    board=[-1]*size
    return queens(board,0,size)

def queens(board,current,size):
    if(current ==size):
        print(board)
        return True
    else:
        rowsCounts=size
        for i in range(rowsCounts):#这里表示每1列都有size == rows种方法，可改为rows
            board[current]=i #当前列的棋子所放在的行
            if (noConflicts(board ,current)):
                done =queens(board,current +1,size)
                if(done):
                    return True
        return False

import math
def noConflicts(board,current):
    for i in range(current):
        if (board[i]==board[current]):
            return False
        if ((current-i) == abs(board[current]-board[i])):
            return False
    return True

if __name__=='__main__':
    calcQueen(4)