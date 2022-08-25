
d2l_map=[
    "",
    "",
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz",]



def letterCombinations(digits: str) -> list:
    res=[]
    if(not len(digits)):
        return res
        
    def _back_tracking(temp:str,digits:str,s=0):
        if(s==len(digits)):
            res.append(temp)
            return
        
        for ch in d2l_map[int(digits[s])]:
            _back_tracking(temp+ch,digits,s+1)
            
    _back_tracking("",digits,0)
    return res

print(letterCombinations("23"))