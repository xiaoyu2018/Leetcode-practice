from linklist import *


def detectCycle1(head: ListNode) -> ListNode:
    
    if(not head):
        return None

    memo=set()
    p=head
    
    while(p):
        if(p in memo):
            return p
        
        memo.add(p)

        p=p.next
    
    return None

# 快慢指针
def detectCycle2(head: ListNode) -> ListNode:
    fast=slow=head

    while(fast and fast.next):
        fast=fast.next.next
        slow=slow.next

        if(fast==slow):

            while(slow!=head):        
                head=head.next
                slow=slow.next
            
            return slow

    return None