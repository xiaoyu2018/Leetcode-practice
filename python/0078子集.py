

def subsets(nums:list)->list:
    res=[]
    temp=[]
    def _backTracking(start:int,nums:list):

        for i in range(start,len(nums)):
            temp.append(nums[i])
            res.append(temp.copy())
            _backTracking(i + 1, nums)
            temp.pop()
        

    res.append(temp)
    _backTracking(0, nums)
    
    return res
