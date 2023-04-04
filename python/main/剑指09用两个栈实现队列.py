
class CQueue:

    def __init__(self):
        
        self.st1=[]
        self.st2=[]

    def appendTail(self, value: int) -> None:
        self.st1.append(value)

    def deleteHead(self) -> int:
        if(len(self.st2)):
            return self.st2.pop()
        
        while(len(self.st1)):
            self.st2.append(self.st1.pop())
        
        
        return self.st2.pop() if len(self.st2) else -1