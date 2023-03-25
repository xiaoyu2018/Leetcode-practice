
def evalRPN(tokens: list) -> int:
    def _add(a,b):
        return a+b
    def _sub(a,b):
        return a-b
    def _mul(a,b):
        return a*b
    

    memo={
        "+":_add,
        "-":_sub,
        "*":_mul,
        "/":lambda x,y:int(x/y) #注意运算符“//”是地板除，负数和题目要求向0截断不符
        }

    st=[]

    for c in tokens:
        if(c in memo.keys()):
            a=st.pop()
            b=st.pop()
            st.append(memo[c](int(b),int(a)))
        else:
            st.append(c)

    return int(st[0])

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
