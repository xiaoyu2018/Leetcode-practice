
# 暴力递归（有重复计算）
def Fibo1(n: int):
    if(n==0 or n==1):
        return n
    
    return Fibo1(n-1)+Fibo1(n-2)

# 记忆化递归（将重复计算的子问题记忆化剪枝）
memo={0:0,1:1}
def Fibo2(n: int):
    if(n==0 or n==1):
        return n
    
    f_n_1=memo[n-1] if n-1 in memo.keys() else Fibo2(n-1)
    f_n_2=memo[n-2] if n-2 in memo.keys() else Fibo2(n-2)
    
    res=f_n_1+f_n_2
    memo[n]=res
    return res

# 动态规划，改写迭代
# 1 确定dp数组（用于保存子问题结果）以及下标的含义：dp[i]的定义为：第i个数的斐波那契数值是dp[i]
# 2 确定递推公式： dp[i] = dp[i - 1] + dp[i - 2]
# 3 dp数组如何初始化：dp[0] = 0 dp[1] = 1
# 4 确定遍历顺序：后项依赖前项，所以肯定是从前到后遍历
# 5 举例推导dp数组（用于分析bug）：N=10时：dp={0,1,1,2,3,5,8,13,21,34,55}
def Fibo3(n: int):
    dp=[0]*(n+2)
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    
    return dp[n]

# 实际上动态维护两个值即可
def Fibo3(n: int):
    if(n==0 or n==1):
        return n
    dp=[0,1]
    
    for _ in range(2,n+1):
        temp=dp[1]
        dp[1]=dp[0]+dp[1]
        dp[0]=temp
    
    return dp[1]
print(Fibo3(5))