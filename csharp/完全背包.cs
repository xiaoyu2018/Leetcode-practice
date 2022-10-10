public partial class Solution
{
    public int CompletePack(int[] weights, int[] values)
    {
        int n = 4 + 1;
        int m = values.Length;

        int[] dp = new int[n];

        for (int i = 0; i < n; i++)
        {
            dp[i] = 0;
        }

        for (int i = 0; i < m; i++)
        {
            for (int j = weights[i]; j < n; j++)
            {
                dp[j] = Math.Max(dp[j], dp[j - weights[i]] + values[i]);
            }
        }

        return dp[n - 1];
    }
}