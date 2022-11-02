public partial class Solution
{
    public int MaxProfit(int[] prices, int fee)
    {
        int[] dp = new int[2] { -prices[0], 0 };
        int size = prices.Length;

        for (int i = 1; i<size;i++)
        {
            dp[0] = Math.Max(dp[0], dp[1] - prices[i]);
            dp[1] = Math.Max(dp[1], dp[0] + prices[i] - fee);
        }

            return dp[1];
    }
}