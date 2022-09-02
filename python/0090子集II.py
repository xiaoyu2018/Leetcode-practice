


def subsetsWithDup (nums: list) -> list:
    res=[]
    temp=[]
    
    def _backTracking(start:int):
        nonlocal nums
        memo=set()
        for i,v in enumerate(nums[start:],start):
            if(v not in memo):
                temp.append(v)
                memo.add(v)
                res.append(temp.copy())
                _backTracking(i+1)
                temp.pop()
    
    # 去重要先排序，要把重复元素聚在一起
    nums.sort()
    res.append(temp.copy())
    _backTracking(0)
    return res    


print(subsetsWithDup([4,4,4,1,4]))