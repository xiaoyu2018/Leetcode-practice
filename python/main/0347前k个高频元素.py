from collections import Counter
import heapq

# 官方排序算法，取前k
def topKFrequent1(nums: list, k: int) -> list:
    c=Counter(nums)
    return sorted(c,key=lambda x:c[x],reverse=True)[:k]


# 优先级队列(堆排序)
def topKFrequent2(nums: list, k: int) -> list:
    pri_que=[] #小顶堆，不使用大顶堆是因为需要将全部元素插入堆中排序

    c=Counter(nums)

    for key,freq in c.items():
        heapq.heappush(pri_que,(freq,key))

        if(len(pri_que)>k):
            heapq.heappop(pri_que)
        
    return [heapq.heappop(pri_que)[1] for i in range(k)][::-1]



print(topKFrequent2([3,0,1,0],1))
# print((3,2)>(2,1))
