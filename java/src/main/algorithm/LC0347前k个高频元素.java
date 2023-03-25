package main.algorithm;

import java.util.HashMap;
import java.util.Map;


public class LC0347前k个高频元素 {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> memo = new HashMap<>();

        for (int i : nums) {
            if (memo.containsKey(i))
                memo.put(i, memo.get(i) + 1);
            else
                memo.put(i, 1);
        }

        return memo.entrySet()
                .stream()
                .sorted(
                        (a, b) -> {
                            return b.getValue() - a.getValue();
                        })
                .limit(k)
                .mapToInt((v) -> v.getKey())
                .toArray();
    }
}
