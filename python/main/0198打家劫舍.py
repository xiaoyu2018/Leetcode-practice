
def rob(nums: list) -> int:
    size=len(nums)
    if(size==0):
        return 0
    if(size<3):
        return max(nums)
    
    dp=[0]*size
    dp[0]=nums[0]
    dp[1]=max(nums[0], nums[1])

    for i in range(2,size):
        dp[i]=max(dp[i - 2] + nums[i], dp[i - 1])
    
    return max(dp)

print(rob([2,1,1,2]))