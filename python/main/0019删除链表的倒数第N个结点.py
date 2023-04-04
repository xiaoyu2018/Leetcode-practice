from linklist import *


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    extra_head=ListNode(next=head)

    slow=extra_head
    fast=head

    while(n>0):
        fast=fast.next
        n-=1

    while(fast):
        fast=fast.next
        slow=slow.next

    slow.next=slow.next.next

    return extra_head.next


head=create([1,2])
show(removeNthFromEnd(head,2))
