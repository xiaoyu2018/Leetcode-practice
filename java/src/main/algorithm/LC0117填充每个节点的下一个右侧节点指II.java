package main.algorithm;

import java.util.ArrayDeque;
import java.util.Queue;

public class LC0117填充每个节点的下一个右侧节点指II {
    public Node connect(Node root) {
        if(root==null)
            return null;
        Queue<Node> que = new ArrayDeque<>();
        que.add(root);

        while(!que.isEmpty())
        {
            int size = que.size();
            Node crt = null, pre = que.poll();
            if (pre.left != null)
                que.add(pre.left);
            if (pre.right != null)
                que.add(pre.right);
            for(int i=1;i<size;i++)
            {
                crt = que.poll();
                if (crt.left != null)
                    que.add(crt.left);
                if (crt.right != null)
                    que.add(crt.right);
                pre.next = crt;
                pre = crt;

            }
            pre.next = null;
        }
        return root;
    }
}

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {
    }

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};