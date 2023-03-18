package main.algorithm;
public class BM2链表内指定区间反转 {
    
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if(head==null||head.next==null||m==0||m==n)
            return head;

        ListNode dummy_head,p, q, c;
        dummy_head = new ListNode(-1);
        dummy_head.next = head;
        p =c = dummy_head;

        for(int i=1;i<=n;++i)
        {
            if (i == m)
                p = c;
            c = c.next;
        }
        q = c;
        c = p.next;
        p.next = q.next;
        q = q.next;
        for(;c!=q;)
        {
            ListNode temp = c.next;
            c.next = p.next;
            p.next = c;
            c = temp;
        }

        return dummy_head.next;

    }
}
