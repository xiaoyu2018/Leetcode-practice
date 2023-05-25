package main.algorithm;

import java.util.ArrayDeque;

public class LC0649Dota2参议院 {
    
    public String predictPartyVictory(String senate) {
        ArrayDeque<Integer> r_q = new ArrayDeque<>();
        ArrayDeque<Integer> d_q = new ArrayDeque<>();

        for(int i=0;i<senate.length();i++){
            boolean tmp = (senate.charAt(i) == 'R') ? r_q.add(i) : d_q.add(i);
        }
        
        while(!r_q.isEmpty()&&!d_q.isEmpty())
        {
            Integer idx = Math.max(d_q.peekLast(), r_q.peekLast()) + 1;
            
            Integer r = r_q.poll();
            Integer d = d_q.poll();

            boolean tmp = r > d ? d_q.add(idx) : r_q.add(idx);
        }

        return r_q.isEmpty() ? "Dire" : "Radiant";
    }
}
