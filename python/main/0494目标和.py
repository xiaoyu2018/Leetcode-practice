
def findTargetSumWays(nums: list, target: int) -> int:
    total=sum(nums)
    
    # neg非负
    if(total-target<0):
        return 0
    # neg是整数
    if((total-target)%2):
        return 0

    # total-neg-neg=target
    neg=(total-target)//2

    # 转化为从nums中凑出等于neg的情况总数
    # 01背包组合
    m=len(nums)
    n=neg+1

    # dp=[1]+[0 if nums[0]!=i else 1 for i in range(1,n)]
    dp=[1]+[0]*neg
    
    for i in range(0,m):
        for j in range(n-1,nums[i]-1,-1):
            dp[j]+=dp[j-nums[i]]
        
    return dp[-1]

print(findTargetSumWays([0,0,0,0,0,0,0,0,1],1))
