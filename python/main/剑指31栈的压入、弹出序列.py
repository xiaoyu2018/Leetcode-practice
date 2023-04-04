from collections import deque

# 栈模拟
def validateStackSequences(pushed: list, popped:list) -> bool:
    st=[]
    dq=deque(pushed)

    for v in popped:
        while(v not in st):
            st.append(dq.popleft())

        top=st.pop()
        if(top!=v):
            return False
    
    return True

print(validateStackSequences([1,2,3,4,5],[4,5,3,2,1]))