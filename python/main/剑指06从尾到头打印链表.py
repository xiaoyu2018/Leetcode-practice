from linklist import ListNode


def reversePrint(head: ListNode) -> list:
    res=[]

    while(head!=None):
        res.append(head.val)
        head=head.next
    
    return res[::-1]



# 递归
def reversePrint2(head: ListNode) -> list:
    res=[]
    def _recursion(p:ListNode):    
        if(p==None):
            return
        _recursion(p.next)
        res.append(p.val)
        
    _recursion(head)
    return res 