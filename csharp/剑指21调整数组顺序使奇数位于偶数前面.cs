public partial class Solution
{
    public int[] Exchange(int[] nums)
    {
        int i, j;
        (i, j) = (0, nums.Length-1);

        while (i < j)
        {
            for (; i < j && nums[i] % 2 == 1; i++) ;
            for (; i < j && nums[j] % 2 == 0; j--) ;

            if(i<j)
                (nums[i], nums[j]) = (nums[j], nums[i]);
            
            
        }

        return nums;
    }
}