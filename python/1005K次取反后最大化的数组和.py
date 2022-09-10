

# 贪心，每次都取反最小值
def largestSumAfterKNegations(nums:list, k: int) -> int:

    def _findMinIndex(nums):

        idx=0
        for i,v in enumerate(nums):
            if(v<nums[idx]):
                idx=i
        
        return idx
    
    for _ in range(k):
        crt_idx=_findMinIndex(nums)
        nums[crt_idx]=-nums[crt_idx]
    
    return sum(nums)

print(largestSumAfterKNegations([2,-3,-1,5,-4],2))
