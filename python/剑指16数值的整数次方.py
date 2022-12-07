
# 暴力 超时
def myPow(x: float, n: int) -> float:
    
    if(n==0):
        return 1
    res=1
    for _ in range(abs(n)):
        res*=x

    return res if n>0 else 1/res

# 快速幂，分治
def myPow1(x: float, n: int) -> float:
    
    def _fast_mu(x:float,n:int):

        if(n==0):
            return 1
        
        y=_fast_mu(x,n//2)
        return y*y if (not n%2) else y*y*x
    
    res=_fast_mu(x,abs(n))
    return res if n>0 else 1/res

print(myPow1(2,214748364))
# 0.00001
# 2147483647