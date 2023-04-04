
def lengthOfLongestSubstring(s: str) -> int:
    
    size=len(s)
    if(size==0):
        return 0
    res=1
    dp=1
    start=0

    for i in range(1,size):
        flag=False
        for j in range(i-1,start-1,-1):
            if(s[j]==s[i]):
                start=j+1
                dp=i-j
                flag=True
        
        if(not flag):
            dp+=1
        res=max(res,dp)
    return res

print(lengthOfLongestSubstring(""))
