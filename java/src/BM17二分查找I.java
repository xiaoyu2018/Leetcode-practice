public class BM17二分查找I {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        int mid;
        while(l<=r)
        {
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
}
