
def numWays(n: int) -> int:
    dp=[1,1]

    for i in range(2,n+1):
        dp.append((dp[i-1]+dp[i-2])%(1e9+7))
    return int(dp[n])