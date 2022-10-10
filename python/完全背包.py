
# 正序遍历一维滚动数组，相当于在一次遍历中可以重复添加某一物品
def completePack(weights:list,values:list):
    n=4+1
    m=len(values)

    dp=[0]*n

    for i in range(m):
        for j in range(weights[i],n):
            dp[j]=max(dp[j],dp[j-weights[i]]+values[i])
    
    return dp[-1]

print(completePack([1,3,4],[15,20,30]))
