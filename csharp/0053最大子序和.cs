public partial class Solution
{
    public int MaxSubArray(int[] nums)
    {
        int crt,res;
        crt = res = nums[0];

        for (int i = 1; i < nums.Length; i++)
        {
            if(crt<0)
                crt = nums[i];

            else
                crt += nums[i];

            res = Math.Max(crt, res);
        }

        return res;
    }
}