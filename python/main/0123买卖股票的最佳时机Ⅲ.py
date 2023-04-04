# 每天可能的 状态 有五种,是说在第i天处于该状态，不是第i天才进行的操作
# 0 无买入
# 1 第一次买入
# 2 第一次卖出
# 3 第二次买入
# 4 第二次卖出
# 5 dp[i][j]中 i表示第i天，j为 [0 - 4] 五个状态
# dp[i][j]表示第i天状态j所剩最大现金

def maxProfit(prices: list) -> int:
    size=len(prices)

    dp=[[0]*5 for _ in range(size)]

    dp[0][1]=dp[0][3]=-prices[0]
    
    for i in range(1,size):
        dp[i][0]=dp[i-1][0]
        dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
        dp[i][2]=max(dp[i-1][2],dp[i-1][1]+prices[i])
        dp[i][3]=max(dp[i-1][3],dp[i-1][2]-prices[i])
        dp[i][4]=max(dp[i-1][4],dp[i-1][3]+prices[i])
    # print(dp)
    return dp[-1][-1]

print(maxProfit([3,4]))
