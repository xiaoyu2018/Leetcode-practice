
def permute(nums:list) -> list:
    res=[]
    temp=[]

    def _backTracking():
        nonlocal nums

        if(len(temp)==len(nums)):
            res.append(temp.copy())
            return
            
        for i in nums:
            if(i not in temp):
                temp.append(i)
                _backTracking()
                temp.pop()
    
    _backTracking()
    return res


print(permute([1,2,3]))