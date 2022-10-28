
public partial class Solution
{
    //贪心
    public int MaxProfit1(int[] prices)
    {
        int res = 0;

        for (int i = 1; i < prices.Length; i++)
        {
            res += Math.Max(0, prices[i] - prices[i-1]);
        }
        return res;
    }

    //dp
    public int MaxProfit2(int[] prices)
    {
        int[] dp = new int[2];
        dp[0] = -prices[0];

        for (int i = 1; i < prices.Length; i++)
        {
            dp[0] = dp[0]>dp[1] - prices[i]?dp[0]:dp[1] - prices[i];
            dp[1] = dp[1] > dp[0] + prices[i] ? dp[1] : dp[0] + prices[i];
        }
        return dp[1];
    }
}