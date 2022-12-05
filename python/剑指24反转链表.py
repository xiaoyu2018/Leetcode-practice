from linklist import ListNode

def reverseList(head: ListNode) -> ListNode:
    res=ListNode()
    res.next=None

    while(head):
        p=head.next
        head.next=res.next
        res.next=head
        head=p
    return res.next
