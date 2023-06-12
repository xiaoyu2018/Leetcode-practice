package main.algorithm;

import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

public class LC1466重新规划路线 {
    public int minReorder(int n, int[][] connections) {
        int res = 0;
        Queue<Integer> nodes = new ArrayDeque<>();
        int size = connections.length;
        Set<Integer> memo = new HashSet<>();
        int[][] matrix = new int[n][n];

        for (int i = 0; i < size; i++) {
            matrix[connections[i][0]][connections[i][1]] = 1;
        }
        nodes.add(0);

        while (!nodes.isEmpty()) {
            int crt = nodes.poll();

            memo.add(crt);
            for (int i = 0; i < n; i++) {
                if (memo.contains(i))
                    continue;
                if (matrix[crt][i] == 1) {
                    res++;
                    nodes.add(i);
                }
                if (matrix[i][crt] == 1) {
                    nodes.add(i);
                }
            }
        }

        return res;
    }
}
