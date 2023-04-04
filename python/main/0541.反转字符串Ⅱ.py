

def reverseStr(s: str, k: int) -> str:
    res=""
    
    while(True):  
        if(not len(s)):
            break
        
        res+=(s[k-1::-1]+s[k:2*k])
        s=s[2*k:]

    return res

s="0123456789"
# print(s[2::-1])
print(reverseStr(s,2))