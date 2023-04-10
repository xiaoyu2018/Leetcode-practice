package main.algorithm;

import java.util.Arrays;

public class LC0455分发饼干 {
    public int findContentChildren(int[] g, int[] s) {
        
        Arrays.sort(g);
        Arrays.sort(s);

        int i = 0, j = 0;
        
        while(i<g.length&&j<s.length)
        {
            if (s[j] >= g[i])
                i++;
            j++;
        }
        
        return i;

    }
}
