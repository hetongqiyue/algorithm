#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/9/6'
"""


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A.__len__()!=B.__len__():
            return False
        # doubleA = A.join(A)
        doubleA=A+A
        if doubleA.find(B)!=-1:
            return True
        return False


def stringToString(input):
    return input[1:-1]


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
            A = stringToString(line);
            line = next(lines)
            B = stringToString(line);

            ret = Solution().rotateString(A, B)

            out = (ret);
            print(out)
        except StopIteration:
            break

def reverseStr(str):
    reverseResult=''
    for index in range(str.__len__()-1,-1,-1):
        reverseResult+=str[index]
    return reverseResult

def reverseStrSpaceExhaust(str):
    str=list(str)
    for index in range(0,str.__len__()//2):
        tempAlpha= str[index]
        str[index]=str[str.__len__()-1-index]
        str[str.__len__()-1-index]=tempAlpha
    return ''.join(str)


def reverseStrWithRightWorld():
    strForReverse=input()
    # strForReverse=list(strForReverse)
    # resultOfStep1=''
    # for index in range(strForReverse.__len__()-1,-1,-1):
    #     resultOfStep1+=strForReverse[index]
    resultOfStep1=reverseStrSpaceExhaust(strForReverse)
    resultOfStep2=resultOfStep1.split(" ")
    # for indexOfWord in range(0,resultOfStep1.__len__()):
    resultOfStep3=''
    for word in  resultOfStep2:
        # for indexOfAlphabet in range(word.__len__()-1,-1,-1):
        #     resultOfStep3+=word[indexOfAlphabet]
        resultOfStep3+=reverseStrSpaceExhaust(word)
        resultOfStep3+=' '
    print(resultOfStep3)


def biggestStr(A, B):
    return A+B if A+B<B+A else B+A


def biggestStrMain():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            A = stringToString(line);
            line = next(lines)
            B = stringToString(line);

            ret =biggestStr(A, B)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    #main()
    #reverseStrWithRightWorld()
    biggestStrMain()