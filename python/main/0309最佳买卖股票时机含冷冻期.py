# 0 买入股票状态（今天买入股票或之前就买入了股票并一直没有后续操作）
# 1 自由卖出状态（前两天就卖出了股票，度过了冷冻期且一直没有后续操作）
# 2 当天卖出状态（今天刚刚卖出股票）
# 3 冷冻状态（处于冷冻期）

# 用二维数组，一维数组会出现数据覆盖的情况
def maxProfit(prices: list) -> int:
    n = len(prices)

    dp = [[0] * 4 for _ in range(n)]
    dp[0][0] = -prices[0]
    for i in range(1, n):
        dp[i][0] = max(
            dp[i - 1][0], dp[i - 1][3] - prices[i], dp[i - 1][1] - prices[i]
        )  # 前一天是状态0 or 1 or 2,才有进入状态0的可能
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])  # 自由卖出状态只可能由状态1 or 3达到
        dp[i][2] = dp[i - 1][0] + prices[i]  # 当天卖出状态只可能由状态0达到
        dp[i][3] = dp[i - 1][2]  # 冷冻状态只可能由状态2达到
    return max(dp[-1][3], dp[-1][1], dp[-1][2])


print(maxProfit([2, 1, 4, 5, 2, 9, 7]))

