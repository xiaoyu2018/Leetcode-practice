


def combinationSum2(candidates: list, target: int) -> list:
    res=[]
    temp=[]
    
    def _backtraking(start:int,s=int,candidates=candidates,target=target):
        used=set()

        if(s>target):
            return
        if(s==target):
            res.append(temp.copy())
            return
        
        for i in range(start,len(candidates)):
            val=candidates[i]
            if(val in used):
                continue
            temp.append(val)
            used.add(val)
            _backtraking(i+1,s+val)
            temp.pop()

    candidates.sort()
    _backtraking(0,0)
    return res

print(combinationSum2([10,1,2,7,6,1,5],8))
