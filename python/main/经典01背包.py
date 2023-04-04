

def zero_one_bag(weight:list,value:list,capcity:int)->int:
    
    # 物品数量
    m=len(weight)
    # 背包容纳量
    n=capcity+1

    # 初始化
    dp=[[0]*n for _ in range(m)]
    dp[0][weight[0]:]=[value[0]]*(n-weight[0])
    
    # print(dp)

    # 递推依赖都在上方或左上，所以保证从左到右，从上到下遍历即可
    for i in range(1,m):
        for j in range(1,n):

            # 装不下第i件物品
            dp[i][j]=dp[i-1][j] if j<weight[i] \
                else max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i]) #能装下则要判断装上第i件物品value是否更大

    return dp[m-1][n-1]

def zero_one_bag_1D(weight:list,value:list,capcity:int)->int:
    m=len(weight)
    n=capcity+1

    dp=[0]*n
    dp[weight[0]:]=[value[0]]*(n-weight[0])

    for i in range(1,m):
        for j in range(n-1,0,-1):
            if(j<weight[i]):
                break
            dp[j]=max(dp[j],dp[j-weight[i]]+value[i])
    return dp[n-1]
    
print(zero_one_bag_1D([1,3,4],[15,20,30],4))
