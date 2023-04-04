
# dp
def maxSubArray(nums: list) -> int:
    res=dp=nums[0]

    for num in nums[1:]:
        dp=max(num,dp+num)
        res=max(res,dp)

    return res
    