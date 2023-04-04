class MinStack:

    def __init__(self):
        
        self.st=[]
        # 辅助栈
        self.as_st= [float('inf')]

    def push(self, x: int) -> None:
        self.st.append(x)
        self.as_st.append(min(self.as_st[-1],x))

    def pop(self) -> None:
        if(len(self.st)):
            self.st.pop()
            self.as_st.pop()

    def top(self) -> int:
        if(len(self.st)):
            return self.st[-1]

    def min(self) -> int:
        if(len(self.st)):
            return self.as_st[-1]


