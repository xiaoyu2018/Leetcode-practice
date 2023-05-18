def findMaxAverage(nums:list, k: int) -> float:
        
    tmp=sum(nums[:k])
    res=tmp/k

    for i in range(1,len(nums)-k+1):
        tmp+=(nums[i+k-1]-nums[i-1])
        res=max(res,tmp/k)
        
        

    return res

print(findMaxAverage([0,1,1,3,3],4))