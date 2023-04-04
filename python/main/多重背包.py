
def multi_pack(values:list,weights:list,nums:list):
    size=len(values)
    values=[j for l in [[values[i]]*nums[i] for i in range(size)] for j in l]
    weights=[j for l in [[weights[i]]*nums[i] for i in range(size)] for j in l]

    m=sum(nums)
    n=45+1

    dp=[0 if i<weights[0] else values[0] for i in range(n)]

    for i in range(1,m):
        for j in range(n-1,weights[i]-1,-1):
            dp[j]=max(dp[j],dp[j-weights[i]]+values[i])
    
    return dp[-1]

print(multi_pack([1,3,4],[15,20,30],[2,3,2]))
# a=[[1,3,4],[15,20,30],[2,3,2]]
