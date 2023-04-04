
def maxSubArray(nums: list) -> int:
    dp=[nums[0]]*len(nums)

    for i in range(1,len(nums)):
        dp[i]=max(nums[i],nums[i]+dp[i-1])
    
    return max(dp)