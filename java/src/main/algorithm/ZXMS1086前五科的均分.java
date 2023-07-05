package main.algorithm;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class ZXMS1086前五科的均分 {
    public int[][] highFive(int[][] items) {
        Map<Integer,PriorityQueue<Integer>> memo=new HashMap<>();
        
        int count=0;
        for(int[] arr :items){
            if(!memo.containsKey(arr[0])){
                memo.put(arr[0],new PriorityQueue<Integer>());
                count++;
            }
            memo.get(arr[0]).add(arr[1]);
        }
        
        int[][] res=new int[count][2];
        Integer[] itr = memo.keySet().toArray(new Integer[0]);
        Arrays.sort(itr);

        for(int i=0;i<count;i++){
            
            var pq = memo.get(itr[i]);
            
            int s = 0;
            for (int j = 0; j < 5; j++) {
                s += pq.poll();
            }
            res[i][0] = itr[i];
            res[i][1] = s / 5;
        }
        return res;
    }
}
