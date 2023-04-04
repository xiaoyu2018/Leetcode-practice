


def combine(n: int, k: int) -> list:
    res=[]
    
    def _combine(s:int,n:int,k:int,temp:list):
        if(k<1):
            # print(temp)
            res.append(temp.copy())
            return

        for i in range(s,n-k+2):
            temp.append(i)
            _combine(i+1,n,k-1,temp)
            temp.pop()

    _combine(1,n,k,[])
    return res


print(combine(5,3))
