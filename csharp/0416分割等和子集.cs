
public partial class Solution
{

    // 暴力回溯（超时）
    public bool CanPartition(int[] nums)
    {
        if(nums.Length<2)
            return false;
        int temp = 0;
        int total = nums.Sum();
        bool res = false;

        void _backTracking(int start)
        {
            if((temp << 1) ==total)
            {
                res = true;
                return;
            }

            for (int i = start; i < nums.Length; i++)
            {
                temp += nums[i];
                if((temp << 1) <=total)
                    _backTracking(i + 1);
                temp -= nums[i];
            }
        }

        _backTracking(0);
        
        return res;
    }

    //转化为01背包
    public bool CanPartition1(int[] nums)
    {
        int total = nums.Sum();
        if(total%2==1) return false;
        int size = total>>1;

        int[] dp = new int[size+1];

        for (int i = 0; i <= size; i++)
        {
            dp[i] = nums[0] > i ? 0 : nums[0];
        }

        for (int i = 1; i < nums.Length; i++)
        {
            //倒序遍历，因为后面的值依赖于前面的值，前面的值不能先变
            for (int j = size; j > 0; j--)
            {
                if(nums[i]<=j)
                    dp[j] = Math.Max(dp[j], dp[j - nums[i]] + nums[i]);
            }
        }

        return dp[size] == size;
    }

}