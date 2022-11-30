public partial class Solution
{
    public int FindRepeatNumber(int[] nums)
    {
        HashSet<int> set = new HashSet<int>();
        set.Add(nums[0]);
        int res = -1;
        for (int i = 1; i < nums.Length; i++)
        {
            res = nums[i];
            if(!set.Add(nums[i]))
                return res;
            
        }
        

        return res;
    }
}