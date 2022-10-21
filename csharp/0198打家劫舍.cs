
public partial class Solution
{
    public int Rob(int[] nums)
    {
        int size = nums.Length;
        if(size==0)return 0;
        if(size==1)return nums[0];

        int[] dp = new int[size];
        dp[0] = nums[0];
        dp[1] = Math.Max(nums[0], nums[1]);

        for (int i = 2; i < size; i++)
        {
            dp[i] = Math.Max(dp[i - 1], dp[i - 2] + nums[i]);

        }

        return dp[size - 1];
    }
}
