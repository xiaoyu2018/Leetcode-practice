
# 第一家和最后一家不能同时偷，只需分别讨论仅不包含第一家和不包含最后一家的打家劫舍Ⅰ的情况
def rob(nums: list) -> int:
    size=len(nums)
    if(size==1):
        return nums[0]
    
    def _rob(ns:list)->int:
        nonlocal size
        if(size==2):
            return ns[0]

        dp=[0]*(size-1)
        dp[0]=ns[0]    
        dp[1]=max(ns[0],ns[1])
        

        for i in range(2,size-1):
            dp[i]=max(dp[i-2]+ns[i],dp[i-1])
        return dp[-1]
    

    return max(_rob(nums[1:]),_rob(nums[:-1]))

print(rob([1,2,3,1]))
