public partial class Solution
{
    public int CoinChange(int[] coins, int amount)
    {
        int[] dp = new int[amount + 1];

        for (int i = 1; i<=amount;i++)
        {
            dp[i] = (int)(10e4 + 1);
        }

        foreach(int c in coins)
        {
            for (int j = c; j<=amount;j++)
            {
                dp[j] = Math.Min(dp[j], dp[j - c] + 1);
            }
        }

        return dp[amount] == (int)(10e4 + 1) ? -1 : dp[amount];
    }
}