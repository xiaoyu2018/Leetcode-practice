package main.algorithm;

import java.util.Arrays;

public class HW412_1 {
    
    private boolean _check(int limit,int[] revokes,int target)
    {
        int s = 0;
        for (int num : revokes) {
            s += num > limit ? limit : num;
        }
        return s<=target;
    }

    public int solve(int[] revokes,int target)
    {
        //二分
        int m=Arrays.stream(revokes).max().getAsInt();
        int l = 0, r = m;
        while(l<=r)
        {
            int mid = l + ((r - l) >> 1);
            if (_check(mid, revokes, target))
                l = mid + 1;
            else
                r = mid - 1;
        }
        // 0 1 2
        return r == m ? -1 : r;
    }
}
