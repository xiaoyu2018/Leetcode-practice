from linklist import *

# 添加虚拟头节点
def removeElements1(head:ListNode,val:int):
    extra_head=ListNode(next=head)
    
    head=extra_head
    
    while(head.next):
        if(head.next.val==val):
            head.next=head.next.next
        else:
            head=head.next

    return extra_head.next

def removeElements2(head:ListNode,val:int):
    if(not head):
        return None
    p=head
    q=head.next
    while(True):
        if(not q):
            break
        
        if(q.val==val):
            while(q and q.val==val):
                q=q.next
            p.next=q
            
        if(not q):
            break

        p=q
        q=q.next
        
    if(head.val==val):
        if(not head.next):
            return None
        head=head.next
    
    return head



nums=[6,6,6]
val=6
head=create(nums)
show(removeElements1(head,6))