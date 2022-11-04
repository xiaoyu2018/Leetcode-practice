
public partial class Solution
{
    public int FindLengthOfLCIS(int[] nums)
    {
        int size = nums.Length;
        int[] dp = new int[size];

        for (int i = 0; i < size; i++)
        {
            dp[i] = 1;
        }

        for (int i = 1; i < size; i++)
        {
            if(nums[i]>nums[i-1])
                dp[i] += dp[i - 1];
        }

        return dp.Max();
    }
}