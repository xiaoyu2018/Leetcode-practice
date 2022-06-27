
class CalcFactory:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    
    def get_result():
        pass
    
class Add(CalcFactory):
    def __init__(self, a, b) -> None:
        super().__init__(a, b)
    def get_result(self):
        return self.a+self.b
class Sub(CalcFactory):
    def __init__(self, a, b) -> None:
        super().__init__(a, b)
    def get_result(self):
        return self.a-self.b
class Mul(CalcFactory):
    def __init__(self, a, b) -> None:
        super().__init__(a, b)
    def get_result(self):
        return self.a*self.b
class Div(CalcFactory):
    def __init__(self, a, b) -> None:
        super().__init__(a, b)
    def get_result(self):
        return self.a/self.b


def evalRPN(tokens: list) -> int:
    st=[]
    m={'+':Add,'-':Sub,'*':Mul,'/':Div}
    
    for i in tokens:
        if(i in m.keys()):
            v2=st.pop()
            v1=st.pop()
            f=m[i](int(v1),int(v2))
            st.append(f.get_result())
        else:
            st.append(int(i))
    return st[0]

print(evalRPN( ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))