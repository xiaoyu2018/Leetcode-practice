from collections import deque

# 暴力
def maxSlidingWindow1(nums: list, k: int) -> list:

    return[max(nums[i:i+k]) for i in range(len(nums)-k+1)]

# 单调队列（适合动态寻找最值）
def maxSlidingWindow2(nums: list, k: int) -> list:
    class OrderedQueue:
        def __init__(self,nums:list) -> None:
            self.dq=deque()

            for i in nums:
                self.push(i)

        def pop(self,num):
            if(self.top()==num):
                self.dq.popleft()
        
        def push(self,num):
            while(self.dq and self.dq[-1]<num):
                self.dq.pop()
            self.dq.append(num)            
    
        def top(self):
            return self.dq[0]
    
    odq=OrderedQueue(nums[:k])

    res=[odq.top()]

    for i in range(len(nums)-k):
        odq.pop(nums[i])
        odq.push(nums[i+k])
        res.append(odq.top())

    return res

print(maxSlidingWindow2([1,3,-1,-3,5,3,6,7],3))
