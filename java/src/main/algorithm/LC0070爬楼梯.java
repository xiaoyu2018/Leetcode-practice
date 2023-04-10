package main.algorithm;

import java.util.Dictionary;
import java.util.Hashtable;

public class LC0070爬楼梯 {
    Dictionary<Integer, Integer> memo = new Hashtable<>();

    public int climbStairs1(int n) {
        if(n==1||n==2)
            return n;
        int v1,v2;
        if (memo.get(n - 1) == null)
        {
            v1 = climbStairs1(n - 1);
            memo.put(n - 1, v1);
        }
        else
            v1 = memo.get(n - 1);

        if (memo.get(n - 2) == null)
        {
            v2 = climbStairs1(n - 2);
            memo.put(n - 2, v2);
        }
        else
            v2 = memo.get(n - 2);
        

        return v1 + v2;
    }
    
    public int climbStairs2(int n) {
        int[] dp = new int[Math.max(n + 1, 4)];
        
        for(int i=0;i<3;i++)
            dp[i] = i;
        
        for(int i=3;i<=n;i++)
        {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }
}
