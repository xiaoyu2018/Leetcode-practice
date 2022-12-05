public class ListNode
{
    public int val;
    public ListNode? next;
}

// 递归翻转链表
public partial class Solution
{
    public ListNode ReverseList(ListNode? head)
    {
        if(head==null || head.next==null)
            return head;
        

        ListNode rh = ReverseList(head.next);
        ListNode newhead = rh;
        for (; rh.next!=null;rh=rh.next );

        rh.next = head;
        rh.next.next = null;

        return newhead;
    }

}