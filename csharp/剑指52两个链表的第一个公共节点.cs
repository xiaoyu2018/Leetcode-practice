public partial class Solution
{
    public ListNode GetIntersectionNode(ListNode headA, ListNode headB)
    {
        int la = 0, lb = 0;
        ListNode p;
        for (p = headA; p != null; p = p.next, la++) ;
        for (p = headB; p != null; p = p.next, lb++) ;
        if (la == 0 || lb == 0)
            return null;

        int displacement = la - lb;
        if (displacement > 0)
            for (; displacement > 0; displacement--, headA = headA.next) ;
        else
            for (; displacement < 0; displacement++, headB = headB.next) ;

        for (; headA!=null&&headB!=null;headA=headA.next,headB=headB.next )
            if(headA==headB)
                return headA;
        return null;
    }
}