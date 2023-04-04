
# 0 第一次买入
# 1 第一次卖出
# 2 第二次买入
# 3 第二次卖出
def maxProfit(k: int, prices: list) -> int:

    dp=[0 if i%2 else -prices[0] for i in range(2*k)]

    for price in prices[1:]:
        dp[0]=max(dp[0],-price)
        for i in range(1,2*k):
            if(i%2):
                dp[i]=max(dp[i],dp[i-1]+price)
            else:
                dp[i]=max(dp[i],dp[i-1]-price)
    
    return dp[-1]