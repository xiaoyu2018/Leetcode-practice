public partial class Solution
{
    public int Search(int[] nums, int target)
    {
        int l = 0;
        int r = nums.Length-1;

        while(l<=r)
        {
            int m = (l + r) >> 1;

            if(nums[m]==target)
                return m;
            
            if(nums[m]<target)
                l = m + 1;
            else
                r = m - 1;
        }

        return -1;
    }
}