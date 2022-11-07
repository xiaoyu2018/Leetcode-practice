public partial class Solution
{
    public int LongestCommonSubsequence(string text1, string text2)
    {
        int m = text1.Length;
        int n = text2.Length;

        int[,] dp = new int[m, n];

        for (int i = 0; i < m; i++)
        {
            if(text2[0]==text1[i])
            {
                for (int j = i; j < m; j++)
                {
                    dp[j,0] = 1;
                }
                break;
            }
        }

        for (int i = 0; i < n; i++)
        {
            if (text2[i] == text1[0])
            {
                for (int j = i; j < n; j++)
                {
                    dp[0, j] = 1;
                }
                break;
            }
        }

        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                if(text1[i]==text2[j])
                    dp[i, j] = dp[i - 1, j - 1] + 1;
                else
                    dp[i, j] = Math.Max(dp[i - 1, j], dp[i, j - 1]);
            }
        }

        return dp[m - 1, n - 1];
    }
}