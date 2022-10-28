
public partial class Solution
{
    public int MaxProfit3(int[] prices)
    {
        int min = Int32.MaxValue;

        int res = 0;
        for (int i = 0; i < prices.Length; i++)
        {
            min = Math.Min(prices[i], min);
            res = Math.Max(prices[i] - min, res);
        }
        return res;
    }

    public int MaxProfit4(int[] prices)
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