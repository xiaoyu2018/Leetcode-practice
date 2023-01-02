
public partial class Solution
{
    private int _getMajority(int[] nums, int l, int r)
    {
        if (l == r)
            return nums[l];
        int lv, rv;
        lv = _getMajority(nums, l, (l + r) >> 1);
        rv = _getMajority(nums, ((l + r) >> 1) + 1, r);

        if(lv==rv)
            return lv;

        int lc=0, rc=0;
        for (int i = l; i<=r;i++)
        {
            if(nums[i]==lv)
                lc++;
            if(nums[i]==rv)
                rc++;
        }

        return lc > rc ? lv : rv;

    }
    // 分治
    public int MajorityElement(int[] nums)
    {
        return _getMajority(nums, 0, nums.Length - 1);
    }
}