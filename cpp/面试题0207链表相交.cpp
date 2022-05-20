#include"mylinklist.h"

ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
{
    ListNode *p1 = headA;
    ListNode *p2 = headB;
    int l1 = 0;
    int l2 = 0;

    while (p1)
    {
        ++l1;
        p1 = p1->next;
    }
    while (p2)
    {
        ++l2;
        p2 = p2->next;
    }

    int d = l1 - l2;

    while(d>0)
    {
        --d;
        headA = headA->next;
    }

    while (d<0)
    {
        ++d;
        headB = headB->next;
    }

    while(headA)
    {
        if(headA==headB)
            return headA;
        headA = headA->next;
        headB = headB->next;
    }

    return NULL;
}