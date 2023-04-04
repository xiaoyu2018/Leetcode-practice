from linklist import *

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    s=set()

    while(headA):
        s.add(headA)
        headA=headA.next
    
    while(headB):
        if(headB in s):
            return headB
        headB=headB.next
    
    return None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    p1=headA
    p2=headB
    l1=0
    l2=0

    while(p1):
        l1+=1
        p1=p1.next
    while(p2):
        l2+=1
        p2=p2.next
    
    d=l1-l2

    while(d<0):
        d+=1
        headB=headB.next
    
    while(d>0):
        d-=1
        headA=headA.next
    
    while(headA):
        if(headA==headB):
            return headA
        headA=headA.next
        headB=headB.next
    
    return None


