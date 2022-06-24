
class MyQueue:

    def __init__(self):
        self.st1=list()
        self.st2=list()

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        if(not len(self.st2)):
            l=len(self.st1)
            while(l>0):
                self.st2.append(self.st1.pop())
                l-=1

        return self.st2.pop()
    def peek(self) -> int:
        if(len(self.st2)):
            return self.st2[-1]
        return self.st1[0]

    def empty(self) -> bool:
        return  not(self.st1 or self.st2)
    

def Test():
    q=MyQueue()
    assert q.empty()==True

    q.push(1)
    assert q.empty()==False
    assert q.peek()==1
    q.push(2)
    assert q.peek()==1
    assert q.pop()==1
    q.push(3)
    assert q.pop()==2

Test()