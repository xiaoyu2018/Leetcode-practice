
public partial class Solution
{
    public class ListNode
    {
        public int val;
        public ListNode? next;

        public ListNode(int val)
        {
            this.val = val;
            next = null;
        }
    }
    public int[] ReversePrint(ListNode head)
    {
        int len = 0;
        for (ListNode p=head;p!=null ;p=p.next,len++);

        int[] res = new int[len];

        for (int i = len-1; i >= 0; --i,head=head.next)
        {
            res[i] = head.val;
        }

        return res;
    }
}