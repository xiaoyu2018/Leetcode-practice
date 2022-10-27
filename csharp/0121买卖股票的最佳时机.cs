
public partial class Solution
{
    public int MaxProfit(int[] prices)
    {
        int[] dp = new int[2];
        int size = prices.Length;

        (dp[0], dp[1]) = (-prices[0], 0);

        for (int i = 0; i < size; i++)
        {
            dp[0] = Math.Max(dp[0], -prices[i]);
            dp[1] = Math.Max(dp[1], dp[0]+prices[i]);
        }

        return dp[1];
    }
}