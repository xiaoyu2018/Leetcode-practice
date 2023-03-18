package main.algorithm;
public class BM17二分查找I {
    // [l,r]查找
    public int search1(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        int mid;
        while (l <= r) {
            mid = l + ((r - l) >> 1);
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] > target)
                r = mid - 1;
            else
                l = mid + 1;
        }
        return -1;
    }

    // [l,r)查找
    public int search2(int[] nums,int target)
    {
        int l = 0, r = nums.length;
        int m;
        while(l<r)
        {
            m = l + ((r - l) >> 1);
            if (nums[m] == target)
                return m;
            else if (nums[m] > target)
                r = m;
            else
                l = m + 1;
        }
        
        return -1;
    }
}
