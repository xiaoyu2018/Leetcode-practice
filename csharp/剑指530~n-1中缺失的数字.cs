public partial class Solution
{
    // 遍历
    public int MissingNumber(int[] nums)
    {
        for (int i = 0; i < nums.Length; i++)
        {
            if(nums[i]!=i)
                return i;
        }

        return nums.Length;
    }

    // 数学
    public int MissingNumber1(int[] nums)
    {
        return nums[nums.Length-1]!=nums.Length ? 
        nums.Length:nums[nums.Length - 1]*(nums[nums.Length - 1]+1)/2-nums.Sum();
    }
    // 二分
    public int MissingNumber2(int[] nums)
    {
        int l = 0, r = nums.Length - 1;
        if(nums[nums.Length - 1] != nums.Length)
            return nums.Length;
        while(l<r)
        {
            int m = l + ((r - l) >> 1);

            if(m==nums[m]) //nums缺失值不在中0-m中
                l = m + 1;
            else            //nums缺失值在中0-m中
                r = m;

        }
        return l;
    }
}