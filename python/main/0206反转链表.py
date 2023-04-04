from linklist import *

# 递归
def reverseList1(head: ListNode) -> ListNode:
    if(not head):
        return None
    if(not head.next):
        return head

    reversed_h=reverseList1(head.next)
    p=reversed_h

    while(p.next):
        p=p.next

    p.next=head
    head.next=None

    return reversed_h

# 双指针
def reverseList2(head: ListNode) -> ListNode:
    if(not head):
        return None
    
    prev=None
    cur=head
    while(cur):
        temp=cur.next
        cur.next=prev
        prev=cur
        cur=temp
    
    return prev

h=create([1,2,3])

show(reverseList2(h))