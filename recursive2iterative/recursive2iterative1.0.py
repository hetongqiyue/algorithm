#!/usr/bin/env python3
"""
__title__ = ''
__author__ = 'P52'
__mtime__ = '2019/9/20'
"""

def exmpIni(n):
    if n<2:
        return n+1
    else:
        return exmpIni(n / 2) * exmpIni(n / 4)

def exmp(n, f):
    u1=0
    u2=0
    if(n<2):
        f=n+1
    else:
        u1=exmp(n/2,u1)
        u2=exmp(n/4,u2)
        f=u1*u2
    return f

class Elem:
    def __init__(self,rd,pn,pf,q1,q2):
        self.rd=rd
        self.pn=pn
        self.pf=pf
        self.q1=q1
        self.q2=q2

class Stack:
    def __init__(self):
        self.stack=list()

    def push(self,element):
        return self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def top(self): #返回栈顶元素
        return self.stack[-1]

S=Stack()

def norec_repalce1(n,f):

    global S

    x =Elem(0,0,0,0,0)
    x.rd=3 #exmp内一共调用了两次递归函数，t=2,td=t+1=3,压到栈底座监视哨
    x.pn=n
    S.push(x)

    #label 0  整个非递归的总入口， 实际上也可以看做在递归函数里面，我们的的第一个语句应该做什么处理
    if S.top().pn<2: #处理递归出口，所有递归出口处需要增加语句 goto lable t+1
        S.pop()
        x.pf=x.pn+1
        S.push(x)
        goto label3  #因为递归出口语句执行完后需要处理函数返回，而label t+1d是用来可处理函数返回需要做的工作的，所以需要goto label3


def norec_exmp(n, f):
    u1=0
    u2=0
    global S

    x = Elem(0, 0, 0, 0, 0)
    x.rd = 3  # exmp内一共调用了两次递归函数，t=2,td=t+1=3,压到栈底座监视哨
    x.pn = n
    S.push(x)

    # label 0
    # if(n<2):
    #     f=n+1
    x=S.top()
    if S.top().pn<2:
        S.pop()
        x.pf=x.pn+1
        S.push(x)
        goto label3

    else:

        #u1=exmp(n/2,u1)
        #开始改写第一个递归函数
        x.rd=1
        x.pn=(int)(x.pn/2)
        S.push(x)
        goto label0
        # label 1 #第i个递归子函数执行结束返回时需要执行的操作，通常是弹出当前函数的堆栈信息，并把计算结果回传给调用者
        tmp=S.top()
        S.pop()
        x=S.pop()
        x.q1=tmp.pf
        S.push(x)

        #u2=exmp(n/4,u2)
        x.rd=2
        x.pn=(int)(x.pn/4)
        S.push(x)
        goto lable0
        # label 2
        tmp = S.top()
        S.pop()
        x = S.pop()
        x.q1 = tmp.pf
        x.pf=x.q1*x.q2
        S.push(x)
        #f=u1*u2

    #label t+1
    if(S.top().rd==1):
        goto label1
    elif(S.top().rd==2):
        goto label2
    elif(S.top().rd==3):
        tmp=S.top()
        f=tmp.pf

    return f



if __name__ == '__main__':
    print(exmpIni(4))
    print(exmp(4,0))

