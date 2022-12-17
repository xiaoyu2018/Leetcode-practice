
public partial class Solution
{
    // dp
    // dp[i]表示长度为i的绳子最大拆分积
    public int CuttingRope(int n)
    {
        int[] dp = new int[n + 1];

        (dp[0], dp[1]) = (0, 1);

        for (int i = 2; i<n+1;i++)
        {
            int crt = 0;
            for (int j=1;j<i ;j++)
            {
                crt = Math.Max(crt, Math.Max(j * (i - j), j * dp[i - j]));
            }
            dp[i] = crt;
        }
        return dp[n];
    }
}