
public partial class Solution
{
    public int LengthOfLIS(int[] nums)
    {
        int res = 1;
        int size = nums.Length;

        int[] dp = new int[size];
        for (int i = 0; i < size; i++)
            dp[i] = 1;

        for (int i = 1; i < size; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (nums[i] > nums[j])
                    dp[i] = Math.Max(dp[i], dp[j] + 1);
            }

            res = Math.Max(res, dp[i]);
        }

        return res;
    }
}