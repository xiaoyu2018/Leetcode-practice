

def Partition(s: str) -> list:
    res=[]
    temp=[]

    def _isPalindrome(left:int,right:int):
        nonlocal s
        
        while(left<right):
            if(s[left]!=s[right]):
                return False
            left+=1
            right-=1
        
        return True

    def _backTracking(start:int):
        nonlocal s
        
        if(start>=len(s)):
            res.append(temp.copy())
            return
        
        for i in range(start,len(s)):
            if(_isPalindrome(start,i)):
                temp.append(s[start:i+1])
                _backTracking(i+1)
                temp.pop()
            
    _backTracking(0)
    return res


print(Partition("aab"))
# print("aab"[0:0])