
# dp，注意不是最长连续递增
def lengthOfLIS(nums: list) -> int:
    size=len(nums)

    dp=[1]*size

    for i in range(1,size):

        for j in range(i):
            if(nums[i]>nums[j]):
                dp[i]=max(dp[i],dp[j]+1)
    
    return max(dp)
print(lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
