
# 暴力递归,与题意不符，按题意最后可能不会到最后一节台阶，而是直接越过最后一节到达顶部
def minCostClimbingStairs1(cost: list) -> int:

    size=len(cost)

    def _mccs(n:int):
        nonlocal cost
        if(n<=2):
            return cost[n-1]

        return cost[n-1]+min(_mccs(n-1),_mccs(n-2))
    
    return _mccs(size)


# dp
def minCostClimbingStairs2(cost: list) -> int:
    # 记录到达两步前和一步前的最小花费
    dp=[cost[0],cost[1]]

    for i in range(2,len(cost)):
        temp=cost[i]+min(dp)
        dp[0]=dp[1]
        dp[1]=temp

    # 考虑最后一阶楼梯不上的情况，即倒数第二节楼梯cost更小
    return min(dp)


print(minCostClimbingStairs2([10, 15, 20]))