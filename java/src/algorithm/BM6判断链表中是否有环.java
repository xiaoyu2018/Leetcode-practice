package algorithm;
public class BM6判断链表中是否有环 {
    public boolean hasCycle(ListNode head) {
        ListNode p1, p2;
        p1 = p2 = head;
        
        while (p2!=null)
        {
            p2 = p2.next;
            if (p2 == null)
                break;
            if(p1==p2)
                return true;
            p2 = p2.next;
            if (p2 == null)
                break;
            if(p1==p2)
                return true;
            p1 = p1.next;
            if(p1==p2)
                return true;
        }

        return false;
    }
}
