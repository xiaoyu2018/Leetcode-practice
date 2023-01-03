
public partial class Solution
{
    
    public ListNode MergeTwoLists(ListNode l1, ListNode l2)
    {
        ListNode dummy_head = new ListNode(-1);
        ListNode? p = dummy_head;

        while(l1!=null&&l2!=null)
        {
            if(l1.val<l2.val)
            {
                p.next = l1;
                p = l1;
                l1 = l1.next;
            }
            else
            {
                p.next = l2;
                p = l2;
                l2 = l2.next;
            }
        }

        p.next = l1 != null ? l1 : l2;

        return dummy_head.next;
    }
}