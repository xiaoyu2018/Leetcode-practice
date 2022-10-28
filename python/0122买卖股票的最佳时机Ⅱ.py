
# 贪心
def maxProfit(prices: list) -> int:
    res=0
    prev=prices[0]
    for i in prices[1:]:
        res=res+i-prev if i>prev else res
        prev=i

    return res 


# dp，dp[0]:持有股票最大现金；dp[1]:不持有股票最大现金；
def maxProfit2(prices: list) -> int:
    dp=[0]*2
    # 第0天持股
    dp[0]=-prices[0]
    # 第0天不持股，现金为0

    for i in range(1,len(prices)):
        # 不买入第i天股票即现今与i-1天相同，买入前先卖出持股（肯定在最大利润卖出），所以现金为dp[1]-prices[i]
        dp[0]=max(dp[0],dp[1]-prices[i])
        # 不卖出持股即现今与i-1天相同，若卖出则计算利润为当前现金
        dp[1]=max(dp[1],dp[0]+prices[i])
    
    return dp[1]

print(maxProfit2([7,6,4,3,1]))