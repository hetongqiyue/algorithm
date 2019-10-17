import copy
import logging

logging.basicConfig(level='INFO',datefmt='%m%d%Y %I:%M:%S %p',format='%(levelname)s %(asctime)s %(message)s')
class Elem:
    def __init__(self,rd,pn,pf,q1,q2):
        self.rd=rd
        self.pn=pn
        self.pf=pf
        self.q1=q1
        self.q2=q2

    def __repr__(self):
        return '节点'+', rd :'+self.rd.__str__()+', pn :'+self.pn.__str__()+', pf :'+self.pf.__str__()+', q1 :'+self.q1.__str__()+', q2 :'+self.q2.__str__()+'\r\n'
class Stack:
    def __init__(self):
        self.stack=list()

    def push(self,element):
        return self.stack.append(copy.deepcopy(element))

    def pop(self):
        return self.stack.pop()

    def top(self): #返回栈顶元素
        return copy.deepcopy(self.stack[-1])

    def __repr__(self):
        return 'stack:\r\n'+self.stack.__repr__()

S=Stack()

def norec_exmp(n, f):
    u1=0
    u2=0
    global S

    x = Elem(0, 0, 0, 0, 0)
    x.rd = 3  # exmp内一共调用了两次递归函数，t=2,td=t+1=3,压到栈底座监视哨
    x.pn = n
    S.push(x)
    logging.info('state:{0}'.format(S.__repr__()));

    while True:

        x=S.top()
        while x.pn>=2:
            x.rd=1
            x.pn=(int)(x.pn/2)
            S.push(x)
            logging.info('state:{0}'.format(S.__repr__()));

        x=S.top()
        S.pop()
        x.pf=x.pn+1
        S.push(x)
        logging.info('state:{0}'.format(S.__repr__()));

        x=S.top()
        while x.rd==2:
            tmp=S.top()
            S.pop()
            x=S.top()
            S.pop()
            x.q2=tmp.pf
            x.pf=x.q1*x.q2
            S.push(x)
            logging.info('state:{0}'.format(S.__repr__()));

        x=S.top()
        if x.rd==1:
            tmp = S.top();
            S.pop();
            x = S.top();
            S.pop();
            x.q1 = tmp.pf;
            S.push(x);
            tmp.rd = 2;
            tmp.pn = (int)(x.pn / 4);
            S.push(tmp);
            logging.info('state:{0}'.format(S.__repr__()));

        x=S.top()
        if x.rd==3:
            break

    x=S.top()
    S.pop()
    f=x.pf

    return f


if __name__ == '__main__':
    print(norec_exmp(4,0))