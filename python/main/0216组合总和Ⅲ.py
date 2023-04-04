

def combinationSum3(k: int, n: int) -> list:
    res=[]
    ss=0
    end=min(10,n)
    
    def _back_tracking(s:int,k:int,n:int,temp:list):
        nonlocal ss
        if(ss>n):
            return
        if(k<1):
            if(ss==n):
                res.append(temp.copy())
            return


        for i in range(s,end-k+1):
            ss+=i
            temp.append(i)
            _back_tracking(i+1,k-1,n,temp)
            temp.pop()
            ss-=i

    _back_tracking(1,k,n,[])

    return res

print(combinationSum3(3,7))