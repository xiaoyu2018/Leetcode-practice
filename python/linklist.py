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

class MyLinkedList:
    class _ListNode:
        def __init__(self,val=0,next=None):
            self.val=val
            self.next=next

    def __init__(self):
        self.head=ListNode()
        

    def get(self, index: int) -> int:
        if(index<0 or self.head.val<index+1):
            return -1

        p=self.head.next
        while(index):
            index-=1
            p=p.next
        return p.val


    def addAtHead(self, val: int) -> None:
        t=ListNode(val,self.head.next)
        self.head.next=t
        self.head.val+=1

    def addAtTail(self, val: int) -> None:
        p=self.head
        while(p.next):
            p=p.next
        p.next=ListNode(val)
        self.head.val+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if(index>self.head.val):
            return
        p=self.head
        while(index):
            index-=1
            p=p.next
        t=ListNode(val,p.next)
        p.next=t
        self.head.val+=1

    def deleteAtIndex(self, index: int) -> None:
        if(-1<index<self.head.val):
            p=self.head
            while(index):
                index-=1
                p=p.next
            
            p.next=p.next.next
            self.head.val-=1

if __name__=='__main__':
    obj=MyLinkedList()
    obj.addAtHead(3)
    obj.addAtHead(2)
    obj.addAtHead(1)
    obj.addAtTail(4)
    obj.addAtIndex(4,0)
    obj.deleteAtIndex(4)

    print(obj.get(3))