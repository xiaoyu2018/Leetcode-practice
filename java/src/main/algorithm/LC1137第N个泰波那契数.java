package main.algorithm;

import java.util.HashMap;
import java.util.Map;

public class LC1137第N个泰波那契数 {

    private Map<Integer,Integer> memo = new HashMap<>(){
        {
            put(0, 0);
            put(1, 1);
            put(2, 1);
        }
    };

    public int tribonacci1(int n) {
        if (memo.containsKey(n))
            return memo.get(n);
        
        memo.put(n - 1, tribonacci1(n - 1));
        memo.put(n - 2, tribonacci1(n - 2));
        memo.put(n - 3, tribonacci1(n - 3));

        return memo.get(n-1)+ memo.get(n - 2)+ memo.get(n - 3);
    }

    public int tribonacci(int n) {
        int[] dp = new int[] { 0, 1, 1 };

        if(n<3)
            return dp[n];
        int res=-1;
        for(int i=3;i<=n;i++)
        {
            res = dp[0] + dp[1] + dp[2];
            dp[0] = dp[1];
            dp[1] = dp[2];
            dp[2] = res;
        }

        return res;
    }
}
