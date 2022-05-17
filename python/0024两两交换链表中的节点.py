from linklist import *

def swapPairs(head: ListNode) -> ListNode:
    if(not head or not head.next):
        return head

    p1=head
    p2=head.next

    p1.next=swapPairs(p2.next)
    p2.next=p1

    return p2

head=create([1])
show(swapPairs(head))
