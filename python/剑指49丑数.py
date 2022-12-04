
# dp，后面的丑数等于前面的丑数*(2/3/5)，递增排序
# dp[i]为第i个丑数
def nthUglyNumber(n: int) -> int:

    dp=[1]*(n+1)
    p2=p3=p5=1
    for i in range(2,n+1):
        num1,num2,num3=dp[p2]*2,dp[p3]*3,dp[p5]*5
        
        dp[i]=min(num1,num2,num3)

        if(dp[i]==num1):
            p2+=1
        if(dp[i]==num2):
            p3+=1
        if(dp[i]==num3):
            p5+=1
    
    return dp[-1]

print(nthUglyNumber(10))