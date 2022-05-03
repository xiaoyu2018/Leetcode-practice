from typing import Optional

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
        print(head.val)
        head=head.next

# 迭代
#  Optional[ListNode]表明参数类型只能为ListNode或None
def MergeTwoList1(list1: Optional[ListNode],list2: Optional[ListNode]) -> Optional[ListNode]:
    if(not list1):
        return list2
    if(not list2):
        return list1

    res=ListNode()
    q=res
    while(True):
        p=ListNode()
        if(list1.val<list2.val):
            p.val=list1.val
            list1=list1.next
        else:
            p.val=list2.val
            list2=list2.next
        q.next=p
        q=p

        if(not(list2 and list1)):
            break
    
    q.next=list1 if not list2 else list2

    return res.next

# 递归 
def MergeTwoList2(list1:ListNode,list2:ListNode):
    if(not list1):
        return list2
    if(not list2):
        return list1
    
    if(list1.val<list2.val):
        list1.next=MergeTwoList2(list1.next,list2)
        return list1
    else:
        list2.next=MergeTwoList2(list1,list2.next)
        return list2


l1=create([1,2,4])
l2=create([1,3,4])
l3=MergeTwoList2(l1,l2)
show(l3)
