package main.algorithm;

import java.util.ArrayDeque;
import java.util.Queue;

public class LC0225用队列实现栈 {
    Queue<Integer> q;

    public LC0225用队列实现栈() {
        q = new ArrayDeque<>(100);
    }

    public void push(int x) {
        q.add(x);
    }

    public int pop() {
        int size = q.size();
        for(int i=0;i<size-1;++i)
        {
            q.add(q.poll());
        }
        return q.poll();
    }

    public int top() {
        
        int size = q.size();
        for (int i = 0; i < size - 1; ++i) {
            q.add(q.poll());
        }
        int res = q.poll();
        q.add(res);
        return res;
    }

    public boolean empty() {
        return q.isEmpty();
    }
}
