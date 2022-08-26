
def combinationSum(candidates: list, target: int) -> list:
    res=[]
    temp=[]
    def _backtrakcing(candidates:list,target:int,s=0,st=0):

        if(s>target):
            return
        if(s==target):
            res.append(temp.copy())
            return
        

        for i in range(st,len(candidates)):
            temp.append(candidates[i])
            _backtrakcing(candidates,target,s+candidates[i],i)
            temp.pop()

    
    _backtrakcing(candidates,target)
    return res



print(combinationSum([2,3,6,7],7))