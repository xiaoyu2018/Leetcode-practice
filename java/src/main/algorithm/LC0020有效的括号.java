package main.algorithm;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public class LC0020有效的括号 {

    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        Map<Character, Character> m1 = new HashMap<>();
        m1.put('(', ')');
        m1.put('[', ']');
        m1.put('{', '}');

        for (char c : s.toCharArray()) {
            if (m1.keySet().contains(c)) {
                stack.add(c);
            }

            else if (m1.values().contains(c)) {
                Character crt = stack.pollLast();
                if (crt == null || c != m1.get(crt))
                    return false;
            } else
                return false;
        }

        return stack.isEmpty();
    }
}
