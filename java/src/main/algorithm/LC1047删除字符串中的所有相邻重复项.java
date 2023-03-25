package main.algorithm;

import java.util.ArrayDeque;
import java.util.Deque;

public class LC1047删除字符串中的所有相邻重复项 {
    public String removeDuplicates(String s) {
        Deque<Character> stack = new ArrayDeque<>(20000);
        

        for(int i=0;i<s.length();i++)
        {
            if (stack.isEmpty())
                stack.add(s.charAt(i));
            else {
                char crt = stack.peekLast();
                if (crt == s.charAt(i))
                    stack.pollLast();
                else
                    stack.add(s.charAt(i));
            }
        }
        StringBuilder sb = new StringBuilder();
        for (Character c : stack) {
            sb.append(c);
        }

        return sb.toString();
    }
}
