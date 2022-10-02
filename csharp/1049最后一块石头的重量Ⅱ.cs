
public partial class Solution
{
    // 分成尽量相同重量的两堆，即接近1/2总重量的最大重量
    //转化为01背包
    public int LastStoneWeightII(int[] stones)
    {
        int total = stones.Sum();
        int m = stones.Length;
        int n = total / 2+1;
        int[,] dp = new int[m, n];

        for (int i = 0; i<m;i++)
            dp[i, 0] = 0;
        for (int i = 0; i<n;i++)
            dp[0, i] = i >= stones[0] ? stones[0] : 0;
        
        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                if(stones[i]>j)
                    dp[i,j] = dp[i - 1, j];
                else
                    dp[i, j] = Math.Max(dp[i - 1, j], dp[i - 1, j - stones[i]] + stones[i]);
            }
        }

        return total - 2 * dp[m-1, n -1];

    }
}