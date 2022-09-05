
def permuteUnique(nums: list) -> list:
    res=[]
    temp=[]
    d_used=[0]*8

    def _backTracking():
        nonlocal nums

        b_used=[0]*21

        if(len(nums)==len(temp)):
            res.append(temp.copy())
            return
        
        for i,v in enumerate(nums):

            if(d_used[i] or b_used[v+10]):
                continue
            
            d_used[i]=~d_used[i]
            b_used[v+10]=~b_used[v+10]
            temp.append(v)
            _backTracking()
            d_used[i]=~d_used[i]
            temp.pop()

    _backTracking()
    return res