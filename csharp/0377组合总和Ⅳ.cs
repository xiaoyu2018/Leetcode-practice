
public partial class Solution
{
    public int CombinationSum4(int[] nums, int target)
    {
        int[] dp = new int[target + 1];

        dp[0] = 1;

        // 先遍历背包容量
        for (int i = 0; i < target+1; i++)
        {
            foreach(int n in nums)
            {
                if(i>=n)
                    dp[i] += dp[i - n];
            }
        }
        return dp[target];
    }
    
}