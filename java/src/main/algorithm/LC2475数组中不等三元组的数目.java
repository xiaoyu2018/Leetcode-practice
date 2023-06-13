package main.algorithm;

import java.util.ArrayList;
import java.util.List;

public class LC2475数组中不等三元组的数目 {
    private int res = 0;
    private List<Integer> tmp = new ArrayList<>();

    private void backTracking(int[] nums,int start)
    {
        if (tmp.size() > 3)
            return;
        if(tmp.size()==3)
            res += 1;
        
        for(int i=start;i<nums.length;i++)
        {
            if(!tmp.contains(nums[i]))
            {
                tmp.add(nums[i]);
                backTracking(nums, i + 1);
                tmp.remove(tmp.size()-1);
            }
        }
    }

    public int unequalTriplets(int[] nums) {
        backTracking(nums, 0);
        return res;
    }
}
