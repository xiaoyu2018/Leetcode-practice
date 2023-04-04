
# 组合完全背包
def coinChange(coins: list, amount: int) -> int:
    
    dp=[10e4+1]*(amount+1)
    dp[0]=0

    for c in coins:
        for j in range(c,amount+1):
            dp[j]=min(dp[j],dp[j-c]+1)
        
    return dp[-1] if dp[-1]!=10e4+1 else -1

print(coinChange([2],3))
