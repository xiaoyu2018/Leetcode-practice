package main.algorithm;

import java.util.HashSet;
import java.util.Set;

public class LC1456定长子串中元音的最大数目 {
    public int maxVowels(String s, int k) {
        Set<Character> memo = new HashSet<>() {
            {
                add('a');
                add('e');
                add('i');
                add('o');
                add('u');
            }
        };

        int res = 0;
        int tmp = 0;
        int size = s.length();
        for (int i = 0; i < k; i++) {
            tmp += memo.contains(s.charAt(i)) ? 1 : 0;
        }
        res = tmp;

        for (int i = 1; i <= size - k; i++) {
            tmp -= memo.contains(s.charAt(i - 1)) ? 1 : 0;
            tmp += memo.contains(s.charAt(i + k - 1)) ? 1 : 0;
            res = Math.max(res, tmp);
        }

        return res;
    }
}
