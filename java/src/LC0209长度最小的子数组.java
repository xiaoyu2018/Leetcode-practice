public class LC0209长度最小的子数组 {
    public int minSubArrayLen(int target, int[] nums) {
        int size = nums.length;
        int l = -1, r = -1;
        int res = size + 1,tmp=0;

        while (l <= r&&r<size)
        {
            
            if(tmp>=target)
            {
                res = Math.min(res, r - l);
                tmp -= nums[++l];
            }
            else
            {
                if (r + 1 >= size)
                    break;
                tmp += nums[++r];
            }
        }

        return res == size + 1 ? 0 : res;
    }
}
