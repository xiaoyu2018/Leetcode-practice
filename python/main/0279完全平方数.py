from math import sqrt

# 组合完全背包
def numSquares(n: int) -> int:
    items=[i*i for i in range(1,int(sqrt(n))+1)]
    
    volume=n+1
    dp=[0 if i==0 else 10e4+1 for i in range(volume)]
    

    for i in items:
        for j in range(i,n+1):
            dp[j]=min(dp[j],dp[j-i]+1)
    
    
    return dp[-1]


print(numSquares(13))