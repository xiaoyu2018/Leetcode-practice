
def findSubsequences(nums: list) -> list:
    res=[]
    temp=[]
    
    def _backTracking(start:int=0):
        nonlocal nums
        memo=[0]*201

        if(len(temp)>1):
            res.append(temp.copy())

        for i,v in enumerate(nums[start:],start):

            if(memo[v+100] or (len(temp) and temp[-1]>v)):
                continue
            
            temp.append(v)
            memo[v+100]=1
            _backTracking(i+1)
            temp.pop()
    
    _backTracking()
    return res