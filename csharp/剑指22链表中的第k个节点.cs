
public partial class Solution
{
    public ListNode GetKthFromEnd(ListNode head, int k)
    {
        ListNode p = head;

        for (int i = 0; i < k; i++, p = p.next) ;

        for (; p!=null;head=head.next, p = p.next) ;
        return head;
    }
}