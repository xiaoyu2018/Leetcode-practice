from linklist import ListNode

def deleteNode(head:ListNode, val: int) -> ListNode:
    dummyhead=ListNode(-1)
    dummyhead.next=head
    p,q=dummyhead,head

    while(q!=None):
        if(q.val==val):
            p.next=p.next.next
            break
        else:
            p=p.next    
        q=q.next
        
    
    return dummyhead.next