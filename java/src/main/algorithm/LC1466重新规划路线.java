package main.algorithm;

import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

public class LC1466重新规划路线 {
    public int minReorder(int n, int[][] connections) {
        int res = 0;
        Queue<Integer> nodes = new ArrayDeque<>();
        int size = connections.length;
        Set<Integer> memo = new HashSet<>();
        Map<Integer, Integer> to = new HashMap<>();
        Map<Integer, Integer> from = new HashMap<>();

        for (int i = 0; i < size; i++) {
            to.put(connections[i][1], connections[i][0]);
            from.put(connections[i][0], connections[i][1]);
        }
        nodes.add(0);
        memo.add(0);

        while (!nodes.isEmpty()) {
            int crt_val = nodes.poll();

            if (to.containsKey(crt_val)) {
                int tmp = to.get(crt_val);
                if (!memo.contains(tmp)) {
                    nodes.add(tmp);
                    memo.add(tmp);
                }
            }
            
            if (from.containsKey(crt_val)) {
                int tmp= from.get(crt_val);
                if (!memo.contains(tmp)) {
                    nodes.add(tmp);
                    memo.add(tmp);
                    res++;
                }
            }

        }

        return res;
    }
}
