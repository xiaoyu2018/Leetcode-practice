public class LC0027移除元素 {
    public int removeElement(int[] nums, int val) {
        int l = 0, r = nums.length - 1;

        while(l<=r)
        {
            for (;l<nums.length&&nums[l] != val; l++)
                ;
            for (;r>=0&&nums[r] == val; --r)
                ;
            if (l > r)
                break;
            
            nums[l] ^= nums[r];
            nums[r] ^= nums[l];
            nums[l] ^= nums[r];
            
        }

        return r + 1;
    }
}
