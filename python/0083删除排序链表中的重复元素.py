class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create(elems:list):
    if(not elems):
        return None
    head=ListNode()
    q=head
    q.val=elems[0]

    for i in elems[1:]:
        p=ListNode(i)
        q.next=p
        q=p
    return head

def show(head):
    while(head):
        print(head.val,end=" ")
        head=head.next

def deleteDuplicates(head:ListNode):
    if(not head):
        return head
    p=q=head
    
    while(q):
        if(p.val!=q.val):
            p.next=q
            p=q
        
        q=q.next
    p.next=None
    return head

head=create([12,3,4])
show(deleteDuplicates(head))