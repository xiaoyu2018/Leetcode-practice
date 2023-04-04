from queue import PriorityQueue
class LinkNode:

    def __init__(self,val=-1,next=None) -> None:
        self.val=val
        self.next=next

class MedianFinder:

    def __init__(self):
        self.head=LinkNode(-1)
        self.length=0


    def addNum(self, num: int) -> None:
        node=LinkNode(num)
        if(self.head.next==None):
            self.head.next=node
        else:
            p=q=self.head
            while(1):
                p=q
                q=q.next
                if(q==None or q.val>num):
                    break
            p.next=node
            node.next=q

        self.length+=1

        

    def findMedian(self) -> float:
        mid=self.length//2
        a=b=0
        p=self.head.next
        for _ in range(mid+1):  
            a=b
            b=p.val 
            p=p.next
        return b if self.length%2 else (a+b)/2

# class MedianFinder:

#     def __init__(self):
#         self.data=PriorityQueue(50000)
#         self.length=0


#     def addNum(self, num: int) -> None:
#         self.data.put((num,num))
#         self.length+=1
        

#     def findMedian(self) -> float:
#         mid=self.length//2
#         a=b=0
#         for _ in range(mid+1):  
#             a=b
#             b=self.data.get()[1]
#         return b if self.length%2 else (a+b)/2



