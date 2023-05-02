package main.algorithm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LC1049最后一块石头的重量Ⅱ {

    public int lastStoneWeightII(int[] stones) {

        int total = Arrays.stream(stones).sum();
        int n=total>>1;
        int[] dp = new int[n + 1];

        for (int j = n; j > 0; j--) {
            if (j < stones[0])
                break;
            dp[j] = stones[0];

        }

        for(int i=1;i<stones.length;i++)
        {
            for (int j = n; j > 0; j--) {
                if (j >= stones[i])
                    dp[j] = Math.max(dp[j], dp[j - stones[i]] + stones[i]);
            }
        }
        
        return total - 2 * dp[n];
    }
}
