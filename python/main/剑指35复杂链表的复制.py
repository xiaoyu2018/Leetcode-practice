class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: Node) -> Node:
    res_head=q=None
    memo={None:None}
    tmp=head
    while(tmp!=None):
        p=Node(tmp.val,tmp.next,None)
        memo[tmp]=p
        if(not res_head):
            res_head=q=p
        else:
            q.next=p
            q=p
        tmp=tmp.next
    if(q):
        q.next=None

    tmp=res_head
    while(head!=None):
        tmp.random=memo[head.random]
        head=head.next
        tmp=tmp.next

    return res_head

