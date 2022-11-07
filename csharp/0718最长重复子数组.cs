public partial class Solution
{
    public int FindLength(int[] nums1, int[] nums2)
    {
        int m, n, res;
        (res, m, n) = (0, nums1.Length, nums2.Length);

        int[] dp = new int[n];

        // 将m=0时的dp数组初始化
        for (int i = 0; i < n; i++)
        {
            if(nums1[0]==nums2[i])
            {
                dp[i] = 1;
                res = 1;
            }
        }
        
        for (int i = 1; i<m;i++)
        {

            for (int j = n-1; j>0;j--)
            {
                if(nums1[i]==nums2[j])
                {
                    dp[j] = dp[j - 1] + 1;
                    res = Math.Max(res, dp[j]);
                }
                else
                    //注意如果不相等，要重新从0开始计算 
                    dp[j] = 0;
            }
            dp[0] = nums1[i] == nums2[0] ? 1 : 0;
        }
        return res;
    }
}