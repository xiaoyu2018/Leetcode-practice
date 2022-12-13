from linklist import ListNode

def getKthFromEnd(head: ListNode, k: int) -> ListNode:
    p=head

    for _ in range(k):
        p=p.next
    
    while(p!=None):
        p=p.next
        head=head.next
    
    return head
