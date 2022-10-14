public partial class Solution
{
    public int NumSquares(int n)
    {
        int item_size = (int)Math.Sqrt(n);
        int[] items = new int[item_size];
        int[] dp = new int[n + 1];

        for (int i = 0; i < item_size; i++)
        {
            items[i] = (i + 1) * (i + 1);
        }

        for (int i = 1; i <= n; i++)
        {
            dp[i] = int.MaxValue;
        }

        foreach(int i in items)
        {
            for (int j=i;j<=n ;j++)
            {
                dp[j] = Math.Min(dp[j], dp[j - i] + 1);
            }
        }

        return dp[n];
    }
}