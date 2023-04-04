# 暴力递归
def fib1(n: int) -> int:
    if n < 2:
        return n

    return fib1(n - 1) + fib1(n - 2)


# 记忆化
def fib2(n: int) -> int:
    memo = {0: 0, 1: 1}

    def _rec(n: int) -> int:
        if n in memo.keys():
            return memo[n]

        f1 = _rec(n - 1)
        f2 = _rec(n - 2)

        memo[n - 1] = f1
        memo[n - 2] = f2

        return f1 + f2
    
    return _rec(n)%(1e9+7)

# dp
def fib3(n: int) -> int:
    dp=[0]*(n+1)
    if(n>=1):
        dp[1]=1
    
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    
    return int(dp[-1]%int((1e9+7)))

print(fib3(81))
    