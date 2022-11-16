public partial class Solution
{
    public bool IsIdealPermutation(int[] nums)
    {
        int size = nums.Length;
        int min_suf = nums[size - 1];

        for (int i = size-3; i >= 0; i--)
        {
            if(nums[i]>min_suf)
                return false;
            min_suf = Math.Min(nums[i + 1], min_suf);
        }
        return true;
    }
}