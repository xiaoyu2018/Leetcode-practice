package main.algorithm;

public class LC0647回文子串 {

    public int countSubstrings(String s) {
        int size = s.length();
        int[][] dp = new int[size][size];
        
        int res = 0;

        for (int i = size - 1; i >= 0; i--)
        {
            for (int j = i; j < size; j++) {
                if(s.charAt(i) == s.charAt(j))
                {
                    if (j - i <= 1) {
                        dp[i][j] = 1;
                        res += 1;
                    } else if (dp[i + 1][j - 1] == 1) {
                        dp[i][j] = 1;
                        res += 1;
                    }

                    else
                        dp[i][j] = 0;
                }
                else
                    dp[i][j] = 0;
            }
        }
        
        
        return res;
    }
}
