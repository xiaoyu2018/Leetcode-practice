s="aaaaaa"
t="aaaaaa"

# 递归
def isSubsequence1(s:str,t:str):
    if(not s):
        return True
    
    if(not t):
        return False

    idx=t.find(s[0])

    if(idx==-1):
        return False
    
    return isSubsequence1(s[1:],t[idx+1:])

# 迭代
def isSubsequence2(s:str,t:str):
    temp=-1
    size=len(t)
    for i in s:
        temp=t.find(i,temp+1,size)
        if(temp==-1):
            return False
    
    return True
        
        

print(isSubsequence2(s,t))