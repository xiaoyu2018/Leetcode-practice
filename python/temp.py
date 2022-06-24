# from functools import lru_cache

# @lru_cache(None)
# def fibo1(n:int):
#     if(n in [1,2]):
#         return 1

#     return fibo1(n-1)+fibo1(n-2)


# memo=dict()
# def fibo2(n:int):
#     if(n in [1,2]):
#         memo[n]=1

#     if(n in memo.keys()):
#         return memo[n]
    
#     val=fibo2(n-1)+fibo2(n-2)
#     memo[n]=val

#     return val

# # print(fibo2(999))

# def createArray2D(h,w):
#     return [[0]*w for j in range(h)]
#     # return [[0]*w]*h 错误写法，低维数组地址相同

# a=createArray2D(3,4)
# a[0][0]=1
# print(a)

# class C1:
#     def show(self):
#         print("c1------------")

# class C2(C1):
#     def show(self):
#         print("c2------------")
    
#     def foo(self):
#         self.show()
#         super().show()
    
# class C3(C2):
#     def show(self):
#         print("c3------------")
#         super().show()

# c3=C3()
# c3.foo()
# print("-------------------")
# c3.show()

class Node:
    def __init__(self,val,next=None) -> None:
        self.val=val
        self.next=next
    


def create_tail():

    head=Node(-1)
    q=head

    while(1):
        val=input()
        if(val==str(-1)):
            break
        
        p=Node(val)
        q.next=p
        q=p
    
    return head

def create_head(nums:list):
    head=Node(-1)
    
    for i in nums:
        p=Node(i)
        p.next=head.next
        head.next=p
    return head
def show(*head:Node):

    if any([(not head),None in head]):
        print(head)
        return 

    head=[i.next if i.val==-1 else i for i in head]
    for h in head:
        while(h):
            print(f"{h.val} ")
            h=h.next
        print("\n")
    
def ReverseLinkList(head:Node):

    if(not head or not head.next):
        return head
    
    new_head=ReverseLinkList(head.next)
    p=new_head
    while(p.next):
        p=p.next
    p.next=head
    
    head.next=None
    return new_head

# l1=create_tail()
l2=create_head([1,2,3,4,5])
l2=ReverseLinkList(l2.next)
show(l2)
