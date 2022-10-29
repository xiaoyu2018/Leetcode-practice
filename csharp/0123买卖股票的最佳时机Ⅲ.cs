public partial class Solution
{
// 0 第一次买入
// 1 第一次卖出
// 2 第二次买入
// 3 第二次卖出
    public int MaxProfit5(int[] prices)
    {
        int[] dp = new int[4];
        dp[0] = dp[2] = -prices[0];

        for (int i = 0; i < prices.Length; i++)
        {
            dp[0] = Math.Max(dp[0], -prices[i]);
            dp[1] = Math.Max(dp[1], dp[0]+prices[i]);
            dp[2] = Math.Max(dp[2], dp[1]-prices[i]);
            dp[3] = Math.Max(dp[3], dp[2]+prices[i]);
        }

        return dp[3];
    }
}