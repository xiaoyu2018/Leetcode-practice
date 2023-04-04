

# 只需要符合要求的排列的总数，可以用动态规划
# 需要把所有排列都列出来，则需要用回溯

def combinationSum4(nums: list, target: int) -> int:
    
    dp=[0]*(target+1)
    dp[0]=1

    # 求组和数时，要外层遍历物品，内层遍历背包
    # 而求排列数时，要外层遍历背包，内层遍历物品
    for j in range(target+1):
        for n in nums:
            dp[j]=dp[j] if j<n else dp[j]+dp[j-n]
        print(dp)
    return dp[-1]

print(combinationSum4([1,2,3],4))