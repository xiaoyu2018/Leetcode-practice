public partial class Solution
{
    public int MinDistance(string word1, string word2)
    {
        int m = word1.Length + 1;
        int n = word2.Length + 1;

        int[,] dp = new int[m, n];

        for (int i = 1; i < m; i++)
        {
            dp[i, 0] = i;
        }
        for (int i = 1; i < n; i++)
        {
            dp[0, i] = i;
        }

        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                if(word1[i-1]==word2[j-1])
                    dp[i, j] = dp[i - 1, j - 1];
                else
                    dp[i, j] = Math.Min(dp[i - 1, j] + 1, Math.Min(dp[i, j - 1] + 1, dp[i - 1, j - 1] + 2));
            }
        }

        return dp[m - 1,n - 1];
    }
}