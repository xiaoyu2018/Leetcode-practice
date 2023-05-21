package main.algorithm;

public class LC0392判断子序列 {
    public boolean isSubsequence(String s, String t) {

        int i = 0, j = 0;
        int size1 = s.length();
        int size2 = t.length();

        while (i < size1 && j < size2) {
            if (s.charAt(i) == t.charAt(j))
                i++;
            j++;
        }

        return i == size1;
    }
}
