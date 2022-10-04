
public partial class Solution
{
    public int FindTargetSumWays(int[] nums, int target)
    {
        int res = 0;
        int size = nums.Length;
        void _backTracking1(int start=0,int sum=0)
        {
            if(start==size)
            {
                if(sum == target)
                    res++;
                return;
            }

            _backTracking1(start + 1, sum + nums[start]);
            _backTracking1(start + 1, sum - nums[start]);
        }
        
        int total = nums.Sum();

        void _backTracking2(int start,int sum)
        {
            if(sum==target)
            {
                res++;
            }    

            for (int i = start; i < size; i++)
            {
                if(sum<target)
                    return;
                _backTracking2(i + 1, sum - 2 * nums[i]);
            }
        }

        _backTracking2(0,total);

        return res;
    }


}