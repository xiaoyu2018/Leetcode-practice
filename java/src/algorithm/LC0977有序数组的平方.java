package algorithm;
public class LC0977有序数组的平方 {
    public int[] sortedSquares(int[] nums) {
        int size=nums.length;
        int l = 0, r = size - 1;
        int[] res = new int[size];

        for(int k=size-1;k>=0;k--)
        {
            int l_v = nums[l] * nums[l];
            int r_v = nums[r] * nums[r];

            if (l_v > r_v) {
                res[k] = l_v;
                l++;
            } else {
                res[k] = r_v;
                r--;
            }
        }
        return res;
    }
}
