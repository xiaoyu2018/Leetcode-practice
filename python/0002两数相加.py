from linklist import *

def addTwoNumbers(l1 :ListNode, l2:ListNode):
    if(not l1):
        return l2
    if(not l2):
        return l1
   
    a=0
    b=0
    i=1
    
    while(l1):
        a+=i*l1.val
        i*=10
        l1=l1.next
    i=1
    while(l2):
        b+=i*l2.val
        i*=10
        l2=l2.next
    s=a+b
    if(s==0):
        return ListNode(0)
    l3=ListNode()
    p=l3
    
    
    while(s>0):
        q=ListNode(s%10)
        p.next=q
        s=s//10
        p=q
    
    return l3.next
    
# 。。。
def addTwoNumbers2(l1 :ListNode, l2:ListNode):
    def _noTempCat(l3,l):
        while(l):
            p=l
            l=l.next
            p.next=l3.next
            l3.next=p
    
    def _addOne(l):
        p=l
        q=p
        while(p):
            if(p.val<9):
                p.val+=1
                break
            p.val=0
            q=p
            p=p.next
        if(not p):
            q.next=ListNode(1)

    
    l3=ListNode()
    l3.next=None
    temp=0

    if(not l1):
        return l2
    if(not l2):
        return l1
    
    while(l1 and l2):
        p=ListNode()
        p.val=temp+l1.val+l2.val
        
        temp=0
        if(p.val>=10):
            p.val-=10
            temp=1
        
        p.next=l3.next
        l3.next=p

        l1=l1.next
        l2=l2.next

    if(not temp):
        if(not l1):
            _noTempCat(l3,l2)
        if(not l2):
            _noTempCat(l3,l1)
            
            
    else:
        if(not l1 and l2):
            _addOne(l2)
            _noTempCat(l3,l2)
            
        if(not l2 and l1):
            _addOne(l1)
            _noTempCat(l3,l1)
        if(not l1 and not l2):
            l3.next=ListNode(1,l3.next)
    
    return l3.next

    

l1=create([0])
l2=create([0])

show(addTwoNumbers(l1,l2))

