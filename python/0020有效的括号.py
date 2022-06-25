s="}"

# 栈
def isValid(s: str) -> bool:
    m={'(':')','[':']','{':'}'}

    st=[]

    for c in s:
        if(c in m.keys()):
            st.append(c)
        elif(not st or m[st.pop()]!=c):
            return False
        
    return True if not st else False
            



print(isValid(s))