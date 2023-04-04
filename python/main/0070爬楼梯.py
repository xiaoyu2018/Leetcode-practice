# 找出规律 1 2 3 5 8 13，缺第一项的斐波那契数列
# 在n-1阶爬1和n-2阶爬2可以得到全部的爬到n阶的情况
# 递归
def climbStairs1(n):
    if(n==1):
        return 1
    if(n==2):
        return 2
    
    return climbStairs1(n-1)+climbStairs1(n-2)

# dp
def climbStairs2(n):
    if(n in [1,2]):
        return n

    x1,x2=1,2
    res=0
    
    for _ in range(3,n+1):
        res=x1+x2
        x1=x2
        x2=res
    
    return res

# 01背包
# 可重复选爬1阶或爬2阶，容量为n阶的完全01背包
# 且是完全排列背包
def climbStairs3(n):
    dp=[0]*(n+1)
    dp[0]=1

    # 先遍历容量，再遍历物品
    for j in range(n+1):
        for i in range(1,3):
            if(j>=i):
                dp[j]+=dp[j-i]
    return dp[-1]


print(climbStairs3(5))