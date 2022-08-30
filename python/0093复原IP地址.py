

def restoreIpAddresses(s: str) -> list:
    res=[]
    temp=[]

    def _isValid(s:str):
        if(any([s[0]=='0' and len(s)>1,int(s)>255])):
            return False
        return True

    def _backTracking(start:int):
        nonlocal s
        
        if(len(temp)==4 and sum([len(i) for i in temp])==len(s)):
            res.append(temp.copy())
            return

        for i in range(start,len(s)):
            frame=s[start:i+1]
            if(_isValid(frame)):
                temp.append(frame)
                _backTracking(i+1)
                temp.pop()

    _backTracking(0)
    return [".".join(i) for i in res]
    

print(restoreIpAddresses("25525511135"))