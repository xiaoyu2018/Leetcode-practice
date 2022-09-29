def goodIndices(nums: list, k: int) -> list:
    size=len(nums)
    left_dp=[1]*size
    right_dp=[1]*size

    for i in range(1,size):
        if(nums[i]<=nums[i-1]):
            left_dp[i]+=left_dp[i-1]
    for i in range(1,size):
        if(nums[i]>=nums[i-1]):
            right_dp[i]+=right_dp[i-1]
            
    print(left_dp)
    print(right_dp)
    return [i for i in range(k,size-k) if left_dp[i-1]>=k and right_dp[i+k]>=k]