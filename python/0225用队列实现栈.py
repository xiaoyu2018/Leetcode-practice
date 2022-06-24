from collections import deque

class MyStack:

    def __init__(self):
        self.q1=deque()
        self.q2=deque()

    def push(self, x: int) -> None:
        if(self.q1):
            self.q1.append(x)
        else:
            self.q2.append(x)

    def pop(self) -> int:
        l1=len(self.q1)
        l2=len(self.q2)

        res=None
        if(l1):
            while(l1>1):
                self.q2.append(self.q1.popleft())
                l1-=1
            res=self.q1.pop()
                
        elif(l2):
            while(l2>1):
                self.q1.append(self.q2.popleft())
                l2-=1
            res=self.q2.pop()
                

        return res

    def top(self) -> int:

        res=self.pop()
        self.push(res)
        return res

    def empty(self) -> bool:
        return not (self.q1 or self.q2)


mys=MyStack()
mys.push(1)
mys.push(2)
print(mys.top())

print(mys.empty())