public partial class Solution
{
    public int Fib(int n)
    {
        if(n<2)
            return n;
        int[] dp = new int[n + 1];

        (dp[0], dp[1]) = (0, 1);
        for (int i = 2; i < n+1; i++)
        {
            dp[i] = (dp[i - 1] + dp[i - 2])%(int)(1e9+7);
        }

        return dp[dp.Length - 1];
    }
}