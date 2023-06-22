package main.algorithm;

import java.util.HashMap;
import java.util.Map;

public class MST0102判定是否为字符重排 {
    public boolean CheckPermutation(String s1, String s2) {
        Map<Character,Integer> memo1 = new HashMap<>();
        Map<Character,Integer> memo2 = new HashMap<>();

        int size1 = s1.length();
        int size2 = s2.length();
        if(size1!=size2)
            return false;
        
        for(int i=0;i<size1;i++)
        {
            if (memo1.containsKey(s1.charAt(i)))
                memo1.put(s1.charAt(i), memo1.get(s1.charAt(i)) + 1);
            else
                memo1.put(s1.charAt(i), 1);

            if (memo2.containsKey(s2.charAt(i)))
                memo2.put(s2.charAt(i), memo2.get(s2.charAt(i)) + 1);
            else
                memo2.put(s2.charAt(i), 1);

        }
        
        return memo1.equals(memo2);
    }
}
